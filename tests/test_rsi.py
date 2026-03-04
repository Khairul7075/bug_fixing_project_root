import pandas as pd
from scripts.utils import calculate_rsi

def test_rsi_calculation():
    """Test RSI calculation with dummy closing prices."""
    data = pd.DataFrame({
        "Close": [100, 102, 101, 105, 107, 106, 108, 110, 109, 111, 113, 115, 114, 116, 118]
    })
    rsi_value = calculate_rsi(data)
    assert 0 <= rsi_value <= 100, "RSI should be between 0 and 100"
    print("RSI test passed:", rsi_value)

if __name__ == "__main__":
    test_rsi_calculation()
