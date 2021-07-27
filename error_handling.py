from time import time


def performance(fn):
    def wrapper(*args, **kwargs):
        t1 = time()
        fn(*args, **kwargs)
        t2 = time()
        print(f"Process Completed in {t2 - t1} Seconds")
    return wrapper


@performance
def age_restriction():
    try:
        age = int(input('What is your age?'))
        if age >= 18:
            print("Thank You\nAccess Granted")
        else:
            print("Sorry\nAccess Denied")
    except:
        print('Please Enter a Number')
        age_restriction()
    else:
        print("=====")
        return
    finally:
        print("Age Restriction Process Completed")


age_restriction()
