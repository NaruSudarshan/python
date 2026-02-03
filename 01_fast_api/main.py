from fastapi import FastAPI , Query , Path , Body
from typing import Annotated , Literal
from pydantic import BaseModel, Field

app = FastAPI()

@app.get("/")
def home():
    return "hello world !!"


# #-------------------------------------------------------------------------------------------
# # path variable 

# @app.get("/item/{id}")
# def print_id(id:int):
#     return f"item id is {id}"

# #  path operations are evaluated in order, 
# # you need to make sure that the path for /users/me is declared before the one for /users/{user_id}


# @app.get("/users/me")
# async def read_user_me():
#     return {"user_id": "the current user"}


# @app.get("/users/{user_id}")
# async def read_user(user_id: str):
#     return {"user_id": user_id}

# # cannot redefine a path operation

# # An Enum is a class that defines a fixed set of allowed values.

# from enum import Enum

# class ModelName(str, Enum):
#     alexnet = "alexnet"
#     resnet = "resnet"
#     lenet = "lenet"
    
# @app.get("/models/{model_name}")
# async def get_model(model_name: ModelName):
#     if model_name is ModelName.alexnet:
#         return {"model_name": model_name, "message": "Deep Learning FTW!"}

#     if model_name.value == "lenet":
#         return {"model_name": model_name, "message": "LeCNN all the images"}

#     return {"model_name": model_name, "message": "Have some residuals"}


# @app.get("/files/{file_path:path}")
# async def read_file(file_path: str):
#     return {"file_path": file_path}

# #---------------------------------------------------------------------------------------------------
# # query parameter 

# # needy is required as no default value
# # skipa nd limit are optional
# # url will be /items/5?needy=hii&skip=10&limit=20
# @app.get("/items/{item_id}")
# async def read_user_item(
#     item_id: str, needy: str, skip: int = 0, limit: int | None = None
# ):
#     item = {"item_id": item_id, "needy": needy, "skip": skip, "limit": limit}
#     return item

# #---------------------------------------------------------------------------------------------------
# # req body

# from pydantic import BaseModel

# class Item(BaseModel):
#     name : str
#     quantity : int
    
# @app.post("/items/")
# def create_item(item:Item):
#     # for converting req body to dict 
#     # item_dict = item.model_dump()
#     return f"name is {item.name} and quantity is {item.quantity}"

# @app.put("/items/{item_id}")
# async def update_item(item_id: int, item: Item):
#     return {"item_id": item_id, **item.model_dump()}

#-----------------------------------------------------------------------------------------------------------

# #data validation in query
# @app.get("/items/")
# def get_items(q : Annotated[str | None , Query(max_length=5) ] = None):
#     return "this is a example for validating quesry parameter"

# #data validation in path 
# @app.get("/items/{item_id}")
# def get_item(item_id : Annotated[int,Path(
#     title="example of validating path",
#     description="asdjfhaksjdhfakljsdfh",
#     le=2
# )]):
#     return "this is an item"

# # query parameter as pydantic model 
# class FilterParams(BaseModel):
#     model_config = {"extra": "forbid"}

#     limit: int = Field(100, gt=0, le=100)
#     offset: int = Field(0, ge=0)
#     order_by: Literal["created_at", "updated_at"] = "created_at"
#     tags: list[str] = []

# @app.get("/items/")
# async def read_items(filter_query: Annotated[FilterParams, Query()]):
#     return filter_query


#-----------------------------------------------------------------------------------------------------------

# #Multiple body parameters with mix of query and path 
# class Item(BaseModel):
#     name: str
#     description: str | None = None
#     price: float
#     tax: float | None = None


# class User(BaseModel):
#     username: str
#     full_name: str | None = None


# @app.put("/items/{item_id}")
# async def update_item(
#     *, # * makes sure there are no posistional arguments after it
#     item_id: int,
#     item: Item,
#     user: User,
#     importance: Annotated[int, Body(gt=0)], # single value body 
#     q: str | None = None,
# ):
#     results = {"item_id": item_id, "item": item, "user": user, "importance": importance}
#     if q:
#         results.update({"q": q})
#     return results

# # item: Annotated[Item, Body(embed=True)] ->>>>>>>>>> item is passed as key with json

#-----------------------------------------------------------------------------------------------------------

# #Pydantic fields 
# class Item(BaseModel):
#     name: str
#     description: str | None = Field(
#         default=None, title="The description of the item", max_length=300
#     ) # can use annotated also 
#     price: float = Field(gt=0, description="The price must be greater than zero")
#     tax: float | None = None


# @app.put("/items/{item_id}")
# async def update_item(item_id: int, item: Annotated[Item, Body(embed=True)]):
#     results = {"item_id": item_id, "item": item}
#     return results

#-----------------------------------------------------------------------------------------------------------

# #nested models 
# from pydantic import HttpUrl

# class Image(BaseModel):
#     url: HttpUrl
#     name: str


# class Item(BaseModel):
#     name: str
#     description: str | None = None
#     price: float
#     tax: float | None = None
#     tags: set[str] = set()
#     images: list[Image] | None = None


# class Offer(BaseModel):
#     name: str
#     description: str | None = None
#     price: float
#     items: list[Item]


# @app.post("/offers/")
# async def create_offer(offer: Offer):
#     return offer

# FastAPI decides the source using these rules (simplified):
# 1 Path parameters
# If the name appears in the path → Path

# 2 Query parameters
# If it’s a simple type (int, str, bool, etc.) and not in the path → Query

# 3 Request body
# If its a complex type → Body

# @app.post("/index-weights/")
# async def create_index_weights(weights: dict[int, float]): # here as dict is complex it is considered body 
#     return weights