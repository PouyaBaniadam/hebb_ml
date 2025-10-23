from hebbian import Hebbian

def display_results(accuracy, total_samples):
    print("""
===== Model Evaluation Results =====
""")
    print(f"The model was tested on {total_samples} unseen samples.")
    print(f"Model Accuracy: {accuracy:.2f}%")

def main():
    file_address = "admissions/admissions.csv"

    print("""
===== Initializing model and preparing datasets... =====
""")
    model = Hebbian(file_address)

    print(f"Data successfully loaded.")
    print(f"Training set size: {len(model.train_dataset)} samples")
    print(f"Test set size: {len(model.test_dataset)} samples")

    print("""
===== Starting model ==training... =====
""")
    model.train()
    print("Training complete.")

    if model.weights:
        formatted_weights = [f"{w:.2f}" for w in model.weights]
        print(f"Final Learned Weights: {formatted_weights}")
        print(f"Final Learned Bias: {model.bias}")

        accuracy, correct, total = model.test()
        display_results(accuracy, total)

if __name__ == "__main__":
    main()