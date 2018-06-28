from .exceptions import TBARequiredArgumentNotSpecified

__all__ = ["TBAQueryArguments"]
ARGS_KEYS = ["team_key", "district_key", "match_key", "event_key", "year", "media_tag", "page_num"]


class TBAQueryArguments:
    def __init__(self, **tba_args):
        self.tba_args = tba_args

    def create_url(self, query_template: str, **union_args):
        new_args = {**self.tba_args, **union_args}
        try:
            return query_template.format(**new_args)
        except KeyError as err:
            raise TBARequiredArgumentNotSpecified("Argument " + str(err) + " was not specified")

    def __str__(self):
        return "-".join(self.tba_args[key] for key in sorted(self.tba_args.keys()) if key in ARGS_KEYS)

    def __bool__(self):
        return bool(list(key for key in self.tba_args.keys() if key in ARGS_KEYS))
