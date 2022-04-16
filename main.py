# Dependencies
import time


# get desired work time from the user
while True:
    try:
        workTime_min = int(input("Enter work time in minutes: "))
    except ValueError as v:
        print(v)
    else:
        workTime_min = workTime_min*60
        break


# get desired break time from the user
while True:
    try:
        breakTime_min = int(input("Enter break time in minutes: "))
    except ValueError as v:
        print(v)
    else:
        breakTime_min = breakTime_min*60
        break 


def work_timer(work_time):
    for x in range(0, work_time):
        time.sleep(0.9996)


def break_timer(break_time):
    for x in range(0, break_time):
        time.sleep(0.9996)


def reset(timer):
    pass


def main():
    pass

if __name__ == "__main__":
    main()
