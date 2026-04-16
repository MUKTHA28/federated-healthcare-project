from data.load_data import load_data
from models.model import create_model, train_model, get_weights

def client_train(file):
    X, y = load_data(file)

    model = create_model()
    model = train_model(model, X, y)

    coef, intercept = get_weights(model)

    print(f"Trained on {file}")
    return coef, intercept


if __name__ == "__main__":
    client_train("data/hospital2.csv")