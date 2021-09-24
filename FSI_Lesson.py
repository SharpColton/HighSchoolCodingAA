import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import plotly.express as px
import pandas as pd



FSI = pd.read_csv("STLFSI2.csv")
FSI["DATE"] = pd.to_datetime(FSI["DATE"], format="%Y-%m-%d")
FSI.sort_values("DATE", inplace=True)

MORTGAGE = pd.read_csv("MORTGAGE30US.csv")
MORTGAGE["DATE"] = pd.to_datetime(MORTGAGE["DATE"], format="%Y-%m-%d")
MORTGAGE.sort_values("DATE", inplace=True)



SIDEBAR_STYLE = {
    'position': 'fixed',
    'top': 0,
    'left': 0,
    'bottom': 0,
    'width': '20%',
    'padding': '20px 10px',
    'background-color': '#f8f9fa'
}
TEXT_STYLE = {
    'textAlign': 'center',
    'color': '#191970'
}
controls = dbc.FormGroup(
    [
        html.P('Dropdown', style={
            'textAlign': 'center'
        }),
        dcc.Dropdown(
            id='dropdown',
            options=[{
                'label': 'Value One',
                'value': 'value1'
            }, {
                'label': 'Value Two',
                'value': 'value2'
            },
                {
                    'label': 'Value Three',
                    'value': 'value3'
                }
            ],
            value=['value1'],  # default value
            multi=True
        ),
        html.Br(),
        #UNCOMMENT FOR MORE SIDEBAR OPTIONS
        # html.P('Range Slider', style={
        #     'textAlign': 'center'
        # }),
        # dcc.RangeSlider(
        #     id='range_slider',
        #     min=0,
        #     max=20,
        #     step=0.5,
        #     value=[5, 15]
        # ),
        # html.P('Check Box', style={
        #     'textAlign': 'center'
        # }),
        # dbc.Card([dbc.Checklist(
        #     id='check_list',
        #     options=[{
        #         'label': 'Value One',
        #         'value': 'value1'
        #     },
        #         {
        #             'label': 'Value Two',
        #             'value': 'value2'
        #         },
        #         {
        #             'label': 'Value Three',
        #             'value': 'value3'
        #         }
        #     ],
        #     value=['value1', 'value2'],
        #     inline=True
        # )]),
        # html.Br(),
        # html.P('Radio Items', style={
        #     'textAlign': 'center'
        # }),
        # dbc.Card([dbc.RadioItems(
        #     id='radio_items',
        #     options=[{
        #         'label': 'Value One',
        #         'value': 'value1'
        #     },
        #         {
        #             'label': 'Value Two',
        #             'value': 'value2'
        #         },
        #         {
        #             'label': 'Value Three',
        #             'value': 'value3'
        #         }
        #     ],
        #     value='value1',
        #     style={
        #         'margin': 'auto'
        #     }
        # )]),
        # html.Br(),
        # dbc.Button(
        #     id='submit_button',
        #     n_clicks=0,
        #     children='Submit',
        #     color='primary',
        #     block=True
        # ),
    ]
)

sidebar = html.Div(
    [
        html.H2('Parameters', style=TEXT_STYLE),
        html.Hr(),
        controls
    ],
    style=SIDEBAR_STYLE,
)
CARD_TEXT_STYLE = {
    'textAlign': 'center',
    'color': '#0074D9'
}
content_first_row = dbc.Row([
    dbc.Col(
        dbc.Card(
            [

                dbc.CardBody(
                    [
                        html.H4(id='card_title_1', children=['Card Title 1'], className='card-title',
                                style=CARD_TEXT_STYLE),
                        html.P(id='card_text_1', children=['Sample text.'], style=CARD_TEXT_STYLE),
                    ]
                )
            ]

        ),
        md=3
    ),
    dbc.Col(
        dbc.Card(
            [

                dbc.CardBody(
                    [
                        html.H4('Card Title 2', className='card-title', style=CARD_TEXT_STYLE),
                        html.P('Sample text.', style=CARD_TEXT_STYLE),
                    ]
                ),
            ]

        ),
        md=3
    ),
    dbc.Col(
        dbc.Card(
            [
                dbc.CardBody(
                    [
                        html.H4('Card Title 3', className='card-title', style=CARD_TEXT_STYLE),
                        html.P('Sample text.', style=CARD_TEXT_STYLE),
                    ]
                ),
            ]

        ),
        md=3
    ),
    dbc.Col(
        dbc.Card(
            [
                dbc.CardBody(
                    [
                        html.H4('Card Title 4', className='card-title', style=CARD_TEXT_STYLE),
                        html.P('Sample text.', style=CARD_TEXT_STYLE),
                    ]
                ),
            ]
        ),

        md=3
    )
])

