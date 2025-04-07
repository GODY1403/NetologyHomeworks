def read_cook_book(file_path):
    cook_book = {}
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = [line.strip() for line in f if line.strip()]
    i = 0
    while i < len(lines):
        dish = lines[i]
        i += 1
        num_ingredients = int(lines[i])
        i += 1
        ingredients = []
        for _ in range(num_ingredients):
            parts = lines[i].split('|')
            ingredient = {
                'ingredient_name': parts[0].strip(),
                'quantity': int(parts[1].strip()),
                'measure': parts[2].strip()
            }
            ingredients.append(ingredient)
            i += 1
        cook_book[dish] = ingredients
    return cook_book


def get_shop_list_by_dishes(dishes, person_count, cook_book):
    shop_list = {}
    for dish in dishes:
        if dish not in cook_book:
            continue
        for ingredient in cook_book[dish]:
            name = ingredient['ingredient_name']
            measure = ingredient['measure']
            quantity = ingredient['quantity'] * person_count
            if name in shop_list:
                shop_list[name]['quantity'] += quantity
            else:
                shop_list[name] = {'measure': measure, 'quantity': quantity}
    return shop_list


def merge_files():
    import os
    files = [f for f in os.listdir('.') if f.endswith('.txt') and f != 'merged.txt']
    file_info = []
    for filename in files:
        with open(filename, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            line_count = len(lines)
            file_info.append((filename, line_count, lines))
    file_info.sort(key=lambda x: x[1])
    with open('merged.txt', 'w', encoding='utf-8') as out_f:
        for fname, count, lines in file_info:
            out_f.write(f"{fname}\n")
            out_f.write(f"{count}\n")
            out_f.writelines(lines)

# Создание cook_book
cook_book = read_cook_book('recipes.txt')
# Получение списка покупок
shop_list = get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2, cook_book)
print(shop_list)

# Объединение файлов
merge_files()
