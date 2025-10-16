import psutil
import time

def show_system_stats(interval=2):
    while True:
        cpu = psutil.cpu_percent(interval=0.5)
        memory = psutil.virtual_memory().percent
        disk = psutil.disk_usage('/').percent
        print(f"CPU: {cpu}% | Memory: {memory}% | Disk: {disk}%")
        time.sleep(interval)

if __name__ == "__main__":
    show_system_stats()
