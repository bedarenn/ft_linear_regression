import pandas as pd
import matplotlib.pyplot as plt
from model_io import save
from model_io import load


def update(theta0: float, theta1: float,
           alpha: float, df: pd.DataFrame
           ) -> tuple[float, float]:
    """
    Update the terms of an affine function.
    """

    assert isinstance(theta0, float), \
        f"update :WrongType: theta0_b = {type(theta0)}"
    assert isinstance(theta1, float), \
        f"update :WrongType: theta1_b = {type(theta1)}"
    assert isinstance(df, pd.DataFrame), \
        f"update :WrongType: tab = {type(df)}"
    assert isinstance(alpha, float), \
        f"update :WrongType: alpha = {type(alpha)}"

    grad0 = 0
    grad1 = 0
    for x, y in zip(df['km'], df['price']):
        y_pred = theta0 + theta1 * x
        error = y_pred - y
        grad0 += error
        grad1 += error * x

    scale = alpha * 1 / len(df)
    theta0 = theta0 - scale * grad0
    theta1 = theta1 - scale * grad1

    return (theta0, theta1)


def plot(df: pd.DataFrame, theta0: float, theta1: float) -> None:
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
    df_norm = pd.read_csv("../data/data.csv")

    km_min = df_norm['km'].min()
    km_max = df_norm['km'].max()
    df_norm['km'] = (df_norm['km'] - km_min) / (km_max - km_min)

    theta0, theta1 = 0, 0
    for i in range(0, 2000):
        theta0_old, theta1_old = load()
        theta0, theta1 = update(theta0_old, theta1_old, 0.5, df_norm)
        save(theta0, theta1)
        if (theta0_old == theta0 and theta1_old == theta1):
            print(f"Model train {i} times.")
            break

    df = pd.read_csv("../data/data.csv")
    theta1_r = theta1 / (km_max - km_min)
    theta0_r = theta0 - theta1_r * km_min
    plot(df, theta0_r, theta1_r)


if __name__ == "__main__":
    main()
