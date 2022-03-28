import dash
from dash import dash_table
import dash_bootstrap_components as dbc

import pandas as pd

from fields import *
from pcap import cap

app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])
from assets.layouts import *

from UMLGenerate import generateUML

app.layout = html.Div(
    [
        dcc.Store(id='side_click'),
        dcc.Location(id="url"),
        navbar,
        sidebar,
        content
    ],
)

pcap_object = cap(CAP_FILENAME)

data_pak = pcap_object.check_communication(dFilter, decodeAs)

svgUML = generateUML(CAP_FILENAME,data_pak, aliases)

from assets.callbacks import *

if __name__ == "__main__":
    app.run_server(debug=True, threaded=True, port=8086)