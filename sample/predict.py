from model_io import load
import sys


def load_json() -> tuple[float | int, float | int]:
    """
    Load theta0 and theta1 from the model.
    Raise an error if the values are invalid.
    """

    theta0, theta1, _ = load()

    assert theta1 != 0.0 and theta1 != 0.0, \
        "load_json :LoadingError: theta value null"

    return (theta0, theta1)


def predict(nb: float | int,
            theta0: float | int, theta1: float | int
            ) -> float | int:
    """
    Predict the output using the linear model: f(x) = theta0 + theta1 * x
    """

    return (theta0 + theta1 * nb)


def main():
    theta0, theta1 = load_json()
    for strParam in sys.argv[1:]:
        nb = float(strParam)
        print(f"{nb:,.2f}km = {predict(nb, theta0, theta1):.2f}")


if __name__ == "__main__":
    main()
