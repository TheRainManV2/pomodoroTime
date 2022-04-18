# Dependencies
import time


# Get time input from users
def get_timer_min(workORbreak):
    while True:
        try:
            time_min = int(input(f"Enter {workORbreak} time in minutes: "))
        except ValueError as v:
            print(v)
        else:
            time_min *= 60
            return time_min
            break


def start_timer(timeMode):
    while timeMode:
        mins, secs = divmod(timeMode, 60)
        timer = f"{mins:02d}:{secs:02d}"
        print(timer, end="\r")
        time.sleep(0.9996)
        timeMode -= 1


# Add desktop notification
def notify(mode):
    if mode == 'break':
        print("It's time to take a break")
    elif mode == 'work':
        print("It's time to work")
    else:
        print('enter a valid mode (work/break)')


def reset(timer):
    pass


def main():
    work_time = get_timer_min("work")
    break_time = get_timer_min("break")
    start_timer(work_time)
    notify('break')
    start_timer(break_time)
    notify("work")

if __name__ == "__main__":
    main()
