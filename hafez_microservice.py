from flask import Flask, jsonify
import hafez
import random
app = Flask(__name__)
@app.route("/fal", methods=['GET'])
def fal():
    poem_id = random.randint(1, 10)  # Adjust the range based on the available poems
    a = hafez.get_poem(poem_id)
    response = {
        "poem": a['poem'],
        "interpretation": a['interpretation']
    }
    return jsonify(response)
if __name__ == "__main__":
    app.run(port=8001, host="127.0.0.1", debug=True)
