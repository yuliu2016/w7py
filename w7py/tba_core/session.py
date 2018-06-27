import json
import os
import pickle
from urllib import request as urllib_request

import requests

from const import *

_connection_test_ip = 'http://216.58.192.142'
_connection_test_query = "team/frc865"


class TBASession:

    def __init__(self, use_cache=True, cache_dir="default"):
        self.auth_key = ""
        self.use_cache = use_cache
        self.tba_key_checked = False
        self.cache = {}
        if self.use_cache:
            if cache_dir == "default":
                self.cache_dir = os.path.join(os.getcwd(), DIR_PREFIX_TBA_CACHE)
            else:
                if os.path.exists(cache_dir):
                    self.cache_dir = cache_dir
                else:
                    raise NotADirectoryError("Cache directory does not exist")
            self.load_cache()

    def load_cache(self):
        if self.use_cache:
            dir_cont = os.listdir(self.cache_dir)
            if TBA_CACHE_PICKLE in dir_cont:
                cache_fp = os.path.join(self.cache_dir, TBA_CACHE_PICKLE)
                with open(cache_fp, "rb") as cache_file:
                    self.cache = pickle.load(cache_file)
            elif TBA_CACHE_JSON in dir_cont:
                cache_fp = os.path.join(self.cache_dir, TBA_CACHE_JSON)
                with open(cache_fp, "r") as cache_file:
                    self.cache = json.load(cache_file)

    def save_cache(self):
        json_fp = os.path.join(self.cache_dir, TBA_CACHE_JSON)
        pickle_fp = os.path.join(self.cache_dir, TBA_CACHE_PICKLE)
        if not self.cache:  # File need to be removed here due to clear_cache
            if os.path.exists(json_fp):
                os.remove(json_fp)
            if os.path.exists(pickle_fp):
                os.remove(pickle_fp)
        if self.use_cache:
            with open(json_fp, "w") as json_file:
                json.dump(self.cache, json_file, indent=4)
            with open(pickle_fp, "wb") as pickle_file:
                pickle.dump(self.cache, pickle_file)

    def get_request_headers(self):
        return {'X-TBA-Auth-Key': self.auth_key}

    def _raw_json(self, url: "str") -> "dict":
        return requests.get(TBA_BASE_URL + url, headers=self.get_request_headers()).json()

    def _checked_json(self, url: "str") -> "dict":
        if not self.tba_key_checked:
            self.check_tba_keyed_connection()
            self.tba_key_checked = True
        return self._raw_json(url)

    def get_json(self, url: "str") -> "dict":
        if self.use_cache and url in self.cache.keys():
            return self.cache[url]
        res = self._checked_json(url)
        if self.use_cache:
            self.cache[url] = res
        return res

    def clear_cache(self):
        self.cache = {}

    def check_tba_keyed_connection(self):
        if self.auth_key:
            try:
                urllib_request.urlopen(_connection_test_ip, timeout=1)  # Test for the connection
                res = self._raw_json(_connection_test_query)
                if len(res.keys()) == 1:
                    raise requests.RequestException("The TBA Key is incorrect!!")
            except urllib_request.URLError:
                raise requests.ConnectionError("Cannot Connect to the Internet")
        else:
            raise ValueError("No TBA key set. Get one from the website!")

    def set_key(self, auth_key: "str"):
        self.auth_key = auth_key
