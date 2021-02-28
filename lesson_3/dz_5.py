# Реализовать функцию get_jokes(), возвращающую n шуток, сформированных из трех случайных слов,
# взятых из трёх списков (по одному из каждого):
from random import choice

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]


# Например:
# >>> get_jokes(2)
# ["лес завтра зеленый", "город вчера веселый"]
# Документировать код функции.
# Сможете ли вы добавить еще один аргумент — флаг, разрешающий или запрещающий повторы слов в шутках
# (когда каждое слово можно использовать только в одной шутке)? Сможете ли вы сделать аргументы именованными?

def get_jokes(namber, flag='allow'):
    list_d = []
    new_nouns, new_adverbs, new_adjectives = nouns, adverbs, adjectives.copy()
    while namber > 0:
        ch_new_nouns, ch_new_adverbs, ch_new_adjectives = choice(new_nouns), choice(new_adverbs), choice(
            new_adjectives)
        list_d.append(f'{ch_new_nouns} {ch_new_adverbs} {ch_new_adjectives}')
        if flag == 'block':
            new_nouns.remove(ch_new_nouns)
            new_adverbs.remove(ch_new_adverbs)
            new_adjectives.remove(ch_new_adjectives)
        namber -= 1

    return list_d


print(get_jokes(5, 'block'))
