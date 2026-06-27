# **myHLS-Authenticated-Stream-Downloader**

A robust, multi-threaded Python wrapper for yt-dlp designed to bypass strict server-side blocks, handle session-authenticated HLS streams, and override non-standard media segment extensions.

## **🚀 Features**

* **Authentication Bypass:** Seamlessly injects custom headers (User-Agent, Referer, Origin) to get past 403 Forbidden errors.  
* **Dynamic Domain Parsing:** Automatically extracts and structures tracking headers from the source URL.  
* **Segment Guardrail Override:** Forces the underlying FFmpeg engine to accept non-standard or masked media stream fragments (e.g., .webp files acting as video chunks).  
* **Parallel Downloading:** Utilizes multi-threaded connection workers (concurrent\_fragments) to dramatically increase download speeds.  
* **Network Resilience:** Aggressive timeout and retry configurations built-in to handle network fluctuations or VPN stability drops without corrupting the final video.

## **🛠️ Prerequisites**

Before running the script, make sure you have the following installed on your system:

1. **Python 3.x**  
2. **FFmpeg** (Ensure it is added to your system's PATH environment variables)  
3. **Python Packages:**  
4. Bash
5. pip install yt-dlp pycryptodomex
 (Note: pycryptodomex is required so yt-dlp can decrypt AES-128 streams natively without crashing).
6. pip install streamlink
## **💻 Installation & Usage**

1. Clone this repository or download the download.py file:  
2. Bash

git clone https://github.com/b-love-dev/myHLS-Authenticated-Stream-Downloader.git  
cd myHLS-Authenticated-Stream-Downloader

3.   
4.   
5. Open download.py in a text editor and replace the placeholders with your actual stream network data obtained from your browser's Developer Tools (Network Tab):  
6. Python

m3u8\_url \= "PASTE\_YOUR\_M3U8\_URL\_HERE"  
referer\_url \= "PASTE\_YOUR\_REFERER\_HERE"

7.   
8.   
9. Run the script:  
10. Bash

python myHLS-Authenticated-Stream-Downloader.py

11.   
12. 

## **⚙️ Configuration Adjustments**

You can easily tweak the ydl\_opts dictionary inside the script to match your network needs:

* concurrent\_fragments: Set to 16 by default for an optimal balance of speed and stability. If your connection or VPN is highly stable, you can increase this to 32 for faster downloads. If the server throws HTTP Error 500, lower it to 8 or 5.  
* socket\_timeout: Set to 60 seconds to allow slow or throttled fragments time to respond before timing out.

## **📄 License**

This project is licensed under the MIT License \- see the LICENSE file for details.

## **🤝 Acknowledgments**

* Built using the powerful [yt-dlp](https://github.com/yt-dlp/yt-dlp) framework.  
* Optimized for handling complex, masked content delivery networks (CDNs).

Is there anything else you need help with to get your repository ready?  
