"""
TBA API v3 specs TODO Incomplete
"""
tba_queries = (
    "/status",
    # Lists

    # "/teams/{page_num}{simple_or_keys}",
    # "/teams/{year}/{page_num}{simple_or_keys}",
    # "/team/{team_key}/events/{year}/statuses",
    # "/events/{year}{simple_or_keys}",
    # "/event/{event_key}/teams{simple_or_keys}",
    # "/event/{event_key}/teams/statuses",
    "/district/{district_key}/events{simple_or_keys}",
    # "/district/{district_key}/teams{simple_or_keys}",
    # "/district/{district_key}/rankings",

    # Team
    "/teams/{page_num}{simple_or_keys}",
    "/teams/{year}/{page_num}{simple_or_keys}",

    "/team/{team_key}",
    "/team/{team_key}/simple",
    "/team/{team_key}/years_participated",
    "/team/{team_key}/districts",
    "/team/{team_key}/robots",

    # "/team/{team_key}/events{simple_or_keys}",
    # "/team/{team_key}/events/{year}{simple_or_keys}",
    # "/team/{team_key}/events/{year}/statuses",

    # "/team/{team_key}/event/{event_key}/matches{simple_or_keys}",
    # "/team/{team_key}/event/{event_key}/awards",
    # "/team/{team_key}/event/{event_key}/status",

    "/team/{team_key}/awards",
    "/team/{team_key}/awards/{year}",

    "/team/{team_key}/matches/{year}{simple_or_keys}",

    "/team/{team_key}/media/{year}",
    "/team/{team_key}/media/tag/{media_tag}",
    "/team/{team_key}/media/tag/{media_tag}/{year}"
    "/team/{team_key}/social_media",

    # "/event/{event_key}/teams{simple_or_keys}",
    # "/event/{event_key}/teams/statuses",

    "/district/{district_key}/teams{simple_or_keys}",
    "/district/{district_key}/rankings",

    # Event
    "/team/{team_key}/events{simple_or_keys}",
    "/team/{team_key}/events/{year}{simple_or_keys}",
    "/team/{team_key}/events/{year}/statuses",

    "/team/{team_key}/event/{event_key}/matches{simple_or_keys}",
    "/team/{team_key}/event/{event_key}/awards",
    "/team/{team_key}/event/{event_key}/status",

    "/events/{year}{simple_or_keys}",
    "/event/{event_key}",
    "/event/{event_key}/simple",
    "/event/{event_key}/alliances",
    "/event/{event_key}/insights",
    "/event/{event_key}/oprs",
    "/event/{event_key}/predictions",
    "/event/{event_key}/rankings",
    "/event/{event_key}/district_points",
    "/event/{event_key}/simple",

    "/event/{event_key}/teams{simple_or_keys}",
    "/event/{event_key}/teams/statuses",

    "/event/{event_key}/matches{simple_or_keys}",
    "/event/{event_key}/matches/timeseries",
    "/event/{event_key}/awards",

    "/district/{district_key}/events{simple_or_keys}",
)
