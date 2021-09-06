# from pydoc import classname

import dash_core_components as dcc
import dash_html_components as html
import dash_table

# from textwrap import dedent as s
import plotly.graph_objs as go
from dash.dependencies import Input, Output

from app import app
from text_store import *


# Layout styles:


board_group_style = {
    "background-color": "rgb(260, 260, 260)",
    "border-radius": "5px",
    "border": "1px solid rgb(190, 190, 190)",
    "box-shadow": "4px 4px 4px lightgrey",
    "padding": "5px",
    "margin": "20px 40px",  # top/ bottom sides I think
}

input_group_style = {
    "background-color": "#f9f9f9",
    # OLD
    "border-radius": "5px",
    "" "border": "1px solid #d9d9d9",
    "position": "relative",
    "box-shadow": "4px 4px 4px lightgrey",
    "padding": "5px",
}

input_group_container_style = {
    "background-color": "rgb(260, 260, 260)",
    # OLD
    "border-radius": "5px",
    "border": "1px solid rgb(190, 190, 190)",
    "position": "relative",
    "box-shadow": "4px 4px 4px lightgrey",
    "padding": "5px",
    "margin": "20px 40px",  # top/ bottom sides I think
    "justify-content": "space-around",
    "display": "flex",
    "align-items": "flex-start"
    # this enables all children to be treated as self adjusting columns, ie if theres 3 children
    # there will be 3 equally spaced columns
    # NOTE: edit the style dictionary of the children so width = 1 / n_columns where n_columns is number
    # of columns/ children of this parent
}

input_side_container_style = {
    "background-color": "rgb(260, 260, 260)",
    "padding": "2px",
    # 'border': '1px solid #d9d9d9',
    "box-sizing": "border-box",
    "width": "25%",
    "margin": "5px 1px",
    "display": "grid",
    "grid-template-columns": "2fr 1fr",
}

input_box_style = "eleven columns"  # old

