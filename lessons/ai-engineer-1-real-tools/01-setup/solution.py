import numpy, pandas, torch, sklearn, fastapi


def versions():
    out = {}
    out["numpy"] = numpy.__version__
    out["pandas"] = pandas.__version__
    out["torch"] = torch.__version__
    out["sklearn"] = sklearn.__version__
    out["fastapi"] = fastapi.__version__
    return out


print(versions())
