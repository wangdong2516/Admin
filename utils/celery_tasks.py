import redis
from datetime import datetime
from utils.celery_app import app
from user.models import WebsiteVisit

connection = redis.Redis(db=1)


@app.task
def to_database():
    """
        将Redis中缓存的访问数量持久化到数据库中
    """
    visit_num = connection.get('visit_num')
    WebsiteVisit.objects.create(visit=visit_num)
