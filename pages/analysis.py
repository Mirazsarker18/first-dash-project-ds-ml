import dash
from dash import html, dcc, callback, Output, Input
import pandas as pd
import plotly.express as px

# Analysis page
dash.register_page(__name__, path="/analysis", name="Analysis")

# data set
df = pd.read_csv("data/sales_data.csv")

# Region data and lop
region_options = [{"label": "All Region", "value": "All"}] + [{"label": r, "value": r} for r in sorted(df["Region"].unique())]

# Year min and max
year_min = int(df["Year"].min())
year_max = int(df["Year"].max())

# layout create
layout = html.Div(
    className = "analysis_page",
    children = [
        html.H2("Sales Analysis"),
        html.Div(
            className = "controls-row",
            children = [
                html.Div(
                    className = "control-box",
                    children = [
                        html.Label("Sales Region:"),
                        dcc.Dropdown(
                            id = "region-dropdown",
                            options = region_options,
                            value = "All",
                            clearable = False,
                        ),
                    ],
                ),
                html.Div(
                    className = "control-box",
                    children = [
                        html.Label("Select Year Range:"),
                        dcc.RangeSlider(
                            id = "year-slider",
                            min = year_min,
                            max = year_max,
                            value = [year_min, year_max],
                            marks= {y:str(y) for y in range(year_min, year_max + 1)},
                        ),
                    ],
                ),
            ],
        ),
        # Graph create
        dcc.Graph(id = "sales-line-chart"),
        dcc.Graph(id = "sales-bar-chart"),

    ],
)




# Callback 
@callback(
    Output("sales-line-chart", "figure"),
    Output("category-bar-chart", "figure"),
    Input("region-dropdown", "value"),
    Input("year-slider", "value"),
)


# chart update function
def update_charts(selected_region, selected_years):
    start_year, end_year = selected_years
    filtered = df[(df["year"] >= start_year) & (df["year"] <= end_year)]

    if selected_region != "All":
        filtered = filtered[filtered["Region"] == selected_region]

    monthly = filtered.groupby("Date", as_index = False)["Sales_BDT"].sum()
    line_fig = px.line(
        monthly,
        x = "Date",
        y = "Sales_BDT",
        title = f"Sales Over Time - {selected_region}",
        markers = "True",
    )
    line_fig.update_layout(template = "plotly_white")

    by_category = filtered.groupby("Category", as_index = False)["Sales_BDT"].sum()
    bar_fig = px.bar(
        by_category,
        x = "Category",
        y = "Sales_BDT",
        title = f"Sales by Category - {selected_region}",
        color ="Category",
    )
    bar_fig.update_layout(templates = "plotly_white", showlegend = False)
    return line_fig, bar_fig








