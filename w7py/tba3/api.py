from .client import TBACachedSession


class _APIQueryDecorationWrapper:

    @classmethod
    def query(cls, query_url_function):
        def fetch_query(self: "TBARawAPI", *_, **kwargs):
            url = self.session.query_args.create_url(query_url_function(self), **kwargs)
            return getattr(self.session, url)

        return fetch_query


class TBARawAPI:
    _query = _APIQueryDecorationWrapper.query

    def __init__(self, session: "TBACachedSession"):
        self.session = session

    # def q(self, query, args):
    #     return getattr(self.session, self.session.query_args.create_url(query, **args))

    @_query
    def status(self):
        return "/status"

    @_query
    def team_events(self):
        return "/team/{team_key}/events"

    @_query
    def team_events_simple(self):
        return "/team/{team_key}/events/simple"

    @_query
    def team_events_keys(self):
        return "/team/{team_key}/events/keys"

    @_query
    def team_events_in_year(self):
        return "/team/{team_key}/events/{year}"

    @_query
    def team_events_in_year_simple(self):
        return "/team/{team_key}/events/{year}/simple"

    @_query
    def team_events_in_year_keys(self):
        return "/team/{team_key}/events/{year}/keys"

    @_query
    def team_events_in_year_statuses(self):
        return "/team/{team_key}/events/{year}/statuses"

    @_query
    def team_event_matches(self):
        return "/team/{team_key}/event/{event_key}/matches"

    @_query
    def team_event_matches_simple(self):
        return "/team/{team_key}/event/{event_key}/matches/simple"

    @_query
    def team_event_matches_keys(self):
        return "/team/{team_key}/event/{event_key}/matches/keys"

    @_query
    def team_event_awards(self):
        return "/team/{team_key}/event/{event_key}/awards"

    @_query
    def team_event_status(self):
        return "/team/{team_key}/event/{event_key}/status"

    @_query
    def events_in_year(self):
        return "/events/{year}"

    @_query
    def events_in_year_simple(self):
        return "/events/{year}/simple"

    @_query
    def events_in_year_keys(self):
        return "/events/{year}/keys"

    @_query
    def event(self):
        return "/event/{event_key}"

    @_query
    def event_simple(self):
        return "/event/{event_key}/simple"

    @_query
    def event_alliances(self):
        return "/event/{event_key}/alliances"

    @_query
    def event_insights(self):
        return "/event/{event_key}"

    @_query
    def event_oprs(self):
        return "/event/{event_key}"

    @_query
    def event_predictions(self):
        return "/event/{event_key}"

    @_query
    def event_rankings(self):
        return "/event/{event_key}/rankings"

    @_query
    def event_district_points(self):
        return "/event/{event_key}/district_points"

    @_query
    def event_teams(self):
        return "/event/{event_key}"

    @_query
    def event_teams_simple(self):
        return "/event/{event_key}"

    @_query
    def event_teams_keys(self):
        return "/event/{event_key}"

    @_query
    def event_teams_statuses(self):
        return "/event/{event_key}"

    @_query
    def event_matches(self):
        return "/event/{event_key}"

    @_query
    def event_matches_simple(self):
        return "/event/{event_key}"

    @_query
    def event_matches_keys(self):
        return "/event/{event_key}"

    @_query
    def event_matches_timeseries(self):
        return "/event/{event_key}"

    @_query
    def event_awards(self):
        return "/event/{event_key}"

    @_query
    def district_events(self):
        return "/district/{district_key}/events"

    @_query
    def district_events_simple(self):
        return "/district/{district_key}/events/simple"

    @_query
    def district_events_keys(self):
        return "/district/{district_key}/events/keys"
