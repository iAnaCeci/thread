import threading
import time

class Verse(threading.Thread):
    def __init__(self, verse):
        threading.Thread.__init__(self)
        self.verse = verse

    def run(self):
        for i in range(4):
            print(self.verse)
            time.sleep(1)

class Chorus(threading.Thread):
    def __init__(self, chorus):
        threading.Thread.__init__(self)
        self.chorus = chorus

    def run(self):
        for i in range(2):
            print(self.chorus)
            time.sleep(2)

class Bridge(threading.Thread):
    def __init__(self, bridge):
        threading.Thread.__init__(self)
        self.bridge = bridge

    def run(self):
        print(self.bridge)
        time.sleep(3)

def main():
    t1 = Verse("This is the first verse.")
    t2 = Chorus("Chorus!")
    t3 = Verse("This is the second verse.")
    t4 = Chorus("Chorus!")
    t5 = Bridge("Bridge...")
    t6 = Verse("This is the third verse.")
    t7 = Chorus("Chorus!")
    t1.start()
    t2.start()
    t3.start()
    t4.start()
    t5.start()
    t6.start()
    t7.start()

if __name__ == '__main__':
    main()
