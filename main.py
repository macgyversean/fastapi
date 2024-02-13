from fastapi import FastAPI

app = FastAPI()

# Create our root route
@app.get("/items/{item_id}")
def root():
    return {"message": "Hello, World!"}
def read_item(item_id: int):
    return {"item_id": item_id}
