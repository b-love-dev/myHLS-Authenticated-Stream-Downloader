"""
HLS Authenticated Stream Downloader
Author: Brandon Scott Love
License: MIT
Description: A robust wrapper for yt-dlp designed to bypass 403 Forbidden 
             errors, handle custom headers/tokens, and override strict 
             FFmpeg segment extension guards (e.g., masked .webp fragments).
"""

import yt_dlp
from urllib.parse import urlparse

# Replace with your custom stream URL (with its active session tokens)
m3u8_url = "PASTE_YOUR_M3U8_URL_HERE"

# Optional: Set your tracking referer page (e.g., 'https://vidora.stream/')
# If left as "AUTO", the script will automatically extract the domain base from your m3u8_url
referer_url = "PASTE_YOUR_REFERER_HERE"

# Automatically parse out the origin domain if placeholders aren't replaced manually
parsed_url = urlparse(m3u8_url)
domain_origin = f"{parsed_url.scheme}://{parsed_url.netloc}" if m3u8_url and "PASTE_YOUR" not in m3u8_url else "PASTE_YOUR_ORIGIN_HERE"
actual_referer = referer_url if "PASTE_YOUR" not in referer_url else domain_origin

ydl_opts = {
    'format': 'best',
    'outtmpl': 'downloaded_video.mp4',
    'hls_prefer_native': True,
    
    # 1. Threading optimization for network stability over VPNs
    'concurrent_fragments': 16,         
    
    # 2. Aggressive retry and timeout guardrails for unstable streaming hosts
    'socket_timeout': 60,                # Give each fragment 60 seconds to respond instead of 20
    'retries': 10,                       # Retry the main connection 10 times if it drops
    'fragment_retries': 20,              # Forcefully retry a timed-out fragment up to 20 times before skipping
    'file_access_retries': 5,
    
    # 3. Security bypass for masked stream fragments (e.g., .webp files acting as video chunks)
    'external_downloader_args': {
        'ffmpeg_i': ['-allowed_extensions', 'ALL']
    },
    'http_headers': {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'Referer': actual_referer,
        'Origin': domain_origin
    }
}

print("Running stable authenticated download with connection guardrails...")
try:
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([m3u8_url])
    print("\nSuccess! The video has been saved as downloaded_video.mp4")
except Exception as e:
    print(f"\nDownload failed: {e}")