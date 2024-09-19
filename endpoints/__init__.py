from fastapi import APIRouter

from .auth import router as auth_router
from .book import router as book_router

router = APIRouter()

router.include_router(router=auth_router)
router.include_router(router=book_router)
