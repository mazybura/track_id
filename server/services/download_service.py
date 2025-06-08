import logging
import threading
from server.models.track_info import TrackInfo
from server.utils import download_tool
from server.services.streaming_service import StreamingService


download_tool.setup_logging()


class DownloadService:
    def __init__(self):
        self.streaming_service = StreamingService()

    def download_track(self, title: str) -> TrackInfo:
        stream_url = self.streaming_service.get_stream_url(title)
        download_url = f"https://mockdownload.com/{title.replace(' ', '_')}.mp3"

        return TrackInfo(
            title=title,
            stream_url=stream_url,
            download_url=download_url,
            source="myfreemp3juices.cc",
        )

    def trigger_download_in_background(self, title: str, download_dir: str):
        def background_download():
            logging.info(f"Background download started for: {title}")
            logging.info(f"Using download folder: {download_dir}")

            driver = download_tool.configure_driver(download_dir)

            try:
                download_tool.download_song(driver, title)
            finally:
                driver.quit()
                logging.info(f"Background download finished for: {title}")

        threading.Thread(target=background_download).start()
