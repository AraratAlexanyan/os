import os
import re

print('**** Problem N1 ****\n')

file_paths = 'text.txt'

count_every_line = dict()
sum_ = 0
index = 0

with open(file_paths, 'r') as txt:
    for line in txt:
        index += 1
        for symbol in line:
            if symbol.isdigit():
                sum_ += int(symbol)
        count_every_line[index] = sum_
        sum_ = 0

txt.close()
print(count_every_line)


print('\n**** Problem N2 ****\n')

sum_all = 0

with open(file_paths, 'r') as txt:
    for line in txt:
        for symbol in line:
            if symbol.isdigit():
                sum_all += int(symbol)

txt.close()
print(sum_all)

print('\n**** Problem N3 ****\n')

spec_words = []

with open(file_paths, 'r') as file:
    for line in file:
        line_words = line.split()
        for word in line_words:
            if word.startswith('<<') and word.endswith('>>'):
                spec_words.append(word)

file.close()
print(spec_words)


print('\n**** Problem N4 ****\n')

write_file_path = os.path.join(os.getcwd(), 'text_no_digits')
custom_line = ''

with open(file_paths) as file:
    with open(write_file_path, 'w') as writer:
        for line in file:
            for symbol in line:
                if not symbol.isdigit():
                    custom_line += symbol
        custom_line = re.sub(' +', ' ', custom_line)
        writer.write(custom_line)
    writer.close()
file.close()

with open(write_file_path) as file:
    for line in file:
        print(line, end='')

    file.close()
