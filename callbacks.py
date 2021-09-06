import os
import abc
import math
import json
import base64
import io
import urllib
import urllib.parse
from tempfile import NamedTemporaryFile

import numpy as np
import pandas as pd

import ezdxf
from ezdxf.filemanagement import dxf_stream_info
from ezdxf.math import Vector

from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate
import dash_table
import plotly.graph_objs as go

from app import app


@app.callback(
    [
        Output("hub-results-table", "children"),
        Output("bearing-results-table", "children"),
    ],
    [Input("calc-bending-moment", "n_clicks")],
    [
        State("general-arrangement-dims", "data"),
        State("stress-concentrations", "data"),
        State("design-criteria-table", "data"),
        State("load-two-table", "data"),
    ],
)
def Calculate_Automatic_Results(
    n_clicks,
    general_arrangement_dims,
    stress_concentrations,
    design_criteria_table2,
    loads,
):
    # Don't update callback when program loads first time to prevent None types being returned:
    if n_clicks is None:
        raise PreventUpdate
    print(general_arrangement_dims, stress_concentrations)
    dummy_shaft_table_data = [
        dict(Component="Selected Shaft Material", Result="to be programmed 1"),
        dict(
            Component="Selected Shaft Yield Stress (MPa)", Result="to be programmed 1"
        ),
    ]

    # Create DataFrame.
    dummy_shaft_table_df = pd.DataFrame(dummy_shaft_table_data)

    # extract data/rows and columns
    columns = [
        {
            "name": i,
            "id": i,
        }
        for i in (dummy_shaft_table_df.columns)
    ]
    data = dummy_shaft_table_df.to_dict("rows")

    # Create a dash datatable
    dummy_shaft_results_table = dash_table.DataTable(
        data=data,
        columns=columns,
        style_as_list_view=True,
        style_cell={
            "textAlign": "center",
            "minWidth": "0px",
            "width": "200px",
            "maxWidth": "200px",
            "overflow": "hidden",
            "textOverflow": "ellipsis",
            "font-family": "sans-serif",
        },
        style_cell_conditional=[
            {"if": {"column_id": "Component"}, "textAlign": "left"}
        ],
    )

    dummy_table_data = [
        dict(Component="Selected Bearing Manufacturer", Result="to be programmed 1"),
        dict(Component="Bearing Life (Hrs)", Result="to be programmed 3"),
    ]

    # Create DataFrame.
    dummy_table_df = pd.DataFrame(dummy_table_data)

    # extract data/rows and columns
    columns = [
        {
            "name": i,
            "id": i,
        }
        for i in (dummy_table_df.columns)
    ]
    data = dummy_table_df.to_dict("rows")

    # Create a dash datatable
    dummy_table = dash_table.DataTable(
        data=data,
        columns=columns,
        style_as_list_view=True,
        style_cell={
            "textAlign": "center",
            "minWidth": "0px",
            "width": "200px",
            "maxWidth": "200px",
            "overflow": "hidden",
            "textOverflow": "ellipsis",
            "font-family": "sans-serif",
        },
        style_cell_conditional=[
            {"if": {"column_id": "Component"}, "textAlign": "left"}
        ],
    )
    return dummy_table, dummy_shaft_results_table


@app.callback(
    [Output("shaft-results-table", "children")],
    [Input("new_element_calculator", "n_clicks")],
    [State("shaft_inputs", "data"), State("shaft_inputs_1", "data")],
)
def shaft_value_calculator(n_clicks, dropdown_data, numerical_data):
    # print(dropdown_data, numerical_data)
    yield_value = [i["Value"] for i in numerical_data if i["id_name"] == "shaft_yield"][
        0
    ]
    ultimate_value = [
        i["Value"] for i in numerical_data if i["id_name"] == "shaft_ultimate"
    ][0]
    endurance_value = [
        i["Value"] for i in numerical_data if i["id_name"] == "shaft_endurance"
    ][0]

    material = [i["Value"] for i in dropdown_data if i["id_name"] == "shaft_material"]

    if yield_value == 800:
        yield_value = 644
    if ultimate_value == 1000:
        ultimate_value = 700
    if endurance_value == 450:
        endurance_value = 350

    result = dash_table.DataTable(
        # width = '75%',
        style_table={
            "width": "auto",
            # 'textAlign': 'center',
            # 'overflowY': 'scroll',
            "border": "thin lightgrey solid",
        },
        style_cell={
            "textAlign": "center",
            "backgroundColor": "rgb(255, 255, 255)",
            "font-family": "sans-serif",
            "width": "7%",
        },
        style_cell_conditional=[
            {
                "if": {"column_id": "id_name"},
                "display": "None",
            },
        ],
        style_data_conditional=[
            {
                "if": {"column_editable": True},
                "color": "rgb(0, 0, 230)",
                "background-color": "var(--color-off-white)",
            },
        ],
        columns=(
            [
                {
                    "id": "Description",
                    "name": "Description",
                    "editable": False,
                }
            ]
            + [{"id": i, "name": i, "editable": False} for i in material]
        ),
        # IF YOU UPDATE THIS YOU UPDATE THE SHAFTDESIGN.PY CODE
        # hidden_columns = ['id_name'],
        data=[
            {
                "Description": "yield",
                material[0]: yield_value,
            },
            {
                "Description": "ultimate",
                material[0]: ultimate_value,
            },
            {
                "Description": "endurance",
                material[0]: endurance_value,
            },
        ],
    )
    return [result]
