# sample/core.py

import pandas as pd
from .train import train_loop, plot
from .predict import predict, load_json as load_model


def train_from_csv(path: str) -> tuple[float, float]:
    """
    Load dataset from CSV and train the model.
    """
    df = pd.read_csv(path)
    return train_loop(df)


def plot_from_csv(path: str, theta0: float, theta1: float) -> None:
    """
    Load dataset from CSV and plot the data with a fitted model line.
    """
    df = pd.read_csv(path)
    plot(df, theta0, theta1)


def predict_mileage(mileage: float) -> float:
    """
    Load trained model and predict price for given mileage.
    """
    theta0, theta1 = load_model()
    return predict(mileage, theta0, theta1)
