from pydantic import BaseModel


# class ItemBase(BaseModel):
#     title: str
#     description: str | None = None
#
#
# class ItemCreate(ItemBase):
#     pass
#
#
# class Item(ItemBase):
#     id: int
#     owner_id: int
#
#     class Config:
#         orm_mode = True

class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    password: str


# orm_mode pydantic kütüphanesi için bir configurasyon ayarı
class User(UserBase):
    id: int
    is_active: bool

    class Config:
        orm_mode = True
