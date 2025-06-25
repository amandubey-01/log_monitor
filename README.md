# Simulated Production Log Monitor

This project simulates production logs from a data pipeline, analyzes them for correctness and performance issues, visualizes trends, and sends real-time alerts via Telegram. It demonstrates production monitoring, data parsing, and automation using Python.

---

## Features

- Simulates logs containing `INFO`, `WARNING`, and `ERROR` entries
- Parses logs into structured data using regular expressions and pandas
- Generates hourly error reports and average processing time insights
- Visualizes log metrics with seaborn and matplotlib
- Sends automated Telegram alerts based on defined thresholds
- Manages sensitive information using environment variables

---

## Project Structure

```
log-monitor/
├── analyze_logs.ipynb      # Interactive notebook for parsing and visualization
├── log_monitor.py          # Script to generate simulated logs
├── send_alert.py           # Script to send alerts via Telegram
├── logs.txt                # Sample log output
├── requirements.txt        # Python dependencies
```

---

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/log-monitor.git
cd log-monitor
```

### 2. Configure Telegram Bot Credentials

- Create a bot using [@BotFather](https://t.me/BotFather)
- Send a message to your bot
- Retrieve your `chat_id` by visiting:
  ```
  https://api.telegram.org/bot<YOUR_TOKEN>/getUpdates
  ```

### 3. Create a `.env` File

Store your Telegram bot token and chat ID in a file named `.env`:

```env
TELEGRAM_TOKEN=your_bot_token
TELEGRAM_CHAT_ID=your_chat_id
```

---

## Usage

### Generate Logs
```bash
python log_monitor.py
```

### Analyze Logs and Generate Visualizations
```bash
jupyter notebook analyze_logs.ipynb
```

### Send Telegram Alerts
```bash
python send_alert.py
```

---

## Skills Demonstrated

- Monitoring and alerting pipeline design
- Log parsing with regular expressions
- Data analysis and visualization using pandas and seaborn
- Secure environment configuration with `python-dotenv`
- API integration with Telegram

---

## License

This project is licensed under the MIT License.

---

## Author

**Aman Dubey**  
[LinkedIn](https://www.linkedin.com/in/amandubey)

