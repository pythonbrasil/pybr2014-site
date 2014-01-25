from storages.backends.s3boto import S3BotoStorage
from django.utils.functional import SimpleLazyObject
from django.contrib.staticfiles.storage import CachedFilesMixin


class CachedS3BotoStorage(CachedFilesMixin, S3BotoStorage):
    pass

StaticRootS3BotoStorage = lambda: CachedS3BotoStorage(location='static')
MediaRootS3BotoStorage  = lambda: S3BotoStorage(location='media')
