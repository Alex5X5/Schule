

class DatabaseCollection:

    def __init__(self, data_type:type):
        self.data_type = data_type
        self.data = [10, 20, 30, 40, 50]

    def __getitem__(self, index):
        return self.data[index]

    def __setitem__(self, index, value):  # for assignment: obj[i] = value
        self.data[index] = value

    def __delitem__(self, index):  # for deletion: del obj[i]
        del self.data[index]
