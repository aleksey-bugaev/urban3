import threading
import time


class Knight(threading.Thread):

    def __init__(self, name, power):
        threading.Thread.__init__(self)
        self.name = name
        self.power = power
        self.enemy = 100

    def timer(self, name, enemy):
        counter = 0
        while enemy:
            enemy -= self.power
            counter += 1
            time.sleep(1)
            print(f'{self.name} сражается {counter} дней, осталось {enemy} воинов' + "\n")
        print(f'{self.name} одержал победу спустя {counter} дней!' + "\n")

    def run(self):
        print(f'{self.name} , на нас напали!' + "\n")
        self.timer(self.name, self.enemy)


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)
first_knight.start()
second_knight.start()
first_knight.join()
second_knight.join()

if not first_knight.is_alive() or not second_knight.is_alive():
    print('Все битвы закончились!' + "\n")
