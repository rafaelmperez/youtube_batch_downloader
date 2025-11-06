#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Descargador batch de YouTube (video+audio en la mejor calidad posible)
----------------------------------------------------------------------
Características:
1) Pide enlaces por terminal uno a uno y los guarda hasta que escribas 'fin'.
2) Descarga todos los vídeos en la carpeta 'descargas_youtube' (se crea sola).
3) Usa yt-dlp; intenta mejor calidad (bestvideo+bestaudio) y fusiona a MP4 si hay ffmpeg.
4) Muestra progreso legible y maneja errores comunes (URL inválida, borrado, red, etc.).
5) Código comentado y compatible con Windows/macOS/Linux.

Nota legal: descarga solo contenido para el que tengas derechos y respeta Términos de Servicio.
"""

from __future__ import annotations
from pathlib import Path
import sys
import shutil
from typing import List, Dict, Any

# Dependencia principal
try:
    import yt_dlp  # pip install yt-dlp
except ImportError:
    print("❌ Falta la librería 'yt-dlp'. Instálala con:  pip install yt-dlp")
    sys.exit(1)


def detectar_ffmpeg() -> bool:
    """Devuelve True si hay ffmpeg disponible en el PATH (necesario para fusionar video+audio)."""
    return shutil.which("ffmpeg") is not None or shutil.which("ffmpeg.exe") is not None


def pedir_enlaces() -> List[str]:
    """Lee enlaces por terminal hasta que el usuario escriba 'fin'. Filtra entradas vacías."""
    print("📥 Introduce enlaces de YouTube (escribe 'fin' para terminar):")
    enlaces: List[str] = []
    while True:
        try:
            linea = input("> ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\n🔚 Entrada interrumpida. Continuamos con los enlaces recogidos.")
            break
        if not linea:
            continue
        if linea.lower() == "fin":
            break
        # Validación mínima: debe aparentar ser un enlace http(s)
        if not (linea.startswith("http://") or linea.startswith("https://")):
            print("⚠️  Eso no parece un enlace válido. Prueba de nuevo o escribe 'fin'.")
            continue
        enlaces.append(linea)
    return enlaces


def formatear_salida(base_dir: Path) -> str:
    """
    Plantilla de salida para yt-dlp.
    Guarda como: descargas_youtube/<TITULO> [ID].ext
    """
    return str(base_dir / "%(title).200B [%(id)s].%(ext)s")


def hook_progreso(d: Dict[str, Any]):
    """
    Hook de progreso de yt-dlp. Se llama periódicamente con info del estado.
    Mostramos mensajes compactos y claros.
    """
    status = d.get("status")
    if status == "downloading":
        # Campos útiles: _percent_str, _speed_str, eta
        pct = d.get("_percent_str", "").strip()
        spd = d.get("_speed_str", "").strip()
        eta = d.get("eta")
        if eta is not None:
            print(f"   ↳ Progreso: {pct}  Vel: {spd}  ETA: {eta}s", end="\r", flush=True)
        else:
            print(f"   ↳ Progreso: {pct}  Vel: {spd}            ", end="\r", flush=True)
    elif status == "finished":
        # Archivo descargado (o listo para post-procesado)
        print("   ↳ Descarga completada. Procesando…          ")


def construir_opciones_salida(dest_dir: Path, usar_ffmpeg: bool) -> Dict[str, Any]:
    """
    Construye opciones sensatas para mejor calidad.
    - Con ffmpeg: bestvideo+bestaudio -> merge MP4.
    - Sin ffmpeg: fallback a 'best' (progresivo) para evitar errores.
    """
    # Formato preferido
    if usar_ffmpeg:
        fmt = "bv*+ba/best"   # mejor video + mejor audio; si no, el mejor disponible
        merge_fmt = "mp4"     # formato de salida tras fusionar
    else:
        fmt = "best"          # progresivo (incluye audio), evita necesidad de ffmpeg
        merge_fmt = None

    ydl_opts: Dict[str, Any] = {
        "format": fmt,
        "noplaylist": True,  # evita bajar listas enormes si pegan un link de playlist
        "outtmpl": formatear_salida(dest_dir),
        "progress_hooks": [hook_progreso],
        "ignoreerrors": True,  # continúa con el resto si hay errores en alguno
        "retries": 3,
        "fragment_retries": 5,
        "concurrent_fragments": 5,  # agiliza HLS/DASH
        "quiet": True,
        "no_warnings": True,
        # Sanitizar nombres de archivo de forma segura
        "restrictfilenames": False,
        "windowsfilenames": True,  # evita caracteres problemáticos en Windows
    }

    if usar_ffmpeg:
        ydl_opts.update({
            "merge_output_format": merge_fmt,
            "postprocessors": [
                {
                    "key": "FFmpegVideoConvertor",
                    "preferedformat": merge_fmt,  # convert/merge a MP4 cuando sea posible
                }
            ]
        })

    return ydl_opts


def obtener_titulo(ydl: yt_dlp.YoutubeDL, url: str) -> str:
    """Intenta extraer metadatos del vídeo sin descargar (para mostrar el título)."""
    try:
        info = ydl.extract_info(url, download=False)
        # Puede ser playlist o vídeo; nos quedamos con el título adecuado
        if info is None:
            return "(desconocido)"
        if "title" in info:
            return info["title"]
        # Si fuera una entrada de playlist, intenta primer elemento
        if "entries" in info and info["entries"]:
            first = info["entries"][0]
            if first and "title" in first:
                return first["title"]
    except Exception:
        pass
    return "(desconocido)"


def descargar_lista(enlaces: List[str], dest_dir: Path) -> None:
    """Descarga todos los enlaces proporcionados con feedback ordenado."""
    if not enlaces:
        print("ℹ️  No se proporcionaron enlaces. Nada que hacer.")
        return

    # Prepara carpeta de salida
    dest_dir.mkdir(parents=True, exist_ok=True)

    # Detecta ffmpeg para elegir mejor estrategia
    hay_ffmpeg = detectar_ffmpeg()
    if not hay_ffmpeg:
        print("ℹ️  ffmpeg no detectado. Se usará 'best' (vídeo+audio progresivo).\n"
              "    Para mejor calidad (fusionar video+audio separados), instala ffmpeg.")

    ydl_opts = construir_opciones_salida(dest_dir, usar_ffmpeg=hay_ffmpeg)

    # Descargas secuenciales con título previo
    total = len(enlaces)
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        for i, url in enumerate(enlaces, start=1):
            print(f"\n[{i}/{total}] Analizando: {url}")
            titulo = obtener_titulo(ydl, url)
            print(f"▶️  Descargando [{i}/{total}]: {titulo}")

            try:
                # Ejecuta la descarga
                ydl.download([url])
                print("✅ Listo.")
            except yt_dlp.utils.DownloadError as e:
                print(f"❌ Error de descarga: {e}")
            except Exception as e:
                print(f"❌ Error inesperado: {e}")


def main() -> None:
    # Carpeta de destino: junto al script
    base_dir = Path(__file__).resolve().parent
    dest_dir = base_dir / "descargas_youtube"

    # 1) Obtener enlaces de la terminal
    enlaces = pedir_enlaces()

    # 2) Descargar secuencialmente
    descargar_lista(enlaces, dest_dir)

    print(f"\n📂 Archivos guardados en: {dest_dir.resolve()}")
    print("🏁 Proceso finalizado.")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n🛑 Cancelado por el usuario.")
