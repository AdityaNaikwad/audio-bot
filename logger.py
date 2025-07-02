import gspread
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime

def log_to_google_sheet(user_input, gpt_reply):
    scope = [
        "https://spreadsheets.google.com/feeds",
        "https://www.googleapis.com/auth/spreadsheets",
        "https://www.googleapis.com/auth/drive"
    ]

    creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)
    client = gspread.authorize(creds)

    sheet = client.open("VoiceAI Logs").sheet1
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    sheet.append_row([timestamp, user_input, gpt_reply])
