# Auto Wisher

Auto Wisher is a Python-based project that automates sending email wishes based on calendar events. It reads events from an iCalendar (.ics) file, extracts relevant details, and sends personalized greetings via email.

## Features
- Fetch events from an iCalendar (.ics) file
- Extract recipient details and event information
- Send personalized email wishes using SMTP
- Supports HTML email templates
- Asynchronous execution for handling multiple emails efficiently

## Getting Started

### Prerequisites
Ensure you have Python installed (>=3.7). Install the required dependencies using:

```sh
pip install -r requirements.txt
```

### Installation
1. Clone this repository:
   ```sh
   git clone https://github.com/your-username/auto-wisher.git
   cd auto-wisher
   ```
2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
3. Configure your email settings inside `config.py` (if applicable).
4. Run the script:
   ```sh
   python main.py
   ```

## Configuration

### SMTP Settings
Ensure you configure your SMTP settings in  `main.py`:
```python
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
GMAIL_ID = "your-email@gmail.com"
GMAIL_PASSWORD = "your-email-password"
```

### Sample iCalendar Event Structure
Ensure your `.ics` file contains valid events, for example:
```plaintext
BEGIN:VEVENT
SUMMARY:John's Birthday
DTSTART;VALUE=DATE:20250215
END:VEVENT
```

## Usage
- Modify the `main.py` script to extract required fields.
- There's a if condition at line 113 which is given True for Testing purpose
- Run the script daily using `Windows Task Scheduler` or `cron` for automation.

## Contributing
Feel free to submit issues or pull requests to improve this project!

## License
This project is licensed under the MIT License.

## Contact
For any queries, reach out to `your-email@example.com`.

