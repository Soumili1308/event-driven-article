from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

from models.article import Article
from events.event_bus import EventBus
from events.domain_events import ARTICLE_CREATED

@csrf_exempt
def create_article(request):
    body = json.loads(request.body)
    article = Article.objects.create(
        title=body["title"],
        content=body["content"]
    )

    EventBus.publish(ARTICLE_CREATED, article)

    return JsonResponse({
        "article_id": article.id,
        "status": article.status
    })


def get_article(request, article_id):
    article = Article.objects.get(id=article_id)
    return JsonResponse({
        "title": article.title,
        "content": article.content,
        "language": article.language,
        "category": article.category,
        "status": article.status
    })


def list_articles(request):
    articles = Article.objects.all().values()
    return JsonResponse(list(articles), safe=False)
