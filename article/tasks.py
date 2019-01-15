from celery.task.schedules import crontab
from celery.decorators import periodic_task
from celery.utils.log import get_task_logger

from .models import Article

logger = get_task_logger(__name__)

@periodic_task(
    run_every=(crontab(minute='*/1')),
    name="task_add_article",
    ignore_result=True
)

def task_add_article():
    p = Article.objects.create(
        title="This is created by automated task",
        description="Periodic Task",
        body="Wow so cool!!!",
    )
    logger.info("Created new article!")