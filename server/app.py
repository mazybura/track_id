from fastapi import FastAPI
from server.controllers.track_controller import router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Track ID API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)
