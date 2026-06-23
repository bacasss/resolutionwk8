import json
import os

DATAFILE = "confessions.json"

def load_conf():
    if not os.path.exists(DATAFILE):
        return []
    with open(DATAFILE, "r") as file:
        return json.load(file)

def save_conf(confessions):
    with open (DATAFILE, "w") as file:
        json.dump(confessions, file, indent=2)

def add_conf(message, channel_id):
    confessions = load_conf()
    if len(confessions) == 0:
        new_id = 1
    else:
        new_id = confessions[-1]["id"] + 1
    confessions.append ({
        "id": new_id,
        "message": message,
        "relates": 0,
        "channel_id": channel_id,
        "message_ts": None
    })
    save_conf(confessions)
    return new_id

def save_message_ts(confession_id, message_ts):
    confessions = load_conf()
    for confession in confessions:
        if confession["id"] == confession_id:
            confession["message_ts"] = message_ts
            break
    save_conf(confessions)

def add_relate(confession_id):
    confessions = load_conf()
    for confession in confessions:
        if confession["id"] == confession_id:
            confession["relates"] += 1
            break
    save_conf(confessions)

def get_conf_by_id(confession_id):
    confessions = load_conf()
    for confession in confessions:
        if confession["id"] == confession_id:
            return confession
    return None