import pandas as pd
import numpy as np


chat_id = 319607269 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array) -> float:
    n = np.arange(0, 1, 1/88)
    r = np.multiply(x, n).sum()
    return r / n.sum() # Ваш ответ