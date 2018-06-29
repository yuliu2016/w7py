from .client import TBACachedSession


class TBABaseAPI:
    def __init__(self, session: "TBACachedSession"):
        self.session = session

    def q(self, query, args):
        return getattr(self.session, self.session.query_args.create_url(query, **args))

    def status(self):
        return self.q("/status", {})

    def team_events(self, **kw):
        return self.q("/team/{team_key}/events", kw)

    def team_events_simple(self, **kw):
        return self.q("/team/{team_key}/events/simple", kw)

    def team_events_keys(self, **kw):
        return self.q("/team/{team_key}/events/keys", kw)

    def team_events_in_year(self, **kw):
        return self.q("/team/{team_key}/events/{year}", kw)

    def team_events_in_year_simple(self, **kw):
        return self.q("/team/{team_key}/events/{year}/simple", kw)

    def team_events_in_year_keys(self, **kw):
        return self.q("/team/{team_key}/events/{year}/keys", kw)

    def team_events_in_year_statuses(self, **kw):
        return self.q("/team/{team_key}/events/{year}/statuses", kw)

    def team_event_matches(self, **kw):
        return self.q("/team/{team_key}/event/{event_key}/matches", kw)

    def team_event_matches_simple(self, **kw):
        return self.q("/team/{team_key}/event/{event_key}/matches/simple", kw)

    def team_event_matches_keys(self, **kw):
        return self.q("/team/{team_key}/event/{event_key}/matches/keys", kw)

    def team_event_awards(self, **kw):
        return self.q("/team/{team_key}/event/{event_key}/awards", kw)

    def team_event_status(self, **kw):
        return self.q("/team/{team_key}/event/{event_key}/status", kw)

    def events_in_year(self, **kw):
        return self.q("/events/{year}", kw)

    def events_in_year_simple(self, **kw):
        return self.q("/events/{year}/simple", kw)

    def events_in_year_keys(self, **kw):
        return self.q("/events/{year}/keys", kw)

    def event(self, **kw):
        return self.q("/event/{event_key}", kw)

    def event_simple(self, **kw):
        return self.q("/event/{event_key}/simple", kw)

    def event_alliances(self, **kw):
        return self.q("/event/{event_key}/alliances", kw)

    def event_insights(self, **kw):
        return self.q("/event/{event_key}", kw)

    def event_oprs(self, **kw):
        return self.q("/event/{event_key}", kw)

    def event_predictions(self, **kw):
        return self.q("/event/{event_key}", kw)

    def event_rankings(self, **kw):
        return self.q("/event/{event_key}/rankings", kw)

    def event_district_points(self, **kw):
        return self.q("/event/{event_key}/district_points", kw)

    def event_teams(self, **kw):
        return self.q("/event/{event_key}", kw)

    def event_teams_simple(self, **kw):
        return self.q("/event/{event_key}", kw)

    def event_teams_keys(self, **kw):
        return self.q("/event/{event_key}", kw)

    def event_teams_statuses(self, **kw):
        return self.q("/event/{event_key}", kw)

    def event_matches(self, **kw):
        return self.q("/event/{event_key}", kw)

    def event_matches_simple(self, **kw):
        return self.q("/event/{event_key}", kw)

    def event_matches_keys(self, **kw):
        return self.q("/event/{event_key}", kw)

    def event_matches_timeseries(self, **kw):
        return self.q("/event/{event_key}", kw)

    def event_awards(self, **kw):
        return self.q("/event/{event_key}", kw)

    def district_events(self, **kw):
        return self.q("/district/{district_key}/events", kw)

    def district_events_simple(self, **kw):
        return self.q("/district/{district_key}/events/simple", kw)

    def district_events_keys(self, **kw):
        return self.q("/district/{district_key}/events/keys", kw)
