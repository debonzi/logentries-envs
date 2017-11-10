# -*- coding: utf-8 -*-
import os
from logentries import LogentriesHandler as _LogentriesHandler


class LogentriesHandler(_LogentriesHandler):
    def __init__(self, token='', envvar_name='LOGENTRIES_TOKEN', **kwargs):
        _token = os.getenv(envvar_name, token)
        super(LogentriesHandler, self).__init__(_token, **kwargs)
