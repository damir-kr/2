from fastapi import FastAPI

app = FastAPI()

@app.get('/damir')
def index():
    return {'Answer': 'dalbaeb'}

