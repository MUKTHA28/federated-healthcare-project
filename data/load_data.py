import pandas as pd

def load_data(file):
    data = pd.read_csv(file)
    X = data[['age', 'glucose', 'bp']]
    y = data['diabetes']
    return X, y

# Test
if __name__ == "__main__":
    X, y = load_data("data/hospital1.csv")
    print(X.head())
    print(y.head())