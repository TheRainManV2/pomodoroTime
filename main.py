# Dependencies
import time


# make function to get time input from users
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


def work_timer(work_time):
    while work_time:
        mins, secs = divmod(work_time, 60)
        timer = f"{mins:02d}:{secs:02d}"
        print(timer, end="\r")
        time.sleep(0.9996)
        work_time -= 1


def break_timer(break_time):
    for x in range(0, break_time):
        time.sleep(0.9996)


def reset(timer):
    pass


def main():
    work_time = get_timer_min("work")
    break_time = get_timer_min("break")
    work_timer(work_time)

if __name__ == "__main__":
    main()
