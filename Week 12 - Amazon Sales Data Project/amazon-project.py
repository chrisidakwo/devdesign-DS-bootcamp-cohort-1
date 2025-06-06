import pandas as pd

def str_to_float(value):
    """Converts the provided value to a float"""
    return float(str(value))

def print_introduction():
    print('\n')
    print('='*50)
    print('📊 AMAZON SALES DATA ANALYSIS')
    print('='*50)
    print('\n')

class AmazonSalesAnalyzer:
    """Analyze Amazon sales data and provide actionable business insights"""

    def __init__(self, path):
        """Initialize with CSV data"""
        try:
            self.df = pd.read_csv(path)
        except FileNotFoundError:
            print(f'File not found at: `{path}`')

        # Rename columns
        self.rename_columns()

        # Data preprocessing
        self.pre_process_data()

    def rename_columns(self):
        """Normalize column names by removing white space and enforcing lowercase"""

        self.df.rename(columns={
            'Order ID': 'order_id',
            'Date': 'date',
            'Product': 'product',
            'Category': 'category',
            'Price': 'price',
            'Quantity': 'qty',
            'Total Sales': 'total_sales',
            'Customer Name': 'customer',
            'Customer Location': 'location',
            'Payment Method': 'payment_method',
            'Status': 'status',
        }, inplace=True)

    def pre_process_data(self):
        """Clean and process the data for analysis"""
        self.df['date'] = pd.to_datetime(self.df['date'], format='%d-%m-%y')

        # Format "Price" and "Total Sales" values
        self.df['price'] = self.df['price'].apply(lambda x: float(str(x)))
        self.df['total_sales'] = self.df['price'].apply(str_to_float)

        # HINT: You can use the code below to strip whitespace from around texts in the text-based columns.
        # columns= ['Product', 'Category']
        # for column in columns:
        #     # self.df[column] = self.df[column].str.strip()
        #     self.df[column] = self.df[column].apply(lambda x: str(x).strip())

    def data_overview(self):
        """Comprehensive data exploration and overview"""

        (rows, columns) = self.df.shape

        minDate = self.df['date'].min()
        maxDate = self.df['date'].max()

        print(f'Total Records: {rows}')
        print(f'Date Range: {minDate.strftime('%Y-%m-%d')} to {maxDate.strftime('%Y-%m-%d')}')
        print(f'Unique Products: {self.df['product'].nunique()}')
        print(f'Unique Categories: {self.df['category'].nunique()}')
        print(f'Unique Locations: {self.df['location'].nunique()}')

        # Revenue Summary
        total_revenue = self.df['total_sales'].sum()
        avg_order_value = self.df['total_sales'].mean()

        print('\n💰 FINANCIAL SUMMARY')
        print(f'Total Revenue: ${total_revenue:,.1f}')
        print(f'Average Order Value: ${avg_order_value}')

        # Data Quality Score
        missing_data = self.df.isnull().sum()
        data_q_score = ((len(self.df) * len(self.df.columns) - missing_data.sum()) / (len(self.df) * len(self.df.columns))) * 100

        print(f'\n🏥 DATA HEALTH SCORE: {data_q_score:.1f}%')

        # Status distribution
        status_distribution = self.df['status'].value_counts()

        print('\nORDER STATUS DISTRIBUTION')
        for status, count in status_distribution.items():
            percentage = (count / len(self.df)) * 100
            print(f'   {status}: {count} ({percentage:.1f}%)')

        return {
            'total_records': rows,
            'total_revenue': total_revenue,
            'avg_order_value': avg_order_value,
            'health_score': data_q_score,
            'status_distribution': status_distribution.to_dict()
        }


if __name__ == '__main__':
    analyzer = AmazonSalesAnalyzer('../data/amazon_sales_data_2025.csv')

    print_introduction()

    result = analyzer.data_overview()

    print('\n', result)
