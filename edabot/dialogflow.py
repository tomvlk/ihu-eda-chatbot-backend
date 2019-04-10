import json
import os
import uuid
import dialogflow_v2 as dialogflow


class Dialogflow:
	INSTANCE = None

	def __new__(cls, *args, **kwargs):
		if not cls.INSTANCE:
			cls.INSTANCE = super().__new__(cls, *args, **kwargs)
		return cls.INSTANCE

	def __init__(self):
		json_file = os.path.join(os.path.abspath(os.path.dirname(os.path.dirname(__file__))), 'key.json')
		self.session_client = dialogflow.SessionsClient.from_service_account_json(json_file)
		self.project_id = 'ihu-try-1'

	def create_session(self, session_id=None):
		if not session_id:
			session_id = uuid.uuid4().hex
		return self.session_client.session_path(self.project_id, session_id), session_id

	def load_session(self, session_id):
		return self.session_client.session_path(self.project_id, session_id)

	def query(self, text, session):
		text_input = dialogflow.types.TextInput(text=text, language_code='en')
		query_input = dialogflow.types.QueryInput(text=text_input)
		response = self.session_client.detect_intent(
			session=session, query_input=query_input,
		)
		return response.query_result.fulfillment_text
