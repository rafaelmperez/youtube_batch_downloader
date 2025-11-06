🎥 YouTube Batch Downloader

Script en **Python 3** que permite descargar varios vídeos de **YouTube** de forma interactiva, en la **mejor calidad disponible (video + audio)**, guardándolos automáticamente en una carpeta llamada `descargas_youtube`.

---

## 🚀 Características principales

✅ Introduce enlaces uno a uno desde la terminal.  
✅ Descarga en la mejor calidad posible (video + audio).  
✅ Crea automáticamente la carpeta `descargas_youtube`.  
✅ Compatible con **Windows, macOS y Linux**.  
✅ Muestra progreso y maneja errores comunes.  
✅ Código limpio y comentado paso a paso.

---

## ⚙️ Requisitos

- **Python 3.8+**
- **yt-dlp**
- **ffmpeg** *(opcional, pero recomendado)*

Instalación rápida:
```bash
pip install -r requirements.txt
sudo apt install ffmpeg

▶️ Uso
Copia y pega el contenido del script:

nano youtube_batch_downloader.py

Ejecuta el script desde la terminal:

python3 youtube_batch_downloader.py

Luego introduce los enlaces uno por uno:

📥 Introduce enlaces de YouTube (escribe 'fin' para terminar):
> https://www.youtube.com/watch?v=dQw4w9WgXcQ
> https://youtu.be/VIDEO_ID_2
> fin

Los vídeos se guardarán en la carpeta:

descargas_youtube/

🧩 Ejemplo de salida

[1/2] Analizando: https://www.youtube.com/watch?v=dQw4w9WgXcQ
▶️  Descargando [1/2]: Rick Astley - Never Gonna Give You Up (Official Music Video)
   ↳ Progreso: 75.3%  Vel: 3.1MiB/s  ETA: 6s
✅ Listo.

📂 Archivos guardados en: /ruta/al/script/descargas_youtube
🏁 Proceso finalizado.

🧠 Autor

👤 Rafael M. P.
💬 Proyecto educativo y personal para practicar Python, automatización y manejo de librerías open source.
⚖️ Licencia

Este proyecto está publicado bajo la licencia MIT

.
Puedes usarlo, modificarlo y distribuirlo libremente, siempre citando la autoría original.
💡 Nota legal

Este script utiliza la librería open source yt-dlp.
YouTube™ es una marca registrada de Google LLC.
Solo debe usarse para descargar contenido de tu propiedad o con licencia libre.

