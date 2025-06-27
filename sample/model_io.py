import json
import os


def save(theta0: float | int, theta1: float | int, alpha: float | int) -> None:
    """
    Save the model parameters (theta0, theta1, alpha) to a JSON file.
    """

    assert isinstance(theta0, float | int), \
        f"save :WrongType: theta0 = {type(theta0)}"
    assert isinstance(theta1, float | int), \
        f"save :WrongType: theta1 = {type(theta1)}"
    assert isinstance(alpha, float | int), \
        f"save :WrongType: alpha = {type(alpha)}"

    data = {
        "theta0": theta0,
        "theta1": theta1,
        "alpha": alpha
    }

    with open("../json/model.json", "w") as f:
        json.dump(data, f)


def load() -> tuple[float | int, float | int, float | int]:
    """
    Load the model parameters (theta0, theta1, alpha) from a JSON file.
    Return default values if the file does not exist.
    """

    path = "../json/model.json"
    os.makedirs(os.path.dirname(path), exist_ok=True)
    try:
        with open("../json/model.json", "r") as f:
            data = json.load(f)

        theta0 = data["theta0"]
        theta1 = data["theta1"]
        alpha = data["alpha"]

        return (float(theta0), float(theta1), float(alpha))
    except FileNotFoundError:
        return (0.0, 0.0, 0.0)
