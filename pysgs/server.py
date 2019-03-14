import smtplib

class Server:
    def __init__(self, api_key=''):
        """
        Create SMTP server
        """
        self.api_key = api_key
        self.api_user = 'apikey'
        self.smtp_host = 'smtp.sendgrid.net'
        self.smtp_port = '587'

    def start(self):
        self.server = smtplib.SMTP("{}: {}".format(self.smtp_host, self.smtp_port))
        self.server.starttls()

        """
        Using Credentials
        """
        self.server.login(self.api_user, self.api_key)

    def close(self):
        self.server.quit()

    def send(self, message):
        """
        Send the message
        """
        self.server.sendmail(message['From'], message['To'], message.as_string())

