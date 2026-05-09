from flask import Flask, request, jsonify
from google.cloud import pubsub_v1
import json

app = Flask(__name__)

# Direct Authentication
KEY_PATH = "gcp-key.json"
PROJECT_ID = "cs323-voting-clean"
TOPIC_ID = "vote-topic"

publisher = pubsub_v1.PublisherClient.from_service_account_json(KEY_PATH)
topic_path = publisher.topic_path(PROJECT_ID, TOPIC_ID)

@app.route('/vote', methods=['POST'])
def receive_vote():
    vote_data = request.json
    data_bytes = json.dumps(vote_data).encode("utf-8")
    
    # Publish to Pub/Sub
    future = publisher.publish(topic_path, data=data_bytes)
    future.result() # Wait for publish to succeed
    
    return jsonify({"status": "Vote buffered in Pub/Sub"}), 200

if __name__ == "__main__":
    app.run(port=8080, debug=True)