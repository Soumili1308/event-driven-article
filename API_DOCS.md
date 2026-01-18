# API Documentation

This document describes the available HTTP and WebSocket interfaces for the Event-Driven Articles system.

---

## 1. Create Article

### Endpoint
POST /articles/create

### Description
Creates a new article and triggers the event-driven processing pipeline.

### Request Body (JSON)
{
  "title": "Sample Article",
  "content": "This is the article content"
}

### Response
{
  "article_id": 1,
  "status": "PROCESSING"
}

### Notes
- Immediately returns without waiting for processing
- Fires `article.created` event internally

---

## 2. Get Article Status

### Endpoint
GET /articles/{id}

### Description
Fetches the current state of an article, including processing results.

### Response
{
  "title": "Sample Article",
  "content": "This is the article content",
  "language": "English",
  "category": "News",
  "status": "READY"
}

---

## 3. List Articles

### Endpoint
GET /articles

### Description
Returns a list of all articles and their current statuses.

### Response
[
  {
    "title": "Article 1",
    "status": "READY"
  },
  {
    "title": "Article 2",
    "status": "PROCESSING"
  }
]

---

## 4. WebSocket Connection

### Endpoint
WS /ws

### Description
Provides real-time updates as events are processed.

### Example Messages
- "Processing article..."
- "Language detected: English"
- "Category assigned: News"
- "Article ready"

---

## Error Handling

- 400 → Invalid request body
- 404 → Article not found
- 500 → Internal server error

---

## Security Notes

- Authentication is omitted for simplicity
- Can be added easily using Django auth or JWT
