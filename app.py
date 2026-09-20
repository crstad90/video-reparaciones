import os
import random
import time
from flask import Flask, render_template_string, jsonify

app = Flask(__name__)

# Base de datos simulada en memoria para que no se borre el historial de la IA
HISTORIAL_VIDEOS = [
    {"id": 1, "nombre": "video_smartphone_pro.mp4", "fecha": "Hace unos minutos", "url": "https://mixkit.co"},
    {"id": 2, "nombre": "video_laptop_gaming.mp4", "fecha": "Hace 30 minutos", "url": "https://mixkit.co"}
]

# Lista de fuentes de video reales de stock de tecnología en internet
VIDEOS_STOCK = [
    "https://mixkit.co",
    "https://mixkit.co",
    "https://mixkit.co",
    "https://mixkit.co"
]

APARATOS = ["smartphone", "laptop", "smartwatch", "gaming-pc", "headphones", "drone", "camera"]

# --- INTERFAZ PREMIUM Y ATRACTIVA (CSS CINEMÁTICO) ---
HTML_PAGINA = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>⚡ Tech Video Gen AI - Galería Premium</title>
    <script src="https://jsdelivr.net"></script>
    <link rel="stylesheet" href="https://cloudflare.com">
    <style>
        .glow-effect {
            box-shadow: 0 0 20px rgba(6, 182, 212, 0.15);
            transition: all 0.3s ease;
        }
        .glow-effect:hover {
            box-shadow: 0 0 30px rgba(6, 182, 212, 0.4);
            transform: translateY(-4px);
        }
    </style>
</head>
<body class="bg-gradient-to-br from-slate-950 via-slate-900 to-cyan-950 text-white font-sans min-h-screen flex flex-col justify-between selection:bg-cyan-500 selection:text-slate-900">

    <!-- BARRA DE NAVEGACIÓN -->
    <header class="backdrop-blur-md bg-slate-900/80 border-b border-slate-800 sticky top-0 z-50 px-6 py-4 shadow-xl">
        <div class="container mx-auto flex flex-col sm:flex-row items-center justify-between gap-4">
            <div class="flex items-center gap-3">
                <div class="bg-gradient-to-tr from-cyan-500 to-blue-600 p-2.5 rounded-xl shadow-lg shadow-cyan-500/20 animate-pulse">
                    <i class="fa-solid fa-robot text-xl text-slate-950"></i>
                </div>
                <div>
                    <h1 class="text-2xl font-black bg-gradient-to-r from-cyan-400 via-teal-300 to-blue-500 bg-clip-text text-transparent tracking-wider">TECH VIDEO GEN AI</h1>
                    <p class="text-slate-400 text-xs font-medium">Sistema Autónomo de Contenido en la Nube</p>
                </div>
            </div>
            <div class="flex items-center gap-4 bg-slate-800/60 px-4 py-2 rounded-full border border-slate-700/50 backdrop-blur">
                <span class="w-2.5 h-2.5 rounded-full bg-emerald-500 animate-ping"></span>
                <span class="text-xs font-semibold text-emerald-400 tracking-wide uppercase">IA Activa (Cada 30m)</span>
            </div>
        </div>
    </header>

    <main class="container mx-auto px-4 py-10 flex-grow max-w-7xl">
        
        <!-- SECCIÓN 1: VIDEO DESTACADO -->
        <section class="mb-16">
            <div class="text-center max-w-3xl mx-auto mb-8">
                <span class="text-xs font-bold tracking-widest text-cyan-400 uppercase bg-cyan-950/60 border border-cyan-800/50 px-3 py-1 rounded-full">Último Lanzamiento</span>
                <h2 class="text-3xl font-extrabold mt-3 tracking-tight sm:text-4xl text-slate-100">Creación Más Reciente de la IA</h2>
            </div>

            <div class="flex justify-center">
                <div class="w-full max-w-[340px] bg-slate-900/90 rounded-2xl border border-cyan-500/30 overflow-hidden shadow-[0_0_40px_rgba(6,182,212,0.2)]">
                    <div class="relative aspect-[9/16] w-full bg-black">
                        <video class="w-full h-full object-cover" controls autoplay loop muted>
                            <source src="{{ video_destacado.url }}" type="video/mp4">
                        </video>
                    </div>
                    <div class="p-4 bg-slate-900 border-t border-slate-800 flex items-center justify-between">
                        <span class="text-xs text-slate-400 font-mono"><i class="fa-regular fa-clock mr-1.5"></i>{{ video_destacado.nombre }}</span>
                    </div>
                </div>
            </div>
        </section>

        <!-- SECCIÓN 2: HISTORIAL Y GALERÍA COMPLETA -->
        <section class="border-t border-slate-800/80 pt-12">
            <div class="flex items-center gap-3 mb-8">
                <i class="fa-solid fa-layer-group text-2xl text-cyan-400"></i>
                <h3 class="text-2xl font-bold tracking-tight text-slate-100">Galería de Videos Archivados ({{ total_videos }})</h3>
            </div>

            <div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-6">
                {% for video in lista_videos %}
                <div class="bg-slate-900/60 rounded-xl border border-slate-800/80 overflow-hidden glow-effect flex flex-col justify-between">
                    <div class="relative aspect-[9/16] w-full bg-black">
                        <video class="w-full h-full object-cover" controls preload="metadata" loop muted>
                            <source src="{{ video.url }}" type="video/mp4">
                        </video>
                    </div>
                    <div class="p-3.5 bg-slate-950/80 border-t border-slate-800/60 flex items-center justify-between gap-2">
                        <span class="text-[11px] text-slate-400 font-mono truncate max-w-[150px]"><i class="fa-regular fa-file-video mr-1 text-cyan-500"></i>{{ video.nombre }}</span>
                    </div>
                </div>
                {% endfor %}
            </div>
        </section>
    </main>

    <footer class="bg-slate-950 border-t border-slate-900 text-center py-6 text-xs text-slate-500 mt-20">
        <div class="container mx-auto px-4 flex flex-col sm:flex-row items-center justify-between gap-4 text-slate-400">
            <p>&copy; 2026 Tech Video Gen AI — Red de Servidores Autónomos.</p>
            <p class="flex items-center gap-1.5 text-xs text-slate-500">Diseñado con ❤️ para crstad90</p>
        </div>
    </footer>

</body>
</html>
"""

@app.route('/')
def inicio():
    return render_template_string(
        HTML_PAGINA, 
        video_destacado=HISTORIAL_VIDEOS[0], 
        lista_videos=HISTORIAL_VIDEOS, 
        total_videos=len(HISTORIAL_VIDEOS)
    )

@app.route('/generar')
def disparar_generacion():
    try:
        nuevo_aparato = random.choice(APARATOS)
        url_elegida = random.choice(VIDEOS_STOCK)
        nuevo_id = len(HISTORIAL_VIDEOS) + 1
        
        # Insertar el nuevo video al inicio del historial
        nuevo_item = {
            "id": nuevo_id,
            "nombre": f"video_{nuevo_aparato}_{int(time.time())}.mp4",
            "fecha": "Recién creado",
            "url": url_elegida
        }
        HISTORIAL_VIDEOS.insert(0, nuevo_item)
        return jsonify({"status": "success", "video_creado": nuevo_item["nombre"]}), 200
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
