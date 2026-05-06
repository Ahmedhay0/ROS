import json
import datetime

LOG_FILE = "mission_log.jsonl"

def log_mission(drone_id, missions_completed, battery_remaining):
    entry = {
        "drone_id": drone_id,
        "missions_completed": missions_completed,
        "battery_remaining": battery_remaining,
        "timestamp": str(datetime.datetime.now())
    }
    with open(LOG_FILE, "a") as f:      
        f.write(json.dumps(entry) + "\n") 

def get_champions():
    try:
        entries = {}
        with open(LOG_FILE, "r") as f:
            for line in f:
                e = json.loads(line)
                did = e["drone_id"]
                if did not in entries or e["missions_completed"] > entries[did]["missions_completed"]:
                    entries[did] = e
        return sorted(entries.values(), key=lambda x: x["missions_completed"], reverse=True)
    except FileNotFoundError:
        return [] 