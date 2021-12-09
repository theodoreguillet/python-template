from app.config import ENVIRONEMENT
from app.math import increment


def hello() -> None:
    print(f"Environment: {ENVIRONEMENT}")
    print("Hello World !")
    print(f"increment(2) = {increment(2)}")
