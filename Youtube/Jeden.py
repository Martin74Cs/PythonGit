import os
from yt_dlp import YoutubeDL

os.system("cls")

Downloads = os.path.join(os.getcwd(), "Downloads")
if not os.path.exists(Downloads):
    os.mkdir(Downloads)

url = "https://www.youtube.com/live/rriw4esRvYw"
options = {
    'outtmpl': os.path.join(Downloads, '%(title)s.%(ext)s'),
    'nocheckcertificate': True,  # Disables SSL certificate verification
    # 'merge_output_format': 'mp4',  # Force output to be MP4
    # 'verbose': True
}

with YoutubeDL(options) as ydl:
    info = ydl.extract_info(url, download=True)  # Extracts info about the video
    print("\nVideo Information:")
    print(f"Title: {info.get('title', 'N/A')}")
    print(f"Uploader: {info.get('uploader', 'N/A')}")
    print(f"Duration: {info.get('duration', 'N/A')} seconds")
    print(f"View count: {info.get('view_count', 'N/A')}")
    print(f"Like count: {info.get('like_count', 'N/A')}")
    ydl.download([url])
print("Download completed!")

# python -m pip install --upgrade certifi
# python -m certifi