from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class Mailer:
	def __init__(self):
		self.message = MIMEMultipart()

	def setup(self, sender, subject, recipients=None):
		pass

	def add_attachment(self, attach):
		pass

	def add_html(self, html):
		pass

	def add_text(self, text):
		pass
