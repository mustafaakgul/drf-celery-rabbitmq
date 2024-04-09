from celery import Celery

app = Celery('tasks', broker='redis://localhost:6379/2')

def send_email_with_attachment():
    pass

def analyze_dns(dns_file):
    pass

@app.task()
def analyze_user_dna_and_email(dna_file, email):
    pdf_report = analyze_dns(dna_file)
    send_email_with_attachment(email, pdf_report)