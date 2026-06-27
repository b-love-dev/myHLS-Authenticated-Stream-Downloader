"""
HLS Authenticated Stream Downloader
Author: Brandon Scott Love
License: MIT
Description: A robust wrapper for yt-dlp designed to bypass 403 Forbidden 
             errors, handle custom headers/tokens, and override strict 
             FFmpeg segment extension guards (e.g., masked .webp fragments).
"""
import subprocess

# The video link and player page from your browser tools
m3u8_url = "PASTE URL HERE"
referer_url = "PASTE URL HERE"

# Building the command to launch the streamlink engine
command = [
    "streamlink",
    m3u8_url,
    "best",
    "-o", "real_video.mp4",
    "--http-header", f"Referer={referer_url}",
    "--http-header", "User-Agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
]

print("Launching Streamlink engine to bypass the PNG masquerade...")
try:
    subprocess.run(command, check=True)
    print("\nSuccess! The real video has been saved as real_video.mp4")
except Exception as e:
    print(f"\nAn error occurred while running Streamlink: {e}")
