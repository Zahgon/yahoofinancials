import logging
import time
import random
import peewee as _peewee
from threading import Lock
import os as _os
import appdirs as _ad
import atexit as _atexit
import datetime as _datetime
import pickle as _pkl

_cache_init_lock = Lock()


# --------------
# TimeZone cache
# --------------

class _TzCacheException(Exception):
    pass


class _TzCacheDummy:
    """Dummy cache to use if tz cache is disabled"""

    def lookup(self, tkr):
        pass

    def store(self, tkr, tz):
        pass

    @property
    def tz_db(self):
        pass


class _TzCacheManager:
    _tz_cache = None

    @classmethod
    def get_tz_cache(cls):
        pass

    @classmethod
    def _initialise(cls, cache_dir=None):
        pass


class _TzDBManager:
    _db = None
    _cache_dir = _os.path.join(_ad.user_cache_dir(), "py-yfinance")

    @classmethod
    def get_database(cls):
        pass

    @classmethod
    def close_db(cls):
        pass

    @classmethod
    def _initialise(cls, cache_dir=None):
        pass

    @classmethod
    def set_location(cls, new_cache_dir):
        pass

    @classmethod
    def get_location(cls):
        pass


# close DB when Python exists
_atexit.register(_TzDBManager.close_db)

tz_db_proxy = _peewee.Proxy()


class _KV(_peewee.Model):
    key = _peewee.CharField(primary_key=True)
    value = _peewee.CharField(null=True)

    class Meta:
        database = tz_db_proxy
        without_rowid = True


class _TzCache:
    def __init__(self):
        self.initialised = -1
        self.db = None
        self.dummy = False

    def get_db(self):
        pass

    def initialise(self):
        pass

    def lookup(self, key):
        pass

    def store(self, key, value):
        pass


def get_tz_cache():
    pass


def set_tz_cache_location(cache_dir: str):
    """
    Sets the path to create the "py-yfinance" cache folder in.
    Useful if the default folder returned by "appdir.user_cache_dir()" is not writable.
    Must be called before cache is used (that is, before fetching tickers).
    :param cache_dir: Path to use for caches
    :return: None
    """
    pass


# --------------
# Cookie cache
# --------------

class _CookieCacheException(Exception):
    pass


class _CookieCacheDummy:
    """Dummy cache to use if Cookie cache is disabled"""

    def lookup(self, tkr):
        pass

    def store(self, tkr, Cookie):
        pass

    @property
    def Cookie_db(self):
        pass


class _CookieCacheManager:
    _Cookie_cache = None

    @classmethod
    def get_cookie_cache(cls):
        pass

    @classmethod
    def _initialise(cls, cache_dir=None):
        pass


class _CookieDBManager:
    _db = None
    _cache_dir = _os.path.join(_ad.user_cache_dir(), "py-yfinance")

    @classmethod
    def get_database(cls):
        pass

    @classmethod
    def close_db(cls):
        pass

    @classmethod
    def _initialise(cls, cache_dir=None):
        pass

    @classmethod
    def set_location(cls, new_cache_dir):
        pass

    @classmethod
    def get_location(cls):
        pass


# close DB when Python exists
_atexit.register(_CookieDBManager.close_db)

Cookie_db_proxy = _peewee.Proxy()


class _CookieSchema(_peewee.Model):
    strategy = _peewee.CharField(primary_key=True)
    fetch_date = _peewee.DateTimeField(default=_datetime.datetime.now)

    # Which cookie type depends on strategy
    cookie_bytes = _peewee.BlobField()

    class Meta:
        database = Cookie_db_proxy
        without_rowid = True


class _CookieCache:
    def __init__(self):
        self.initialised = -1
        self.db = None
        self.dummy = False

    def get_db(self):
        pass

    def initialise(self):
        pass

    def lookup(self, strategy):
        pass

    def store(self, strategy, cookie):
        pass
            # # Integrity error means the strategy already exists. Try updating the strategy.
            # old_value = self.lookup(strategy)
            # if old_value != cookie:
            #     get_yf_logger().debug(f"cookie for strategy {strategy} changed from {old_value} to {cookie}.")
            #     with db.atomic():
            #         q = _CookieSchema.update(cookie=cookie).where(_CookieSchema.strategy == strategy)
            #         q.execute()


def get_cookie_cache():
    pass
