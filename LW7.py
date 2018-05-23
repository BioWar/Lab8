#  +Визначити ієрархію дорогоцінного та напівкоштовного каміння.
#  +Відібрати камені для намиста.
#  +Порахувати загальну вагу (у каратах) і вартість намиста.
#  +Провести сортування каміння намиста за цінністю.
#  +Знайти каміння в намисто, що відповідає заданому діапазону параметрів прозорості. //заломлення світла//
#
# Cтворити не менше ніж 3 конструктори
#  +1 – порожній,
#   2 – в який передається 1 об’єкт узагальненого класу,
#  +3 – в який передається стандартна колекція об’єктів
#  +Створити клас, що описує типізовану колекцію (типом колекції є узагальнений клас з лабораторної роботи №6),
#  +що реалізує заданий варіантом інтерфейс SET та має задану внутрішню структуру DOUBLY LINKED LIST
from collections import defaultdict
import weakref, operator


class Main:
    """
    set() -> new empty set object
    set(iterable) -> new set object
    Build an unordered collection of unique elements.
    """

    def add(self, stone,  *args, **kwargs):  # real signature unknown
        """
        Add an element to a set.

        This has no effect if the element is already present.
        """
        for i in stone:
            self.all.addFirst(i)

    def clear(self, item):  # real signature unknown
        """ Remove all elements from this set. """
        del self._dict[item]

    def copy(self, *args, **kwargs):  # real signature unknown
        """ Return a shallow copy of a set. """
        pass

    def difference(self, *args, **kwargs):  # real signature unknown
        """
        Return the difference of two or more sets as a new set.

        (i.e. all elements that are in this set but not the others.)
        """
        pass

    def difference_update(self, *args, **kwargs):  # real signature unknown
        """ Remove all elements of another set from this set. """
        pass

    def discard(self, *args, **kwargs):  # real signature unknown
        """
        Remove an element from a set if it is a member.

        If the element is not a member, do nothing.
        """
        pass

    def intersection(self, *args, **kwargs):  # real signature unknown
        """
        Return the intersection of two sets as a new set.

        (i.e. all elements that are in both sets.)
        """
        pass

    def intersection_update(self, *args, **kwargs):  # real signature unknown
        """ Update a set with the intersection of itself and another. """
        pass

    def isdisjoint(self, *args, **kwargs):  # real signature unknown
        """ Return True if two sets have a null intersection. """
        pass

    def issubset(self, *args, **kwargs):  # real signature unknown
        """ Report whether another set contains this set. """
        pass

    def issuperset(self, *args, **kwargs):  # real signature unknown
        """ Report whether this set contains another set. """
        pass

    def pop(self, *args, **kwargs):  # real signature unknown
        """
        Remove and return an arbitrary set element.
        Raises KeyError if the set is empty.
        """
        pass

    def remove(self, item):  # real signature unknown
        """
        Remove an element from a set; it must be a member.

        If the element is not a member, raise a KeyError.
        """
        del self._dict[item]

    def symmetric_difference(self, *args, **kwargs):  # real signature unknown
        """
        Return the symmetric difference of two sets as a new set.

        (i.e. all elements that are in exactly one of the sets.)
        """
        pass

    def symmetric_difference_update(self, *args, **kwargs):  # real signature unknown
        """ Update a set with the symmetric difference of itself and another. """
        pass

    def union(self, *args, **kwargs):  # real signature unknown
        """
        Return the union of sets as a new set.

        (i.e. all elements that are in either set.)
        """
        pass

    def update(self, *args, **kwargs):  # real signature unknown
        """ Update a set with the union of itself and others. """
        pass

    def __init__(self, *args):  # known special case of set.__init__
        """
        set() -> new empty set object
        set(iterable) -> new set object

        Build an unordered collection of unique elements.
        # (copied from class doc)
        """
        self._dict = {}
        for arg in args:
            self.add(arg)


class DoublyLinkedList():
    class Node:
        def __init__(self, data, prevNode, nextNode):
            self.data = data
            self.prevNode = prevNode
            self.nextNode = nextNode

    def __init__(self):
        super().__init__()
        self.first = None
        self.last = None
        self.count = 0

    def addFirst(self, data):

        if self.count == 0:
            self.first = self.Node(data, None, None)
            self.last = self.first

        elif self.count > 0:

            # create a new node pointing to self.first
            node = self.Node(data, None, self.first)

            # have self.first point back to the new node
            self.first.prevNode = node

            # finally point to the new node as the self.first
            self.first = node

        self.current = self.first
        self.count += 1

    def addLast(self, data):
        if self.count == 0:
            self.addFirst(0)
        else:
            self.last.nextNode = self.Node(data, self.last, None)
            self.last = self.last.nextNode
            self.count += 1

    def popFirst(self):
        if self.count == 0:
            raise RuntimeError("Cannot pop from an empty linked list")
        result = self.first.data
        if self.count == 1:
            self.first = None
            self.last = None
        else:
            self.first = self.first.nextNode
            self.first.prevNode = None
        self.current = self.first
        self.count -= 1
        return result

    def popLast(self):
        if self.count == 0:
            raise RuntimeError("Cannot pop from an empty linked list")
        result = self.last.data
        if self.count == 1:
            self.first = None
            self.last = None
        else:
            self.last = self.last.prevNode
            self.last.nextNode = None
        self.count -= 1
        return result

    def __repr__(self):
        result = ""
        if self.count == 0:
            return "..."
        cursor = self.first
        for i in range(self.count):
            result += "{}".format(cursor.data)
            cursor = cursor.nextNode
            if cursor is not None:
                result += " <=> "
        return result

    def __iter__(self):
        result = list()
        if self.count == 0:
            return None
        cursor = self.first
        for i in range(self.count):
            result.append(cursor.data)
            cursor = cursor.nextNode
            if cursor is None:
                break
        return result

    def next(self):
        # provides things iterating over class with next element
        if self.current is None:
            # allows us to re-iterate
            self.current = self.first
            raise StopIteration
        else:
            result = self.current.data
            self.current = self.current.nextNode
            return result

    def __len__(self):
        return self.count


