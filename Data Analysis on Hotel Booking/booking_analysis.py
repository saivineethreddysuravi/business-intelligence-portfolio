import pandas as pd
import numpy as np
import os

def generate_dummy_data(rows=100):
    """Generates dummy hotel booking data for testing/demo purposes."""
    np.random.seed(42)
    data = {
        'is_canceled': np.random.choice([0, 1], size=rows, p=[0.7, 0.3]),
        'lead_time': np.random.randint(0, 365, size=rows),
        'arrival_date_year': np.random.choice([2015, 2016, 2017], size=rows),
        'arrival_date_month': np.random.choice(['January', 'February', 'March', 'April', 'May', 'June'], size=rows),
        'adr': np.random.uniform(50, 200, size=rows),  # Average Daily Rate
        'customer_type': np.random.choice(['Transient', 'Contract', 'Group'], size=rows)
    }
    return pd.DataFrame(data)

def analyze_bookings(file_path='hotel_bookings.csv'):
    """
    Analyzes hotel booking data to derive insights on cancellations and revenue.
    """
    print("--- Hotel Booking Intelligence Module ---")
    
    if os.path.exists(file_path):
        print(f"Loading data from {file_path}...")
        df = pd.read_csv(file_path)
    else:
        print(f"Warning: {file_path} not found. Generating dummy data for demonstration.")
        df = generate_dummy_data()
        
    # 1. Cancellation Rate Analysis
    total_bookings = len(df)
    cancellation_rate = (df['is_canceled'].sum() / total_bookings) * 100
    print(f"\nTotal Bookings Processed: {total_bookings}")
    print(f"Overall Cancellation Rate: {cancellation_rate:.2f}%")
    
    # 2. Revenue Impact (ADR)
    avg_adr_canceled = df[df['is_canceled'] == 1]['adr'].mean()
    avg_adr_not_canceled = df[df['is_canceled'] == 0]['adr'].mean()
    
    print(f"\nAverage Daily Rate (ADR) Analysis:")
    print(f"  Confirmed Bookings: ${avg_adr_not_canceled:.2f}")
    print(f"  Canceled Bookings:  ${avg_adr_canceled:.2f}")
    
    # 3. Lead Time correlation
    # Simple binning of lead time
    df['lead_time_category'] = pd.cut(df['lead_time'], bins=[0, 7, 30, 90, 365, 999], labels=['Last Minute', 'Short Term', 'Medium Term', 'Long Term', 'Very Long Term'])
    cancel_by_lead_time = df.groupby('lead_time_category', observed=True)['is_canceled'].mean() * 100
    
    print("\nCancellation Rate by Lead Time Category:")
    print(cancel_by_lead_time.to_string(float_format="%.1f%%"))
    
    return df

if __name__ == "__main__":
    analyze_bookings()
