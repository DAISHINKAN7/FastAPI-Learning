from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def index():
    # return 'hey'
    return {'data': {
        'name': 'John',
        'age': 30,
        'city': 'New York'
    }}

@app.get('/about')
def about():
    return {
        'data': {
            'about page': 'This is an about page'
        }
    }

@app.get('/blog/unpublished')
def unpublished():
    return {'data' : "All unpublished blogs"}

@app.get('/blog/{id}')   #parenthesis for dynamic routing
def show(id: int):
    return {'data': id}


@app.get('/blog/{id}/comments')
def comments(id):
    #Fetch comments of blog with id = id
    return {'data' : {'1', '2'}}