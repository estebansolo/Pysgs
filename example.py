import pysgs
from pysgs.exceptions import SGSError

try:
    """Start connection"""
    service = pysgs.mailer("SENDGRID_API_KEY")

    """Set message headers"""
    sender = "user@example.com"
    recipient = "anotheruser@example.com"
    subject = "This is a Subject!!"
    service.headers(sender, recipient, subject)

    """Set content"""
    service.content('<h1>Hello World!</h1>', 'html') # Set HTML
    service.content('Message from sendgrid') # Set Plain text
    service.content('/path/to/file/audio.mp3', is_attach=True) # Set Attachment

    """Send message"""
    service.send()

    """Finish service"""
    service.close()

except SGSError as e:
    print('There was an error: ' + str(e))
