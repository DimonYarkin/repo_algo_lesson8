"""
Задание 1.
Реализуйте кодирование строки "по Хаффману".
У вас два пути:
1) тема идет тяжело? тогда вы можете, опираясь на пример с урока, сделать свою версию алгоритма
Разрешается и приветствуется изменение имен переменных, выбор других коллекций, различные изменения
и оптимизации.
КОПИПАСТ ПРИМЕРА ПРИНИМАТЬСЯ НЕ БУДЕТ!
2) тема понятна? постарайтесь сделать свою реализацию.
Вы можете реализовать задачу, например, через ООП или предложить иной подход к решению.

ВНИМАНИЕ: примеры заданий будут размещены в последний день сдачи.
Но постарайтесь обойтись без них.
"""
import heapq
from collections import Counter, namedtuple


# Структура дерева имеет потомков
class Node(namedtuple('Node', ['left', 'right'])):
    def walk(self, code, acc):
        self.left.walk(code, acc + '0')
        self.right.walk(code, acc + '1')


# Листья дерева не имееют потомков но имеют значения
class Leat(namedtuple('Leat', ['char'])):
    def walk(self, code, acc):
        code[self.char] = acc or '0'


# Функция кодирования
def huffman_encode(s):
    h = []
    for ch, freq in Counter(s).items():
        h.append((freq, len(h), Leat(ch)))

    heapq.heapify(h)
    count = len(h)
    while len(h) > 1:
        freq1, _count1, left = heapq.heappop(h)
        freq2, _count2, rigth = heapq.heappop(h)
        heapq.heappush(h, (freq1 + freq2, count, Node(left, rigth)))
        count += 1
    code = {}
    if h:
        [(_freq, _count, root)] = h
        root.walk(code, '')

    return code


# Функция декодирования
def huffman_decoder(encoded, code):
    sx = []
    en_ch = ''
    for ch in encoded:
        en_ch += ch
        for dec_ch in code:
            if code.get(dec_ch) == en_ch:
                sx.append(dec_ch)
                en_ch = ''
                break
    return ''.join(sx)


def main():
    s = 'beep boop beer!'
    code = huffman_encode(s)
    encoded = ''.join(code[ch] for ch in s)
    for ch in sorted(code):
        print(f'{ch}: {code[ch]}')
    print(encoded)
    print(huffman_decoder(encoded, code))


if __name__ == '__main__':
    main()
