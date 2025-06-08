# track_id

An application to search for and download Jumpstyle tracks from online sources.

Built with React frontend + FastAPI backend + Selenium automation.

<img src="docs/assets/prtSc_app.png" alt="App Screenshot" width="90%"/>

# Motivation

Used to be an active Jumpstyle dancer. Over the years, I noticed that many tracks; especially from genres like Hardstyle and Jumpstyle have disappeared from mainstream platforms like YouTube.
However, some of these tracks still exist on various online databases.
I created this application to help recover and archive these tracks by providing a tool where I can enter the artist and track name, and automatically download them if available.

⚠️ Disclaimer:
This project was built for educational and personal use only.
I do not intend to make this tool public, host it on a server, or monetize it in any way.
Downloading copyrighted content may be illegal in some jurisdictions; please respect the rights of content creators.

## How to run

### Backend (FastAPI):

```sh
cd server
pip install -r requirements.txt
uvicorn app:app --reload
```

Runs on: http://localhost:8000

### Frontend:

```sh
cd client
npm install
npm start
```

Runs on: http://localhost:3000

## Stack

React - frontend

FastAPI - backend REST API

Selenium - automation of download

Scrapy - for scraping track URLs

Wavesurfer - waveform player in React
