import pandas as pd
import smtplib
from email.mime.text import MIMEText

file_location = "C:\\Users\\ertan\\Downloads\\call_logging_data.xlsx"
email_body = []

df = pd.read_excel(file_location)
# print(df.head(5))
# print(df.dtypes)
# Created On - Date, Case Number, Serial Number, PIM, Summary, Country, Case Status, Created By
# Summary statistics
count_of_cases = df['Case Number'].count()
email_body.append(f"Count of cases: {count_of_cases}")

total_no_serial = df['Serial Number'].isna().sum()
email_body.append(f"No serial: {total_no_serial}")

total_no_pim = df['PIM'].isna().sum()
email_body.append(f"No PIM: {total_no_pim}")

total_no_summary = df['Summary'].isna().sum()
email_body.append(f"No summary: {total_no_summary}")

# Filter DataFrame to include only rows where 'Serial Number' is NaN
no_serial_filtered_df = df[df["Serial Number"].isna()]

# Filter DataFrame to include only rows where 'Serial Number' is not NaN
serial_filtered_df = df[df["Serial Number"].notna()]

count_serial_by_agent = serial_filtered_df.groupby('Created By').size()
# Calculate percentage of serial numbers logged by each agent
count_total_cases = df.groupby('Created By').size()

calculate_serial_percentage_by_agent = (count_serial_by_agent / count_total_cases) * 100
# Round percentages to 2 decimal places with percentage sign
round_serial_percentage_by_agent = calculate_serial_percentage_by_agent.round(2)
# Sort the percentages in descending order
sorted_serial_percentage_by_agent = calculate_serial_percentage_by_agent.sort_values(ascending=False)
# Convert the sorted numeric values to strings with a percentage sign
sorted_serial_percentage_by_agent = sorted_serial_percentage_by_agent.astype(str) + '%'

email_body.append("\nPercentage of serial numbers logged by each agent:")
for agent, percentage in sorted_serial_percentage_by_agent.items():
    email_body.append(f"{agent}: {percentage}")

# Combine the email body into a single string
email_content = "\n".join(email_body)

# SMTP email configuration
smtp_server = "smtp.gmail.com"
smtp_port = 465
sender_email = "your_email@gmail.com"
sender_password = "your_password"
receiver_email = "recipient_email@example.com"

# Create the email message
msg = MIMEText(email_content)
msg['Subject'] = "Serial Number Call Logging Data Summary"
msg['From'] = sender_email
msg['To'] = receiver_email

# Send the email
try:
    with smtplib.SMTP_SSL(smtp_server, smtp_port) as server:  # Using SMTP_SSL for port 465
        server.login(sender_email, sender_password)
        server.send_message(msg)
        print("Email sent successfully.")
except Exception as e:
    print(f"Error sending email: {str(e)}")