

from flask import Flask

app = Flask(__name__)


@app.route("/login")
def hello_world():
    return {"username": "test", "password": "testtest"}, 200


if __name__ == "__main__":
    app.run()
