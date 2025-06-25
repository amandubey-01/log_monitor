# Randomly generating logs.
import random, datetime

def generate_logs(filename="logs.txt", lines=100):
    statuses = ["INFO", "ERROR", "WARNING"]
    with open(filename, "w") as f:
        start_time = datetime.datetime.now().replace(minute=0, second=0, microsecond=0)
        for i in range(lines):
            t = start_time + datetime.timedelta(minutes=i*2)
            status = random.choices(statuses, weights=[0.6, 0.2, 0.2])[0]
            if status == "INFO":
                time_taken = round(random.uniform(1.0, 5.0), 2)
                f.write(f"{t} INFO: batch processed in {time_taken}s\n")
            elif status == "ERROR":
                f.write(f"{t} ERROR: batch failed at {t.strftime('%H:%M')}\n")
            else:
                time_taken = round(random.uniform(5.0, 10.0), 2)
                f.write(f"{t} WARNING: slow response {time_taken}s\n")

if __name__ == "__main__":
    generate_logs()