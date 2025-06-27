import json


def save(theta0: float | int, theta1: float | int, alpha: float | int) -> None:
    """
    Save coefficient in a JSON file.
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
    Load coefficient from a JSON file.
    """

    try:
        with open("../json/model.json", "r") as f:
            data = json.load(f)

        theta0 = data["theta0"]
        theta1 = data["theta1"]
        alpha = data["alpha"]

        return (float(theta0), float(theta1), float(alpha))
    except FileNotFoundError:
        return (0.0, 0.0, 0.0)
