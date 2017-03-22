import csv

faculty_email_addresses = []
with open('faculty.csv') as csv_file:
    reader = csv.reader(csv_file)
    next(reader)
    for faculty in reader:
        email_address = faculty[3]
        faculty_email_addresses.append(email_address)

with open('emails.csv', 'w') as csv_write_file:
    write_emails = csv.writer(csv_write_file)
    for email in faculty_email_addresses:
        write_emails.writerow([email])
