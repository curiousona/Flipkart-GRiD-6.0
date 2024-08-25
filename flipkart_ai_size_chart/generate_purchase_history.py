import pandas as pd
import numpy as np

def generate_purchase_history(file_path):
    # Simulate a purchase history dataset
    np.random.seed(0)
    user_ids = np.arange(1, 101)
    product_ids = np.random.randint(1, 21, size=100)
    purchase_dates = pd.date_range(start='2023-01-01', periods=100, freq='D')
    quantities = np.random.randint(1, 5, size=100)
    prices = np.random.uniform(10, 100, size=100)

    data = {
        'user_id': user_ids,
        'product_id': product_ids,
        'purchase_date': purchase_dates,
        'quantity': quantities,
        'price': prices
    }

    df = pd.DataFrame(data)
    df.to_csv(file_path, index=False)
    print(f"Purchase history dataset generated at {file_path}")

if __name__ == "__main__":
    file_path = 'dataset/purchase_history.csv'
    generate_purchase_history(file_path)
