import os
import sys
import toml
import time
import rich
import psutil 

try:
    flag = sys.argv[1]

    if flag[1] == "s" or flag[1] == "m":
        t = int(sys.argv[2])
        unit_display = 'second' if flag[1] == 's' else 'minute'
        reminder = ' '.join(sys.argv[3::]) if len(sys.argv[3::]) != 0 else f"{t} {unit_display} reminder"
        
        if not os.path.exists("/tmp/remindme"):
            os.mkdir("/tmp/remindme")

        open("/tmp/remindme/reminders.toml", "a").close()

        with open("/tmp/remindme/reminders.toml", "r", encoding="utf-8") as f:
            config = toml.load(f)
            config[reminder] = [str(t), str(flag[1])]
        with open("/tmp/remindme/reminders.toml", "w", encoding="utf-8") as f:
            toml.dump(config, f)

        rich.print(f"Reminder for: [bold green]{reminder} set for [italic yellow]{t} {unit_display}")
        time.sleep(t if flag[1] == "s" else t * 60)
        os.system(f'notify-send -t 4000 "{reminder}"')
        os.system("paplay ./testing.mp3")

        del config[reminder]

        with open("/tmp/remindme/reminders.toml", "w", encoding="utf-8") as f:
            toml.dump(config, f)

    elif flag[1] == "l":
        try:
            with open("/tmp/remindme/reminders.toml", "r", encoding="utf-8") as f:
                config = toml.load(f)
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
            with open("/tmp/remindme/reminders.toml", "r", encoding="utf-8") as f:
                config = toml.load(f)
            
            if sys.argv[2] in config:
                reminder_to_kill = sys.argv[2]
                for proc in psutil.process_iter():
                    if ' '.join(proc.cmdline()) == f"python remindme.py -{config[sys.argv[2]][-1]} {config[sys.argv[2]][0]} {reminder_to_kill}":
                        proc.kill()

                del config[sys.argv[2]]
                with open("/tmp/remindme/reminders.toml", "w", encoding="utf-8") as f:
                    toml.dump(config, f)

                rich.print(f"[bold green]{reminder_to_kill} successfully stopped!")
            
            else:
                raise Exception("This reminder does not exist.")

        except:
            pass

    elif flag[1] == "help":
        pass
    elif flag[1] == "conf":
        pass

except Exception as e:
    print(e)
    rich.print("[red]Please use the correct command format: [green]remindme -[flag] [time] [your reminder]")

