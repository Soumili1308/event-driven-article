# Event Flow Documentation

This document explains how events move through the system from start to finish.

---

## High-Level Flow

1. Client sends POST /articles/create
2. Article is created in initial state
3. `article.created` event is published
4. Multiple handlers react independently
5. Article state is updated progressively
6. Frontend receives real-time updates

---

## Detailed Event Flow

### Step 1: Article Creation

Action:
POST /articles/create

Effect:
- Article is created with status = PROCESSING
- `article.created` event is published

---

### Step 2: article.created Event

Triggered Handlers:
- Language detection handler
- Categorization handler

Purpose:
This event represents a meaningful business action: a new article entering the system.

---

### Step 3: language.detected Event

Handler Responsibility:
- Determine article language
- Update article record

Result:
- `language` field populated
- Intermediate status update possible

---

### Step 4: article.categorized Event

Handler Responsibility:
- Assign article category
- Mark article as READY

Result:
- Processing pipeline completes
- Article becomes usable

---

## Why Events Instead of Direct Calls?

Using events instead of function calls provides:
- Loose coupling between components
- Independent failure handling
- Easier scalability
- Clear separation of concerns

---

## Extensibility Example

A new feature like:
- Sentiment analysis
- Content moderation
- Keyword extraction

can be added by:
1. Subscribing a new handler
2. Without changing existing code

---

## Summary

The event flow demonstrates how real-world backend systems handle asynchronous processes efficiently while keeping the core API responsive and maintainable.
