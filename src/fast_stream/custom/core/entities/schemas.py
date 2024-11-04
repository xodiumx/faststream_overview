from pydantic import BaseModel


class City(BaseModel):
    name: str
    country: str


class AddressInfo(BaseModel):
    name: str
    city: City


class Person(BaseModel):
    first_name: str
    last_name: str
    phone: str
    company: str


class Data(BaseModel):
    id: str
    name: str
    description: str
    address: AddressInfo
    person: Person
