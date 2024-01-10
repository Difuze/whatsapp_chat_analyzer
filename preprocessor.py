import re
import pandas as pd
import warnings


warnings.filterwarnings("ignore")


f = open("WhatsApp Chat with Harsh.txt" , "r", encoding = "utf-8")
data = f.read()

def preprocess(data):

    # Define a regular expression pattern to match date, time, and message
    pre_pattern = re.compile(r'(\d+/\d+/\d+), (\d+:\d+\s[APMapm]+) - (\w+): (.+)')

    dates = re.findall(pre_pattern, data)

    post_pattern = re.compile(r'(\d+/\d+/\d+), (\d+:\d+\s[APMapm]+), (\w+), (.+)')
    # Define a regular expression pattern to match date, time, and message

    date = []
    time = []
    sender = []
    message_content = []

    for message in dates:
        message_text = ', '.join(message)

        match = post_pattern.match(message_text)
        if match:
            date.append(match.group(1))
            time.append(match.group(2))
            sender.append(match.group(3))
            message_content.append(match.group(4))
        else:
            print(f"Pattern did not match for message: {message_text}")

    # Create a DataFrame
    df = pd.DataFrame({
        'date': date,
        'time': time,
        'sender': sender,
        'message': message_content
    })

    df['date'] = pd.to_datetime(df['date'], format='%m/%d/%y')

    df['year'] = df['date'].dt.year

    df['month'] = df['date'].dt.month_name()

    df['day'] = df['date'].dt.day

    df['time'] = pd.to_datetime(df['time'] ).dt.time

    df['hour'] = pd.to_datetime(df['time'], format='%H:%M:%S').dt.hour

    df['minute'] = pd.to_datetime(df['time'], format='%H:%M:%S').dt.minute


    return df