import dash
import dash_core_components as dcc
import dash_html_components as html

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets = external_stylesheets)

colors = {
    'background': '#111111',
    'text': '#7FDBFF'
    }

app.layout = html.Div(children=[
    html.H1('Hello Dashboard'),

    html.Div('Dash: A web application', style={
        'textAlign': 'center',
        'color': colors['text']
        }),

    dcc.Graph(
        id='Example',
        figure={
            'data': [
                {'x': [1,2,3], 'y': [4,2,3], 'type': 'bar', 'name': 'MTP'},
                {'x': [1,2,3], 'y': [2,2,5], 'type': 'bar', 'name': 'DTN'},
                ],
            'layout': {
                'title': 'Dashboard'
                }
            }
        )
    ])

if __name__ == '__main__':
    app.run_server(debug=True)


