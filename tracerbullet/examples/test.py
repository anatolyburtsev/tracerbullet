import time

def sleep_some_more():
    time.sleep(0.2)
    try:
        sleep_again()
    except BaseException:
        time.sleep(0.4)

def sleep_again():
    time.sleep(0.3)
    raise BaseException("boo!")

if __name__ == '__main__':
    time.sleep(0.1)
    sleep_some_more()