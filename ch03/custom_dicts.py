# To create custom dicts we gotta inherit from the
# UserDict class instead of the ususal dict
import collections


class StrKeyDict(collections.UserDict):
    def __missing__(self, key):
        if isinstance(key, str):
            raise KeyError(key)
        return self[str(key)]

    def __contains__(self, key):
        return str(key) in self.data

    def __setitem__(self, key, item):
        self.data[str(key)] = item


pins = StrKeyDict({'1': 'Pin 1', '13': 'Pin 13'})
print(pins)

print('Pin 1 exists:', pins[1])
print('Pin 13 exists:', pins[13])

pins[12] = 'Pin 12'
print('Pin 12 now exists:', pins[12])
