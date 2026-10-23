import dash
from dash import html
import pandas as pd

dash.register_page(__name__, path="/", name="Home ")

df = pd.read_csv("data/sales_data.csv")

total_sales = df["Sales_BDT"].sum()
total_profit = df["Profit_BDT"].sum()
total_units = df["Units_Sold"].sum()
regions = df["Region"].nunique()

def stat_card(title, value, icon):
    return html.Div(
        className = "stat-card",
        children = [
            html.Div(icon, className = "stat-icon"),
            html.H3(value, className = "stat-value"),
            html.P(title, className = "state-title"),
        ],
    )

layout = html.Div(
    className = "home-page",
    children = [
        html.H2("Welcome"),
        html.P("This is a mini sales dashboard that provides insights into sales performance."),
        html.Div(
            className = "stats-grid",
            children = [
                stat_card("Total Sales (BDT)", f"{total_sales:,.0f}", "💰"),
                stat_card("Total Profit (BDT)", f"{total_profit:,.0f}", "📈"),
                stat_card("Total Units Sold", f"{total_units:,.0f}", "📦"),
                stat_card("Regions Covered", f"{regions}", "🌍"),

            ],
        ),
    ],
    
)

