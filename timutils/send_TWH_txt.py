"""
short module to send a text message to Tim Hilton's phone using
Verizon's email-to-sms support and gmail's smtp mail server.  I was
unable to get UC Merced's outlook.com server to accept the outgoing
message.

Timothy W. Hilton, UC Merced, 25 Feb 2014
"""

import smtplib
import getpass


def get_outgoing_mail_password():
    """
    prompts user for the password for the email account to be used to
    the send the text message.

    .. note::
        Uses
        `getpass <https://docs.python.org/2/library/getpass.html>`_, so
        is subject to the same security considerations.

    YIELDS:
        string containing the password.
    """
    pwd = getpass.getpass(prompt='Gmail password: ')
    if len(pwd) == 0:
        pwd = None
    return(pwd)


def send_vtext_gmail(gmail_passwd,
                     gmail_uname='timothy.w.hilton@gmail.com',
                     dest_phone_num='4153147478',
                     msg_txt='testing 123'):
    """
    Send a text message to a specified phone number from a specified
    gmail account.

    ARGS:
       gmail_passwd (string): the password for the gmail account to be
           used to send the text message
       gmail_uname (string): the username for the gmail account to be
           used to send the text message
       dest_phone_num (string): the ten-digit phone number to send the
           text message to.
       msg_txt (string): the content of the text message to send.

    EXAMPLE:
        >>> passwd = get_outgoing_mail_password()
        >>> if passwd is not None:
            send_vtext_gmail(passwd,
                             msg_txt='here is the message')

    .. note::
       uses the
       `vtext.com <http://www.verizonwireless.com/support/vtext-website-faqs/>`_
       feature offered by Verizon Wireless. Behavior for non-Verizon
       dest_phone_num is untested.
    """
    vtext_addr = "{}@vtext.com".format(dest_phone_num)

    msg = """From: %s
    To: %s
    Subject: text-message\n
    %s""" % (gmail_uname, vtext_addr, msg_txt)

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(gmail_uname, gmail_passwd)
    server.sendmail(gmail_uname, vtext_addr, msg)
    server.quit()


def send_vtext_outlook(ucmerced_uname,
                       smtp_password,
                       dest_phone_num,
                       msg_txt):
    """
    .. warning::
        25 Feb 2014: couldn't get sending mail through UC Merced's
        outlook.com SMTP server to work.  Probably something related to
        the formatting of the outlook.com username? -TWH
    """
    # vtext_addr = "{}@vtext.com".format(dest_phone_num)
    smtp_uname = "{}@ucmerced.edu".format(ucmerced_uname)

    # msg = """From: %s
    # To: %s
    # Subject: text-message
    # %s""" % (smtp_uname, vtext_addr, msg_txt)

    print(smtp_uname)
    result = 0

    # server = smtplib.SMTP('pod51011.outlook.com',587)
    # server.starttls()
    # server.login(smtp_uname,smtp_password)
    # result = server.sendmail(smtp_uname, vtext_addr, msg)
    # server.quit()

    print(result)


if __name__ == "__main__":
    passwd = get_outgoing_mail_password()
    if passwd is not None:
        send_vtext_gmail(passwd,
                         msg_txt='here is the message')
    else:
        print('no password provided')
