from flask import Flask, jsonify, send_file, request
import requests
from io import BytesIO

app = Flask(__name__)

FAL_MICROSERVICE_URL = "http://localhost:8001/fal"
TODAY_MICROSERVICE_URL = "http://localhost:8002/today"
QR_MICROSERVICE_URL = "http://localhost:8003/generate_qr"

def get_fal():
    response = requests.get(FAL_MICROSERVICE_URL)
    return response.json()

def get_today():
    response = requests.get(TODAY_MICROSERVICE_URL)
    return response.json()

@app.route("/", methods=['GET'])
def combined():
    fal_data = get_fal()
    today_data = get_today()

    combined_data = {
        "fal": fal_data["interpretation"],
        "today": today_data["today"]
    }
    # Store the QR code image
    qr_response = requests.post(QR_MICROSERVICE_URL, json=combined_data)
    qr_img = BytesIO(qr_response.content)

    # Save the QR image to a file
    with open("qr_image.png", "wb") as f:
        f.write(qr_img.getvalue())

    return jsonify(combined_data)

@app.route("/qr-image", methods=['GET'])
def qr_image():
    # Serve the saved QR image file
    return send_file("qr_image.png", mimetype='image/png')
if __name__ == "__main__":
    app.run(port=8080, debug=True)
