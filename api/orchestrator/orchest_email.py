from django.core.mail import send_mail, EmailMessage


class OrchestEmail:

    def __init__(self,  msg,  to):
        self.msg = None
        self.to = None
        self.email = None
        self.fromm = "mmaccaferri@magnasistemas.com.br"

    def sendEmail(self, msg, fromm, to, file):
        """
         name: sendEmail
        :param msg: msg
        :param fromm: fromm
        :param to: to
        :param file: file
        :return: True
        """
        try:

            self.msg = getattr(msg, '')
            self.to = getattr(to, '')
            self.fromm = getattr(fromm, '')
            self.email = EmailMessage(self.msg, self.msg, [self.to], [self.fromm])

            if file != {} or file is None:
                self.email.message.attach(file.name, file)

            self.email.send()

            return True

        except:
           return False
