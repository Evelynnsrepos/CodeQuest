from sklearn.datasets import load_breast_cancer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import cross_val_score, train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler


def split(X, y):
    return X, X, y, y


def make_model():
    return None


def evaluate(X, y):
    return (0.0, 0.0)


X, y = load_breast_cancer(return_X_y=True)
print(evaluate(X, y))
