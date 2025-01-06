from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy import select
from src.base.db import get_db
from src.schemas.product import ProductCreate, ProductUpdate
from src.model.product import Product
from src.other.utils import handle_db_errors

router = APIRouter(prefix="/product")



def get_product_by_barcode(barcode: str, db: Session = Depends(get_db)):
    query = db.execute(select(Product).where(Product.barcode == barcode))
    return query.scalars().first()


@router.post("/add")
@handle_db_errors
def add(product_item: ProductCreate, db: Session = Depends(get_db)):

    result = get_product_by_barcode(product_item.barcode, db)
    if result:
        result.quantity += 1
        db.commit()
        db.refresh(result) 
        return result


    new_product = Product(**product_item.model_dump())
    db.add(new_product)
    db.commit()
    db.refresh(new_product)
    return new_product


@router.get("/find")
@handle_db_errors
def read(barcode: str, db: Session = Depends(get_db)):
    find_product = get_product_by_barcode(barcode, db)
    if not find_product:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Product not found"
        )
    return {
        "id" : find_product.id,
        "name" : find_product.name,
        "barcode" : find_product.barcode,
        "quantity" : find_product.quantity
    }


@router.put("/update")
@handle_db_errors
def update(update_items: ProductUpdate, db: Session = Depends(get_db)):
    find_product = get_product_by_barcode(update_items.barcode, db)
    if not find_product:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Product not found"
        )


    if update_items.name:
        find_product.name = update_items.name
    if update_items.quantity:
        find_product.quantity = update_items.quantity

    db.commit()
    db.refresh(find_product)  
    return find_product


@router.delete("/delete")
@handle_db_errors
def delete(barcode: str, db: Session = Depends(get_db)):
    find_product = get_product_by_barcode(barcode, db)
    if not find_product:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Product not found"
        )

    db.delete(find_product)
    db.commit()
    return {"message": "Product deleted successfully"}
