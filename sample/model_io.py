import json


def save(theta0: float, theta1: float) -> None:
    """
    Save coefficient in a JSON file.
    """

    assert isinstance(theta0, float), \
        f"save :WrongType: theta0 = {type(theta0)}"
    assert isinstance(theta1, float), \
        f"save :WrongType: theta1 = {type(theta1)}"

    data = {
        "theta0": theta0,
        "theta1": theta1
    }

    with open("../json/model.json", "w") as f:
        json.dump(data, f)


def load() -> tuple[float, float]:
    """
    Load coefficient from a JSON file.
    """

    try:
        with open("../json/model.json", "r") as f:
            data = json.load(f)

        theta0 = data["theta0"]
        theta1 = data["theta1"]

        return (float(theta0), float(theta1))
    except FileNotFoundError:
        return (0.0, 0.0)
