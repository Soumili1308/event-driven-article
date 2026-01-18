class EventBus:
    _subscribers = {}

    @classmethod
    def subscribe(cls, event_name, handler):
        if event_name not in cls._subscribers:
            cls._subscribers[event_name] = []
        cls._subscribers[event_name].append(handler)

    @classmethod
    def publish(cls, event_name, payload):
        handlers = cls._subscribers.get(event_name, [])
        for handler in handlers:
            try:
                handler(payload)
            except Exception as e:
                print(f"[EventBus] Handler error for {event_name}: {e}")
