# dash_app/layout.py

import dash_bootstrap_components as dbc
from dash import html, dcc

def create_layout():
    # Color scheme
    COLORS = {
        "primary": "#ed1d26",      # Red
        "secondary": "#909ca1",    # Gray-blue
        "background": "#d8d8d8",   # Light gray
        "text": "#221f20",         # Dark gray/black
    }
    return dbc.Container([
        dbc.Row([
            dbc.Col([
                html.H1("RK Mechanical Course Catalogue Search", style={
                    "color": COLORS["primary"],
                    "padding": "0.5em",
                    "borderRadius": "0.5em",
                    "textAlign": "center",
                    "fontWeight": "bold",
                }),
                dbc.Row([
                    dbc.Col(dbc.Input(id="filter-section", type="text", placeholder="Section", debounce=True, style={
                        "color": COLORS["text"], "background": "#fff", "borderColor": COLORS["secondary"], "borderRadius": "0.3em"
                    }), width=2),
                    dbc.Col(dbc.Input(id="filter-course-num", type="text", placeholder="Course #", debounce=True, style={
                        "color": COLORS["text"], "background": "#fff", "borderColor": COLORS["secondary"], "borderRadius": "0.3em"
                    }), width=2),
                    dbc.Col(dbc.Input(id="filter-course-name", type="text", placeholder="Course Name or Description", debounce=True, style={
                        "color": COLORS["text"], "background": "#fff", "borderColor": COLORS["secondary"], "borderRadius": "0.3em"
                    }), width=4),
                    dbc.Col(dbc.Input(id="filter-instructor", type="text", placeholder="Instructor(s)", debounce=True, style={
                        "color": COLORS["text"], "background": "#fff", "borderColor": COLORS["secondary"], "borderRadius": "0.3em"
                    }), width=3),
                ], className="mb-2 g-2", style={"marginRight": 0, "marginLeft": 0}),
                html.Div(id="course-search-results"),
            ]),
        ]),
    ], style={"minHeight": "100vh", "paddingTop": "2em"})