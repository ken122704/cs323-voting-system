import json
from google.cloud import pubsub_v1, firestore

KEY_PATH = "gcp-key.json"
PROJECT_ID = "cs323-voting-clean"
SUB_ID = "vote-sub"

# Direct Authentication
db = firestore.Client.from_service_account_json(KEY_PATH)
subscriber = pubsub_v1.SubscriberClient.from_service_account_json(KEY_PATH)
subscription_path = subscriber.subscription_path(PROJECT_ID, SUB_ID)

def process_vote(message):
    try:
        vote = json.loads(message.data.decode("utf-8"))
        doc_id = f"{vote['user_id']}_{vote['poll_id']}"
        
        # Write to Firestore
        db.collection("votes").document(doc_id).set(vote)
        print(f"Processed vote for user: {vote['user_id']}")
        
        message.ack() # Tell Pub/Sub we are done with it
    except Exception as e:
        print(f"Error processing: {e}")

def start_worker():
    print("Worker listening for votes...")
    future = subscriber.subscribe(subscription_path, callback=process_vote)
    try:
        future.result()
    except KeyboardInterrupt:
        future.cancel()

if __name__ == "__main__":
    start_worker()