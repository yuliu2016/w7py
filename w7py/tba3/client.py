import json
import os
import pickle
from contextlib import contextmanager
from urllib import request as urllib_request

import requests

from .exceptions import *


class TBAClient:

    @contextmanager
    def cached_session(self,
                       write_json: "bool" = True,
                       overwrite_id: "str" = "",
                       online_only: "bool" = False,
                       no_cache_value: "str" = "empty_dict",
                       existing_args=None,
                       **preset_tba_args):
        """
        Creates a cached session to access the TBA API
        :param write_json: whether the json file should be made (may slow down slightly)
        :param overwrite_id: specifies the session id to overwrite (especially for testing)
        :param online_only: specifies raising an error if not connected
        :param no_cache_value: specifies the value to return if no cache is found, or "raise" to raise exception
        :param existing_args: if not None, specifies a previous argument set
        :param preset_tba_args: query arguments that will union with newer arguments when requested,
               and includes "team_key", "district_key", "match_key", "event_key", "year", "media_tag", "page_num"
        :return: A context managed object to be used for TBA requests
        """
        connection_test_ip: "str" = 'http://216.58.192.142'
        connection_test_tba_query: "str" = "/team/frc865"
        is_connectible = True
        if self.auth_key:
            try:
                urllib_request.urlopen(connection_test_ip, timeout=1)  # Test for internet connection
            except urllib_request.URLError:
                is_connectible = False
                if online_only:
                    raise requests.ConnectionError("Cannot Connect to the Internet")
            if is_connectible:
                res = self.raw_json(connection_test_tba_query)  # Test for the Blue Alliance connection
                if len(res.keys()) == 1:
                    is_connectible = False
                    if online_only:
                        raise requests.RequestException("The TBA Key is incorrect!!")
        else:
            is_connectible = False
            if online_only:
                raise ValueError("No TBA key set. Get one from the website!")
        if type(existing_args) is TBAQueryArguments:
            q_args = existing_args
        else:
            q_args = TBAQueryArguments(**preset_tba_args)
        if overwrite_id:
            session_id = overwrite_id
        elif q_args:
            session_id = str(q_args)
        else:
            session_id = "main"
        if not os.path.exists(self.cache_directory):
            os.makedirs(self.cache_directory)
        pkl_path = os.path.join(self.cache_directory, "${}.pkl".format(session_id))
        pkl_exists = os.path.exists(pkl_path)
        json_path = os.path.join(self.cache_directory, "{}.json".format(session_id))
        json_exists = os.path.exists(json_path)
        loaded_cache = {}
        if pkl_exists:
            with open(pkl_path, "rb") as pickle_cache:
                loaded_cache = pickle.load(pickle_cache)
        session = TBACachedSession(self)
        session.session_cache = loaded_cache
        session.is_connectible = is_connectible
        session.online_only = online_only
        session.no_cache_value = no_cache_value
        session.query_args = q_args
        yield session
        res_cache = session.session_cache
        if res_cache:
            with open(pkl_path, "wb") as pickle_file:
                pickle.dump(res_cache, pickle_file)
            if write_json:
                with open(json_path, "w") as json_file:
                    json.dump(res_cache, json_file, indent=2)
        else:  # File need to be removed here due to clear_cache
            if json_exists:
                os.remove(json_path)
            if pkl_exists:
                os.remove(pkl_path)

    def __init__(self):
        self.auth_key = ''
        self.cache_directory = ''
        self.set_cache(os.getcwd())

    def set_key(self, key):
        self.auth_key = key

    def set_cache(self, cache_directory: "str"):
        self.cache_directory = os.path.join(cache_directory, self.DIR_PREFIX_TBA_CACHE)

    def get_request_headers(self):
        return {'X-TBA-Auth-Key': self.auth_key}

    def raw_json(self, url: "str") -> "dict":
        return requests.get(self.TBA_BASE_URL + url, headers=self.get_request_headers()).json()

    TBA_BASE_URL = "https://www.thebluealliance.com/api/v3"
    DIR_PREFIX_TBA_CACHE = "w7/.tba-cache/"


class TBACachedSession:
    def __init__(self, parent_client: "TBAClient"):
        self.__parent_client = parent_client
        self.is_connectible = True
        self.online_only = False
        self.session_cache = {}
        self.session_name = ""
        self.no_cache_value = "empty_dict"
        self.query_args: "TBAQueryArguments" = None

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

    def clear_cache(self):
        self.session_cache = {}


class TBAQueryArguments:
    ARGS_KEYS = ["team_key", "district_key", "match_key", "event_key", "year", "media_tag", "page_num"]

    def __init__(self, **tba_args):
        self.tba_args = tba_args

    def create_url(self, query_template: str, **union_args):
        new_args = {**self.tba_args, **union_args}
        try:
            return query_template.format(**new_args)
        except KeyError as err:
            raise TBARequiredArgumentNotSpecified("Argument " + str(err) + " was not specified")

    def __str__(self):
        return "-".join(self.tba_args[key] for key in sorted(self.tba_args.keys()) if key in self.ARGS_KEYS)

    def __bool__(self):
        return bool(list(key for key in self.tba_args.keys() if key in self.ARGS_KEYS))


client_instance = TBAClient()
