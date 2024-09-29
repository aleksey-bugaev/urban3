class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = []
        for i in file_names:
            self.file_names.append(i)

    def get_all_words(self):
        result = []
        all_words = {}
        s_replace = [',', '.', '=', '!', '?', ';', ':', ' - ']
        for s_file in self.file_names:
            with open(s_file, 'r', encoding='UTF-8') as file:
                lines = file.readlines()
                for line in lines:
                    for s_item in s_replace:
                        line = line.lower().replace(s_item, '')
                    s_line = line.split()
                    for _str in s_line:
                        result.append(_str)
                all_words[s_file] = result

        return all_words

    def find(self, word):
        find_words = {}
        for name, words in self.get_all_words().items():
            if word.lower() in words:
                find_words[name] = words.index(word.lower()) + 1
                return find_words

    def count(self, word):
        find_words = {}
        for name, words in self.get_all_words().items():
            if word.lower() in words:
                find_words[name] = words.count(word.lower())
                return find_words


finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())  # Все слова
print(finder2.find('TEXT'))  # 3 слово по счёту
print(finder2.count('teXT'))  # 4 слова teXT в тексте всего
