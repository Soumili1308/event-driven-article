from events.event_bus import EventBus
from events.domain_events import LANGUAGE_DETECTED, ARTICLE_CATEGORIZED

def handle_article_created(article):
    EventBus.publish(LANGUAGE_DETECTED, article)
    EventBus.publish(ARTICLE_CATEGORIZED, article)
