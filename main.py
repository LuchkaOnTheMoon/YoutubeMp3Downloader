import shutil
import yt_dlp as youtube_dl
from settings import *


def run():
    if not enable_download_archive:
        # Clean-up output folder.
        shutil.rmtree(output_folder)

    for url in playlist:
        # Set download options.
        options = {
            'format': 'bestaudio/best',
            'keepvideo': False,
            'outtmpl': f"{output_folder}/%(title)s.mp3",
            'download_archive': f"{output_folder}/downloaded.txt",
        }

        # Download as MP3.
        with youtube_dl.YoutubeDL(options) as ydl:
            ydl.download(url)

    # Print user message.
    print("All done!")


if __name__ == '__main__':
    run()

