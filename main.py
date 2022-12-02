class CookBook:
    def __init__(self):
        self.full_book = read_file('base.txt')

    def __str__(self):
        s = ''
        for k, v in self.full_book.items():
            s += k + ':\n'
            for i in v:
                s += ' '.join(map(str, i.values()))
                s += '\n'
            s += '\n'
        return s

    def get_shop_list_by_dishes(self, dishes, person_count):
        """Return dict of ingredients of dishes multiplied by person_count"""
        result = {}
        for dish in dishes:
            if dish not in self.full_book:
                print(f'Блюда "{dish}" нет в кулинарной книге.')
                continue
            for ingredient in self.full_book[dish]:
                if ingredient['ingredient_name'] in result:
                    result[ingredient['ingredient_name']]['quantity'] += ingredient['quantity'] * person_count
                else:
                    result[ingredient['ingredient_name']] = {'measure': ingredient['measure'],
                                                             'quantity': ingredient['quantity'] * person_count}
        return result


def read_file(file_name):
    """Return file content as dict"""
    result = {}
    with open(file_name, encoding='utf-8') as file:
        while line := file.readline():
            dish_name = line.strip()
            ingredients_count = int(file.readline())
            ingredients = []
            for i in range(ingredients_count):
                name, count, measure = file.readline().strip().split(' | ')
                ingredients.append({'ingredient_name': name, 'quantity': int(count), 'measure': measure})
            result[dish_name] = ingredients
            file.readline()
    return result


def main():
    cook_book = CookBook()
    print(cook_book.full_book)
    # print(cook_book) # if you want to see more convenient view
    print(cook_book.get_shop_list_by_dishes(['Фахитос', 'Омлет'], 2))


if __name__ == '__main__':
    main()
