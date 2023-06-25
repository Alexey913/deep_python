# Создайте функцию для сортировки файлов по директориям: видео, изображения, текст и т.п. 
# Каждая группа включает файлы с несколькими расширениями. 
# В исходной папке должны остаться только те файлы, которые не подошли для сортировки.

import os
from pathlib import Path

DICT_EXT = {"Музыка": ("mp3", "flac", "wav"),
            "Видео": ("mkv", "mp4", "avi"),
            "Изображения": ("jpg", "png", "gif"),
            "Текст": ("txt", "doc", "bin")}

def sort_files(directory):
    file_list = [files for *_, files in os.walk(directory)]
    return file_list
print (sort_files(os.getcwd()+"/files/"))