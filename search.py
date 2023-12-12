import os
from PyPDF2 import PdfFileReader
from methods import get_number, get_contractor, get_address, get_start_date, get_deadline, get_budget


path_digital = "digital"
html_file = "search.html"


def get_text(file_path):
    """Получает текст из pdf файла"""
    with open(file_path, 'rb') as file:
        pdf_reader = PdfFileReader(file)
        num_pages = pdf_reader.numPages

        text = ""
        for page_num in range(num_pages):
            page = pdf_reader.getPage(page_num)
            text += page.extractText()

        return text


def get_files(path):
    """Получает все PDF файлы в папке и возвращает список"""
    pdf_files = [f for f in os.listdir(path) if f.endswith('.pdf')]
    return pdf_files


def set_to_html(file, data_dict, first=False):
    if first:
        with open(html_file, 'w', encoding='utf-8') as html:
            html.write("""<DOCTYPE html>
                       <html>
                           <head>
                               <meta charset="utf-8">
                               <title>Search Results</title>
                               <style>
                                .one-file {
                                    border: 1px solid black;
                                    padding: 8px;
                                    margin: 8px;
                                }
                                p {
                                    border: 1px solid silver;
                                    padding: 4px;   
                                    margin-top: 14px;
                                }
                               </style>
                           </head>
                           <body>
                       """)
            return ""
    
    """Записывает данные в конец html файла содержимое в text"""
    text = f'''
        <div class="one-file">
            <h3>{file}</h3>
            <p>НОМЕР ДОГОВОРА: {data_dict["number"]}</p>
            <p>КОНТРАГЕНТ: {data_dict["contractor"]}</p>
            <p>АДРЕС: {data_dict["address"]}</p>
            <p>ДАТА ПОДПИСАНИЯ: {data_dict["start_date"]}</p>
            <p>СРОК ДЕЙСТВИЯ: {data_dict["deadline"]}</p>
            <p>СУММА: {data_dict["budget"]}</p>
        </div>
    '''
    with open(html_file, 'a', encoding='utf-8') as html:
        html.write(text)


def main():
    """Получает файлы с папки path_digital и записывает в set_to_html"""
    
    
    if not os.path.exists(html_file):
        with open(html_file, 'w', encoding='utf-8') as html:
            html.write("""<DOCTYPE html>
                       <html>
                           <head>
                               <meta charset="utf-8">
                               <title>Search Results</title>
                               <style>
                                .one-file {
                                    border: 1px solid black;
                                    padding: 8px;
                                    margin: 8px;
                                }
                                p {
                                    border: 1px solid silver;
                                    padding: 4px;
                                    margin-top: 14px;
                                }
                               </style>
                           </head>
                           <body>
                       """)

    set_to_html(html_file, {}, first=True)
    for file in get_files(path_digital):
        file_path = os.path.join(path_digital, file)
        text = get_text(file_path)
        text_array = list(filter(lambda x: x != "\n", text.split("\n")))
        
        # Пример словаря с данными (замените на свои данные)
        data_dict = {
            "number": get_number(text_array),
            "contractor": get_contractor(text_array),
            "address": get_address(text_array),
            "start_date": get_start_date(text_array),
            "deadline": get_deadline(text_array),
            "budget": get_budget(text_array)
        }

        # Запись данных в HTML файл
        set_to_html(file, data_dict)

    with open(html_file, 'a', encoding='utf-8') as html:
        html.write('</body></html>')