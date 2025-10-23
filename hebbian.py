import csv
import random


class Hebbian:
    def __init__(self, file_address):
        self.file_address = file_address
        self.train_dataset = []
        self.test_dataset = []
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

            random.shuffle(csv_content)

            for index, row in enumerate(csv_content):
                if len(row) != num_columns_ref:
                    continue # Skipping. Invalid data!

                inputs = [float(item) for item in row[:-1]]
                label = int(row[-1])

                if index < len(csv_content) * 0.8:
                    self.train_dataset.append([inputs, label])
                else:
                    self.test_dataset.append([inputs, label])

    def train(self):
        self.weights = [0.0] * self.features_count
        self.bias = 0

        for inputs, label in self.train_dataset:
            for index in range(self.features_count):
                self.weights[index] += inputs[index] * label
            self.bias += label

    def test(self):
        correct_predictions = 0
        total_samples = len(self.test_dataset)

        for inputs, true_label in self.test_dataset:
            prediction = self.predict(inputs)
            if prediction == true_label:
                correct_predictions += 1

        accuracy = (correct_predictions / total_samples) * 100

        return accuracy, correct_predictions, total_samples

    def predict(self, inputs):
        score = self.bias
        for i in range(self.features_count):
            score += self.weights[i] * inputs[i]

        return 1 if score > 0 else -1
