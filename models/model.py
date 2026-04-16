from sklearn.linear_model import LogisticRegression

def create_model():
    model = LogisticRegression()
    return model

def train_model(model, X, y):
    model.fit(X, y)
    return model

def get_weights(model):
    return model.coef_, model.intercept_