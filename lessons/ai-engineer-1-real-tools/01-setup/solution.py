import numpy, pandas, torch, sklearn, fastapi


def versions():
    return {m.__name__: m.__version__ for m in (numpy, pandas, torch, sklearn, fastapi)}


print(versions())
