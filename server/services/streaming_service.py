class StreamingService:
    def get_stream_url(self, title: str) -> str:
        # Na razie prosty placeholder — można potem podpiąć prawdziwy streaming URL (np. SoundCloud, YouTube, itp.)
        return f"https://mockstream.com/{title.replace(' ', '_')}.mp3"
