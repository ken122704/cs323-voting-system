import requests
import uuid
import time
import random

API_URL = "http://localhost:8080/vote"
CANDIDATES = ["Alice", "Bob", "Charlie"]

def generate_votes():
    while True:
        vote = {
            "user_id": str(uuid.uuid4())[:8],
            "poll_id": "presidential_2026",
            "choice": random.choice(CANDIDATES),
            "timestamp": time.time()
        }
        
        try:
            response = requests.post(API_URL, json=vote)
            print(f"Vote sent: {vote['choice']} | Status: {response.status_code}")
        except Exception as e:
            print(f"Failed to connect to API: {e}")
            
        time.sleep(random.uniform(0.5, 2.0)) # Random delay between votes

if __name__ == "__main__":
    generate_votes()