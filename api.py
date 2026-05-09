import os
import json
from flask import Flask, request, jsonify
from google.cloud import pubsub_v1

# Using the absolute path to force Windows to find it
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = r"D:\cs323-voting-system\gcp-key.json"

app = Flask(__name__)

# REPLACE THIS WITH YOUR ACTUAL GCP PROJECT ID
PROJECT_ID = "engaged-oarlock-495814-p6" 
TOPIC_ID = "vote-topic"

publisher = pubsub_v1.PublisherClient()
topic_path = publisher.topic_path(PROJECT_ID, TOPIC_ID)

@app.route("/vote", methods=["POST"])
def receive_vote():
    vote = request.get_json()
    if not vote or not all(k in vote for k in ("user_id", "poll_id", "choice")):
        return jsonify({"error": "Invalid payload"}), 400

    try:
        message_data = json.dumps(vote).encode("utf-8")
        publisher.publish(topic_path, data=message_data)
        return jsonify({"status": "accepted"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)