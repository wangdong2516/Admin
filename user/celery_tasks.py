from utils.celery_app import app


@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')


@app.task(bind=True)
def print_test(self):
    print('kkk')