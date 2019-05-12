import json
import logging
import os
from json import JSONDecodeError

import tornado.web

from typing import Optional

from edabot.dialogflow import Dialogflow


class AppHandler(tornado.web.StaticFileHandler):
	def validate_absolute_path(self, root: str, absolute_path: str) -> Optional[str]:
		# flow = Dialogflow()
		# session = flow.create_session()
		# flow.query('Hi', session)

		try:
			return super().validate_absolute_path(root, absolute_path)
		except tornado.web.HTTPError as e:
			if e.status_code == 404:
				return super().validate_absolute_path(
					root, os.path.join(self.application.build_dir, 'index.html')
				)
			raise e


class SessionHandler(tornado.web.RequestHandler):
	SUPPORTED_METHODS = ('POST',)

	def post(self, *args, **kwargs):
		self.write(dict(
			session_id=Dialogflow().create_session()[1]
		))


class MessageHandler(tornado.web.RequestHandler):
	SUPPORTED_METHODS = ('POST',)

	def post(self, session_id, **kwargs):
		flow = Dialogflow()
		session = flow.load_session(session_id)
		try:
			data = json.loads(self.request.body.decode())
			if 'text' not in data:
				raise Exception('Text not in body')
		except Exception as e:
			logging.exception(e)
			self.send_error(status_code=400)
			return

		response = flow.query(data['text'], session)

		self.write(dict(
			response=response[0], id=response[1],
		))
