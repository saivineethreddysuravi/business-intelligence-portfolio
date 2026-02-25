import os
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

def generate_advanced_dashboard():
    print('Generating advanced BI dashboard for Hotel Bookings...')
    sns.set_theme(style='darkgrid')
    
    # Simulating data for advanced insights
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
    direct_revenue = [45000, 48000, 52000, 61000, 75000, 89000]
    ota_revenue = [120000, 115000, 130000, 145000, 160000, 180000]
    
    fig, axes = plt.subplots(2, 2, figsize=(16, 12))
    
    # 1. Revenue Stream Analysis
    axes[0, 0].stackplot(months, direct_revenue, ota_revenue, labels=['Direct', 'OTA'], alpha=0.8, colors=['#3498db', '#e74c3c'])
    axes[0, 0].set_title('Revenue Streams: Direct vs OTA')
    axes[0, 0].legend(loc='upper left')
    
    # 2. Lead Time Distribution
    lead_times = np.random.gamma(2, 30, 1000)
    sns.kdeplot(lead_times, fill=True, color='#2ecc71', ax=axes[0, 1])
    axes[0, 1].set_title('Booking Lead Time Distribution (Days)')
    
    # 3. Market Segment ROI
    segments = ['Online TA', 'Offline TA', 'Direct', 'Corporate']
    roi = [15.2, 8.5, 22.1, 12.4]
    sns.barplot(x=segments, y=roi, palette='magma', ax=axes[1, 0])
    axes[1, 0].set_title('Marketing ROI by Segment (%)')
    
    # 4. Cancellation Correlation
    cancel_data = pd.DataFrame({
        'lead_time': np.random.normal(50, 20, 100),
        'cancel_prob': np.random.uniform(0.1, 0.9, 100)
    })
    sns.regplot(data=cancel_data, x='lead_time', y='cancel_prob', color='#9b59b6', ax=axes[1, 1])
    axes[1, 1].set_title('Correlation: Lead Time vs Cancellation Probability')
    
    plt.tight_layout()
    plt.savefig('docs/advanced_booking_dashboard.png')
    print('Advanced dashboard saved: docs/advanced_booking_dashboard.png')

if __name__ == '__main__':
    if not os.path.exists('docs'):
        os.makedirs('docs')
    generate_advanced_dashboard()
