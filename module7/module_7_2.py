from pprint import pprint


def custom_write(file_name, strings):
    file = open(file_name, 'a', encoding="UTF-8")
    # file.read()
    num_str = 1
    nom_poz = {}

    for i in strings:
        nom_poz[(num_str, file.tell())] = i
        file.write(i + "\n")
        num_str += 1

    file.close()
    return nom_poz


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
]

result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)
