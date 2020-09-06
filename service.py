import threading

from send_email import send_email_with_text

TASKS = []
NUMBER_OF_TASKS = 10
EMAIL_FROM = 'pippinrus@gmail.com'


def worker(text, email_to):
    send_email_with_text(text, email_to, EMAIL_FROM)


def add_email_to_emails(email, text, timer):
    TASKS.append({"email": email, "text": text, "timer": timer})
    t = threading.Timer(timer, worker, args=(text, email,))
    t.start()


def get_last_tasks():
    return TASKS[-NUMBER_OF_TASKS:]
