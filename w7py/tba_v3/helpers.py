import pandas as pd

from .api import TBARawAPI
from .client import TBACachedSession
from .exceptions import *

__all__ = ["event_helper"]


class TBABaseHelper:
    def __init__(self, session: "TBACachedSession"):
        self._api = TBARawAPI(session)

    def _get_api(self) -> "TBARawAPI":
        return self._api


class TBAEventHelper(TBABaseHelper):
    def __init__(self, session: "TBACachedSession"):
        super().__init__(session)
        if "event_key" not in session.query_args.tba_args:
            raise TBARequiredArgumentNotError("Cannot use TBAEventHelper without an event")
        self.event_key = session.query_args.tba_args["event_key"]

    def list_matches(self, simple: "bool" = False) -> "dict":
        if simple:
            return self._api.event_matches_simple()
        else:
            return self._api.event_matches()

    def qualification_match_schedule(self,
                                     use_df=True,
                                     df_one_indexed=True,
                                     transpose=False,
                                     convert_to_int=True):

        positions = [(colour, number) for colour in ["Red", "Blue"] for number in [0, 1, 2]]
        qualification_matches = {match["match_number"]: match
                                 for match in self.list_matches(simple=True) if match["comp_level"] == "qm"}

        schedule_rows = []
        for match_number in sorted(qualification_matches.keys()):
            match_data = qualification_matches[match_number]
            schedule_row = {}
            for colour, number in positions:
                match_key = match_data["alliances"][colour.lower()]["team_keys"][number]
                if convert_to_int:
                    match_value = int(match_key[3:])
                else:
                    match_value = match_key
                schedule_row["{} {}".format(colour, number + 1)] = match_value
            schedule_rows.append(schedule_row)

        columns = ["{} {}".format(colour, number + 1) for colour, number in positions]

        if use_df:
            table = pd.DataFrame(schedule_rows, columns=columns)
            if df_one_indexed:
                table.index += 1
            if transpose:
                return table.T
            else:
                return table
        else:
            if transpose:
                return {column: [row[column] for row in schedule_rows] for column in columns}
            else:
                return schedule_rows


event_helper = TBAEventHelper
