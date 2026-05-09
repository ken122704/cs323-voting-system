import os
import json
from google.cloud import pubsub_v1, firestore

# Absolute path to your key
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = r"D:\cs323-voting-system\gcp-key.json"

# Your ACTUAL Project ID
PROJECT_ID = "engaged-oarlock-495814-p6"
SUBSCRIPTION_ID = "vote-sub"

subscriber = pubsub_v1.SubscriberClient()
subscription_path = subscriber.subscription_path(PROJECT_ID, SUBSCRIPTION_ID)

# Notice how we use the PROJECT_ID variable here!
db = firestore.Client(project=PROJECT_ID)

# IF you named your database something else, change the line above to this:
# db = firestore.Client(project=PROJECT_ID, database="your-database-name")

def process_vote(message):
    try:
        vote = json.loads(message.data.decode("utf-8"))
        doc_id = f"{vote['user_id']}_{vote['poll_id']}"
        
        db.collection("votes").document(doc_id).set(vote)
        print(f"Processed vote: {vote['user_id']} | Poll: {vote['poll_id']}")
        message.ack()
    except Exception as e:
        print("Error processing message:", e)

def start_worker():
    print(f"Worker listening on {subscription_path}...")
    streaming_pull_future = subscriber.subscribe(subscription_path, callback=process_vote)
    try:
        streaming_pull_future.result() 
    except KeyboardInterrupt:
        streaming_pull_future.cancel()

if __name__ == "__main__":
    start_worker()