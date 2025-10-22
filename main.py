from hebbian import Hebbian


model = Hebbian("data.csv")
model.train()

if __name__ == "__main__":
    if model.weights:
        sample = [9.0, 8.5, 7.9]
        prediction = model.predict(sample)
        print(f"Prediction: {prediction}")
