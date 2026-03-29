# Import
from pathlib import Path
import datetime
import smtplib
from email.message import EmailMessage

def log(s):
    fn = Path(__file__).resolve().parent / 'auto-login-sites-log.txt'
    log = open(fn, mode='a', encoding='utf-8')
    log.write(str(datetime.datetime.now()) + ': ')
    print(s, file=log) # print adds a newline
    log.close()

def email(t, f, port, smtp, sub, body, user, pw):
    msg = EmailMessage()
    msg['To'] = t
    msg['From'] = f
    msg['Subject'] = sub
    msg.set_content(body)

    try:
        server = None
        server = smtplib.SMTP(smtp, int(port))
        server.starttls()
        server.login(user, pw)
        server.send_message(msg)
        ret = f"SMTP sent '{sub}' email to {t}"
    except smtplib.SMTPAuthenticationError:
        ret = "SMTP authentication failed, check username/password"
    except smtplib.SMTPRecipientsRefused:
        ret = f"SMTP {t} was rejected"
    except smtplib.SMTPException as e:
        ret = f"SMTP {e}"
    except Exception as e:
        ret = f"SMTP {e}" # sock or dns errors
    finally:
        if server is not None:
            server.quit()

    return ret
