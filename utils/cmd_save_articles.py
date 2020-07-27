import json

from worker import pocket_api as api

articles = api.get_articles()

with open('tests/articles_sample.json', 'w') as file:
    json.dump(articles, file)

