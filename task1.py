import os
import shutil
import time


def compare_folders(folder1, folder2):
    '''
    Данная функция сопоставляет/сравнивает
    наполнение папок
    :param folder1: первая папка
    :param folder2: вторая папка
    :return: измененные файлы/отсутствие изменений
    '''
    files1 = os.listdir(folder1) #возвращает список имен файлов в каталоге
    files2 = os.listdir(folder2)

    # Проверяем содержимое папок
    if set(files1) == set(files2):
        #(set(files1), set(files2))
        print("Содержимое папок совпадает")
    else:
        print("Содержимое папок не совпадает")
        # Добавляем недостающие файлы
        missing_files = set(files1) - set(files2)
        for file in missing_files:
            shutil.copy(os.path.join(folder1, file), folder2)
            print(f"Добавлен файл: {file}")

        # Удаляем лишние файлы
        extra_files = set(files2) - set(files1)
        for file in extra_files:
            os.remove(os.path.join(folder2, file))
            print(f"Удален файл: {file}")


def main(folder1, folder2, interval):
    while True:
        compare_folders(folder1, folder2)
        time.sleep(interval)


if __name__ == "__main__":
    folder1 = r"C:\Users\ASUS\Documents\testfolder1" #путь к папке
    folder2 = r"C:\Users\ASUS\Documents\testfolder2" #путь к папке
    interval = 5  # Проверка каждые 5 секунд

    main(folder1, folder2, interval)