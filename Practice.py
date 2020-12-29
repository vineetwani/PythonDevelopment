import threading as th


def start_func():
    for i in range(1000):
        print("This is my Thread")


if __name__ == "__main__":
    th1 = th.Thread(target=start_func)
    th1.start()
    th1.join()
    print("Main Ends")
