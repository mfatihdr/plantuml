import dash_bootstrap_components as dbc
from dash import dcc
from dash import html
import dash_daq as daq
from dash_svg import Svg, G, Path, Circle

from assets.styles import *

page_names =["network-map","http-headers","connections"]

navbar = dbc.NavbarSimple(
    children=[
        dbc.Button("PCap Analayze", outline=True, color="secondary", className="mr-1", id="btn_sidebar"),
        dbc.NavItem(dbc.NavLink("Network Map", href="#")),
        dbc.DropdownMenu(
            children=[
                dbc.DropdownMenuItem("Pages", header=True),
                dbc.DropdownMenuItem("Page 2", href="#"),
                dbc.DropdownMenuItem("Page 3", href="#"),
            ],
            nav=True,
            in_navbar=True,
            label="More",
        ),
    ],
    brand="Brand",
    brand_href="#",
    color="dark",
    dark=True,
    fluid=True,
)

sidebar = html.Div(
    [
        html.H2("Network analyzer", className="display-4"),
        html.Hr(),
        html.P(
            "A simple app to analyze pcap files", className="lead"
        ),
        dbc.Nav(
            [
                dbc.NavLink("Network", href="/network-map", id="network-map-link"),
                dbc.NavLink("HTTP Headers", href="/http-headers", id="http-headers-link"),
                dbc.NavLink("Page 3", href="/connections", id="connections-link"),
            ],
            vertical=True,
            pills=True,
        ),
    ],
    id="sidebar",
    style=SIDEBAR_STYLE,
)

page_1_content = [ 
                    html.Div([
                        html.Iframe(id="svgImage", src="",
                        style={"height": "1067px", "width": "100%"}),

                        html.Button('Get Analyze', id='analyzeButton')
                    ])
                    
        ]

content = html.Div(
    id="page-content",
    style=CONTENT_STYLE)

