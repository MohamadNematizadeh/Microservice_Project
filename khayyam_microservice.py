from flask import Flask, jsonify
from khayyam.jalali_datetime import JalaliDatetime

app = Flask(__name__)

@app.route("/today", methods=['GET'])
def fal():
    today = JalaliDatetime.now().strftime('%C')
    return jsonify({"today": today})

if __name__ == "__main__":
    app.run(port=8002, debug=True)