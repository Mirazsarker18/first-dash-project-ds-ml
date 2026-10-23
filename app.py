import dash
from dash import Dash, html, dcc

app = Dash(__name__, use_pages = True, suppress_callback_exceptions = True)
server = app.server

app.layout = html.Div(
    className = "app-container",
    children = [
        html.Header(
            className = "navbar",
            children = [
                html.H1("Mini Sales Dashboard", className = "brand"),
                html.Nav(
                    className = "nave-links",
                    children = [
                        dcc.Link(
                            f"{page["name"]}",
                            href=page["path"],
                            className = "nav-link",
                        )
                        for page in dash.page_registry.values()
                    ],
                ),
            ],
        ),
        html.Main(dash.page_container, className = "page-container"),
        html.Footer(
            "Prepared for lab - Dash Framework",
            className = "footer"
        )

    ],

)

if __name__ == "__main__":
    app.run(debug = True, port = 8050)



