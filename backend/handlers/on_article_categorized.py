def handle_article_categorized(article):
    # Mocked AI response
    article.category = "News"
    article.status = "READY"
    article.save()
