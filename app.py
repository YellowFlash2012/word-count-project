import os

from flask import Flask

app = Flask(__name__)
env_config = os.getenv("APP_SETTINGS", "config.DevelopmentConfig")
app.config.from_object(env_config)

@app.route('/')
def home():
    secret_key = app.config.get("SECRET_KEY")
    return f"The configured secret key is {secret_key}."

#if __name__ == "__main__":
    #app.run(debug=True)