class KeepRefs():
    __refs__ = defaultdict(list)

    def __init__(self):
        super().__init__()
        self.__refs__[self.__class__].append(weakref.ref(self))

    @classmethod
    def get_instances(cls):
        for inst_ref in cls.__refs__[cls]:
            inst = inst_ref()
            if inst is not None:
                yield inst


class Jewelry(DoublyLinkedList):

    def __init__(self):
        super().__init__()
        self.all = DoublyLinkedList()
        self.weight = 0.0
        self.price = 0.0
        self.cost = 0.0
        self.value_list = list()
        self.clarity_list = list()

    def add(self, stone):
        for i in stone:
            self.all.addFirst(i)

    def count_weight(self):
        for stone in self.all.__iter__():
            self.weight += stone.carat
        print("{:.2f}".format(self.weight))
        return self.weight

    def count_price(self):
        for stone in self.all.__iter__():
            self.price += stone.value
        print("{:.2f}".format(self.price))
        return self.price

    def sort_value(self):
        self.value_list = dict((gem.name, gem.value) for gem in self.all.__iter__())
        self.value_list = dict(sorted(self.value_list.items(), key=operator.itemgetter(1)))
        print(self.value_list)

    def clarity_check(self, clarity_min: float, clarity_max: float):
        for gem in self.all.__iter__():
            if clarity_min < gem.clarity < clarity_max:
                self.clarity_list.append(tuple((gem.name, gem.clarity)))
        print(dict(self.clarity_list))


class Stones(KeepRefs):

    def __init__(self):
        super().__init__()
        pass

    @classmethod
    def all_instances(cls):
        inventory = list()
        for r in cls.get_instances():
            inventory.append(r)
        return inventory


class PreciousStones(Stones):

    def __init__(self, name: str,  carat: float):
        super().__init__()
        self.carat = carat
        self.name = name


class PreciousStonesFO(PreciousStones):

    def __init__(self, name,  carat, value: int, clarity: float, hardness: float, hue: str):
        super().__init__(carat, name)
        self.carat = carat
        self.name = name
        self.value = value
        self.clarity = clarity
        self.hardness = hardness
        self.hue = hue


class PreciousStonesSO(PreciousStones):

    def __init__(self, name, carat, value: int, clarity: float, hardness: float, hue: str):
        super().__init__(carat, name)
        self.carat = carat
        self.name = name
        self.value = value
        self.clarity = clarity
        self.hardness = hardness
        self.hue = hue


class SemiPreciousStones(Stones):

    def __init__(self, name: str,  carat: float):
        super().__init__()
        self.name = name
        self.carat = carat


class SemiPreciousStonesFO(SemiPreciousStones):

    def __init__(self, name, carat, value: int, clarity: float, hardness: float, hue: str = None):
        super().__init__(carat, name)
        self.carat = carat
        self.name = name
        self.value = value
        self.clarity = clarity
        self.hardness = hardness
        self.hue = hue


class SemiPreciousStonesSO(SemiPreciousStones):

    def __init__(self, name, carat, value: int, clarity: float, hardness: float, hue: str):
        super().__init__(carat, name)
        self.carat = carat
        self.name = name
        self.value = value
        self.clarity = clarity
        self.hardness = hardness
        self.hue = hue


d_list = list(["diamond",   5.0, 50000, 2.402, 10.0, "clear"])
r_list = list(["ruby",      2.2, 39000, 1.762, 9.0,   " red"])
s_list = list(["sapphire",  3.1, 27000, 1.762, 9.0,   "blue"])
o_list = list(["onyx",      18.9, 1000, 1.535, 7.0,  "brown"])
m_list = list(["malachite", 14.2, 4500, 1.655, 4.0,  "green"])

diamond   = PreciousStonesFO    (*d_list)
ruby      = PreciousStonesFO    (*r_list)
sapphire  = PreciousStonesSO    (*s_list)
onyx      = SemiPreciousStonesSO(*o_list)
malachite = SemiPreciousStonesFO(*m_list)

necklace  = Jewelry()

necklace.add(SemiPreciousStonesSO.all_instances())
necklace.add(SemiPreciousStonesFO.all_instances())
necklace.add(PreciousStonesFO.all_instances())
necklace.add(PreciousStonesSO.all_instances())

necklace.count_price()
necklace.count_weight()
necklace.sort_value()
necklace.clarity_check(1.5, 1.75)
