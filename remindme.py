from utils import (
    read_temp_toml_file,
    write_temp_toml_file,
    TEMP_FOLDER_LOCATION,
    TEMP_FILE_LOCATION
)
import os
import sys
import time
import rich
import psutil

flag = sys.argv[1]

if flag[1] == "s" or flag[1] == "m":
    t, unit_display, reminder = 0, "", ""
    try:
        t = int(sys.argv[2])
        unit_display = 'second' if flag[1] == 's' else 'minute'
        reminder = ' '.join(sys.argv[3::]) if len(sys.argv[3::]) != 0 else f"{t} {unit_display} reminder"
    except Exception:
        rich.print("[bold red]Please use the command format: [bold green]remindme -[s|m] [time] [reminder]")

    if not os.path.exists(TEMP_FOLDER_LOCATION):
        os.mkdir(TEMP_FOLDER_LOCATION)

    open(TEMP_FILE_LOCATION, "a").close()

    config = read_temp_toml_file(TEMP_FILE_LOCATION)
    config[reminder] = [str(t), str(flag[1])]

    write_temp_toml_file(config, TEMP_FILE_LOCATION)

    rich.print(f"Reminder for: [bold green]{reminder} set for [italic yellow]{t} {unit_display}")
    time.sleep(t if flag[1] == "s" else t * 60)
    os.system(f'notify-send -t 4000 "{reminder}"')
    os.system("paplay ./testing.mp3")

    del config[reminder]

    write_temp_toml_file(config, TEMP_FILE_LOCATION)

elif flag[1] == "l":
    try:
        
        config = read_temp_toml_file("/tmp/remindme/reminders.toml")

        if len(config) == 0:
            rich.print("[bold red]No reminders have been set yet!")
        else:
            i = 1
            print("\n")
            for key, value in config.items():
                unit_display = 'second' if value[-1] == 's' else 'minute'
                rich.print(f"[bold cyan]{i}.) [bold green]Reminder: {key} ==> [bold yellow]set for {value[0]} {unit_display}")
                i+=1
            print("\n")

    except FileNotFoundError as fnfe:
        rich.print("[bold red]No reminders have been set yet!")

elif flag[1] == "d":
    try:
        config = read_temp_toml_file(TEMP_FILE_LOCATION)
        
        if sys.argv[2] in config:
            reminder_to_kill = sys.argv[2]
            for proc in psutil.process_iter():
                if ' '.join(proc.cmdline()) == f"python remindme.py -{config[sys.argv[2]][-1]} {config[sys.argv[2]][0]} {reminder_to_kill}":
                    proc.kill()

            del config[sys.argv[2]]
            write_temp_toml_file(config, TEMP_FILE_LOCATION)

            rich.print(f"[bold green]{reminder_to_kill} successfully stopped!")
        
        else:
            raise Exception("This reminder does not exist.")

    except:
        pass

elif flag[1] == "help":
    pass
elif flag[1] == "conf":
    pass

