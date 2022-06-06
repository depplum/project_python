import sys, argparse, os

parser = argparse.ArgumentParser() # создаем парсер
parser.add_argument('--directory', '-d') # добавляем аргументы
parser.add_argument('--action', '-a')
parser.add_argument('--count', '-c')
args = parser.parse_args(sys.argv[1:]) # собираем аргументы из командной строки

def main(directory, action, count):
    if not os.path.isdir(directory): # проверяем существует ли директория
        print('Ошибка! Указанный путь это не директория или ее не существует')
        return # в таком случае завершаем выполнение
    try:
        if not int(count) > 0: # проверяем является ли count числом и что оно больше нуля
            print('Ошибка! Аргумент -c должен быть целым числом больше нуля')
            return # в таком случае завершаем выполнение
    except ValueError: # обрабытываем ошибку, если count указан строкой
        print('Ошибка! Аргумент -c должен быть целым числом')
        return # в таком случае завершаем выполнение

    files_dict = {} # словарь время-файл
    time_list = [] # словарь времени для сортировки
    if action == 'change': # если выбрано изменение файла
        for root, dirs, files in os.walk(directory):
            for title in files: # для каждого файла в списке файлов
                full = root + '/' + title # получаем полный путь файла
                time = os.path.getmtime(full) # получаем время изменения файла
                files_dict[time] = full # заносим время изменения и путь к файлу в словарь
                time_list.append(time) # добавляем время изменения в общий список
    elif action == 'access': # если выбрано чтение файла
        for root, dirs, files in os.walk(directory):
            for title in files: # для каждого файла в списке файлов
                full = root + '/' + title # получаем полный путь файла
                time = os.path.getatime(full) # получаем время чтения файла
                files_dict[time] = full # заносим время чтения и путь к файлу в словарь
                time_list.append(time) # добавляем время чтения в общий список
    else: # если не указан верный режим, выводим ошибку
        print('Ошибка! Не указано действие или указано неверно. Укажите -a change либо access')
        return

    time_list.sort(reverse=True) # сортируем список со временем по убыванию
    for i in range(0, int(count)): # выполняем цикл заданное количество раз
        print(files_dict[time_list[i]]) # выводим название файла по времени изменения или чтения

main(args.directory, args.action, args.count) # запускаем функцию с аргументами, которые мы получили вначале

# python3 script.py -d [path/to/dir] -a [access or change] -c [the first n]