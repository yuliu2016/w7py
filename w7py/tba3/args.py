from .exceptions import TBARequiredArgumentNotSpecified


class TBAArguments:
    def __init__(self, **kwargs):
        self.tba_args = kwargs

    def create_url(self, query_template: str, **union_args):
        new_args = {**self.tba_args, **union_args}
        try:
            return query_template.format(**new_args)
        except KeyError as err:
            raise TBARequiredArgumentNotSpecified("Argument " + str(err) + " was not specified")

    def __str__(self):
        return "-".join(self.tba_args[key] for key in sorted(self.tba_args.keys()))
