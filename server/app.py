from fastapi import FastAPI
from server.controllers.track_controller import router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Track ID API")

# Dodaj middleware CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # frontend React
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Dodaj router z track_controller
app.include_router(router)
