from fastapi import APIRouter
from .product import router as product

router = APIRouter()

router.include_router(product)