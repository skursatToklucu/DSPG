from pydantic import BaseModel


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
    pattern: str


class TripletCreate(TripletBase):
    pass


class Triplet(TripletBase):
    id: int

    class Config:
        orm_mode = True


# endregion

# region Cuarta
class CuartaBase(BaseModel):
    pattern: str


class CuartaCreate(CuartaBase):
    pass


class Cuarta(CuartaBase):
    id: int

    class Config:
        orm_mode = True


# endregion

# region Quintuplet
class QuintupletBase(BaseModel):
    pattern: str


class QuintupletCreate(QuintupletBase):
    pass


class Quintuplet(QuintupletBase):
    id: int

    class Config:
        orm_mode = True


# endregion


# region Sextuplet
class SextupletBase(BaseModel):
    pattern: str


class SextupletCreate(SextupletBase):
    pass


class Sextuplet(SextupletBase):
    id: int

    class Config:
        orm_mode = True


# endregion


# region Septuplet
class SeptupletBase(BaseModel):
    pattern: str


class SeptupletCreate(SeptupletBase):
    pass


class Septuplet(SeptupletBase):
    id: int

    class Config:
        orm_mode = True
# endregion
