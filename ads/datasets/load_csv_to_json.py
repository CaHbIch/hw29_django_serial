import csv, json

# Параметры
csv_file_ad = 'ad.csv'
json_file_ad = '../fixtures/ad.json'
ad_model = 'ads.ad'

csv_file_category = 'category.csv'
json_file_category = '../fixtures/category.json'
category_model = 'ads.category'

csv_file_location = 'location.csv'
json_file_location = '../fixtures/location.json'
location_model = 'users.location'

csv_file_user = 'user.csv'
json_file_user = '../fixtures/user.json'
users_model = 'users.user'


# Функция конвертации
def csv_to_json(csv_file_path: str, json_file_path: str, model: str) -> str:
    """Конвертировать csv в json"""

    fields_json = []
    # прочитать файл csv и добавить в словарь
    with open(csv_file_path, encoding='utf-8') as file:
        for row in csv.DictReader(file):

            data = {'model': model, 'pk': int(row['Id'] if 'Id' in row else int(row['id']))}

            if 'id' in row:
                del row['id']
            else:
                del row['Id']

            if 'is_published' in row:
                if row['is_published'] == 'TRUE':
                    row['is_published'] = True
                else:
                    row['is_published'] = False

            if 'location_id' in row:
                row['location'] = [int(row['location_id'])]
                del row['location_id']

            if 'price' in row:
                row['price'] = float(row['price'])

            data['fields'] = row
            fields_json.append(data)

        # создать новый файл json и записать данные
    with open(json_file_path, 'w', encoding='utf-8') as file:
        file.write(json.dumps(fields_json, indent=4, ensure_ascii=False))

    return f'Данные из CSV ({csv_file_path}) преобразовано в json ({json_file_path})'


if __name__ == '__main__':
    print(csv_to_json(csv_file_ad, json_file_ad, ad_model))
    print(csv_to_json(csv_file_category, json_file_category, category_model))
    print(csv_to_json(csv_file_location, json_file_location, location_model))
    print(csv_to_json(csv_file_user, json_file_user, users_model))
