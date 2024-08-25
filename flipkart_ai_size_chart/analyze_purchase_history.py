import pandas as pd

def analyze_purchase_history(purchase_file):
    # Load purchase history data
    df = pd.read_csv(purchase_file)
    
    # Example analysis: Average quantity purchased per product
    avg_quantity_per_product = df.groupby('product_id')['quantity'].mean()
    print("Average quantity purchased per product:")
    print(avg_quantity_per_product)
    
    # Example analysis: Total spending per user
    df['total_spent'] = df['quantity'] * df['price']
    total_spent_per_user = df.groupby('user_id')['total_spent'].sum()
    print("Total spending per user:")
    print(total_spent_per_user)

if __name__ == "__main__":
    analyze_purchase_history('dataset/purchase_history.csv')
