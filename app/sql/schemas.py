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

# region User
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


# endregion

# region Triplet
class TripletBase(BaseModel):
    name: str
    pattern: str


class TripletCreate(TripletBase):
    pass


class Triplet(TripletBase):
    id: int

    class Config:
        orm_mode = True

# endregion
