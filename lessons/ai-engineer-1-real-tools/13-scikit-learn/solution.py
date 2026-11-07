from sklearn.datasets import load_breast_cancer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import cross_val_score, train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler


def split(X, y):
    return train_test_split(X, y, test_size=0.2, random_state=0, stratify=y)


def make_model():
    return make_pipeline(StandardScaler(), LogisticRegression(max_iter=1000))


def evaluate(X, y):
    X_train, X_test, y_train, y_test = split(X, y)
    model = make_model()
    model.fit(X_train, y_train)
    test_accuracy = model.score(X_test, y_test)
    cv = cross_val_score(make_model(), X_train, y_train, cv=5)
    return (test_accuracy, cv.mean())


X, y = load_breast_cancer(return_X_y=True)
print(evaluate(X, y))
