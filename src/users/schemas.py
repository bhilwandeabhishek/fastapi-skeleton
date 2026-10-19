from pydantic import BaseModel, ConfigDict, Field


class UserInput(BaseModel):
    model_config = ConfigDict(extra="forbid")

    userName: str = Field(min_length=1, max_length=50)
    userEmail: str = Field(
        min_length=3,
        max_length=255,
        pattern=r"^[^@\s]+@[^@\s]+\.[^@\s]+$",
    )


class UserRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    username: str = Field(serialization_alias="userName")
    email: str = Field(serialization_alias="userEmail")
