from models.article import Article
from handlers.on_language_detected import handle_language_detected

def test_language_handler(db):
    article = Article.objects.create(title="t", content="c")
    handle_language_detected(article)
    assert article.language == "English"
