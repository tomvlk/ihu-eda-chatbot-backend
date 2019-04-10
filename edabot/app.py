import os
import tornado.web

from tornado.log import enable_pretty_logging
from tornado.web import RedirectHandler

from edabot.handler import AppHandler, MessageHandler, SessionHandler


class App(tornado.web.Application):
	def __init__(self, root_dir, handlers=None, default_host=None, transforms=None, **settings):
		self.root_dir = root_dir
		self.build_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), 'eda-chatbot-frontend', 'dist', 'eda-chatbot-frontend')

		print('Build Dir: ', self.build_dir)

		if not handlers:
			handlers = list()

		handlers += [
			(r'/',									RedirectHandler, dict(url='/index.html')),
			(r'/api/session', 						SessionHandler),
			(r'/api/(.*)/chat', 					MessageHandler),
			(r'/(.*)',								AppHandler, dict(path=self.build_dir)),
		]

		enable_pretty_logging()
		settings['debug'] = True
		settings['autoreload'] = False
		settings['default_handler_class'] = AppHandler

		super().__init__(handlers, default_host, transforms, **settings)


def create_app(root_dir, listen_address, listen_port):
	app = App(root_dir)
	app.listen(listen_port, listen_address)
	return app