from datetime import timedelta

from celery import Celery
from kombu import Queue

redis_url = "redis://localhost:6379/0"

app = Celery("test_celery", broker=redis_url, backend=redis_url)

app.conf.task_queues = (
    Queue("A", routing_key="open_courtesy_car_1"),
    Queue("B", routing_key="open_admin_api_1"),
)


@app.task(name="add_one", queue="B")
def add_one():
    return 666


@app.task(name="add_two", queue="A")
def add_two():
    return 888


app.conf.beat_schedule = {
    "add_two": {
        "task": "add_two",
        "schedule": timedelta(seconds=2),
    },
}

if __name__ == "__main__":
    add_one.delay()
