# Pysgs - SendGrid SMTP
Send messages through SendGrid using SMTP

Installation
============
    $ pip install pysgs

Setup
=====
    from pysgs import Mailer
    
    service = Mailer('SENDGRID_API_KEY')
    service.setup(
        sender="EMAIL",
        recipients="EMAIL",
        subject="SUBJECT"
    )
#### You can send messages to multiple recipients by passing a list of emails
    service.setup(
        sender="EMAIL",
        recipients=[
            'EMAIL',
            'EMAIL'
        ],
        subject="SUBJECT"
    )
    
Usage
=====
#### Send a basic email
    service.add_content('Hello world!', 'text')
    service.send()
    
#### Send an email with HTML
    service.add_content('<h1>Hello world!</h1>', 'html')
    service.send()
    
#### Send email with attachment
    service.add_content('<h1>Hello world!</h1>', 'html')
    service.add_attachment("FILE PATH")
    service.send()
    
# Full Example
    from pysgs import Mailer
    from pysgs.exceptions import SGSError

    try:
        service = Mailer('SENDGRID_API_KEY')
        service.setup(
            sender="EMAIL",
            recipients="EMAIL",
            subject="SUBJECT"
        )

        service.add_content('<h1>Message from sendgrid</h1>')
        service.send()

        # Close Connection
        service.close()
    except SGSError as e:
        print("There was an error: " + e)
