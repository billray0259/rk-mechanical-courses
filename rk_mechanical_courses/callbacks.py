from dash.dependencies import Input, Output, State, ALL
from dash import dcc, html, callback_context, no_update
import dash_bootstrap_components as dbc
import pandas as pd
import os

def register_callbacks(app):
    CATALOGUE_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), "course_catalogue.csv")

    @app.callback(
        Output("output", "children"),
        [Input("input", "value")],
    )
    def update_output(value):
        return value

    @app.callback(
        Output("course-search-results", "children"),
        [
            Input("filter-section", "value"),
            Input("filter-course-num", "value"),
            Input("filter-course-name", "value"),
            Input("filter-instructor", "value"),
        ],
    )
    def search_courses(section, course_num, course_name, instructor):
        try:
            df = pd.read_csv(CATALOGUE_PATH)
            df.columns = df.columns.str.strip()
            df = df.apply(lambda col: col.map(lambda x: x.strip() if isinstance(x, str) else x))
        except Exception as e:
            return dbc.Alert(f"Error loading course catalogue: {e}", color="danger")
        df = df.fillna("N/A")
        # Apply filters if provided
        if section and section.strip():
            df = df[df['Section'].astype(str).str.contains(section.strip(), case=False, na=False)]
        if course_num and course_num.strip():
            df = df[df['Course #'].astype(str).str.contains(course_num.strip(), case=False, na=False)]
        if course_name and course_name.strip():
            mask = df['Course Name'].astype(str).str.contains(course_name.strip(), case=False, na=False) | df['Description/Notes'].astype(str).str.contains(course_name.strip(), case=False, na=False)
            df = df[mask]
        if instructor and instructor.strip():
            df = df[df['Instructor(s)'].astype(str).str.contains(instructor.strip(), case=False, na=False)]
        if df.empty:
            return dbc.Alert("No courses found matching your filters.", color="warning")
        table_header = [
            html.Thead(html.Tr([
                html.Th("Section", style={"width": "12%", "background": "#ed1d26", "color": "#fff", "borderColor": "#ed1d26"}),
                html.Th("Course #", style={"width": "12%", "background": "#ed1d26", "color": "#fff", "borderColor": "#ed1d26"}),
                html.Th("Course Name", style={"width": "32%", "background": "#ed1d26", "color": "#fff", "borderColor": "#ed1d26"}),
                html.Th("Description/Notes", style={"width": "28%", "background": "#ed1d26", "color": "#fff", "borderColor": "#ed1d26"}),
                html.Th("Instructor(s)", style={"width": "16%", "background": "#ed1d26", "color": "#fff", "borderColor": "#ed1d26"}),
            ]))
        ]
        table_body = [
            html.Tbody([
                html.Tr([
                    html.Td(row['Section'], style={"background": "#fff", "color": "#221f20", "borderColor": "#909ca1"}),
                    html.Td(row['Course #'], style={"background": "#fff", "color": "#221f20", "borderColor": "#909ca1"}),
                    html.Td(row['Course Name'], style={"background": "#fff", "color": "#221f20", "borderColor": "#909ca1"}),
                    html.Td(row['Description/Notes'], style={"background": "#fff", "color": "#221f20", "borderColor": "#909ca1"}),
                    html.Td(row['Instructor(s)'], style={"background": "#fff", "color": "#221f20", "borderColor": "#909ca1"}),
                ]) for _, row in df.iterrows()
            ])
        ]
        return dbc.Table(table_header + table_body, bordered=True, hover=True, responsive=True, striped=True, style={"marginTop": "1em", "background": "#d8d8d8", "borderColor": "#909ca1"})