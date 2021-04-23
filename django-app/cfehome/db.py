import os

'''
POSTGRES_DB=dockerdc
POSTGRES_PASSWORD=mysecretpassword
POSTGRES_USER=myuser
POSTGRES_HOST=db
POSTGRES_PORT=5432
'''
POSTGRES_DB=os.environ.get("POSTGRES_DB")
POSTGRES_PASSWORD=os.environ.get("POSTGRES_PASSWORD")
POSTGRES_USER=os.environ.get("POSTGRES_USER")
POSTGRES_HOST=os.environ.get("POSTGRES_HOST")
POSTGRES_PORT=os.environ.get("POSTGRES_PORT")

POSTGRES_READY = (
    POSTGRES_DB is not None and
    POSTGRES_PASSWORD is not None and
    POSTGRES_USER is not None and
    POSTGRES_HOST is not None and
    POSTGRES_PORT is not None
)

if POSTGRES_READY:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.postgresql",
            "NAME": POSTGRES_DB,
            "USER": POSTGRES_USER,
            "PASSWORD":POSTGRES_PASSWORD,
            "HOST": POSTGRES_HOST,
            "PORT":POSTGRES_PORT
        }
    }