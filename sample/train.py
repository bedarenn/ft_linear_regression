import pandas as pd
import matplotlib.pyplot as plt
from model_io import save, load


ALPHA = 0.5


def load_json() -> tuple[float | int, float | int, float | int]:
    """
    Load model parameters (theta0, theta1, alpha) from file.
    Use default alpha if not saved.
    """

    theta0, theta1, alpha = load()

    if (alpha == 0.0):
        alpha = ALPHA

    return (theta0, theta1, alpha)


def update(df: pd.DataFrame,
           theta0: float | int, theta1: float | int, alpha: float | int
           ) -> tuple[float, float]:
    """
    Perform one gradient descent update for the model parameters
    based on the input DataFrame.
    """

    assert isinstance(theta0, float | int), \
        f"update :WrongType: theta0_b = {type(theta0)}"
    assert isinstance(theta1, float | int), \
        f"update :WrongType: theta1_b = {type(theta1)}"
    assert isinstance(df, pd.DataFrame), \
        f"update :WrongType: tab = {type(df)}"
    assert isinstance(alpha, float | int), \
        f"update :WrongType: alpha = {type(alpha)}"

    grad0 = 0
    grad1 = 0
    for x, y in zip(df['km_norm'], df['price']):
        y_pred = theta0 + theta1 * x
        error = y_pred - y
        grad0 += error
        grad1 += error * x

    scale = alpha * 1 / len(df)
    theta0 = theta0 - scale * grad0
    theta1 = theta1 - scale * grad1

    return (theta0, theta1)


def train_loop(df: pd.DataFrame) -> tuple[float | int, float | int]:
    """
    Train the model until convergence using gradient descent.
    Normalize input data and update parameters iteratively.
    Save the final parameters to file.
    """

    theta0, theta1, alpha = load_json()

    km_min = df['km'].min()
    km_max = df['km'].max()
    df['km_norm'] = (df['km'] - km_min) / (km_max - km_min)

    theta1_norm = theta1 * (km_max - km_min)
    theta0_norm = theta0 + theta1 * km_min

    i = 0

    theta0_old, theta1_old = theta0_norm, theta1_norm
    theta0_norm, theta1_norm = update(df, theta0_old, theta1_old, alpha)
    while ((theta0_norm, theta1_norm) != (theta0_old, theta1_old)):
        i += 1
        theta0_old, theta1_old = theta0_norm, theta1_norm
        theta0_norm, theta1_norm = update(df, theta0_old, theta1_old, alpha)

    print(f"Model train {i} times with a total of {len(df) * i} values.")

    theta1 = theta1_norm / (km_max - km_min)
    theta0 = theta0_norm - theta1 * km_min
    save(theta0, theta1, alpha)

    return (theta0, theta1)


def plot(df: pd.DataFrame, theta0: float | int, theta1: float | int) -> None:
    """
    Plot the data points and the resulting affine regression line.
    """

    print(theta0, theta1)

    x_val = [0, -theta0 / theta1]
    y_val = [theta0, 0]

    plt.figure(figsize=(8, 4.5))
    plt.grid(True)

    plt.scatter(df['km'], df['price'], color='blue', marker='o')
    plt.plot(x_val, y_val,
             color='red', linestyle='-', label='Affine approximation')

    plt.title("Car sales")
    plt.xlabel("Mileage (km)")
    plt.ylabel("Price")

    plt.show()
    plt.show()


def main():
    df = pd.read_csv("../data/data.csv")
    theta0, theta1 = train_loop(df)
    plot(df, theta0, theta1)


if __name__ == "__main__":
    main()
