# ele é onde estara todas as funções deste pacote.

def initialize():
    from carbonmail.email_sender import Email_Sender
    ems = Email_Sender()
    ems.enable_window()
