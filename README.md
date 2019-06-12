# PYSGS

This is a small tool designed as part of learning, allows sending SendGrid messages via SMTP

## Table of Contents
- [Installation](#installation)
- [Setup](#setup)
  - [Headers](#headers)
  - [Sender](#sender)
- [Usage](#usage)
  - [Plain text](#plain-text)
  - [HTML Content](#html-content)
  - [Attachment](#attachment)
- [Example](#example)


## Installation

```
pip install pysgs
```

## Setup

```python
import pysgs
service = pysgs.mailer('SENDGRID_API_KEY')
```

### Headers

```python
sender = "user@example.com"
recipient = "anotheruser@example.com"
subject = "This is a Subject!!"
service.headers(sender, recipient, subject)
```

### Sender

There are different ways to set recipent emails.

  - user@example.com
  - user@example.com, anotheruser@example.com
  - User <user@example.com>
  - User <user@example.com>, Another User <anotheruser@example.com>

You can also send a list of recipients

```python
recipients = [
    "User <user@example.com>",
    "Another User <anotheruser@example.com>"
]
```

## Usage

### Plain text

```python
service.content('Message from sendgrid')
service.send()
```

### HTML Content

```python
service.content('<h1>Hello World!</h1>', 'html')
service.send()
```

### Attachment

```python
service.content('/path/to/file/audio.mp3', is_attach=True)
service.send()
```

## Example

```python
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
    service.content('Message from sendgrid')
    service.content('<h1>Hello World!</h1>', 'html')
    service.content('/path/to/file/audio.mp3', is_attach=True)

    """Send message"""
    service.send()

    """Finish service"""
    service.close()

except SGSError as e:
    print('There was an error: ' + str(e))
```
