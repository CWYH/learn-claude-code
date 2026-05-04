from algorithms.binary_heap import BinaryHeap


def assert_min_heap_property(heap: BinaryHeap[int]) -> None:
    data = heap.data
    for index, value in enumerate(data):
        left = 2 * index + 1
        right = left + 1
        if left < len(data):
            assert value <= data[left]
        if right < len(data):
            assert value <= data[right]


def test_push_pop_min_heap() -> None:
    heap = BinaryHeap[int]()
    for value in [5, 1, 3, 1, 9, -2, 0]:
        heap.push(value)
        assert_min_heap_property(heap)

    assert [heap.pop() for _ in range(len(heap))] == [-2, 0, 1, 1, 3, 5, 9]


def test_heapify_and_peek() -> None:
    heap = BinaryHeap([4, 7, 2, 6, 1])
    assert heap.peek() == 1
    assert heap.to_sorted_list() == [1, 2, 4, 6, 7]
    assert len(heap) == 5


def test_replace_and_pushpop() -> None:
    heap = BinaryHeap([2, 4, 6])
    assert heap.replace(1) == 2
    assert heap.pop() == 1

    assert heap.pushpop(3) == 3
    assert heap.to_sorted_list() == [4, 6]


def test_max_heap() -> None:
    heap = BinaryHeap.max_heap([5, 3, 8, 1, 2])
    heap.push(10)
    assert [heap.pop() for _ in range(len(heap))] == [10, 8, 5, 3, 2, 1]


def test_empty_errors() -> None:
    heap = BinaryHeap[int]()

    try:
        heap.pop()
        assert False
    except IndexError:
        pass

    try:
        heap.peek()
        assert False
    except IndexError:
        pass
