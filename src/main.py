from fastapi import APIRouter, FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.modules.application.router import application_router
from src.modules.batch.router import batch_router
from src.modules.course.router import course_router
from src.modules.dashboard.router import dashboard_router
from src.modules.department.router import department_router
from src.modules.program.router import program_router
from src.modules.student.router import student_router

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


@app.get("/api")
def read_api():
    return {"Message": "Hello DIC API"}


router = APIRouter(prefix="/api")
router.include_router(application_router)
router.include_router(dashboard_router)
router.include_router(program_router)
router.include_router(department_router)
router.include_router(course_router)
router.include_router(student_router)
router.include_router(batch_router)

app.include_router(router)
