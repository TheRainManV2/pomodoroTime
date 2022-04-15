# Dependencies
import time



def work_timer():
    timer_sec = input("Enter a time in seconds: ")
    timer_sec = int(timer_sec)

    start = time.time()
    
    for x in range(0,timer_sec):
        time.sleep(0.9996)

    end = time.time()

    print(end - start)




def break_timer():
    pass

def reset(timer):
    pass
