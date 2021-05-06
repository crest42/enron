from db import setup
setup()

import sys
import transforms

from maltego_trx.registry import register_transform_function, register_transform_classes
from maltego_trx.server import app, application
from maltego_trx.handler import handle_run

register_transform_classes(transforms)


class RateLimitingMiddleware(object):
	def __init__(self, app):
		self.app = app

	def __call__(self, environ, start_response):
		# TODO add rate limiting mechanism
		return self.app(environ, start_response)


app.wsgi_app = RateLimitingMiddleware(app.wsgi_app)

handle_run(__name__, sys.argv, app)
