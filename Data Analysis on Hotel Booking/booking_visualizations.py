import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
try:
    from booking_analysis import analyze_bookings
except ImportError:
    from .booking_analysis import analyze_bookings

def plot_booking_insights(df):
    sns.set_theme(style="whitegrid")
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6))
    sns.barplot(data=df, x="customer_type", y="is_canceled", ax=ax1, palette="viridis", errorbar=None)
    ax1.set_title("Cancellation Rate by Customer Type")
    ax1.set_ylabel("Probability of Cancellation")
    sns.boxplot(data=df, x="is_canceled", y="adr", ax=ax2, palette="Set2")
    ax2.set_title("ADR Distribution: Confirmed vs Canceled")
    ax2.set_xticklabels(["Confirmed", "Canceled"])
    plt.tight_layout()
    output_path = "booking_trends_dashboard.png"
    plt.savefig(output_path)
    print(f"Visualization saved to {output_path}")

if __name__ == "__main__":
    df = analyze_bookings()
    plot_booking_insights(df)