layout1 = html.Main(
    style={"margin": "0px 0px", "padding": "0px"},
    children=[
        ########### HEADER ########################################################################################
        html.Header(
            (
                html.Div(
                    children=[
                        html.H3(
                            title_text,
                            style={
                                "margin-bottom": "0.5rem",
                            },
                        ),
                        html.H6(version_text),
                    ]
                ),
            ),
            className="container",
            style={
                "display": "flex",
                "flex-direction": "row",
                "justify-content": "space-between",
                "align-items": "center",
                # "background-image": "url('/dashboard/assets/preffered_banner7.png')",
                "background-color": "var(--color-off-black)",
                # "background-image": "radial-gradient(farthest-side at 60% 85%, rgb(0, 77, 153), rgb(20, 20, 20))",
                "color": "#fff",
                "margin": "0px 0px",
                "padding-top": "0rem",
                "padding-bottom": "0rem",
                "height": "125px",
            },
        ),
        # END HEADER
        ########### TAB INPUT BOXES  ########################################################################################
        html.Div(
            className="block container",
            children=[
                html.H4("General Information"),
                html.Div(
                    className="GroupContainer",
                    style={
                        # "margin-bottom": "5px",
                        # 'display': 'grid',
                        # 'grid-template-columns': '1fr 1fr',
                        # 'grid-column-gap': '1%',
                        "textAlign": "left",
                        "margin": "0px",
                    },
                    children=[
                        dcc.Markdown(
                            """
                            This is a general layout of a program in development.
                            * The layout takes inputs
                            * The layout it then data crunches the inputs, and returns graphs.
                            """,
                        ),
                    ],
                ),
            ],
        ),
        html.Div(
            className="block container",
            children=[
                html.H4("Arrangement Input Data"),
                dcc.Tabs(
                    id="tabs",
                    content_className="TabGroupContainer",
                    children=[
                        dcc.Tab(
                            label="Pulley General Arrangement",
                            children=[
                                html.H4(
                                    "Enter dimensions",
                                    style={
                                        # "display": "flex",
                                        "textAlign": "center",
                                    },
                                ),
                                html.Div(
                                    className="Container",
                                    style={
                                        # "display": "flex",
                                        # "flex-direction": "column",
                                        # "justify-content": "center",
                                        "display": "grid",
                                        "grid-template-columns": "1fr 3fr",
                                        # 'grid-template-rows': '1fr 1fr',
                                        "grid-column-gap": "1%",
                                        "textAlign": "center",
                                        "margin": "0px",
                                    },
                                    children=[
                                        html.Div(
                                            style={
                                                "display": "flex",
                                                "justify-content": "center",
                                            },
                                            children=[
                                                dash_table.DataTable(
                                                    id="general-arrangement-dims",
                                                    editable=True,
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
                                                            "if": {
                                                                "column_id": "id_name"
                                                            },
                                                            "display": "None",
                                                        },
                                                    ],
                                                    style_data_conditional=[
                                                        {
                                                            "if": {
                                                                "column_editable": True
                                                            },
                                                            "color": "rgb(0, 0, 230)",
                                                            "background-color": "var(--color-off-white)",
                                                        },
                                                    ],
                                                    columns=(
                                                        {
                                                            "id": "Description",
                                                            "name": "Description",
                                                            "editable": False,
                                                        },
                                                        {
                                                            "id": "Value",
                                                            "name": "Value",
                                                            "editable": True,
                                                        },
                                                        {
                                                            "id": "id_name",
                                                            "name": "id_name",
                                                            "editable": True,
                                                        },
                                                    ),
                                                    # IF YOU UPDATE THIS YOU UPDATE THE SHAFTDESIGN.PY CODE
                                                    # hidden_columns = ['id_name'],
                                                    data=[
                                                        {
                                                            "Description": "Bearing Centres (mm)",
                                                            "Value": "2500",
                                                            "id_name": "bearing_centres",
                                                        },
                                                        {
                                                            "Description": "Face Width (mm)",
                                                            "Value": "2000",
                                                            "id_name": "face_width",
                                                        },
                                                        {
                                                            "Description": "Dia Overlagging (mm)",
                                                            "Value": "920",
                                                            "id_name": "dia_ol",
                                                        },
                                                        {
                                                            "Description": "Lagging Thickness (mm)",
                                                            "Value": "16",
                                                            "id_name": "lagging_t",
                                                        },
                                                        {
                                                            "Description": "Drive Shaft Ext LHS (m)",
                                                            "Value": "160",
                                                            "id_name": "drive_shaft_ext_length",
                                                        },
                                                        {
                                                            "Description": "Belt Speed (m/s)",
                                                            "Value": "3.6",
                                                            "id_name": "v_belt",
                                                        },
                                                        {
                                                            "Description": "Belt Width (mm)",
                                                            "Value": "1800",
                                                            "id_name": "w_belt",
                                                        },
                                                    ],
                                                ),
                                            ],
                                        ),
                                        html.Div(
                                            style={"textAlign": "center"},
                                            children=[
                                                html.Img(
                                                    src=app.get_asset_url(
                                                        "pulley_dims_input_good.jpg"
                                                    ),
                                                    style={
                                                        "margin-top": "5px",
                                                        "margin-bottom": "5px",
                                                        "width": "90%",
                                                    },
                                                ),
                                            ],
                                        ),
                                    ],
                                ),
                            ],
                        ),
                        dcc.Tab(
                            label="Loads",
                            children=[
                                html.Div(
                                    className="Container",
                                    style={
                                        "display": "grid",
                                        "grid-template-columns": "1fr 1fr 1fr",
                                        # 'grid-template-rows': '1fr 1fr',
                                        "grid-column-gap": "1%",
                                        "textAlign": "center",
                                        "margin": "0px",
                                    },
                                    children=[
                                        html.Div(
                                            style={
                                                "display": "flex",
                                                "justify-content": "center",
                                                "flex-direction": "column",
                                            },
                                            children=[
                                                dash_table.DataTable(
                                                    id="load-two-table",
                                                    editable=True,
                                                    # width = '75%',
                                                    style_table={
                                                        # 'width': '900px',
                                                        "width": "auto",
                                                        # 'textAlign': 'center',
                                                        # 'overflowY': 'scroll',
                                                        "border": "thin lightgrey solid",
                                                    },
                                                    style_cell={
                                                        "textAlign": "center",
                                                        "backgroundColor": "rgb(255, 255, 255)",
                                                        "font-family": "sans-serif",
                                                        # 'width': '7%'
                                                        "width": "auto",
                                                    },
                                                    # style_cell_conditional=[
                                                    #     {'if': {'column_id': 'Dimension_Reference'},
                                                    #      'width': '10%'},
                                                    # ],
                                                    style_data_conditional=[
                                                        {
                                                            "if": {
                                                                "column_editable": True
                                                            },
                                                            "color": "rgb(0, 0, 230)",
                                                            "background-color": "var(--color-off-white)",
                                                        },
                                                    ],
                                                    columns=(
                                                        [
                                                            {
                                                                "id": "Load_Description",
                                                                "name": "Load Description",
                                                                "editable": False,
                                                            }
                                                        ]
                                                        + [
                                                            {
                                                                "id": "Running",
                                                                "name": "Running",
                                                                "editable": True,
                                                            }
                                                        ]
                                                        + [
                                                            {
                                                                "id": "Starting",
                                                                "name": "Starting",
                                                                "editable": True,
                                                            }
                                                        ]
                                                    ),
                                                    # IF YOU UPDATE THIS YOU UPDATE THE SHAFTDESIGN.PY CODE
                                                    data=[
                                                        {
                                                            "Load_Description": "T1 (kN)",
                                                            "Running": "50",
                                                            "Starting": "56",
                                                        },
                                                        {
                                                            "Load_Description": "T2 (kN)",
                                                            "Running": "20",
                                                            "Starting": "22",
                                                        },
                                                        {
                                                            "Load_Description": "Drive torque (kNm)",
                                                            "Running": "-13.7",
                                                            "Starting": "27",
                                                        },
                                                        {
                                                            "Load_Description": "Overhungload(kN)",
                                                            "Running": "6",
                                                            "Starting": "10",
                                                        },
                                                        {
                                                            "Load_Description": "Direction of Overhung load (kN)",
                                                            "Running": "270",
                                                            "Starting": "270",
                                                        },
                                                    ],
                                                ),
                                                html.Br(),
                                                dash_table.DataTable(
                                                    id="load-two-table-2",
                                                    editable=True,
                                                    # width = '75%',
                                                    style_table={
                                                        # 'width': '900px',
                                                        "width": "auto",
                                                        # 'textAlign': 'center',
                                                        # 'overflowY': 'scroll',
                                                        "border": "thin lightgrey solid",
                                                    },
                                                    style_cell={
                                                        "textAlign": "center",
                                                        "backgroundColor": "rgb(255, 255, 255)",
                                                        "font-family": "sans-serif",
                                                        # 'width': '7%'
                                                        "width": "auto",
                                                    },
                                                    style_cell_conditional=[
                                                        {
                                                            "if": {
                                                                "column_id": "id_name"
                                                            },
                                                            "display": "None",
                                                        },
                                                        # {'if': {'column_id': 'Dimension_Reference'},
                                                        #  'width': '10%'},
                                                    ],
                                                    style_data_conditional=[
                                                        {
                                                            "if": {
                                                                "column_editable": True
                                                            },
                                                            "color": "rgb(0, 0, 230)",
                                                            "background-color": "var(--color-off-white)",
                                                        },
                                                    ],
                                                    columns=(
                                                        {
                                                            "id": "Description",
                                                            "name": "Description",
                                                            "editable": False,
                                                        },
                                                        {
                                                            "id": "Value",
                                                            "name": "Value",
                                                            "editable": True,
                                                        },
                                                        {
                                                            "id": "id_name",
                                                            "name": "id_name",
                                                            "editable": True,
                                                        },
                                                    ),
                                                    data=[
                                                        {
                                                            "Description": "Angle of T1(deg)",
                                                            "Value": "180",
                                                            "id_name": "t1_theta",
                                                        },
                                                        {
                                                            "Description": "Angle of T2(deg)",
                                                            "Value": "180",
                                                            "id_name": "t2_theta",
                                                        },
                                                    ],
                                                ),
                                            ],
                                        ),
                                        html.Div(
                                            style={"textAlign": "center"},
                                            children=[
                                                html.Img(
                                                    src=app.get_asset_url(
                                                        "OL_theta.jpg"
                                                    ),
                                                    style={
                                                        "margin-top": "10px",
                                                        "margin-bottom": "10px",
                                                        "width": "75%",
                                                    },
                                                ),
                                            ],
                                        ),
                                        html.Div(
                                            style={"textAlign": "center"},
                                            children=[
                                                html.Img(
                                                    src=app.get_asset_url(
                                                        "T_theta.jpg"
                                                    ),
                                                    style={
                                                        "margin-top": "10px",
                                                        "margin-bottom": "10px",
                                                        "width": "75%",
                                                    },
                                                ),
                                            ],
                                        ),
                                    ],
                                ),
                            ],
                        ),
                    ],
                ),
            ],
        ),
        ######################### END INPUT BOXES #########################
        html.Div(
            style={"fontsize": 30, "textAlign": "center", "justify-content": "center"},
            children=[
                html.Button(
                    id="calc-bending-moment",
                    n_clicks=0,
                    children="Calculate",
                    style={
                        "fontsize": 30,
                        "background-color": "#33C3F0",
                        "color": "rgb(255, 255, 255)",
                        # 'textAlign': 'center',
                        "justify-content": "center",
                    },
                ),
            ],
        ),
        html.Div(
            className="block container",
            children=[
                html.Div(
                    className="GroupContainer",
                    children=[
                        html.H4(
                            "Preliminary Component Selection Results",
                            style={
                                "textAlign": "center",
                                "textAlign": "center",
                            },
                        ),
                        html.Div(
                            style={
                                "display": "grid",
                                "grid-template-columns": "1fr 1fr",
                                "textAlign": "center",
                                "padding": "0px",
                                "margin": "0px",
                                # 'background-color': 'rgb(245, 245, 245)'
                            },
                            children=[
                                html.Div(
                                    id="hub-results-table",
                                    style={
                                        "margin-bottom": "10px",
                                        "display": "flex",
                                        "justify-content": "center",
                                    },
                                ),
                                html.Div(
                                    id="bearing-results-table",
                                    style={
                                        "margin-bottom": "10px",
                                        "display": "flex",
                                        "justify-content": "center",
                                    },
                                ),
                            ],
                        ),
                    ],
                ),
            ],
        ),
        html.Div(
            id="current-housing-data-for-storage",
            style={
                "display": "none",
            },
        ),
        html.Div(
            id="current-hub-data-for-storage",
            style={
                "display": "none",
            },
        ),
        ############ New Element ################################################################################
        html.Div(
            className="block container",
            children=[
                html.H4("New Element"),
                dcc.Tabs(
                    id="new_element",
                    content_className="TabGroupContainer",
                    children=[
                        ## Bearing #########################################################################################################
                        dcc.Tab(
                            label="Bearings",
                            children=[
                                html.Div(
                                    className="Container",
                                    style={
                                        # "display": "flex",
                                        # "flex-direction": "column",
                                        # "justify-content": "center",
                                        "display": "grid",
                                        "grid-template-columns": "1fr 3fr",
                                        # 'grid-template-rows': '1fr 1fr',
                                        "grid-column-gap": "1%",
                                        "textAlign": "center",
                                        "margin": "0px",
                                    },
                                    children=[
                                        html.Div(
                                            style={
                                                "display": "flex",
                                                "justify-content": "center",
                                            },
                                            children=[
                                                dash_table.DataTable(
                                                    id="bearing_inputs",
                                                    editable=True,
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
                                                            "if": {
                                                                "column_id": "id_name"
                                                            },
                                                            "display": "None",
                                                        },
                                                    ],
                                                    style_data_conditional=[
                                                        {
                                                            "if": {
                                                                "column_editable": True
                                                            },
                                                            "color": "rgb(0, 0, 230)",
                                                            "background-color": "var(--color-off-white)",
                                                        },
                                                    ],
                                                    columns=(
                                                        {
                                                            "id": "Description",
                                                            "name": "Description",
                                                            "editable": False,
                                                        },
                                                        {
                                                            "id": "Value",
                                                            "name": "Input",
                                                            "editable": True,
                                                            "presentation": "dropdown",
                                                        },
                                                        {
                                                            "id": "id_name",
                                                            "name": "id_name",
                                                            "editable": True,
                                                        },
                                                    ),
                                                    # IF YOU UPDATE THIS YOU UPDATE THE SHAFTDESIGN.PY CODE
                                                    # hidden_columns = ['id_name'],
                                                    data=[
                                                        {
                                                            "Description": "Manufacturer",
                                                            "Value": "Timken",
                                                            "id_name": "bearing_manufacturer",
                                                        },
                                                        {
                                                            "Description": "Seal Type",
                                                            "Value": "standard",
                                                            "id_name": "bearing_seal_type",
                                                        },
                                                        {
                                                            "Description": "Design life (hrs)",
                                                            "Value": 100000,
                                                            "id_name": "bearing_design_hrs",
                                                        },
                                                        {
                                                            "Description": "Stress concentration",
                                                            "Value": 3,
                                                            "id_name": "bearing_stress_k",
                                                        },
                                                    ],
                                                    dropdown_conditional=[
                                                        {
                                                            "if": {
                                                                "column_id": "Value",
                                                                "filter_query": "{id_name} eq 'bearing_manufacturer'",
                                                            },
                                                            "clearable": False,
                                                            "options": [
                                                                {
                                                                    "label": i,
                                                                    "value": i,
                                                                }
                                                                for i in [
                                                                    "SKF",
                                                                    "Timken",
                                                                    "FAG",
                                                                ]
                                                            ],
                                                        },
                                                        {
                                                            "if": {
                                                                "column_id": "Value",
                                                                "filter_query": "{id_name} eq 'bearing_seal_type'",
                                                            },
                                                            "clearable": False,
                                                            "options": [
                                                                {
                                                                    "label": i,
                                                                    "value": i,
                                                                }
                                                                for i in [
                                                                    "standard",
                                                                    "double labrynth",
                                                                ]
                                                            ],
                                                        },
                                                    ],
                                                ),
                                            ],
                                        ),
                                    ],
                                ),
                            ],
                        ),
                        ## Shaft #########################################################################################################
                        dcc.Tab(
                            label="Shaft",
                            children=[
                                html.Div(
                                    className="Container",
                                    style={
                                        # "display": "flex",
                                        # "flex-direction": "column",
                                        # "justify-content": "center",
                                        "display": "grid",
                                        "grid-template-columns": "1fr 3fr",
                                        # 'grid-template-rows': '1fr 1fr',
                                        "grid-column-gap": "1%",
                                        "textAlign": "center",
                                        "margin": "0px",
                                    },
                                    children=[
                                        html.Div(
                                            style={
                                                "display": "flex",
                                                "justify-content": "center",
                                            },
                                            children=[
                                                dash_table.DataTable(
                                                    id="shaft_inputs",
                                                    editable=True,
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
                                                            "if": {
                                                                "column_id": "id_name"
                                                            },
                                                            "display": "None",
                                                        },
                                                    ],
                                                    style_data_conditional=[
                                                        {
                                                            "if": {
                                                                "column_editable": True
                                                            },
                                                            "color": "rgb(0, 0, 230)",
                                                            "background-color": "var(--color-off-white)",
                                                        },
                                                    ],
                                                    columns=(
                                                        {
                                                            "id": "Description",
                                                            "name": "Description",
                                                            "editable": False,
                                                        },
                                                        {
                                                            "id": "Value",
                                                            "name": "Input",
                                                            "presentation": "dropdown",
                                                            "editable": True,
                                                        },
                                                        {
                                                            "id": "id_name",
                                                            "name": "id_name",
                                                            "editable": True,
                                                        },
                                                    ),
                                                    # IF YOU UPDATE THIS YOU UPDATE THE SHAFTDESIGN.PY CODE
                                                    # hidden_columns = ['id_name'],
                                                    data=[
                                                        {
                                                            "Description": "Material",
                                                            "Value": "K1045",
                                                            "id_name": "shaft_material",
                                                        },
                                                        {
                                                            "Description": "Design method",
                                                            "Value": "AS1403",
                                                            "id_name": "shaft_design_method",
                                                        },
                                                    ],
                                                    dropdown_conditional=[
                                                        {
                                                            "if": {
                                                                "column_id": "Value",
                                                                "filter_query": "{id_name} eq 'shaft_material'",
                                                            },
                                                            "clearable": False,
                                                            "options": [
                                                                {
                                                                    "label": i,
                                                                    "value": i,
                                                                }
                                                                for i in [
                                                                    "K1045",
                                                                    "4140",
                                                                ]
                                                            ],
                                                        },
                                                        {
                                                            "if": {
                                                                "column_id": "Value",
                                                                "filter_query": "{id_name} eq 'shaft_design_method'",
                                                            },
                                                            "clearable": False,
                                                            "options": [
                                                                {
                                                                    "label": i,
                                                                    "value": i,
                                                                }
                                                                for i in [
                                                                    "AS1403",
                                                                    "DIN",
                                                                ]
                                                            ],
                                                        },
                                                    ],
                                                ),
                                                dash_table.DataTable(
                                                    id="shaft_inputs_1",
                                                    editable=True,
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
                                                            "if": {
                                                                "column_id": "id_name"
                                                            },
                                                            "display": "None",
                                                        },
                                                    ],
                                                    style_data_conditional=[
                                                        {
                                                            "if": {
                                                                "column_editable": True
                                                            },
                                                            "color": "rgb(0, 0, 230)",
                                                            "background-color": "var(--color-off-white)",
                                                        },
                                                    ],
                                                    columns=(
                                                        {
                                                            "id": "Description",
                                                            "name": "Description",
                                                            "editable": False,
                                                        },
                                                        {
                                                            "id": "Value",
                                                            "name": "Input",
                                                            "editable": True,
                                                        },
                                                        {
                                                            "id": "id_name",
                                                            "name": "id_name",
                                                            "editable": True,
                                                        },
                                                    ),
                                                    # IF YOU UPDATE THIS YOU UPDATE THE SHAFTDESIGN.PY CODE
                                                    # hidden_columns = ['id_name'],
                                                    data=[
                                                        {
                                                            "Description": "Yield Stress(Mpa)",
                                                            "Value": 800,
                                                            "id_name": "shaft_yield",
                                                        },
                                                        {
                                                            "Description": "Ultimate Stress(Mpa)",
                                                            "Value": 1000,
                                                            "id_name": "shaft_ultimate",
                                                        },
                                                        {
                                                            "Description": "Endurance Stress(Mpa)",
                                                            "Value": 1000,
                                                            "id_name": "shaft_endurance",
                                                        },
                                                        {
                                                            "Description": "Maximum deflection 1",
                                                            "Value": 2000,
                                                            "id_name": "shaft_max_deflection",
                                                        },
                                                        {
                                                            "Description": "Safety Factor",
                                                            "Value": 1.2,
                                                            "id_name": "shaft_safety_factor",
                                                        },
                                                    ],
                                                ),
                                            ],
                                        ),
                                    ],
                                ),
                            ],
                        ),
                        ## Hub ############################################################################################################
                        dcc.Tab(
                            label="Hub",
                            children=[
                                html.Div(
                                    className="Container",
                                    style={
                                        # "display": "flex",
                                        # "flex-direction": "column",
                                        # "justify-content": "center",
                                        "display": "grid",
                                        "grid-template-columns": "1fr 3fr",
                                        # 'grid-template-rows': '1fr 1fr',
                                        "grid-column-gap": "1%",
                                        "textAlign": "center",
                                        "margin": "0px",
                                    },
                                    children=[
                                        html.Div(
                                            style={
                                                "display": "flex",
                                                "justify-content": "center",
                                            },
                                            children=[],
                                        ),
                                    ],
                                ),
                            ],
                        ),
                    ],
                ),
            ],
        ),
        ######################### END INPUT BOXES #########################
        html.Div(
            style={"fontsize": 30, "textAlign": "center", "justify-content": "center"},
            children=[
                html.Button(
                    id="new_element_calculator",
                    n_clicks=0,
                    children="Calculate",
                    style={
                        "fontsize": 30,
                        "background-color": "#33C3F0",
                        "color": "rgb(255, 255, 255)",
                        # 'textAlign': 'center',
                        "justify-content": "center",
                    },
                ),
            ],
        ),
        html.Div(
            className="block container",
            children=[
                html.Div(
                    className="GroupContainer",
                    children=[
                        html.H4(
                            "Results",
                            style={
                                "textAlign": "center",
                                "textAlign": "center",
                            },
                        ),
                        html.Div(
                            style={
                                "display": "grid",
                                "grid-template-columns": "1fr 1fr",
                                "textAlign": "center",
                                "padding": "0px",
                                "margin": "0px",
                                # 'background-color': 'rgb(245, 245, 245)'
                            },
                            children=[
                                html.Div(
                                    id="shaft-results-table",
                                    style={
                                        "margin-bottom": "10px",
                                        "display": "flex",
                                        "justify-content": "center",
                                    },
                                ),
                            ],
                        ),
                    ],
                ),
            ],
        ),
        html.Div(
            className="block container",
            children=[
                html.Div([]),
                # html.P(legal_text),
                html.H5(copyright_text),
            ],
        ),
    ],
)
############ END LAYOUT 1 ############################################################


# Setup layout parameters
layout = dict(
    autosize=True,
    automargin=True,
    margin=dict(l=30, r=30, b=20, t=40),
    hovermode="closest",
    plot_bgcolor="rgb(30, 30, 30)",
    paper_bgcolor="rgb(30, 30, 30)",
    # paper_bgcolor="#F9F9F9",
    legend=dict(font=dict(size=10), orientation="h"),
    title="Satellite Overview",
    mapbox=dict(
        style="light",
        center=dict(lon=-78.05, lat=42.54),
        zoom=7,
    ),
)
