from events.event_bus import EventBus

def test_event_bus_publish():
    called = {"ok": False}

    def handler(payload):
        called["ok"] = True

    EventBus.subscribe("test.event", handler)
    EventBus.publish("test.event", {})

    assert called["ok"] is True
