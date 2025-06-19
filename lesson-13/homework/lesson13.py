from datetime import datetime, timedelta
import time
import re
import pytz

# 1. Age Calculator
def age_calculator():
    birthdate_str = input("Enter your birthdate (YYYY-MM-DD): ")
    birthdate = datetime.strptime(birthdate_str, "%Y-%m-%d")
    today = datetime.today()
    
    years = today.year - birthdate.year
    months = today.month - birthdate.month
    days = today.day - birthdate.day

    if days < 0:
        months -= 1
        days += (birthdate.replace(month=birthdate.month % 12 + 1, day=1) - timedelta(days=1)).day
    if months < 0:
        years -= 1
        months += 12

    print(f"You are {years} years, {months} months, and {days} days old.")

# 2. Days Until Next Birthday
def days_until_birthday():
    birthdate_str = input("Enter your birthdate (YYYY-MM-DD): ")
    birthdate = datetime.strptime(birthdate_str, "%Y-%m-%d")
    today = datetime.today()
    next_birthday = birthdate.replace(year=today.year)
    
    if next_birthday < today:
        next_birthday = next_birthday.replace(year=today.year + 1)

    remaining = next_birthday - today
    print(f"Days until your next birthday: {remaining.days}")

# 3. Meeting Scheduler
def meeting_scheduler():
    current_str = input("Enter current date and time (YYYY-MM-DD HH:MM): ")
    duration_hours = int(input("Meeting duration - Hours: "))
    duration_minutes = int(input("Meeting duration - Minutes: "))
    
    current = datetime.strptime(current_str, "%Y-%m-%d %H:%M")
    end_time = current + timedelta(hours=duration_hours, minutes=duration_minutes)
    
    print(f"Meeting will end at: {end_time}")

# 4. Timezone Converter
def timezone_converter():
    date_str = input("Enter date and time (YYYY-MM-DD HH:MM): ")
    from_zone = input("Enter your current timezone (e.g. Asia/Tashkent): ")
    to_zone = input("Enter the timezone to convert to (e.g. US/Eastern): ")

    local = pytz.timezone(from_zone)
    target = pytz.timezone(to_zone)

    local_dt = local.localize(datetime.strptime(date_str, "%Y-%m-%d %H:%M"))
    converted = local_dt.astimezone(target)
    
    print(f"Converted time: {converted.strftime('%Y-%m-%d %H:%M (%Z)')}")

# 5. Countdown Timer
def countdown_timer():
    target_str = input("Enter future date and time (YYYY-MM-DD HH:MM:SS): ")
    target = datetime.strptime(target_str, "%Y-%m-%d %H:%M:%S")

    while True:
        now = datetime.now()
        remaining = target - now
        if remaining.total_seconds() <= 0:
            print("Time's up!")
            break
        print(f"Time remaining: {remaining}")
        time.sleep(1)

# 6. Email Validator
def email_validator():
    email = input("Enter email address: ")
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    if re.match(pattern, email):
        print("Valid email address.")
    else:
        print("Invalid email address.")

# 7. Phone Number Formatter
def phone_formatter():
    phone = input("Enter 10-digit phone number: ")
    if len(phone) == 10 and phone.isdigit():
        formatted = f"({phone[:3]}) {phone[3:6]}-{phone[6:]}"
        print(f"Formatted phone number: {formatted}")
    else:
        print("Invalid phone number.")

# 8. Password Strength Checker
def password_checker():
    password = input("Enter password: ")
    errors = []
    if len(password) < 8:
        errors.append("Password should be at least 8 characters.")
    if not re.search(r'[A-Z]', password):
        errors.append("Password should contain an uppercase letter.")
    if not re.search(r'[a-z]', password):
        errors.append("Password should contain a lowercase letter.")
    if not re.search(r'[0-9]', password):
        errors.append("Password should contain a digit.")
    
    if errors:
        print("Weak password:")
        for error in errors:
            print(f"- {error}")
    else:
        print("Strong password!")

# 9. Word Finder
def word_finder():
    text = """Python is a great programming language. Python is easy to learn and very powerful."""
    word = input("Enter word to search: ")
    matches = [m.start() for m in re.finditer(r'\b' + re.escape(word) + r'\b', text)]
    
    if matches:
        print(f"Found '{word}' at positions: {matches}")
    else:
        print(f"No occurrences of '{word}' found.")

# 10. Date Extractor
def date_extractor():
    text = input("Enter text: ")
    date_pattern = r'\b\d{4}-\d{2}-\d{2}\b'
    found = re.findall(date_pattern, text)
    if found:
        print("Dates found in text:")
        for date in found:
            print(date)
    else:
        print("No dates found.")

# Run all functions one by one
print("\n1. Age Calculator")
age_calculator()

print("\n2. Days Until Next Birthday")
days_until_birthday()

print("\n3. Meeting Scheduler")
meeting_scheduler()

print("\n4. Timezone Converter")
timezone_converter()

# Uncomment to test countdown (Ctrl+C to stop after it finishes)
# print("\n5. Countdown Timer")
# countdown_timer()

print("\n6. Email Validator")
email_validator()

print("\n7. Phone Number Formatter")
phone_formatter()

print("\n8. Password Strength Checker")
password_checker()

print("\n9. Word Finder")
word_finder()

print("\n10. Date Extractor")
date_extractor()
