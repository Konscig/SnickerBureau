from fastapi import FastAPI, APIRouter
from api.v1.routers import router as api_v1_router

app = FastAPI()

# Including routers
routers: list[APIRouter] = [
    api_v1_router,
]

for router in routers:
    app.include_router(router)
