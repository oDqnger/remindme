import toml
from pathlib import Path

TEMP_FOLDER_LOCATION = "/tmp/remindme/"
TEMP_FILE_LOCATION = "/tmp/remindme/reminders.toml"
USER_CONFIG_FILE_LOCATION = str(Path.home()) + "/.config/remindme/config.toml"

def write_temp_toml_file(config, file):
    with open(file, "w", encoding="utf-8") as file:
        toml.dump(config, file)

def read_temp_toml_file(file):
    with open(file, "r", encoding="utf-8") as file:
        config = toml.load(file)

    return config
