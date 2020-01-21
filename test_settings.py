import os

from django.urls import (
    include,
    path,
)

BASE_DIR = os.path.dirname(__file__)
STATIC_URL = "/static/"

INSTALLED_APPS = (
    'gcloudc',
    'djangae',
    'djangae.commands',  # Takes care of emulator setup
    'djangae.tasks',
)

DATABASES = {
    'default': {
        'ENGINE': 'gcloudc.db.backends.datastore',
        'INDEXES_FILE': os.path.join(os.path.abspath(os.path.dirname(__file__)), "djangaeidx.yaml"),
        "PROJECT": "test",
        "NAMESPACE": "ns1",  # Use a non-default namespace to catch edge cases where we forget
    }
}

SECRET_KEY = "secret_key_for_testing"

USE_TZ = True

CSRF_USE_SESSIONS = True

CLOUD_TASKS_LOCATION = "[LOCATION]"

# Define two required task queues
CLOUD_TASKS_QUEUES = [
    {
        "name": "default"
    },
    {
        "name": "another"
    }
]

# Point the URL conf at this file
ROOT_URLCONF = __name__

urlpatterns = [
    path('tasks/', include('djangae.tasks.urls')),
]