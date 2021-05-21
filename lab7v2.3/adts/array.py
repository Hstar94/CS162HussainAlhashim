from adts.iarray import IArray
import copy
class Array:

    def __init__(self, size: int = 0, instance=None) -> None:

        if instance is not None and not isinstance(instance, Array):
            raise TypeError

        if instance is not None:
            self.array = Array.clone(instance)
        else:
            self.array = [None] * size

    @staticmethod
    def clone(instance):

        if not isinstance(instance, Array):
            raise TypeError
        return copy.deepcopy(instance)

    def __getitem__(self, index: int):

        if len(self.array) > index and index >=0:
            return self.array[index]
        else:
            raise IndexError

    def __setitem__(self, index: int, data) -> None:
 
        if len(self.array) > index and index >=0:
            self.array[index] = data
        else:
            raise IndexError

    def __len__(self) -> int:
  
        return len(self.array)

    def resize(self, new_size: int) -> None:

        length = new_size - len(self.array)
        self.array.extend([None]*length)

    def __eq__(self, other) -> bool:

        if not len(self.array) == len(other):
            return False

        for i in range(len(self.array)):
            if not self.array[i] == other[i]:
                return False
        return True

    def __iter__(self):
        for i in self.array:
            yield i

    def __delitem__(self, index: int) -> None:

        self.array[index] = None

    def __contains__(self, item) -> bool:

        for i in self.array:
            if i == item:
                return True
        return False

    def clear(self) -> None:

        for i in range(len(self.array)):
            self.array[i] = None

    def __str__(self) -> str:

        res = ""
        for i in self.array:
            res = res + str(i) + " "
        return res
