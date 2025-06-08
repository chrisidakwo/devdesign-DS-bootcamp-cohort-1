import pandas as pd
import matplotlib.pyplot as plt
from pprint import pprint

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

    df = None

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

    def plot_status_distribution(self, status_distribution: dict, save_path):
        """Create a pie chart for order status distribution"""
        fig, ax = plt.subplots(figsize=(10, 8))

        # Create pie chart
        wedges, texts, autotexts = ax.pie(
            list(status_distribution.values()),
            labels=list(status_distribution.keys()),
            autopct='%1.1f%%',
            startangle=90,
            explode=[0.05 if status == 'Cancelled' else 0 for status in status_distribution.keys()],
        )

        ax.set_title('Order Status Distribution', fontsize=16, fontweight='bold', pad=20)

        plt.tight_layout()

        # Save plot image
        plt.savefig(save_path, dpi=300, bbox_inches='tight')

        # Show the plot
        plt.show()

    def product_performance_analysis(self):
        """" """
        product_performance = self.df.groupby('product').agg({
            'total_sales': ['sum', 'count'],
            'qty': 'sum',
        })

        product_performance.columns = ['total_revenue', 'order_count', 'units_sold']
        product_performance = product_performance.sort_values('total_revenue', ascending=False)

        print('\n')
        print(product_performance)
        print('\n')

        # Calculate revenue percentage
        total_revenue = self.df['total_sales'].sum()
        product_performance['revenue_percentage'] = ((product_performance['total_revenue'] / total_revenue) * 100).round(2)

        # Top and bottom performers
        top_3_products = product_performance.head(3)
        bottom_3_products = product_performance.tail(3)

        print('\nHALL OF FAME - TOP 3 PRODUCTS:')
        for i, (product, data) in enumerate(top_3_products.iterrows(), 1):
            print(f'{product}')
            print(f'Revenue: ${data['total_revenue']:,} ({data['revenue_percentage']:.1f}% of total)')
            print(f'Units Sold: {data['units_sold']:.0f} | Orders: {data['order_count']:.0f}')
            print('')

        print('\nHALL OF SHAME - BOTTOM 3 PRODUCTS:')
        for i, (product, data) in enumerate(bottom_3_products.iterrows(), 1):
            print(f'{product}')
            print(f'Revenue: ${data['total_revenue']:,} ({data['revenue_percentage']:.1f}% of total)')
            print(f'Units Sold: {data['units_sold']:.0f} | Orders: {data['order_count']:.0f}')
            print('')


        # Performance gap analysis
        top_revenue = top_3_products['total_revenue'].sum()
        bottom_revenue = bottom_3_products['total_revenue'].sum()
        performance_gap = top_revenue / bottom_revenue if bottom_revenue > 0 else float('inf')

        print('\nPERFORMANCE GAP ANALYSIS:')
        print(f'Top 3 Revenue: ${top_revenue:,} ({((top_revenue / total_revenue) * 100):.1f}% of total)')
        print(f'Bottom 3 Revenue: ${bottom_revenue:,} ({((bottom_revenue / total_revenue) * 100):.1f}% of total)')
        print(f'Performance Multiplier: {performance_gap:.2f}x')


    def payment_method_analysis(self):
        """
        - Discover if certain payment methods correlate with higher-value purchases (correlation analysis between total_sales and payment_method)
        """
        
        # Payment method analysis
        payment_analysis = self.df.groupby('payment_method').agg({
            'total_sales': ['sum', 'count', 'mean'],
            'qty': ['sum'],
        }).round(2)

        payment_analysis.columns = ['total_revenue', 'order_count', 'avg_order_value', 'units_sold']
        payment_analysis = payment_analysis.sort_values('total_revenue', ascending=False)

        total_revenue = self.df['total_sales'].sum()
        payment_analysis['revenue_percentage'] = ((payment_analysis['total_revenue'] / total_revenue) * 100).round(2)

        print('\nPAYMENT METHOD PERFORMANCE:')
        for method, data in payment_analysis.iterrows():
            print(f'{method}')
            print(f'Revenue: ${data['total_revenue']:,} ({data['revenue_percentage']:.1f}% of total)')
            print(f'Orders: {data['order_count']:.0f}')
            print(f'Average Order Value: ${data['avg_order_value']:.2f}')
            print(f'Units Sold: {data['units_sold']:.0f}')
            print('')

        # Geographic payment preference
        location_payment = pd.crosstab(self.df['location'], self.df['payment_method'], normalize='index') * 100

        print(f'\nGEOGRAPHIC PAYMENT PREFERENCE')
        top_locations = self.df['location'].value_counts().head().index
        for location in top_locations:
            if location in location_payment.index:
                top_payment_method = location_payment.loc[location].idxmax()
                top_pct = location_payment.loc[location].max()

                print(f'    {location} prefers {top_payment_method} ({top_pct:.1f}%)')
        
        return {
            'payment_performance': payment_analysis.to_dict('index'),
            'grographic_preferences': location_payment.to_dict('index'),
        }

    def geographical_analysis(self):
        """
            - Identify top 5 cities/states driving the most revenue
            - Calculate revenue per capita for major markets
            - Discover untapped markets with growth potential
            - **Deliverable:** Market expansion strategy with priority rankings
        """

        location_performance = self.df.groupby('location').agg({
            'total_sales': ['sum', 'count', 'mean'],
            'qty': ['sum'],
        })

        print(location_performance)
        print('\n')

        location_performance.columns = ['total_revenue', 'order_count', 'avg_order_value', 'units_sold']
        location_performance = location_performance.sort_values('total_revenue', ascending=False)

        total_revenue = self.df['total_sales'].sum()
        location_performance['revenue_percentage'] = ((location_performance['total_revenue'] / total_revenue) * 100).round(2)

        # Top 5 locations
        top_5_markets = location_performance.head()

        print('\nTOP 5 REVENUE GENERATING MARKETS:')
        for location, data in top_5_markets.iterrows():
            print(f'{location}')
            print(f'Revenue: ${data['total_revenue']:,} ({data['revenue_percentage']:.1f}% of total)')
            print(f'Orders: {data['order_count']:.0f}')
            print(f'Average Order Value: ${data['avg_order_value']:.2f}')
            print(f'Units Sold: {data['units_sold']:.0f}')
            print('')
        
        # Untapped market = [low revenue, high AOV (averge order value)]
        # Low revenue = location total revenue less than the total revenue median
        # High AOV = location AOV > median AOV 
        untapped_market =  location_performance[
            (location_performance['total_revenue'] < location_performance['total_revenue'].median()) &
            (location_performance['avg_order_value'] > location_performance['avg_order_value'].median()) 
        ]

        print(untapped_market)


    def run_analysis(self):
        print_introduction()

        print(analyzer.df.columns.tolist())
        print('\n')
        print(analyzer.df.head())
        print('\n')

        result = analyzer.data_overview()

        # analyzer.plot_status_distribution(result['status_distribution'], 'status_distribution.png')

        # analyzer.product_performance_analysis()

        # analyzer.payment_method_analysis()

        analyzer.geographical_analysis()


if __name__ == '__main__':
    analyzer = AmazonSalesAnalyzer('../data/amazon_sales_data_2025.csv')
    analyzer.run_analysis()
