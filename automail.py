import yagmail
import os
import datetime
import Info
import pandas as pd
import numpy as np
def mail():
    date = datetime.date.today().strftime("%B %d, %Y")
    path = 'Attendance'
    os.chdir(path)
    files = sorted(os.listdir(os.getcwd()), key=os.path.getmtime)
    df = pd.read_csv(r'C:\Users\Prasanna Reddy\Downloads\Face-Recognition-based-Attendance-System\Face-Recognition-based-Attendance-System\EmployeeDetails\EmployeeDetails.csv')

    receivers = df["Email"]
    newest = files[-1]
    filename = newest
    sub = "Attendance Report for " + str(date)
    body = " Attendance Submitted."

    for receiver in receivers:
        # mail information
        if pd.isnull(receiver):
            continue
        else:
            yag = yagmail.SMTP(Info.EMAIL_ID, Info.PASSWORD)

            # sent the mail
            yag.send(
                to=receiver,
                subject=sub, # email subject
                contents=body,  # email body
                attachments=filename  # file attached
            )
            print("Email Sent to "+receiver)
