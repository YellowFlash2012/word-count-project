from __init__ import app

@app.route('/')
def home():
    return "Yo, I'm back!"