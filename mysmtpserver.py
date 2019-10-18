import smtpd
import asyncore


class mysmtpserver(smtpd.SMTPServer):
    def process_message(self, peer, mailfrom, rcpttos, data, **kwargs):
        print("recieving mail from client.{0}".format(peer))
        print("From mail id {0}".format(mailfrom))
        print("To mail id{0}".format(rcpttos))
        print("Mail body{0}".format(data))
        


server = mysmtpserver(('192.168.0.111', 1025),None)
asyncore.loop()
