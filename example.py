from pysgs import Mailer
from pysgs.exceptions import SGSError

try:
    # Start connection
    service = Mailer('SENDGRID_API_KEY')
    
    service.setup(
        sender="EMAIL",
        recipients="EMAIL",
        subject="SUBJECT"
    )

    service.add_content('<h1>Hello World!</h1>')
    
    # Send message
    service.send()

    # Close Connection
    service.close()
except SGSError as e:
    print('There was an error: ' + e)
