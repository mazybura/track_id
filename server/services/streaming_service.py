class StreamingService:
    def get_stream_url(self, title: str) -> str:
        return f"https://mockstream.com/{title.replace(' ', '_')}.mp3"
