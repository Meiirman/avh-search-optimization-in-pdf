import os
import shutil
from PyPDF2 import PdfFileReader


path_input = "input"
path_scan = "scan"
path_digital = "digital"


def get_files(path):
    """Получает все PDF файлы в папке и возвращает список"""
    pdf_files = [f for f in os.listdir(path) if f.endswith('.pdf')]
    return pdf_files


def to_scan(file, path_input, path_scan):
    """Перемещает file с path_input на path_scan"""
    source_path = os.path.join(path_input, file)
    destination_path = os.path.join(path_scan, file)
    shutil.move(source_path, destination_path)


def to_digital(file, path_input, path_digital):
    """Перемещает file с path_input на path_digital"""
    source_path = os.path.join(path_input, file)
    destination_path = os.path.join(path_digital, file)
    shutil.move(source_path, destination_path)



def is_scanned(file_path):
    """Проверяет, является ли файл полностью сканированным"""
    with open(file_path, 'rb') as file:
        pdf_reader = PdfFileReader(file)
        num_pages = pdf_reader.numPages

        for page_num in range(num_pages):
            page = pdf_reader.getPage(page_num)
            text = page.extractText()

            # Проверяем наличие текста на странице
            if text.strip():
                return False  # Если хотя бы на одной странице есть текст, то файл не считается полностью сканированным

    return True


def main():
    """Основная функция
    Получает get_files и открывает каждый pdf файл.
    Если это полностью скан, то он кладет его в path_scan,
    если это цифровой PDF из которого можно получить текст, то кладет его в path_digital
    """
    pdf_files = get_files(path_input)
    for i in pdf_files:
        print(i)

    for file in pdf_files:
        file_path = os.path.join(path_input, file)

        if is_scanned(file_path):
            to_scan(file, path_input, path_scan)
        else:
            to_digital(file, path_input, path_digital)