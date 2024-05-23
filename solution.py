import numpy as np
import scipy.stats as sps

chat_id = 334982039 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array, y: np.array) -> bool:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    result = sps.anderson_ksamp([x, y])

    # Check if null hypothesis is rejected at alpha=0.02
    return result.significance_level < 0.02
