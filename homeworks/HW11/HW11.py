
# TASK 1
# Створити логер який дозволяє працювати з файлами як звичайний open,
# але разом з тим в файл logs.txt записує:
# коли був відкритий файл, назва файла, коли закритий файл
# для інформації про час можемо використати datetime.now()
# приклад відпрацювання
# with my_custom_manager('file.txt', 'r') as f:
#     f.read()
# В файл буде записано
# 2022-07-11 22:17:59.782551 file.txt OPEN
# 2022-07-11 22:18:00.782551 file.txt CLOSE
import datetime as dt
import csv
import json

class new_contex_manager:

    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = open(filename, mode)
        with open('logs.txt', 'a') as self.file_object:
            self.file_object.write(f'{dt.datetime.now()} {self.filename} OPEN\n')

    def __enter__(self):
        return self.file

    def __exit__(self, exc_type, exc_value, exc_traceback):
        with open('logs.txt', 'a') as self.file_object:
            self.file_object.write(f'{dt.datetime.now()} {self.filename} CLOSE\n')
        self.file.close()


with new_contex_manager('logs.txt', 'w') as file_object1:
    file_object1.write('')




#  TASK 2
# Написати ф-цію яка переводить файл logs.txt в logs.csv
# Приклад такого файлу
# 2022-07-11 22:17:59.782551, file.txt, OPEN
# 2022-07-11 22:18:00.782551, file.txt, CLOSE


def convert():
    with open('logs.txt', 'r') as h_txt:
        lines = (line.split() for line in h_txt)
        with open('logs.csv', 'w') as h_csv:
            writer = csv.writer(h_csv)
            writer.writerows(lines)


convert()
with open('logs.csv', 'r') as h:
    print(h.read())

# TASK 3 (з зірочкою)
# Написати ф-цію, яка обраховує з файла logs.csv скільки раз був відкритий файл і його остання дата відкриття.
# Цю інформацію записати в logs.json. Приклад:
# {
#     "file.txt": {
#         "count": 2,
#         "last_time_opened": "2022-07-11 22:17:59.782551"
#     }
# }

csv_file_new = 'logs.csv'

def json_count(csv_file_new):

    with open(csv_file_new, 'r') as file:
        reader1 = csv.reader(file, delimiter=';')
        log_dict = {}
        for raw in reader1:
            if raw[0] == 'Date':
                continue
            elif raw[3] == 'OPEN' and raw[2] not in log_dict.keys():
                log_dict.update({raw[2]: {'count': 1, 'last opened': f'{raw[0]} {raw[1]}'}})
            elif raw[3] == 'OPEN' and raw[2] in log_dict.keys():
                log_dict[raw[2]]['count'] += 1
                log_dict[raw[2]]['last opened'] = f'{raw[0]} {raw[1]}'
    with open('logs.json', 'a+') as j_file:
        json.dump(log_dict, j_file, indent=4)