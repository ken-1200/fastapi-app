from fastapi import FastAPI, APIRouter
from fastapi.middleware.cors import CORSMiddleware

from todo.api.todo import router as todo_router


router = APIRouter()
router.include_router(
    todo_router,
    prefix='',
    tags=['todo']
)

app = FastAPI()
app.include_router(router)


origins = (
    'http://0.0.0.0:8080',
    'http://localhost:8080',
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
