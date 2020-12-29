import threading as th
import time

#If we use a Queue, instead of buff here ->
#We need not worry about COndition Wait, notify and stuff
#Queue encapsulates the behaviour of Condition, wait(), notify(), acquire() etc.
#import Queue

buff = []
MAX_NUM = 20
#lock = th.Lock()
condition = th.Condition()


class Producer(th.Thread):
    singletonProducer = None

    def __init__(self):
        th.Thread.__init__(self)
        self.start()

    @classmethod
    def get_producer(cls):
        if cls.singletonProducer is None:
            return Producer()
        else:
            return cls.singletonProducer

    @classmethod
    def produce(cls, item):
        global buff
        condition.acquire()
        if len(buff) == MAX_NUM:
            print("Queue full, producer is waiting for consumer")
            condition.wait()
            print("Consumer has notified Producer about item consumption")

        buff.append(item)
        print "Produced", len(buff)
        condition.notify()
        condition.release()
        #time.sleep(0.5)

    def run(self):
        while True:
            for item in range(1, MAX_NUM):
                self.produce(item)


class Consumer(th.Thread):
    singletonConsumer = None

    def __init__(self):
        th.Thread.__init__(self)
        self.start()

    @classmethod
    def get_consumer(cls):
        if cls.singletonConsumer is None:
            return Consumer()
        else:
            return cls.singletonConsumer

    @staticmethod
    def consume():
        global buff
        condition.acquire()

        if not buff:
            print "Nothing in buffer, Consumer is waiting for Producer"
            condition.wait()
            print "Producer added something in buffer, and notified consumer"

        buff.pop(0)
        print "Consumed"
        condition.notify()
        condition.release()
        time.sleep(0.5)

    def run(self):
        while True:
            self.consume()


if __name__ == "__main__":
    producer = Producer.get_producer()

    print("{0}, Buffer : {1}".format(len(buff), buff))

    consumer = Consumer.get_consumer()

    producer.join()
    consumer.join()
    print("{0}, Buffer : {1}".format(len(buff), buff))
