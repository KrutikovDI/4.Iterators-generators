import types

def flat_generator(list_of_lists):
    count1 = 0
    count2 = 0
    while count1 < len(list_of_lists):
        if count2 < len(list_of_lists[count1]):
            iter = list_of_lists[count1][count2]
            count2 += 1
            yield iter
        else:
            count1 += 1
            count2 = 0

def test_2():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            flat_generator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item

    assert list(flat_generator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]

    assert isinstance(flat_generator(list_of_lists_1), types.GeneratorType)


if __name__ == '__main__':
    test_2()