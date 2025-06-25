import pandas as pd
import re
from datetime import datetime
import requests
from dotenv import load_dotenv
import os

# Load .env from external path
dotenv_path = r"E:\Coding_with_python\API-secret_files\.env"
load_dotenv(dotenv_path=dotenv_path)

TELEGRAM_TOKEN = os.getenv("LogMonitorBot_token")
TELEGRAM_CHAT_ID = os.getenv("_0287_chat_id")

def parse_logs_to_df(filename="logs.txt"):
    records = []
    with open(filename, "r") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            try:
                timestamp_str = line[:19]
                timestamp = datetime.strptime(timestamp_str, "%Y-%m-%d %H:%M:%S")
                if "INFO" in line:
                    status = "INFO"
                    match = re.search(r"processed in ([\d\.]+)s", line)
                    time_taken = float(match.group(1)) if match else None
                elif "ERROR" in line:
                    status = "ERROR"
                    time_taken = None
                elif "WARNING" in line:
                    status = "WARNING"
                    match = re.search(r"slow response ([\d\.]+)s", line)
                    time_taken = float(match.group(1)) if match else None
                else:
                    continue
                records.append({
                    "timestamp": timestamp,
                    "hour": timestamp.hour,
                    "status": status,
                    "time_taken": time_taken
                })
            except:
                continue
    return pd.DataFrame(records)

def send_telegram_alert(message, token, chat_id):
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": message,
        "parse_mode": "Markdown"
    }
    try:
        r = requests.post(url, data=payload)
        if r.status_code == 200:
            print("Telegram alert sent.")
        else:
            print("Failed:", r.text)
    except Exception as e:
        print("Exception:", e)

if __name__ == "__main__":
    df = parse_logs_to_df()

    error_count = df[df["status"] == "ERROR"].shape[0]
    warning_count = df[df["status"] == "WARNING"].shape[0]
    avg_proc_time = df[df["status"] == "INFO"]["time_taken"].mean()

    message = "*Log Monitor Alert:*\n"
    alert_triggered = False

    if error_count > 5:
        message += f"- ⚠ High Errors: *{error_count}*\n"
        alert_triggered = True
    if warning_count > 3:
        message += f"- ⚠ Warnings: *{warning_count}*\n"
        alert_triggered = True
    if avg_proc_time > 6:
        message += f"- ⚠ High Avg. Time: *{avg_proc_time:.2f}s*\n"
        alert_triggered = True

    if alert_triggered:
        send_telegram_alert(message, TELEGRAM_TOKEN, TELEGRAM_CHAT_ID)
