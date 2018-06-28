import json
import os
import pickle
from contextlib import contextmanager
from urllib import request as urllib_request

import requests

from const import *
from .exceptions import *


class TBACachedSession:
    def __init__(self, parent_client: "TBAClient"):
        self.__parent_client = parent_client
        self.__session_already_set = False
        self.is_connectible = True
        self.online_only = False
        self.session_cache = {}
        self.session_name = ""
        self.no_cache_value = "empty_dict"

    def __getattr__(self, item) -> "dict":
        if self.online_only:
            return self.__parent_client.raw_json(item)
        if item in self.session_cache.keys():
            return self.session_cache[item]
        if not self.is_connectible:
            if self.no_cache_value == "raise":
                raise TBANoCacheAvailableException("No cache for query '{}'".format(item))
            return {}
        res = self.__parent_client.raw_json(item)
        self.session_cache[item] = res
        return res

    def set_session(self, name: "str" = ""):
        if type(name) is str and name.isalnum():
            if not self.__session_already_set:
                self.session_name = name
                self.session_cache = self.__parent_client.load_cache_data(name)
                self.__session_already_set = True
            else:
                raise TBASessionAlreadyUsedException("Session already set for {}"
                                                     .format(self.session_name))


class TBAClient:

    def __init__(self):
        self.auth_key = ''
        self.cache_directory = ''
        self.set_cache(os.getcwd())

    def set_key(self, key):
        self.auth_key = key

    def set_cache(self, cache_directory: "str"):
        self.cache_directory = os.path.join(cache_directory, DIR_PREFIX_TBA_CACHE)

    def get_request_headers(self):
        return {'X-TBA-Auth-Key': self.auth_key}

    def raw_json(self, url: "str") -> "dict":
        return requests.get(TBA_BASE_URL + url, headers=self.get_request_headers()).json()

    def compute_paths(self, session_name):
        if not os.path.exists(self.cache_directory):
            os.makedirs(self.cache_directory)
        json_path = os.path.join(self.cache_directory, "{}.json".format(session_name))
        pkl_path = os.path.join(self.cache_directory, "{}.pkl".format(session_name))
        pkl_exists = os.path.exists(pkl_path)
        json_exists = os.path.exists(json_path)
        return (json_path, json_exists), (pkl_path, pkl_exists)

    def load_cache_data(self, session_name):
        _, (pkl_path, pkl_exists) = self.compute_paths(session_name)
        if pkl_exists:
            with open(pkl_path, "rb") as pickle_cache:
                return pickle.load(pickle_cache)
        return {}

    @contextmanager
    def cached_session(self,
                       online_only: "bool" = False,
                       no_cache_value: "str" = "empty_dict",
                       connection_test_ip='http://216.58.192.142',
                       connection_test_query="team/frc865"):
        is_connectible = True
        if self.auth_key:
            try:
                urllib_request.urlopen(connection_test_ip, timeout=1)  # Test for internet connection
            except urllib_request.URLError:
                is_connectible = False
                if online_only:
                    raise requests.ConnectionError("Cannot Connect to the Internet")
            if is_connectible:
                res = self.raw_json(connection_test_query)  # Test for the Blue Alliance connection
                if len(res.keys()) == 1:
                    is_connectible = False
                    if online_only:
                        raise requests.RequestException("The TBA Key is incorrect!!")
        else:
            is_connectible = False
            if online_only:
                raise ValueError("No TBA key set. Get one from the website!")
        session = TBACachedSession(self)
        session.is_connectible = is_connectible
        session.online_only = online_only
        session.no_cache_value = no_cache_value
        yield session
        res_name = session.session_name
        if res_name:
            res_cache = session.session_cache
            (json_path, json_exists), (pkl_path, pkl_exists) = self.compute_paths(res_name)
            if not res_cache:  # File need to be removed here due to clear_cache
                if json_exists:
                    os.remove(json_path)
                if pkl_exists:
                    os.remove(pkl_path)
            else:
                with open(json_path, "w") as json_file:
                    json.dump(res_cache, json_file, indent=4)
                with open(pkl_path, "wb") as pickle_file:
                    pickle.dump(res_cache, pickle_file)


client_instance = TBAClient()
