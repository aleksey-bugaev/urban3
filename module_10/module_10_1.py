from time import sleep
import threading
import time


def write_words(word_count, file_name):
    file = open(file_name, 'w', encoding='UTF-8')

    for i in range(word_count):
        file.write(f'Какое-то слово № {i}' + "\n")
    file.close()

    print(f"Завершилась запись в файл {file_name}")
    # print(threading.current_thread())
    sleep(0.1)

start_time = time.time()

write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')

print(f'Работа функций {time.time()-start_time}')

start_time = time.time()

thread1 = threading.Thread(target=write_words, args=([10, 'example5.txt']))
thread1.start()
thread2 = threading.Thread(target=write_words, args=([30, 'example6.txt']))
thread2.start()
thread3 = threading.Thread(target=write_words, args=([200, 'example7.txt']))
thread3.start()

thread1.join()

write_words(100, 'example8.txt')

print(f'Работа потоков {time.time()-start_time}')


