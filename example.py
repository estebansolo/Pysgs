from pysgs import mailer
from pysgs.exceptions import SGSError

try:
    """Start connection"""
    service = mailer('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')
    
    for i in [1, 2]:
        sender = "madabet92@gmail.com"
        recipient = "estebansolorzano27@gmail.com"
        subject = f"This is the {i} Subject!!"
        service.setup(sender, recipient, subject)

        service.add_content('<h1>Hello World!</h1>', 'html')
        
        """Send message"""
        service.send()

    """Close Connection"""
    service.close()
except SGSError as e:
    print('There was an error: ' + str(e))
