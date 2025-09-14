import subprocess
import schedule, time

def job():
    subprocess.run(["python", "scripts/eda_and_report.py"])

# every month’s first day at 09:00
schedule.every().month.at("09:00").do(job)

while True:
    schedule.run_pending()
    time.sleep(60)
