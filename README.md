# Distributed Voting System with Edge-Cloud Architecture (CS323)

## Team Members

- **Ken Charles Besa**
- **Vonmar Viscayno**
- **Paul Vincent Noval**
- **Birky Andrei Pacuribot**
- **Carlos Jorge Gamale**

## System Overview & Architecture

[cite_start]This project implements a fault-tolerant, event-driven Distributed Voting System on Google Cloud Platform (GCP)[cite: 7, 24]. [cite_start]The architecture is designed to handle high-concurrency data generation at the edge and ensure reliable processing in the cloud[cite: 5, 8].

[cite_start]**The Pipeline:** `Edge Nodes (Python) → Cloud Run API (Ingestion) → Pub/Sub (Messaging) → Cloud Run Worker (Processing) → Firestore (Storage)` [cite: 26-28]

## Key Distributed Concepts Applied

- [cite_start]**Edge Computing:** Decentralized data generation simulating real-world user devices[cite: 16, 68].
- [cite_start]**Asynchronous Messaging:** Using Pub/Sub to decouple components and prevent system-wide failure during downtime[cite: 64, 131].
- [cite_start]**Idempotency:** Ensuring that duplicate messages do not result in multiple records in the database[cite: 21, 149].
- [cite_start]**Fault Tolerance:** The system remains functional and recovers automatically even when the processing layer is offline[cite: 19, 194].

---

## Individual Reflections

### Ken Charles Besa

[cite_start]During the implementation, I observed a significant difference between sequential and distributed execution, particularly in how the system handles service interruptions[cite: 271]. [cite_start]When we encountered a database 404 error, the Pub/Sub layer acted as a critical buffer, holding all incoming votes in a persistent queue[cite: 191, 204]. [cite_start]Once the Firestore database was initialized and the worker restarted, the system demonstrated asynchronous recovery by processing the entire backlog automatically[cite: 199, 214]. [cite_start]This experience highlighted how distributed architectures isolate failures to specific components without losing data[cite: 194].

### Vonmar Viscayno

[cite_start]My focus during this activity was on the ingestion layer and the trade-offs between latency and reliability[cite: 11, 260]. [cite_start]By using a non-blocking API to push data to Pub/Sub, we ensured that the edge nodes received a fast "accepted" response without waiting for the database write to finish[cite: 132, 135]. [cite_start]While this introduces a small delay before the data appears in Firestore, it greatly improves the system's ability to handle bursts of traffic from multiple concurrent edge sources[cite: 113, 262].

### Paul Vincent Noval

[cite_start]Implementing idempotency was the most valuable lesson for me in this lab[cite: 21]. [cite_start]By using a unique composite document ID consisting of the `user_id` and `poll_id`, we ensured that even if a vote was transmitted multiple times due to network retries, Firestore only stored a single consistent record [cite: 147-149]. [cite_start]This logic is essential for maintaining eventual consistency in distributed systems where message duplication is a common occurrence[cite: 259, 264].

### Birky Andrei Pacuribot

[cite_start]I analyzed the behavior of the system under simulated failure states[cite: 164, 242]. [cite_start]By disabling the Cloud Run worker instances, I saw how the Cloud Run API continued to function and accept votes from the edge nodes[cite: 180, 190]. [cite_start]This demonstrated the power of decoupling; the "front-end" of our cloud system remained alive even when the "back-end" was down[cite: 126, 193]. [cite_start]The persistence provided by Pub/Sub ensures that the system is resilient against intermittent service outages[cite: 64].

### Carlos Jorge Gamale

[cite_start]Working with edge computing simulation showed me the complexity of coordinating distributed sources[cite: 274]. [cite_start]Each of our edge nodes operated independently with random delays, mimicking real-world user activity[cite: 69, 100]. [cite_start]I realized that while edge computing reduces the immediate processing load on the server, it requires a robust cloud infrastructure to handle the synchronization and storage of data arriving at different speeds and times[cite: 271, 273].

---

## Live Deployment

- **Cloud Run API URL:** `https://engaged-oarlock-495814-p6-api-endpoint.a.run.app` (Example)
- **GitHub Repository:** `[INSERT_YOUR_GITHUB_URL_HERE]`
