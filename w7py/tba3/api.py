from .client import TBACachedSession


class _APIQueryDecorationWrapper:

    @classmethod
    def query(cls, query_url_function):
        def fetch_query(self: "TBARawAPI", *_, **kwargs) -> "dict":
            url = self.session.query_args.create_url(query_url_function(self), **kwargs)
            return getattr(self.session, url)

        return fetch_query


class TBARawAPI:
    _query = _APIQueryDecorationWrapper.query

    def __init__(self, session: "TBACachedSession"):
        self.session = session

    @_query
    def status(self):
        return "/status"

    @_query
    def teams_by_page_num(self):
        return "/team/{page_num}"

    @_query
    def teams_by_page_num_simple(self):
        return "/team/{page_num}/simple"

    @_query
    def teams_by_page_num_keys(self):
        return "/team/{page_num}/keys"

    @_query
    def teams_in_year_by_page_num(self):
        return "/team/{year}/{page_num}"

    @_query
    def teams_in_year_by_page_num_simple(self):
        return "/team/{year}/{page_num}/simple"

    @_query
    def teams_in_year_by_page_num_keys(self):
        return "/team/{year}/{page_num}/keys"

    @_query
    def team(self):
        return "/team/{team_key}"

    @_query
    def team_simple(self):
        return "/team/{team_key}"

    @_query
    def team_years_participated(self):
        return "/team/{team_key}"

    @_query
    def team_districts(self):
        return "/team/{team_key}"

    @_query
    def team_robots(self):
        return "/team/{team_key}"

    @_query
    def team_awards(self):
        return "/team/{team_key}/awards"

    @_query
    def team_awards_year(self):
        return "/team/{team_key}/awards/{year}"

    @_query
    def team_matches_in_year(self):
        return "/team/{team_key}/matches/{year}"

    @_query
    def team_matches_in_year_simple(self):
        return "/team/{team_key}/matches/{year}/simple"

    @_query
    def team_matches_in_year_keys(self):
        return "/team/{team_key}/matches/{year}/keys"

    @_query
    def team_media_in_year(self):
        return "/team/{team_key}/media/{year}"

    @_query
    def team_media_by_tag(self):
        return "/team/{team_key}/media/tag/{media_tag}"

    @_query
    def team_media_by_tag_in_year(self):
        return "/team/{team_key}/media/tag/{media_tag}/{year}"

    @_query
    def team_social_media(self):
        return "/team/{team_key}/social_media"

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
        return "/event/{event_key}/insights"

    @_query
    def event_oprs(self):
        return "/event/{event_key}/oprs"

    @_query
    def event_predictions(self):
        return "/event/{event_key}/predictions"

    @_query
    def event_rankings(self):
        return "/event/{event_key}/rankings"

    @_query
    def event_district_points(self):
        return "/event/{event_key}/district_points"

    @_query
    def event_teams(self):
        return "/event/{event_key}/teams"

    @_query
    def event_teams_simple(self):
        return "/event/{event_key}/teams/simple"

    @_query
    def event_teams_keys(self):
        return "/event/{event_key}/teams/keys"

    @_query
    def event_teams_statuses(self):
        return "/event/{event_key}/teams/statuses"

    @_query
    def event_matches(self):
        return "/event/{event_key}/matches"

    @_query
    def event_matches_simple(self):
        return "/event/{event_key}/matches/simple"

    @_query
    def event_matches_keys(self):
        return "/event/{event_key}/matches/keys"

    @_query
    def event_matches_timeseries(self):
        return "/event/{event_key}/matches/timeseries"

    @_query
    def event_awards(self):
        return "/event/{event_key}/awards"

    @_query
    def district_events(self):
        return "/district/{district_key}/events"

    @_query
    def district_events_simple(self):
        return "/district/{district_key}/events/simple"

    @_query
    def district_events_keys(self):
        return "/district/{district_key}/events/keys"
