"""
tells django that in production we want to use s3 to store our
static files whenever someone runs collectstatic.
And that we want any uploaded product images to go there also.
"""

from django.conf import settings
from storages.backends.s3boto3 import S3Boto3Storage


# our custom class will inherit the one from django storages.
# Giving it all its functionality.
class StaticStorage(S3Boto3Storage):
    location = settings.STATICFILES_LOCATION


class MediaStorage(S3Boto3Storage):
    location = settings.MEDIAFILES_LOCATION