content_second_row = dbc.Row([

    dbc.Col(
        dbc.Card(
            [

                dbc.CardBody(
                    [
                        html.H4('Card Title 5', className='card-title', style=CARD_TEXT_STYLE),
                        html.P('Sample text.', style=CARD_TEXT_STYLE),
                    ]
                ),
            ]

        ),
        md=4
    ),
    dbc.Col(
        dbc.Card(
            [
                dbc.CardBody(
                    [
                        html.H4('Card Title 6', className='card-title', style=CARD_TEXT_STYLE),
                        html.P('Sample text.', style=CARD_TEXT_STYLE),
                    ]
                ),
            ]

        ),
        md=4
    ),
    dbc.Col(
        dbc.Card(
            [
                dbc.CardBody(
                    [
                        html.H4('Card Title 7', className='card-title', style=CARD_TEXT_STYLE),
                        html.P('Sample text.', style=CARD_TEXT_STYLE),
                    ]
                ),
            ]
        ),
        md=4
    )
])

content_third_row = dbc.Row([


    dbc.Col(
        dbc.Card(
            [
                dbc.CardBody(
                    [
                        html.H4('Card Title 8', className='card-title', style=CARD_TEXT_STYLE),
                        html.P('Sample text.', style=CARD_TEXT_STYLE),
                    ]
                ),
            ]

        ),
        md=6
    ),
    dbc.Col(
        dbc.Card(
            [
                dbc.CardBody(
                    [
                        html.H4('Card Title 9', className='card-title', style=CARD_TEXT_STYLE),
                        html.P('Sample text.', style=CARD_TEXT_STYLE),
                    ]
                ),
            ]
        ),
        md=6
    )
])

content_fourth_row = dbc.Row([



    dbc.Col(
        dbc.Card(
            [
                dbc.CardBody(
                    [
                        html.H4('Card Title 10', className='card-title', style=CARD_TEXT_STYLE),
                        html.P('Sample text.', style=CARD_TEXT_STYLE),
                    ]
                ),
            ]
        ),
        md=12
    )
])

content_fifth_row = dbc.Row([

    dbc.Col(
        dcc.Graph(
            figure={
                "data": [
                    {
                        "x": FSI["DATE"],
                        "y": FSI["STLFSI2"],
                        "type": "lines",
                    },
                ],
                "layout": {"title": "St. Louis Fed Financial Stress Index (STLFSI2)"},
            },
        ), md=12
    )
])
content_sixth_row = dbc.Row([

    dbc.Col(
        dcc.Graph(
            figure={
                "data": [
                    {
                        "x": MORTGAGE["DATE"],
                        "y": MORTGAGE["RATE"],
                        "type": "lines",
                    },
                ],
                "layout": {"title": "30-Year Fixed Rate Mortgage Average in the United States (MORTGAGE30US)"},
            },
        ), md=12
    )
])

content_seventh_row = dbc.Row([

    dbc.Col(
        dcc.Graph(
            figure={
                "data": [
                    {
                        "x": MORTGAGE["DATE"],
                        "y": MORTGAGE["RATE"],
                        "type": "lines",
                    },
                ],
                "layout": {"title": "30-Year Fixed Rate Mortgage Average in the United States (MORTGAGE30US)"},
            },
        ), md=12
    )
])
CONTENT_STYLE = {
    'margin-left': '25%',
    'margin-right': '5%',
    'padding': '20px 10p'
}
content = html.Div(
    [
        html.H2('Analytics Dashboard Template', style=TEXT_STYLE),
        html.Hr(),
        content_first_row,
        html.Hr(),
        content_second_row,
        html.Hr(),
        content_third_row,
        html.Hr(),
        content_fourth_row,
        html.Hr(),
        content_fifth_row,
        html.Hr(),
        content_sixth_row,
    ],
    style=CONTENT_STYLE
)






app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])
app.layout = html.Div([sidebar, content])


if __name__ == '__main__':
    app.run_server(port='8085')
