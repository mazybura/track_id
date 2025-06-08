from fastapi import APIRouter, Query, Body
from server.services.download_service import DownloadService
from server.models.track_info import TrackInfo
from pydantic import BaseModel
from server.utils import download_tool
from fastapi.responses import FileResponse
import os

router = APIRouter()
download_service = DownloadService()


@router.post("/search", response_model=TrackInfo)
def search_track(title: str = Query(..., description="Song title to search")):
    track_info = download_service.download_track(title)
    return track_info


@router.post("/download")
def download_track(request: dict = Body(...)):
    track_name = request.get("track")
    if not track_name:
        return {"status": "error", "message": "Missing track name"}

    unique_download_dir = download_tool.create_unique_download_folder(
        download_tool.Config.download_base_dir
    )

    driver = download_tool.configure_driver(unique_download_dir)

    try:
        download_tool.download_song(driver, track_name)

        # Czekamy aż plik się pojawi (polling)
        timeout = 60  # sekundy
        poll_interval = 2
        elapsed = 0

        downloaded_file = None

        while elapsed < timeout:
            all_files = os.listdir(unique_download_dir)

            downloaded_files = [
                file_name
                for file_name in all_files
                if os.path.isfile(os.path.join(unique_download_dir, file_name))
                and file_name.lower().endswith((".mp3", ".wav"))
            ]

            crdownload_files = [
                file_name
                for file_name in all_files
                if os.path.isfile(os.path.join(unique_download_dir, file_name))
                and file_name.lower().endswith(".crdownload")
            ]

            if downloaded_files and not crdownload_files:
                downloaded_file = downloaded_files[0]
                break

            logging.info(f"Waiting for downloaded file... {elapsed}/{timeout} seconds")
            time.sleep(poll_interval)
            elapsed += poll_interval

        if downloaded_file:
            file_url = f"http://localhost:8000/downloads/{os.path.basename(unique_download_dir)}/{downloaded_file}"

            return {
                "status": "success",
                "track": track_name,
                "file_url": file_url,
            }
        else:
            return {"status": "error", "message": "No files downloaded"}

    finally:
        driver.quit()


class DownloadBatchRequest(BaseModel):
    titles: list[str]


@router.post("/download_batch")
def download_batch(request: DownloadBatchRequest):
    unique_download_dir = download_tool.create_unique_download_folder(
        download_tool.Config.download_base_dir
    )

    for title in request.titles:
        download_service.trigger_download_in_background(title, unique_download_dir)

    return {
        "status": "Batch download started",
        "num_tracks": len(request.titles),
        "download_dir": unique_download_dir,
    }


@router.get("/downloads/{subdir}/{filename}")
def serve_downloaded_file(subdir: str, filename: str):
    download_dir = os.path.join(download_tool.Config.download_base_dir, subdir)
    file_path = os.path.join(download_dir, filename)

    if os.path.exists(file_path):
        return FileResponse(file_path, media_type="audio/mpeg", filename=filename)
    else:
        return {"status": "error", "message": "File not found"}
