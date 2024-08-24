from RPA_APP.sql.repository import Repository
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import os
import time
import requests
import smtplib
from RPA_APP.config import SMTP_HOST, SMTP_PORT, SMTP_USER, SMTP_PASWORD


class Service:

    repository = Repository()

    # >>>>>>>>>SQL Functions>>>>>>>>>
    def get_by_id(self, id):
        return self.repository.get_by_id(id)

    def get_all(self, paginate: bool = False, page: int = None, per_page: int = None):
        return self.repository.get_all(paginate, page, per_page)

    def add(self, model):
        return self.repository.add(model)

    def delete(self, model):
        return self.repository.delete(model)

    def update(self, model, fields_update):
        return self.repository.update(model, fields_update)

    def commit_changes(self):
        return self.repository.commit_changes()
    # <<<<<<<<<SQL Functions<<<<<<<<<

    # >>>>>>>>>Function to get the execution time>>>>>>>>>
    def execution_time(self, begin = None):
        if begin == None:
            begin = time.time()
            return begin
        ExecutionTime = "{:.2f}".format(time.time() - begin)
        return ExecutionTime
    # <<<<<<<<<Function to get the execution time<<<<<<<<<

    # >>>>>>>>>Function to download and save news images>>>>>>>>>
    def store_picture(self, directory, id, url):
        # >>>>>>>>>Check if directory already exists or create it>>>>>>>>>
        if not os.path.exists(directory):
            os.makedirs(directory)
        # <<<<<<<<<Check if directory already exists or create it<<<<<<<<<

        # >>>>>>>>>Declare aljazeera news item image path>>>>>>>>>
        image_path = os.path.join(directory, f"{id}-Aljazeera.jpg")
        # <<<<<<<<<Declare aljazeera news item image path<<<<<<<<<

        # >>>>>>>>>Download and save image>>>>>>>>>
        response = requests.get(url)
        if response.status_code == 200:
            with open(image_path, "wb") as file:
                file.write(response.content)
            return True
        else:
            return False
        # <<<<<<<<<Download and save image<<<<<<<<<
    # <<<<<<<<<Function to download and save news images<<<<<<<<<

    # >>>>>>>>>Function to send any excel by email>>>>>>>>>
    def excel_by_email(self, excel_file_path, email, subject):
        # >>>>>>>>>SMTP server settings>>>>>>>>>
        smtp_host = SMTP_HOST
        smtp_port = SMTP_PORT
        smtp_user = SMTP_USER
        smtp_password = SMTP_PASWORD
        # <<<<<<<<<SMTP server settings<<<<<<<<<

        # >>>>>>>>>Create email message>>>>>>>>>
        msg = MIMEMultipart()
        msg['From'] = smtp_user
        msg['To'] = email
        msg['Subject'] = subject
        # <<<<<<<<<Create email message<<<<<<<<<

        # >>>>>>>>>Email body>>>>>>>>>
        body = 'Hello,\n\nAttached is the requested Excel file.'
        msg.attach(MIMEText(body, 'plain'))
        # <<<<<<<<<Email body<<<<<<<<<

        # >>>>>>>>>Attach Excel file>>>>>>>>>
        with open(excel_file_path, 'rb') as attachment:
            part = MIMEBase('application', 'octet-stream')
            part.set_payload(attachment.read())
            encoders.encode_base64(part)
            part.add_header('Content-Disposition', f'attachment; filename={os.path.basename(excel_file_path)}')
            msg.attach(part)
        # <<<<<<<<<Attach Excel file<<<<<<<<<

        # >>>>>>>>>Send email>>>>>>>>>
        with smtplib.SMTP(smtp_host, smtp_port) as server:
            server.starttls()
            server.login(smtp_user, smtp_password)
            server.sendmail(smtp_user, email, msg.as_string())
        # <<<<<<<<<Send email<<<<<<<<<
    # <<<<<<<<<Function to send any excel by email<<<<<<<<<
