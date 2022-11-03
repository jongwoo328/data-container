from collections import deque


class Container:
    def __init__(self):
        self.data_list = deque()

    def __len__(self):
        return len(self.data_list)

    def __str__(self):
        return f"Container<data: {len(self.data_list)}>"

    def add(self, data):
        assert data is not None

        self.data_list.append(data)

        while len(self.data_list) > 200:
            self.data_list.popleft()

    def delete_all(self):
        self.data_list.clear()

    def get_data(self):
        return [*self.data_list]
