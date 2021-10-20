new_f = open("New file.txt", "r", encoding="utf-8")
word = list((line.split() for line in new_f))
for el in word:
    print(f"Слов в строке: {len(el)}")
print(f"Количество строк в файле: {sum(1 for line in open('New file.txt'))}")
new_f.close()
