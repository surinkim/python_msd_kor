from flask import session
import logging

class InfoFilter(logging.Filter):
    def filter(self, record):
        record.username = session.get('username', 'Anonymous')
        return True

app.logger.addFilter(InfoFilter())
