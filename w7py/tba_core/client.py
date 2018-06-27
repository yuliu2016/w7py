import json
import os
import pickle
from contextlib import contextmanager
from urllib import request as urllib_request

import requests

from const import *
from .session import TBASession

_connection_test_ip = 'http://216.58.192.142'
_connection_test_query = "team/frc865"


class TBAClient:

    def __init__(self):
        self.auth_key = ''
        self.cache_directory = ''
        self.set_cache(os.getcwd())
        self.sessions = []

    def set_key(self, key):
        self.auth_key = key

    def set_cache(self, cache_directory):
        self.cache_directory = os.path.join(cache_directory, DIR_PREFIX_TBA_CACHE)
        if os.path.exists(self.cache_directory):
            sessions_path = os.path.join(self.cache_directory, TBA_CLIENT_SESSIONS_FILE)
            self.sessions = pickle.load(sessions_path)

    def check_tba_keyed_connection(self):
        if self.auth_key:
            try:
                urllib_request.urlopen(_connection_test_ip, timeout=1)  # Test for internet
                res = self.raw_json(_connection_test_query)  # Test for the Blue Alliance
                if len(res.keys()) == 1:
                    raise requests.RequestException("The TBA Key is incorrect!!")
            except urllib_request.URLError:
                raise requests.ConnectionError("Cannot Connect to the Internet")
        else:
            raise ValueError("No TBA key set. Get one from the website!")

    def get_request_headers(self):
        return {'X-TBA-Auth-Key': self.auth_key}

    def raw_json(self, url: "str") -> "dict":
        return requests.get(TBA_BASE_URL + url, headers=self.get_request_headers()).json()

    @contextmanager
    def cached_session(self, session_name: "str"):
        self.check_tba_keyed_connection()
        if session_name not in self.sessions:
            self.sessions.append(session_name)
        if not os.path.exists(self.cache_directory):
            os.makedirs(self.cache_directory)
        json_path = os.path.join(self.cache_directory, "{}.json".format(session_name))
        pkl_path = os.path.join(self.cache_directory, "{}.pkl".format(session_name))
        loaded_cache = {}
        if os.path.exists(pkl_path):
            with open(pkl_path, "rb") as pickle_cache:
                loaded_cache = pickle.load(pickle_cache)
        elif os.path.exists(json_path):
            with open(json_path, "r") as json_cache:
                loaded_cache = json.load(json_cache)
        session = TBASession(loaded_cache)
        yield session
        res_cache = session.cache
        if not res_cache:  # File need to be removed here due to clear_cache
            if os.path.exists(json_path):
                os.remove(json_path)
            if os.path.exists(pkl_path):
                os.remove(pkl_path)
        else:
            with open(json_path, "w") as json_file:
                json.dump(res_cache, json_file, indent=4)
            with open(pkl_path, "wb") as pickle_file:
                pickle.dump(res_cache, pickle_file)
