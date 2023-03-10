#FastAPI
from fastapi import APIRouter
from fastapi import status, HTTPException
from fastapi import Depends
from fastapi import Body, Path, Query

#SQLAlchemy
from sqlalchemy.ext.asyncio import AsyncSession

from ....api.deps import get_async_db, get_current_user
from .... import crud, models, schemas


router = APIRouter()

@router.post(
    path="/", 
    response_model=schemas.User,
    status_code=status.HTTP_200_OK
)
async def create_user(
    db:AsyncSession = Depends(get_async_db),
    user:schemas.UserCreate = Body(...)
):
    db_user = await crud.user.get_user_by_email(db=db, email=user.email) 
    if db_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="This email address already exists"
        )
    db_user = await crud.user.create(db=db, model=user)
    return db_user

@router.get(path="/", response_model=list[schemas.User])
async def get_users(
    db:AsyncSession = Depends(get_async_db),
    skip:int = Query(default=0),
    limit:int = Query(default=5)
):
    users = await crud.user.get_multi(db, skip=skip, limit=limit)
    return users

@router.get(
    path="/me",
    response_model=schemas.User,
    status_code=status.HTTP_200_OK
) 
async def read_user_me(
    current_user:models.User = Depends(get_current_user)
)-> any:
    """
    Get Current User
    """
    return current_user

@router.get(
    path="/{id}", 
    response_model=schemas.User,
    status_code= status.HTTP_200_OK
)
async def get_user_by_id(
    db:AsyncSession = Depends(get_async_db),
    id:int = Path(
        ...,
        gt=0
    )
):
    db_user = await crud.user.get(db=db, id=id)
    if db_user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="This person doesn't exist"
        )
    return db_user