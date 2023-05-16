from datetime import datetime, timedelta
from typing import Optional

from pydantic import BaseModel, validator, root_validator, Extra, Field


# Разные варианты форматироания вывода времени по ТЗ
FROM_TIME = (datetime.now() + timedelta(minutes=10)).strftime('%Y-%m-%dT%H:%M')
TO_TIME = (datetime.now() + timedelta(minutes=60)).isoformat(timespec='minutes')


class ReservationBase(BaseModel):
    from_reserve: datetime = Field(..., example=FROM_TIME)
    to_reserve: datetime = Field(..., example=TO_TIME)

    class Config:
        extra = Extra.forbid


class ReservationUpdate(ReservationBase):

    @validator('from_reserve')
    def check_from_reserve_later_than_now(cls, value):
        if value <= datetime.now():
            raise ValueError(
                'Нельзя бронировать задним числом!'
            )
        return value

    @root_validator(skip_on_failure=True)
    def check_from_reserve_before_to_reserve(cls, values):
        if values['from_reserve'] >= values['to_reserve']:
            raise ValueError(
                'Время начала бронирования не может быть больше времени окончания бронирования!'
            )
        return values


class ReservationCreate(ReservationUpdate):
    meetingroom_id: int


class ReservationDB(ReservationBase):
    id: int
    meetingroom_id: int
    # Добавьте опциональное поле user_id.
    user_id: Optional[int]

    class Config:
        orm_mode = True
