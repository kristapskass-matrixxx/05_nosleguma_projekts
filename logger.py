from datetime import datetime

LOG_FILE = "activity.log"

def log(message):
    """Pieraksta darbību log failā ar datumu un laiku."""
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(f"[{now}] {message}\n")