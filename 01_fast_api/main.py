from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return "hello world !!"


#-------------------------------------------------------------------------------------------
# path variable 

@app.get("/item/{id}")
def print_id(id:int):
    return f"item id is {id}"

#  path operations are evaluated in order, 
# you need to make sure that the path for /users/me is declared before the one for /users/{user_id}


@app.get("/users/me")
async def read_user_me():
    return {"user_id": "the current user"}


@app.get("/users/{user_id}")
async def read_user(user_id: str):
    return {"user_id": user_id}

# cannot redefine a path operation

# An Enum is a class that defines a fixed set of allowed values.

from enum import Enum

class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"
    
@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name is ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}

    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}

    return {"model_name": model_name, "message": "Have some residuals"}


@app.get("/files/{file_path:path}")
async def read_file(file_path: str):
    return {"file_path": file_path}

#---------------------------------------------------------------------------------------------------
# query parameter 

# needy is required as no default value
# skipa nd limit are optional
# url will be /items/5?needy=hii&skip=10&limit=20
@app.get("/items/{item_id}")
async def read_user_item(
    item_id: str, needy: str, skip: int = 0, limit: int | None = None
):
    item = {"item_id": item_id, "needy": needy, "skip": skip, "limit": limit}
    return item