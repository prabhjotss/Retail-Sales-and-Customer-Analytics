import pandas as pd
import plotly.graph_objects as go
import plotly.io as pio
from plotly.subplots import make_subplots
from sqlalchemy import create_engine

# ----- Database -----
engine = create_engine("sqlite:///retail.db")
sales = pd.read_sql("SELECT * FROM sales", engine)
customers = pd.read_sql("SELECT * FROM customers", engine)

# ----- Fix IDs -----
sales['customer_id'] = sales['customer_id'].str.replace('C','').astype(int)
customers['customer_id'] = customers['customer_id'].astype(int)
df = sales.merge(customers, on='customer_id')

# ----- Prepare Data -----
df['revenue'] = df['quantity'] * df['price']
df['order_date'] = pd.to_datetime(df['order_date'])
df['month'] = df['order_date'].dt.to_period('M').astype(str)
df['weekday'] = df['order_date'].dt.day_name()

# ----- Aggregations -----
monthly_rev = df.groupby('month')['revenue'].sum().reset_index()
top_cust = df.groupby('customer_name')['revenue'].sum().sort_values(ascending=False).head(10).reset_index()
city_rev = df.groupby('city')['revenue'].sum().reset_index()
prod_rev = df.groupby('product')['revenue'].sum().reset_index().sort_values(by='revenue', ascending=False)
weekday_rev = df.groupby('weekday')['revenue'].sum().reindex([
    "Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"
]).reset_index()
avg_price = df.groupby('product')['price'].mean().reset_index()  # 6th chart

# ----- Create 2-column, 3-row subplot figure -----
fig = make_subplots(
    rows=3, cols=2,
    subplot_titles=("Monthly Revenue Trend", "Top 10 Customers",
                    "Revenue by City", "Product Revenue",
                    "Revenue by Weekday", "Average Product Price"),
    specs=[[{"type":"xy"}, {"type":"xy"}],
           [{"type":"domain"}, {"type":"xy"}],
           [{"type":"xy"}, {"type":"xy"}]]
)

# 1️⃣ Monthly Revenue
fig.add_trace(go.Scatter(x=monthly_rev['month'], y=monthly_rev['revenue'],
                         mode='lines+markers', name='Monthly Revenue',
                         line=dict(color='royalblue', width=3),
                         marker=dict(size=8), showlegend=True), row=1, col=1)

# 2️⃣ Top 10 Customers
fig.add_trace(go.Bar(x=top_cust['revenue'], y=top_cust['customer_name'],
                     orientation='h', name='Top Customers', marker_color='teal', showlegend=True), row=1, col=2)

# 3️⃣ Revenue by City (Pie)
fig.add_trace(go.Pie(labels=city_rev['city'], values=city_rev['revenue'],
                     name='City Revenue', showlegend=True), row=2, col=1)

# 4️⃣ Product Revenue
fig.add_trace(go.Bar(x=prod_rev['product'], y=prod_rev['revenue'],
                     name='Product Revenue', marker_color='orange', showlegend=True), row=2, col=2)
fig.add_trace(go.Scatter(x=prod_rev['product'], y=prod_rev['revenue'], mode='lines+markers',
                         name='Trend', line=dict(color='darkgreen', width=2), showlegend=True), row=2, col=2)

# 5️⃣ Weekly Revenue
fig.add_trace(go.Bar(x=weekday_rev['weekday'], y=weekday_rev['revenue'],
                     name='Weekly Revenue', marker_color='purple', showlegend=True), row=3, col=1)

# 6️⃣ Average Product Price
fig.add_trace(go.Bar(x=avg_price['product'], y=avg_price['price'],
                     name='Avg Price', marker_color='pink', showlegend=True), row=3, col=2)

# ----- Layout -----
fig.update_layout(
    height=2000,
    width=1200,
    title_text="Retail Analytics Dashboard - 6 Charts",
    template='plotly_white',
    legend=dict(font=dict(size=12), bordercolor="LightGray", borderwidth=1)
)

# ----- Save HTML -----
pio.write_html(fig, file='Retail_Dashboard_6Charts.html', auto_open=True)
