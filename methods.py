import json

def get_json():
    """Получает JSON из файла data.json"""

    try:
        with open('data.json', 'r', encoding='utf-8') as file:
            json_data = json.load(file)
        return json_data
    except FileNotFoundError:
        print(f"Файл data.json не найден.")
        return None
    except json.JSONDecodeError as e:
        print(f"Ошибка декодирования JSON в файле data.json: {e}")
        return None


def get_search_results(text_array, template):
    results = []
    for row, string in enumerate(text_array):
            for tmpl in template:
                if tmpl.lower() in string.lower():
                    text = ""
                    try: text ="<br>" + text_array[row-1]
                    except: pass

                    text += "<br>" + string

                    try: text += "<br>" + text_array[row+1]
                    except: pass

                    results.append(text)
    return "<br><span>___________________________________</span><br>".join(results)


def get_number(text_array):
    results = []
    templates = get_json()
    if templates:
        template = templates["number"]
        result = get_search_results(text_array, template)
        return result
    return ""


def get_contractor(text_array):
    templates = get_json()
    if templates:
        template = templates["contractor"]
        result = get_search_results(text_array, template)
        return result
    return ""


def get_address(text_array):
    templates = get_json()
    if templates:
        template = templates["address"]
        result = get_search_results(text_array, template)
        return result
    return ""


def get_start_date(text_array):
    templates = get_json()
    if templates:
        template = templates["start_date"]
        result = get_search_results(text_array, template)
        return result
    return ""


def get_deadline(text_array):
    templates = get_json()
    if templates:
        template = templates["deadline"]
        result = get_search_results(text_array, template)
        return result
    return ""


def get_budget(text_array):
    templates = get_json()
    if templates:
        template = templates["budget"]
        result = get_search_results(text_array, template)
        return result
    return ""

