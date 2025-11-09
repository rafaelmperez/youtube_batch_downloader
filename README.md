## 🎥 YouTube Batch Downloader

Descarga múltiples vídeos de **YouTube** en la **mejor calidad disponible (video + audio)** de forma interactiva, con un script simple en **Python 3**.  
Ideal para automatizar descargas en lote desde la terminal — rápido, limpio y multiplataforma.  

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](#)
[![Status](https://img.shields.io/badge/Status-Active-success)](#)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

---

## 🧠 Overview

Este script te permite descargar fácilmente varios vídeos de YouTube sin interfaces gráficas, directamente desde la terminal.  
Cada vídeo se guarda automáticamente en una carpeta llamada `descargas_youtube`, combinando audio y video en la **mejor calidad posible** mediante `yt-dlp`.

Perfecto para:
- Automatizar descargas en lote.
- Practicar **Python, automatización y manejo de librerías CLI**.
- Entornos educativos, personales o de prueba.

---

## 🚀 Características principales

✅ Introduce enlaces uno a uno desde la terminal.  
✅ Descarga la **mejor calidad posible (video + audio)** automáticamente.  
✅ Crea la carpeta `descargas_youtube` si no existe.  
✅ Compatible con **Windows, macOS y Linux**.  
✅ Muestra progreso y maneja errores comunes.  
✅ Código limpio, modular y comentado paso a paso.  

---

## ⚙️ Requisitos

- **Python 3.8+**
- **yt-dlp**
- **ffmpeg** *(opcional pero recomendado para unir audio y video)*

### Instalación rápida

```bash
pip install yt-dlp
sudo apt install ffmpeg   # En Linux
````

También puedes crear un entorno virtual y usar un `requirements.txt`:

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

---

## ▶️ Uso

1️⃣ Copia el contenido del script y guárdalo como:

```bash
nano youtube_batch_downloader.py
```

2️⃣ Ejecuta el script desde la terminal:

```bash
python3 youtube_batch_downloader.py
```

3️⃣ Introduce los enlaces uno por uno:

```text
📥 Introduce enlaces de YouTube (escribe 'fin' para terminar):
> https://www.youtube.com/watch?v=dQw4w9WgXcQ
> https://youtu.be/VIDEO_ID_2
> fin
```

🎬 Los vídeos se descargarán automáticamente en la carpeta:

```
descargas_youtube/
```

---

## 🧩 Ejemplo de salida

```
[1/2] Analizando: https://www.youtube.com/watch?v=dQw4w9WgXcQ
▶️  Descargando [1/2]: Rick Astley - Never Gonna Give You Up (Official Music Video)
   ↳ Progreso: 75.3%  Vel: 3.1MiB/s  ETA: 6s
✅ Listo.

📂 Archivos guardados en: /ruta/al/script/descargas_youtube
🏁 Proceso finalizado.
```

---

## 🧰 Estructura del proyecto

```
youtube-batch-downloader/
├─ youtube_batch_downloader.py
├─ requirements.txt
├─ .gitignore
├─ LICENSE
└─ README.md
```

---

## 💡 Ejemplo de `requirements.txt`

```
yt-dlp
```

*(Puedes añadir `ffmpeg` si lo gestionas por pip o sistema.)*

---

## ⚙️ Configuración opcional

Puedes editar el script para personalizar:

* Carpeta de destino (`descargas_youtube`)
* Calidad preferida (por defecto `bestvideo+bestaudio/best`)
* Nombre de archivo (`%(title)s.%(ext)s`)

Ejemplo de línea modificable dentro del script:

```python
ydl_opts = {
    "outtmpl": "descargas_youtube/%(title)s.%(ext)s",
    "format": "bestvideo+bestaudio/best",
}
```

---

## 🧠 Autor

👤 **Rafael M. P.**
💬 Proyecto educativo y personal para practicar Python, automatización y manejo de librerías open source.

---

## ⚖️ Licencia

Este proyecto está publicado bajo la licencia **MIT**.
Puedes usarlo, modificarlo y distribuirlo libremente, siempre citando la autoría original.
Consulta el archivo [LICENSE](LICENSE) para más detalles.

---

## 💬 Nota legal

Este script utiliza la librería open source [yt-dlp](https://github.com/yt-dlp/yt-dlp).
**YouTube™** es una marca registrada de Google LLC.

> ⚠️ Solo debe usarse para descargar contenido de **tu propiedad** o con **licencia libre**.

---

## 🔎 GitHub SEO

**Keywords:**
`python`, `youtube-downloader`, `yt-dlp`, `video`, `automation`, `cli`, `batch`, `ffmpeg`, `open-source`, `youtube`, `downloader`

**One-liner SEO description:**

> Download multiple YouTube videos in the best quality with Python — simple, fast, and interactive batch downloader powered by yt-dlp.

---

**GitHub Topics:**
`python` · `youtube` · `yt-dlp` · `downloader` · `automation` · `cli` · `video` · `audio` · `batch` · `ffmpeg`
