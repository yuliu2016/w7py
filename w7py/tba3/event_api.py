from ixr import event_
from .client import TBACachedSession


class TBAEventAPI:
    def __init__(self, session: "TBACachedSession", event):
        self.session = session
        self.event = event_(event)
        self.session.set_session(self.event.make_tba_string())

    def __str__(self):
        return "<TBA Event API: {}>".format(self.event.make_tba_string())

    def __repr__(self):
        return str(self)

    def info(self):
        return getattr(self.session, "event/{}".format(self.event.make_tba_string()))

    def alliances(self):
        pass

    def matches(self):
        pass

    def opr(self):
        pass

    def insights(self):
        pass

    def district_points(self):
        pass

    def predictions(self):
        pass

    def rankings(self):
        pass

    def teams(self):
        pass
