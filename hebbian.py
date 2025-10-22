import csv


class Hebbian:
    def __init__(self, file_address):
        self.file_address = file_address
        self.dataset = []
        self.features_count = 0
        self.weights = None
        self.bias = None

        self._load_and_process_data()

    def _load_and_process_data(self):
        with open(self.file_address, mode='r') as file:
            csv_reader = csv.reader(file)
            csv_content = [row for row in csv_reader]

            num_columns_ref = len(csv_content[0])
            self.features_count = num_columns_ref - 1

            for row in csv_content:
                if len(row) != num_columns_ref:
                    continue # Skipping. Invalid data!

                inputs = [float(item) for item in row[:-1]]
                label = int(row[-1])
                self.dataset.append([inputs, label])

    def train(self):
        self.weights = [0.0] * self.features_count
        self.bias = 0.0

        for inputs, label in self.dataset:
            for index in range(self.features_count):
                self.weights[index] += inputs[index] * label
            self.bias += label

    def predict(self, inputs):
        score = self.bias
        for i in range(self.features_count):
            score += self.weights[i] * inputs[i]

        return 1 if score > 0 else -1
