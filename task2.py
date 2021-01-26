"""
Задание 2.**

Доработайте пример структуры "дерево",
рассмотренный на уроке.

Предложите варианты доработки и оптимизации
(например, валидация значений узлов в соответствии с требованиями для бинарного дерева)

Поработайте с доработанной структурой, позапускайте на реальных данных.
"""

''' 
Оптимизируем класс по принципу бинарного дерева 
исходя из условия если дочерний узел меньше главного узла то ветка в лево
иначе в право

Добавляем вот этот метод
    def insert_child(self, new_node):
        if new_node <= self.root:
            self.insert_left(new_node)
        else:
            self.insert_right(new_node)


'''


class BinaryTree:
    def __init__(self, root_obj):
        # корень
        self.root = root_obj
        # левый потомок
        self.left_child = None
        # правый потомок
        self.right_child = None

    # Метод добавления потомка с валидауией для бинарного дерева
    def insert_child(self, new_node):
        if new_node <= self.root:
            self.insert_left(new_node)
        else:
            self.insert_right(new_node)

    # добавить левого потомка
    def insert_left(self, new_node):
        # если у узла нет левого потомка

        if self.left_child == None:
            # тогда узел просто вставляется в дерево
            # формируется новое поддерево
            self.left_child = BinaryTree(new_node)
        # если у узла есть левый потомок
        else:
            # тогда вставляем новый узел
            tree_obj = BinaryTree(new_node)
            # и спускаем имеющегося потомка на один уровень ниже
            tree_obj.left_child = self.left_child
            self.left_child = tree_obj

    # добавить правого потомка
    def insert_right(self, new_node):
        # если у узла нет правого потомка

        if self.right_child == None:
            # тогда узел просто вставляется в дерево
            # формируется новое поддерево
            self.right_child = BinaryTree(new_node)
        # если у узла есть правый потомок
        else:
            # тогда вставляем новый узел
            tree_obj = BinaryTree(new_node)
            # и спускаем имеющегося потомка на один уровень ниже
            tree_obj.right_child = self.right_child
            self.right_child = tree_obj

    # метод доступа к правому потомку
    def get_right_child(self):
        return self.right_child

    # метод доступа к левому потомку
    def get_left_child(self):
        return self.left_child

    # метод установки корня
    def set_root_val(self, obj):
        self.root = obj

    # метод доступа к корню
    def get_root_val(self):
        return self.root


def print_child(r):
    if r.left_child == None:
        rrl = None
    else:
        rrl = r.left_child.root

    if r.right_child == None:
        rrr = None
    else:
        rrr = r.right_child.root

    print(rrl, rrr)


r = BinaryTree(8)
print('Главный узел', r.get_root_val())
print(f'Левый потомок: {r.get_left_child()} Правый потомок: {r.get_right_child()}')
print_child(r)
r.insert_child(4)
print('Главный узел', r.get_root_val())
print(f'Левый потомок: {r.left_child} Правый потомок: {r.get_right_child()}')
print_child(r)
r.insert_child(12)
print('Главный узел', r.get_root_val())
print(f'Левый потомок: {r.get_left_child()} Правый потомок: {r.get_right_child()}')
print_child(r)

r.insert_child(9)
print('Главный узел', r.get_root_val())
print(f'Левый потомок: {r.get_left_child()} Правый потомок: {r.get_right_child()}')
print_child(r)

r.insert_child(2)
print('Главный узел', r.get_root_val())
print(f'Левый потомок: {r.get_left_child()} Правый потомок: {r.get_right_child()}')
print_child(r)
