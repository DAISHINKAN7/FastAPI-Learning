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