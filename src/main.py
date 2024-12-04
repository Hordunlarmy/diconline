from fastapi import APIRouter, FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.modules.application.router import application_router
from src.modules.program.router import program_router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def read_root():
    return {"Message": "Hello DIC"}


router = APIRouter(prefix="/api")
router.include_router(application_router)
router.include_router(program_router)

app.include_router(router)
