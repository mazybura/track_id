from pydantic import BaseModel


class TrackInfo(BaseModel):
    title: str
    stream_url: str
    download_url: str
    source: str
