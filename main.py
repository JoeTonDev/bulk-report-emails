import pandas as pd
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
import matplotlib.pyplot as plt

# Read the email list from excel spreadsheet
df = pd.read_excel('email_list.xlsx')

# Connect to the email server
server = smtplib.SMTP('smtp.gmail.com', 587)
server.ehlo()
server.starttls()
server.login('you_email_address@gmail.com', 'your_email_password')

# Loop through each row in the email list
for index, row in df.iterrows():
  # Get teh recipient email addresss and chart data
  recipient = row['Email']
  chart_data = row['Chart_dat']
  
  # Plot the chart using matplotlib
  plt.plot(chart_data)
  plt.title('Chart')
  plt.xlabel('X Axis')
  plt.ylabel('Y Axis')
  
  # Save the chart as image
  plt.savefig('chart.png')
  
  # Create email message
  message = MIMEMultipart()
  message['From'] = 'your_email_address@gmail.com'
  message['To'] = recipient
  message['Subject'] = 'Chart Data'
  text = MIMEText('Please find attached chart data')
  message.attach(text)
  
  # Attach the chart image to email
  with open('chart.png', 'rb') as f:
    img = MIMEImage(f.read())
    message.attach(img)
    
  # Send the email
  server.sendmail('Your_email_address@gmail.com', recipient)
  message.as_string()
  
  # Close email server connection
  server.quit()

