class FlatIterator:
    def __init__(self, list_of_list):
        self.list_of_list = list_of_list

    def __iter__(self):
        self.count1 = 0
        self.count2 = 0
        self.len1 = len(self.list_of_list)
        self.list = []
        return self

    def __next__(self):
        while self.count1 < self.len1:
            if self.count2 < len(self.list_of_list[self.count1]):
                item = self.list_of_list[self.count1][self.count2]
                self.count2 += 1
                return item
            else:
                self.count1 += 1
                self.count2 = 0
        raise StopIteration

def test_1():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]


if __name__ == '__main__':
    test_1()