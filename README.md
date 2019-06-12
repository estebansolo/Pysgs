# PYSGS

This is a small tool designed as part of learning, allows sending SendGrid messages via SMTP

## Installation

```
pip install pysgs
```

## Setup

```python
from pysgs import Mailer

service = Mailer('SENDGRID_API_KEY')

sender = "YOUR_EMAIL"
recipient = "RECIPIENT_EMAIL"
subject = "This is a Subject!!"
service.setup(sender, recipient, subject)

"""You can send messages to multiple recipients by passing a list of emails"""

recipient = [
    "RECIPIENT_EMAIL_1",
    "RECIPIENT_EMAIL_2"
]

service.setup(sender, recipients, subject)
```

## Usage

### Send a basic email
```python
service.add_content('Hello world!')
service.send()
```

### Send email with HTML

```python
service.add_content('<h1>Hello world!</h1>', 'html')
service.send()
```

### Send email with attachment

```python
service.add_content('<h1>Hello world!</h1>', 'html')
service.add_attachment("FILE PATH")
service.send()
```

## Example

```python
from pysgs import Mailer
from pysgs.exceptions import SGSError

try:
    service = Mailer('SENDGRID_API_KEY')

    sender = "YOUR_EMAIL"
    recipient = "RECIPIENT_EMAIL"
    subject = "This is a Subject!!"
    service.setup(sender, recipient, subject)

    service.add_content('Message from sendgrid')
    service.send()

    # Close Connection
    service.close()
    
except SGSError as e:
    print("There was an error: " + str(e))
```