from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

image_status = "no_change"


@app.route("/check-image", methods=["GET"])
def check_image():
    global image_status
    status = image_status
    image_status = "no_change"
    return status


@app.route("/change-image", methods=["GET"])
def change_image():
    global image_status
    image_status = "change"
    return "Image changed"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
