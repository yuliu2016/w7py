import tbapy

__all__ = ["tba_"]


class _TBAPyWrapper(tbapy.TBA):

    def __init__(self):
        super().__init__("")

    def set_key(self, auth_key):
        self.auth_key = auth_key

    def get_raw(self, url):
        return super()._get(url)


tba_ = _TBAPyWrapper()
