import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import datetime

def send_email(subject, body, to_email):
    from_email = 'matidza46@gmail.com'  # Change this to your email address
    password = '0664347295'  # Change this to your email password

    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject

    msg.attach(MIMEText(body, 'plain'))

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(from_email, password)
    text = msg.as_string()
    server.sendmail(from_email, to_email, text)
    server.quit()

def generate_report():
    # Replace this with your report generation logic
    today = datetime.date.today()
    report = f"Daily Report for {today}\n\n"
    # Add your report content here
    return report

def main():
    to_email = 'patrickmatidza46@gmail.com'  # Change this to the recipient's email address
    subject = 'Daily Report'
    body = generate_report()
    send_email(subject, body, to_email)

if __name__ == "__main__":
    main()
