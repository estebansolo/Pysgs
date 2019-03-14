from pysgs import Server, Mailer

# Start connection
server = Server('SENDGRID_API_KEY')


# Send message
server.send()

# Close connection
server.close()
