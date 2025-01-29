import requests
from icalendar import Calendar
import datetime
import vobject
import asyncio
import smtplib

s=smtplib.SMTP('smtp.gmail.com',587)

# Gmail ID and password
GMAIL_ID = ''
GMAIL_PASSWORD = ''

def connect_smtp():
    s.starttls()
    s.login(GMAIL_ID,GMAIL_PASSWORD)
    
def disconnect_smtp():
    if(s) :
        s.quit()
    
def send_email(to,msg):
    s.sendmail(GMAIL_ID,to,msg)

def execute(contact,component):
    subject = "On the Occassion of "+component.get("SUMMARY")
    message = f"Subject: {subject}\n\nHi {contact['Full Name']},\n\nWishing you a very happy {component.get('SUMMARY')}!\n\nHave a great day!"

    # Send the email
    send_email("kunaljainwin@gmail.com", message)
    
def parse_vcard(vcard_str):
    """Parse a single vCard string and extract relevant details."""
    vcard = vobject.readOne(vcard_str)
    
    contact_details = {}
    
    # Extract full name
    if hasattr(vcard, 'fn'):
        contact_details['Full Name'] = vcard.fn.value
    
    # Extract phone numbers
    if hasattr(vcard, 'tel'):
        contact_details['Phone Numbers'] = [tel.value for tel in vcard.tel_list]
    
    # Extract emails
    if hasattr(vcard, 'email'):
        contact_details['Emails'] = [email.value for email in vcard.email_list]
    
    # Extract addresses
    if hasattr(vcard, 'adr'):
        contact_details['Addresses'] = [adr.value for adr in vcard.adr_list]
    
    return contact_details


def read_vcards_from_file(vcard_file_path):
    """Read and parse all vCards from a .vcf file."""
    with open(vcard_file_path, 'r') as file:
        vcard_data = file.read()

    # Split the content by 'BEGIN:VCARD' and parse each vCard
    vcards = vcard_data.split('BEGIN:VCARD')[1:]  # Skip content before the first vCard
    contacts = []

    for vcard_str in vcards:
        vcard_str = 'BEGIN:VCARD' + vcard_str  # Add BEGIN:VCARD back to each part
        try:
            contact_details = parse_vcard(vcard_str)
            contacts.append(contact_details)
        except Exception as e:
            print(f"Error parsing vCard: {e}")

    return contacts

# Print details of all contacts
def display_contacts(contacts):
    """Display contact details."""
    for idx, contact in enumerate(contacts, start=1):
        print(f"\nContact {idx}:")
        print(f"\nContact {idx}:")
        for key, value in contact.items():
            print(f"  {key}: {value}")

# Example usage
vcard_file = '../raw/contacts.vcf'  # Path to your VCF file
contacts = read_vcards_from_file(vcard_file)

# def generate_custom_message():
    
async def main():
    # URL of the ICS file
    ics_url = "https://calendar.google.com/calendar/ical/en.indian%23holiday%40group.v.calendar.google.com/public/basic.ics"

    try:
        # Connect Gmail SMTP Server
        connect_smtp()
        
        # Fetch the ICS file
        response = requests.get(ics_url)
        response.raise_for_status()  # Raise an error for HTTP issues

        # Parse the ICS content
        cal = Calendar.from_ical(response.content)
        tasks = []
        # Iterate through events in the calendar
        for component in cal.walk():
            if component.name == "VEVENT" :
                start=component.get("DTSTART").dt
                end=component.get("DTEND").dt
                if True :# Condition to check if the event is today True for Testing
                  for idx, contact in enumerate(contacts, start=1):
                      print(f"\nContact {idx}:")
                      if len(contact["Phone Numbers"]) : 
                          # Perform below asychronously
                          tasks.append(execute(contact,component))
                        
        # Wait for all tasks to complete
        await asyncio.gather(*tasks)
        # Disconnect Gmail SMTP Server
        disconnect_smtp()
                
                
    except requests.exceptions.RequestException as e:
        print(f"Error fetching ICS file: {e}, {ics_url}")


if __name__ == "__main__":
    asyncio.run(main())
    # Disconnect Gmail SMTP Server in case of Exception
    disconnect_smtp()