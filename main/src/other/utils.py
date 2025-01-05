from fastapi import HTTPException, status
from functools import wraps
from sqlalchemy.orm import Session


def handle_db_errors(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        db: Session = kwargs.get("db")  # Assuming `db` is passed as a keyword argument
        try:
            return func(*args, **kwargs)
        except Exception as e:
            if db:
                db.rollback()  # Rollback the session on error
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=f"An unexpected error occurred: {e}",
            )
    return wrapper
