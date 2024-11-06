from random import randint
import threading
import time

lock = threading.Lock()


class Bank:
    def __init__(self):
        self.lock = lock
        self.balance = 0

    def deposit(self):
        for i in range(100):
            money = randint(50, 500)
            self.balance += money
            print(f'Пополнение: {money}. Баланс: {self.balance}')
            time.sleep(0.001)
            if self.balance >= 500 and self.lock == lock.locked():
                self.lock = lock.release()

    def take(self):
        for i in range(100):
            money = randint(50, 500)
            print(f'Запрос на {money}.')
            if money <= self.balance:
                self.balance -= money
                print(f'"Снятие: {money} Баланс: {self.balance}".')
            elif money > self.balance:
                print(f'Запрос отклонён, недостаточно средств. ')
                self.lock = lock.acquire()


bk = Bank()

# Т.к. методы принимают self, в потоки нужно передать сам объект класса Bank
th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')
