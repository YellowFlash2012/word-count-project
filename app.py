from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Yo, this is to test staging and prod pipeline!"

#if __name__ == "__main__":
# app.run(debug=True)
