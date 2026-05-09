import uuid
import random
import time
import requests

API_URL = "http://localhost:8080/vote" 

def generate_vote():
    return {
        "user_id": str(uuid.uuid4()),
        "poll_id": "poll_1",
        "choice": random.choice(["A", "B", "C"]),
        "timestamp": time.time(),
        "edge_id": "node_ken"
    }

def send_vote(vote):
    try:
        response = requests.post(API_URL, json=vote)
        response.raise_for_status()
        print(f"Vote generated: {vote['user_id']} | Choice: {vote['choice']}")
    except Exception as e:
        print("Transmission failed:", e)

def run_edge_node():
    print("Edge node active. Generating votes...")
    while True:
        vote = generate_vote()
        send_vote(vote)
        time.sleep(random.uniform(1, 3))

if __name__ == "__main__":
    run_edge_node()