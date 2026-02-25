import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

class FinancialAnalyzer:
    """
    Enterprise-grade financial data analysis engine.
    Focuses on Loan Conversion Analysis and Customer Segmentation.
    """
    
    def __init__(self, filepath):
        self.filepath = filepath
        self.df = None
        
    def load_data(self):
        """Loads data from Excel source."""
        print(f"Loading data from {self.filepath}...")
        try:
            # Using sheet_name=1 as seen in the original notebook analysis
            self.df = pd.read_excel(self.filepath, sheet_name=1)
            print("Data loaded successfully.")
            print(f"Columns: {list(self.df.columns)}")
            return True
        except Exception as e:
            print(f"Error loading data: {e}")
            return False

    def calculate_conversion_metrics(self):
        """Calculates Personal Loan conversion rates."""
        if self.df is None:
            return

        print("\n--- Conversion Metrics ---")
        total_customers = len(self.df)
        converted_customers = self.df[self.df['Personal Loan'] == 1].shape[0]
        conversion_rate = (converted_customers / total_customers) * 100
        
        print(f"Total Base: {total_customers}")
        print(f"Converted (Loan Accepted): {converted_customers}")
        print(f"Conversion Rate: {conversion_rate:.2f}%")
        
        return conversion_rate

    def analyze_income_distribution(self, output_dir='output'):
        """Analyzes income distribution for converted vs non-converted."""
        if self.df is None:
            return

        print("\n--- Income Distribution Analysis ---")
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        plt.figure(figsize=(10, 6))
        sns.boxplot(x='Personal Loan', y='Income', data=self.df, palette='coolwarm')
        plt.title('Income Distribution by Loan Acceptance')
        plt.xlabel('Accepted Personal Loan (0=No, 1=Yes)')
        plt.ylabel('Annual Income ($000)')
        
        output_path = os.path.join(output_dir, 'income_distribution.png')
        plt.savefig(output_path)
        print(f"Saved income plot to {output_path}")

    def generate_summary_report(self):
        """Generates a text summary of high-value segments."""
        if self.df is None:
            return

        print("\n--- High Value Segment Identification ---")
        # Define High Value: Income > 100k
        high_value = self.df[self.df['Income'] > 100]
        hv_conversion = high_value[high_value['Personal Loan'] == 1].shape[0] / len(high_value) * 100
        
        print(f"High Income Segment (>100k) Conversion Rate: {hv_conversion:.2f}%")
        
        # Education impact
        # Assuming Education levels: 1: Undergrad, 2: Graduate, 3: Advanced/Professional
        for edu_level in sorted(self.df['Education'].unique()):
            segment = self.df[self.df['Education'] == edu_level]
            rate = segment[segment['Personal Loan'] == 1].shape[0] / len(segment) * 100
            print(f"Education Level {edu_level} Conversion Rate: {rate:.2f}%")

    def analyze_spending_power(self, output_dir='output'):
        """
        Analyzes the correlation between Credit Card spending and Loan uptake.
        Calculates approximate Credit Utilization/Spending Power ratio.
        """
        if self.df is None:
            return

        print("\n--- Spending Power Analysis ---")
        # CCAvg is Avg. spending on credit cards per month ($000)
        # Income is Annual Income ($000)
        # Spending Ratio = (CCAvg * 12) / Income
        
        # Avoid division by zero
        self.df['Annual_CC_Spend'] = self.df['CCAvg'] * 12
        self.df['Spending_to_Income_Ratio'] = self.df['Annual_CC_Spend'] / (self.df['Income'] + 0.01)
        
        avg_ratio_loan = self.df[self.df['Personal Loan'] == 1]['Spending_to_Income_Ratio'].mean()
        avg_ratio_no_loan = self.df[self.df['Personal Loan'] == 0]['Spending_to_Income_Ratio'].mean()
        
        print(f"Avg Spending/Income Ratio (Loan Takers): {avg_ratio_loan:.2%}")
        print(f"Avg Spending/Income Ratio (Non-Takers): {avg_ratio_no_loan:.2%}")
        
        # Visualization
        plt.figure(figsize=(10, 6))
        sns.kdeplot(data=self.df, x='Spending_to_Income_Ratio', hue='Personal Loan', fill=True, palette='crest')
        plt.title('Spending Power Density by Loan Status')
        plt.xlabel('Credit Card Spending / Annual Income Ratio')
        plt.xlim(0, 1) # Limit to reasonable range
        
        output_path = os.path.join(output_dir, 'spending_power_density.png')
        plt.savefig(output_path)
        print(f"Saved spending power plot to {output_path}")

if __name__ == "__main__":
    # Path relative to script execution
    FILE_PATH = "Bank_Personal_Loan_Modelling.xlsx" 
    
    engine = FinancialAnalyzer(FILE_PATH)
    if engine.load_data():
        engine.calculate_conversion_metrics()
        engine.analyze_income_distribution()
        engine.generate_summary_report()
        engine.analyze_spending_power()
