import threading

counter = 0


def worker():
    """
    my job is to print something
    :return:
    """
    global counter
    print("current number is %d"% counter)


if __name__ == "__main__":
    for i in range(10):
        threading.Thread(target=worker()).start()
        counter += 1
