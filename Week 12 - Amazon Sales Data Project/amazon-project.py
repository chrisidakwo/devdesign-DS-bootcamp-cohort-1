import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

desired_width=580

pd.set_option('display.width', desired_width)
np.set_printoptions(linewidth=desired_width)
pd.set_option('display.max_columns', 14)

def str_to_float(value):
    """Converts the provided value to a float"""
    return float(str(value))


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

    def plot_status_distribution(self, status_distribution, save_path):
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

        return {
            'product_performance': product_performance
        }

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
            'geographic_preferences': location_payment.to_dict('index'),
        }

    def geographical_analysis(self):
        """
            - Calculate revenue per capita for major markets
            - **Deliverable:** Market expansion strategy with priority rankings
        """

        location_performance = self.df.groupby('location').agg({
            'total_sales': ['sum', 'count', 'mean'],
            'qty': ['sum'],
        })

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
        
        # Untapped market = [low revenue, high AOV (average order value)]
        # Low revenue = location total revenue less than the total revenue median
        # High AOV = location AOV > median AOV 
        untapped_market =  location_performance[
            (location_performance['total_revenue'] < location_performance['total_revenue'].median()) &
            (location_performance['avg_order_value'] > location_performance['avg_order_value'].median()) 
        ]

        print('\nUNTAPPED MARKETS:')
        for location, data in untapped_market.iterrows():
            print(f'{location}: AOV ${data['avg_order_value']:.2f}, Revenue: ${data["total_revenue"]:,.2f}')

        return {
            'top_markets': top_5_markets.to_dict('index'),
            'market_concentration': location_performance.head(1)['revenue_percentage'].iloc[0],
            'untapped_markets': untapped_market.to_dict('index')
        }

    def temporal_analysis(self):
        """"""

        # Extract temporal features
        self.df['year'] = self.df['date'].dt.year
        self.df['month'] = self.df['date'].dt.month
        self.df['week_day'] = self.df['date'].dt.day_name()
        self.df['week_number'] = self.df['date'].dt.isocalendar().week

        weekly_sales = self.df.groupby('week_number')['total_sales'].sum().sort_values(ascending=False)
        golden_week = weekly_sales.index[0]
        golden_week_revenue = weekly_sales.iloc[0]

        print('\nGOLDEN WEEK:')
        print(f'Week {golden_week} is the golden week with a revenue of ${golden_week_revenue:,.2f}')

        # Day of week pattern
        dow_performance = self.df.groupby('week_day').agg({
            'total_sales': ['sum', 'count', 'mean'],
        }).round(2)

        dow_performance.columns = ['total_revenue', 'order_count', 'avg_order_value']

        days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        dow_performance = dow_performance.reindex(days)

        print('\nDAY-OF-WEEK PERFORMANCE:')
        for day, data in dow_performance.iterrows():
            print(f'    {day}: ${data["total_revenue"]:,.2f} in revenue | {data['order_count']:.0f} orders')

        best_day = dow_performance['total_revenue'].idxmax()
        worst_day = dow_performance['total_revenue'].idxmin()

        print('\nBEST TIMING INSIGHT')
        print(f'Best sales day: {best_day}')
        print(f'Worst sales day: {worst_day} (Perfect for marketing campaigns and promotions)')

        # Monthly trends
        monthly_sales = self.df.groupby('month')['total_sales'].sum()
        peak_month = monthly_sales.idxmax()
        slow_month = monthly_sales.idxmin()

        month_names = {
            1: 'January',
            2: 'February',
            3: 'March',
            4: 'April',
            5: 'May',
            6: 'June',
            7: 'July',
            8: 'August',
            9: 'September',
            10: 'October',
            11: 'November',
            12: 'December',
        }

        print('\nSEASONAL PATTERN')
        print(f'Peak Month: {month_names[peak_month]} (${monthly_sales[peak_month]:,.2f})')
        print(f'Slow Month: {month_names[slow_month]} (${monthly_sales[slow_month]:,.2f})')

        return {
            'golden_week': {
                'week': golden_week,
                'revenue': golden_week_revenue
            },
            'best_day': best_day,
            'worst_day': worst_day,
            'peak_month': peak_month,
            'slow_month': slow_month,
            'dow_performance': dow_performance.to_dict('index'),
        }

    def create_visualizations(self, save_path):
        """Create visualizations for presentation"""

        # Setup of the plot environment
        fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(25, 20))
        fig.suptitle('Amazon Sales Analytics', fontsize=16, fontweight='bold')

        # Top products by revenue
        products_revenue = self.df.groupby('product')['total_sales'].sum()
        axes[0, 0].barh(range(len(products_revenue)), products_revenue.values)
        axes[0, 0].set_yticks(range(len(products_revenue)))
        axes[0, 0].set_yticklabels(products_revenue.index)
        axes[0, 0].set_title('Top Products By Revenue')
        axes[0, 0].grid()

        # Payment method
        payment_performance = self.df.groupby('payment_method')['total_sales'].sum()
        axes[0, 1].pie(payment_performance.values, labels=payment_performance.index, autopct='%1.1f%%')
        axes[0, 1].set_title('Revenue by Payment Method')

        # Geographic Distribution
        location_revenue = self.df.groupby('location')['total_sales'].sum().nlargest(10)
        axes[1, 0].bar(range(len(location_revenue)), location_revenue.values)
        axes[1, 0].set_xticks(range(len(location_revenue)))
        axes[1, 0].set_xticklabels(location_revenue.index, rotation=45, ha='right')
        axes[1, 0].set_title('Total 10 Markets By Revenue')
        axes[1, 0].set_ylabel('Revenue ($)')

        # Category Performance
        category_performance = self.df.groupby('category')['total_sales'].sum()
        axes[1, 1].bar(category_performance.index, category_performance.values)
        axes[1, 1].set_ylabel('Revenue ($)')
        axes[1, 1].set_title('Revenue by Category')
        axes[1, 1].grid(axis='y', alpha=0.5, linestyle='--')
        axes[1, 1].tick_params(axis='x', rotation=45)

        plt.savefig(save_path, dpi=300, bbox_inches='tight')

        plt.tight_layout()
        plt.show()

    def run_analysis(self):
        """Run all analysis"""

        print('\n')
        print('='*80)
        print('📊 AMAZON SALES DATA ANALYSIS')
        print('='*80)
        print('\n')

        # Execute all analysis
        result = self.data_overview()
        self.plot_status_distribution(result['status_distribution'], '../data/amazon_order_status_distribution.png')
        self.product_performance_analysis()
        self.payment_method_analysis()
        self.geographical_analysis()
        self.temporal_analysis()
        self.create_visualizations('../data/amazon_sales_analysis_dashboard.png')

if __name__ == '__main__':
    analyzer = AmazonSalesAnalyzer('../data/amazon_sales_data_2025.csv')
    analyzer.run_analysis()
