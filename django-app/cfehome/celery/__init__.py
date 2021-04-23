import os
import pathlib
import dotenv
from celery import Celery


USE_DOTENV = os.environ.get("USE_DOTENV_PKG")
if str(USE_DOTENV) == "1":
    base_path = pathlib.Path(__file__).resolve().parent.parent.parent
    dotenv.read_dotenv(base_path / ".env-dev")
    
# from django.conf import settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cfehome.settings')

REDIS_HOST = os.environ.get("REDIS_HOST", "localhost")
REDIS_PORT = os.environ.get("REDIS_PORT", 6379)
REDIS_URL  = f"redis://{REDIS_HOST}:{REDIS_PORT}"

app = Celery('cfehome')
app.config_from_object("django.conf:settings", namespace='CELERY')
app.autodiscover_tasks()
app.conf.broker_url = REDIS_URL
app.conf.beat_scheduler = "django_celery_beat.schedulers.DatabaseScheduler"
