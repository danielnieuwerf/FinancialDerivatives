from enum import Enum
import math
from scipy.stats import norm

class OptionType(Enum):
    CALL = 1
    PUT = 2

# The Black-Scholes formula computes the fair price of a call or put option based on several parameters:
# S: the spot price of the underlying asset
# K: the strike price of the option
# T: the time to expiration in years
# r: the risk-free interest rate
# sigma: the volatility of the underlying asset
# optionType: the type of the option, either call or put.
def black_scholes(S: float, K: float, T: float, r: float, sigma: float, optionType: OptionType) -> float:
    d1 = (math.log(S / K) + (r + 0.5 * sigma ** 2) * T) / (sigma * math.sqrt(T))
    d2 = (math.log(S / K) + (r - 0.5 * sigma ** 2) * T) / (sigma * math.sqrt(T))
    
    if optionType == OptionType.CALL:
        return S * norm.cdf(d1) - K * math.exp(-r * T) * norm.cdf(d2)
    elif optionType == OptionType.PUT:
        return K * math.exp(-r * T) * norm.cdf(-d2) - S * norm.cdf(-d1)
    else:
        raise TypeError("Only call and put options are allowed.")

S = 30
K = 40
T = 240/365
r = 0.05
sigma = 3.0

print(f"Call price: ${black_scholes(S, K, T, r, sigma, OptionType.CALL):.2f}")
print(f"Put price: ${black_scholes(S, K, T, r, sigma, OptionType.PUT):.2f}")