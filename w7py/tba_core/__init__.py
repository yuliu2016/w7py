from .client import TBAClient as _TBAClient
from .client import client_instance as _tba_instance
from .exceptions import *

__all__ = ["TBANoCacheAvailableException",
           "TBASessionAlreadyUsedException",
           "set_key",
           "set_cache",
           "cached_session"]


def set_key(key: "str"):
    _tba_instance.set_key(key)


def set_cache(cache_directory: "str"):
    _tba_instance.set_cache(cache_directory)


def cached_session(online_only: "bool" = False, no_cache_value: "str" = "empty_dict",
                   connection_test_ip: "str" = 'http://216.58.192.142',
                   connection_test_query: "str" = "team/frc865"):
    return _tba_instance.cached_session(online_only, no_cache_value, connection_test_ip, connection_test_query)
