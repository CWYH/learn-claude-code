from __future__ import annotations

from collections.abc import Callable, Iterable, Iterator
from typing import Generic, TypeVar

T = TypeVar('T')


class BinaryHeap(Generic[T]):
    def __init__(
        self,
        values: Iterable[T] | None = None,
        *,
        key: Callable[[T], object] | None = None,
    ) -> None:
        self._data: list[T] = list(values or [])
        self._key = key or (lambda value: value)
        if self._data:
            self._heapify()

    @classmethod
    def max_heap(cls, values: Iterable[T] | None = None) -> 'BinaryHeap[T]':
        return cls(values, key=lambda value: _ReverseKey(value))

    def __len__(self) -> int:
        return len(self._data)

    def __bool__(self) -> bool:
        return bool(self._data)

    def __iter__(self) -> Iterator[T]:
        return iter(self._data)

    def __repr__(self) -> str:
        return 'BinaryHeap(' + repr(self._data) + ')'

    @property
    def data(self) -> tuple[T, ...]:
        return tuple(self._data)

    def peek(self) -> T:
        if not self._data:
            raise IndexError('peek from empty heap')
        return self._data[0]

    def push(self, item: T) -> None:
        self._data.append(item)
        self._sift_up(len(self._data) - 1)

    def pop(self) -> T:
        if not self._data:
            raise IndexError('pop from empty heap')

        top = self._data[0]
        last = self._data.pop()
        if self._data:
            self._data[0] = last
            self._sift_down(0)
        return top

    def replace(self, item: T) -> T:
        if not self._data:
            raise IndexError('replace on empty heap')
        top = self._data[0]
        self._data[0] = item
        self._sift_down(0)
        return top

    def pushpop(self, item: T) -> T:
        if self._data and self._less(self._data[0], item):
            item, self._data[0] = self._data[0], item
            self._sift_down(0)
        return item

    def clear(self) -> None:
        self._data.clear()

    def to_sorted_list(self) -> list[T]:
        clone = BinaryHeap(self._data, key=self._key)
        return [clone.pop() for _ in range(len(clone))]

    def _heapify(self) -> None:
        for index in range(len(self._data) // 2 - 1, -1, -1):
            self._sift_down(index)

    def _sift_up(self, index: int) -> None:
        while index > 0:
            parent = (index - 1) // 2
            if not self._less(self._data[index], self._data[parent]):
                break
            self._data[index], self._data[parent] = self._data[parent], self._data[index]
            index = parent

    def _sift_down(self, index: int) -> None:
        size = len(self._data)
        while True:
            left = 2 * index + 1
            right = left + 1
            best = index

            if left < size and self._less(self._data[left], self._data[best]):
                best = left
            if right < size and self._less(self._data[right], self._data[best]):
                best = right
            if best == index:
                break

            self._data[index], self._data[best] = self._data[best], self._data[index]
            index = best

    def _less(self, left: T, right: T) -> bool:
        return self._key(left) < self._key(right)


class _ReverseKey:
    def __init__(self, value: object) -> None:
        self.value = value

    def __lt__(self, other: '_ReverseKey') -> bool:
        return self.value > other.value

    def __eq__(self, other: object) -> bool:
        return isinstance(other, _ReverseKey) and self.value == other.value


if __name__ == '__main__':
    heap = BinaryHeap([5, 3, 8, 1, 2])
    heap.push(0)
    print(heap.to_sorted_list())

    max_heap = BinaryHeap.max_heap([5, 3, 8, 1, 2])
    print(max_heap.to_sorted_list())
