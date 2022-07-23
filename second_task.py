# Как то я надумал только одну реализацию циклического буфера fifo

class CycleBuffer:
    def __init__(self, custom_size):
        self._data = []
        self.size = custom_size

    def put_element(self, obj):
        if len(self._data)+1 > self.size:
            self.get_element()
            self._data.append(obj)
        else:
            self._data.append(obj)

    def get_element(self):
        if self._data:
            return self._data.pop(0)

    def get_size(self):
        return len(self._data)


# Тесты созданного класса
b = CycleBuffer(7)
print(b.get_element())  # Если буфер пуст показывает None

b.put_element(5)
b.put_element('str')
print(b.get_element())
print(b.get_element())
print(b.get_element())  # Добавление и получение элементов работает корректно

for i in range(10):
    b.put_element(i)

for i in range(b.get_size()):  # Можно при помощи метода get_size забирать элементы из буфера
    print(b.get_element())
