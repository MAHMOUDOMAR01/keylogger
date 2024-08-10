import psutil
import time
import logging

logging.basicConfig(filename='logs/performance.log', level=logging.INFO, format='%(asctime)s: %(message)s')

def monitor_performance():
    while True:
        cpu = psutil.cpu_percent(interval=1)
        memory = psutil.virtual_memory().percent
        logging.info(f"CPU: {cpu}%, Memory: {memory}%")
        time.sleep(60)

if __name__ == "__main__":
    monitor_performance()
