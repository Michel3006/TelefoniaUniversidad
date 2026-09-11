from fastapi import Depends
from sqlalchemy.orm import Session

from app.core.security import get_current_user
from app.db.session import get_db

db_dependency = Depends(get_db)
current_user = Depends(get_current_user)