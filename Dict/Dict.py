class DefaultDict(dict):

    def __init__(self, *args, **kwargs):
        if "default" in kwargs:
            self.default = kwargs['default']
            kwargs.pop('default')

        else:
            self.default = None

        super().__init__(*args, **kwargs)

    def __getitem__(self, key):
        if key in self:
            return super().__getitem__(key)

        else:
            return self.default


d = DefaultDict([('name', "Adin"), ('age', 20)], gio = 10, default="Gio")
d[2] = 1

print(d[1])
print(d[2])
print(d[3])


class SuperList(list):
    def __getitem__(self, index):
        return super().__getitem__(index) * 10


l = SuperList([1, 2, 3, 4])
print(l[1])
l.pop()
print(l)

for key, val in d.items():
    print(key, val)


