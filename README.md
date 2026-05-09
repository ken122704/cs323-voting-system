# Distributed Voting System with Edge-Cloud Architecture (CS323)

## Team Members

- **Ken Charles Besa**
- **Vonmar Viscayno**
- **Paul Vincent Noval**
- **Birky Andrei Pacuribot**
- **Carlos Jorge Gamale**

---

## System Overview & Architecture

This project implements a fault-tolerant, event-driven Distributed Voting System on Google Cloud Platform (GCP). The architecture is designed to handle high-concurrency data generation at the edge and ensure reliable processing in the cloud.

**The Pipeline:**  
`Edge Nodes (Python) → Cloud Run API (Ingestion) → Pub/Sub (Messaging) → Cloud Run Worker (Processing) → Firestore (Storage)`

---

## Key Distributed Concepts Applied

- **Edge Computing:** Decentralized data generation simulating real-world user devices.
- **Asynchronous Messaging:** Using Pub/Sub to decouple components and prevent system-wide failure during downtime.
- **Idempotency:** Ensuring that duplicate messages do not result in multiple records in the database.
- **Fault Tolerance:** The system remains functional and recovers automatically even when the processing layer is offline.

---

## Individual Reflections

### Ken Charles Besa

During the implementation, I observed a significant difference between sequential and distributed execution, particularly in how the system handles service interruptions. When we encountered a database error, the Pub/Sub layer acted as a critical buffer, holding all incoming votes in a persistent queue. Once the database was initialized and the worker restarted, the system demonstrated asynchronous recovery by processing the entire backlog automatically. This experience highlighted how distributed architectures isolate failures to specific components without losing data.

---

### Vonmar Viscayno

My focus during this activity was on the ingestion layer and the trade-offs between latency and reliability. By using a non-blocking API to push data to Pub/Sub, we ensured that the edge nodes received a fast "accepted" response without waiting for the database write to finish. While this introduces a small delay before the data appears in storage, it greatly improves the system's ability to handle bursts of traffic from multiple concurrent edge sources.

---

### Paul Vincent Noval

Implementing idempotency was the most valuable lesson for me in this lab. By using a unique composite document ID consisting of the `user_id` and `poll_id`, we ensured that even if a vote was transmitted multiple times due to network retries, the database only stored a single consistent record. This logic is essential for maintaining eventual consistency in distributed systems where message duplication is a common occurrence.

---

### Birky Andrei Pacuribot

I analyzed the behavior of the system under simulated failure states. By disabling the Cloud Run worker instances, I saw how the API layer continued to function and accept votes from the edge nodes. This demonstrated the power of decoupling; the front-end of our cloud system remained alive even when the back-end was down. The persistence provided by Pub/Sub ensures that the system is resilient against intermittent service outages.

---

### Carlos Jorge Gamale

Working with edge computing simulation showed me the complexity of coordinating distributed sources. Each of our edge nodes operated independently with random delays, mimicking real-world user activity. I realized that while edge computing reduces the immediate processing load on the server, it requires a robust cloud infrastructure to handle the synchronization and storage of data arriving at different speeds and times.

## System Demo

A short demonstration of the Distributed Voting System in action.

▶️ [Watch Demo Video](./demo.mp4)
