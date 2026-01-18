# Development Process

## 1. Problem Understanding

The goal of this assignment was to design a simplified event-driven system using Django, where a single user action (article creation) triggers multiple asynchronous processes such as language detection, categorization, and real-time notifications.

Instead of tightly coupling these operations inside a single request-response cycle, the problem encourages an event-based approach that reflects real-world backend system design.

---

## 2. Why Event-Driven Architecture?

An event-driven architecture was chosen because:

- One action (article creation) triggers multiple independent operations
- Operations should not block the HTTP request
- The system should be easy to extend without modifying existing logic
- Handlers should remain loosely coupled

By publishing domain events (e.g., `article.created`) and allowing handlers to subscribe independently, the system achieves better modularity, scalability, and testability.

---

## 3. Architectural Decisions

### a. Event Bus
A simple in-memory `EventBus` was implemented to:
- Register event handlers
- Publish events
- Execute handlers independently

This avoids overengineering while still demonstrating the core concept of event-based communication.

### b. Domain Events
Domain events such as:
- `article.created`
- `language.detected`
- `article.categorized`

represent meaningful business state changes rather than technical operations.

---

## 4. Handler Design

Each handler performs **one responsibility only**:

- `on_article_created` → triggers downstream events
- `on_language_detected` → updates article language
- `on_article_categorized` → updates category and final status

This separation makes handlers:
- Easy to test
- Easy to replace with async queues (Celery, Kafka) later
- Independent of each other

---

## 5. Django Usage

Django is used as the main framework to:
- Handle HTTP APIs
- Provide project structure and configuration
- Enable future ORM and admin support

For simplicity, the database layer is kept minimal, as the focus of this assignment is architectural design rather than persistence complexity.

---

## 6. AI / LLM Integration Strategy

Actual LLM calls (Gemini / OpenAI) are **mocked** in handlers because:
- Real API calls are slow and expensive
- Assignment focuses on system design, not API keys
- Keeps the system deterministic and testable

In production, these handlers can easily be replaced with real AI integrations.

---

## 7. Testing Strategy

Unit tests focus on:
- Event bus correctness
- Handler execution logic
- Isolation of business logic from infrastructure

This ensures confidence that:
- Events fire correctly
- Handlers modify state as expected
- The system behaves predictably

---

## 8. Scalability Considerations

This architecture can scale to:
- Background workers (Celery)
- Message brokers (Kafka / RabbitMQ)
- Distributed systems

without major refactoring, proving that the design is production-minded.

---

## Conclusion

This implementation prioritizes clarity, correctness, and architectural thinking over unnecessary complexity. It demonstrates how event-driven systems can be designed in Django while remaining simple, extensible, and testable.
