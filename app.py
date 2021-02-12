import plotly.express as px
# from jupyter_dash import JupyterDash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import dash
import dash_table.DataTable as DT
# from  dash_dangerously_set_inner_html import DangerouslySetInnerHTML as DSIH
import json

import Get_Data

bar = df.groupby('name').count().sort_values(by = 'rating')
rest_dict = {}
for drop in bar.index.unique():
    rest =  df[df.name == drop].sort_values('date')
    rest['date'] = rest['date'].astype('string')
    rest = rest[pd.notna(rest['review'])]
    rest['smooth_sentiment'] = rest['sentiment'].rolling(int(len(rest)/5)).mean()
    rest = rest[pd.notna(rest['smooth_sentiment'])]
    rest = rest.set_index(i for i in range(len(rest)))
    rest_dict[drop] = rest

# external_css = ['https://codepen.io/chriddyp/pen/bWLwgP.css']


app = JupyterDash(__name__)#,external_stylesheets=external_css)

    
app_colors = {
    'background': '#1e2130',
    'layout': '#161a28',
    'text':'#000000',
    'text-shadow':'#0A76BA',
    'someothercolor':'#FF206E',
}
#'border':'1px solid grey',
dropdown_label_style = {'width':'20%','height':'40px','line-height': '35px','float':'left',
                        'color':'white','font-size':'20px','text-shadow': '2px 2px 5px #0A76BA'}
graph_style = {'width': '70%','float': 'left'}
figure_text_style={'text-shadow': '2px 2px 5px #0A76BA'}
head_style = {'font-size':'20px','text-align':'center','text-shadow': '2px 2px 5px #0A76BA','margin':'5%'}
text_style = {'font-size':'50px','text-align':'center','text-shadow': '2px 2px 5px #0A76BA'}
rating_div_style = {'width': '50%','float': 'left','color':'white','height':'120px',
                    'background-color':app_colors['layout']}
Sentiment_div_style = {'width': '49%','float': 'right','color':'white','height':'120px',
                       'background-color':app_colors['layout']}
review_div_style = {'height':'282.5px','overflow-y':'scroll','background-color':app_colors['layout']}
review_text_style = {'width': '86%','font-size':'15px','text-align':'centre','color':'white','margin':'5% 5%'}
graph_hover_data_style = {'width': '29%','float': 'right'}
gap_div = html.Div(style={'height':'15px','clear':'both'})

app.layout = html.Div([
                       html.Div([
                                 html.H1("Zomato Review Analysis",style={'text-align': 'center','color':'White','font-size':'50px'}),
                                 html.Div([html.Div('Select Restaurant', style=dropdown_label_style),
                                           html.Div(dcc.Dropdown(id='restaurant-dropdown',
                                                                 options=[{'label': i, 'value': i} for i in bar.index.unique()],
                                                                 value='Local'),
                                                    style={'width':'75%','height':'40px','float':'right','color':'black'})]
                                          ),
                                 gap_div,
                                 html.Div(children=[
                                                    html.Div(children = [
                                                                         dcc.Graph(id='graph',style = figure_text_style),
                                                                         gap_div, 
                                                                         html.Div([
                                                                                   dcc.Graph(id='radar',style={'width' : '49%','float': 'left'}),
                                                                                   dcc.Graph(id='pie',style={'width' : '49%','float': 'right'}),
                                                                                   ],
                                                                                  ),
                                                                         ],
                                                             style=graph_style
                                                             ),
                                                    html.Div(children=[
                                                                       html.Div(children=[
                                                                                          html.Div([
                                                                                                    html.Div(children='Rating',style = head_style),
                                                                                                    html.Div(id='cust_rating',style=text_style)
                                                                                                    ],
                                                                                                   style=rating_div_style
                                                                                                   ),
                                                                                          html.Div([
                                                                                                    html.Div(children='Sentiment',style = head_style),
                                                                                                    html.Div(id='sentiment',style=text_style)
                                                                                                    ],
                                                                                                   style=Sentiment_div_style
                                                                                                   ),
                                                                                          ],
                                                                                # style = {'height' : '100px'}
                                                                                ),
                                                                       gap_div,
                                                                       html.Div([
                                                                                 html.Div(id = 'review',style=review_text_style),
                                                                                 ],
                                                                                style = review_div_style
                                                                                ),
                                                                       gap_div,
                                                                       html.Div("asdfasdfasdf",style = review_div_style),
                                                                       ],
                                                             style = graph_hover_data_style
                                                             ),
                                                    ],
                                          ),
                                 gap_div,
                                 html.Div(id='table'),
                                 ],
                                style={'margin':'4% 3%'}
                                ),
                       ],
                      style = {'background-color':app_colors['background']}
                      )


@app.callback(
    Output('table', 'children'),
    Input("get", "height")
)
def debug(value):
    return value

# Define callback to update graph
@app.callback(
    Output('graph', 'figure'),
    Output('radar', 'figure'),
    Output('pie', 'figure'),
    Input("restaurant-dropdown", "value")
)

def update_figure(drop):
    fig_font_size = 10

    rest_data = rest_dict[drop]

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=rest_data.index,
                             y=rest_data.smooth_sentiment,
                             mode='lines+markers',
                             name='confirmed',line=dict(color='#C2BF20', width=2)))
    fig.update_layout(margin=dict(l=60,r=10,b=20,t=50,pad=0),
                      paper_bgcolor=app_colors['layout'],
                      height= 350,
                      legend=dict(x=.01,y=.98),
                      title_text = 'Reviews',
                      font_size=fig_font_size,
                      xaxis_title="Number of reviews",
                      yaxis_title="Sentiment with rolling mean",
                    #   gridcolor = 'Red',
                    #   clickmode='event+select',
                      xaxis = {'gridcolor':'grey'},
                      yaxis = {'gridcolor':'grey'},
                      plot_bgcolor=app_colors['layout'],
                      font = {'color':'white'},
                    #   hovermode='x'
                      )
    
    radar = go.Figure()
    radar.add_trace(go.Scatterpolar(r=[1,2,3,4,5,6],
                                    theta=[heart,'b','c','d','e','f'],
                                    mode='lines+markers',fill='toself',line=dict(width=2,color='#4E7094')))
    radar.update_layout(margin=dict(l=50,r=50,b=20,t=50,pad=0),
                    paper_bgcolor=app_colors['layout'],
                    height= 350,
                    # legend=dict(x=.01,y=.98),
                    title_text = 'Emotions',
                    font_size=fig_font_size,
                    xaxis_title="none",
                    yaxis_title="Emotional value",
                    plot_bgcolor=app_colors['layout'],
                    font = {'color':'white'},
                    polar = dict(angularaxis = dict(tickfont = dict(size = 25)),
                                 radialaxis=dict(visible = True,range = [0,10])),
                    )

   
    positive,negative,neutral = 0,0,0
    for senti in rest_data['sentiment']:
        if senti > 0:
            positive += 1
        if senti < 0:
            negative += 1
        else:
            neutral += 1
    pie = go.Figure()
    pie.add_trace(go.Pie(values=[positive,negative,neutral],
                 labels= ['Positive','Negative','Neutral'],
                 text=['Positive','Negative','Neutral'],
                 marker={'colors' :['#2EB848','#B82E2E','#2D35B4']},
                 hole = 0.4))
    pie.update_layout(margin=dict(l=20,r=20,b=20,t=50,pad=0),
                      paper_bgcolor=app_colors['layout'],
                      height= 350,
                    #   legend=dict(x=.01,y=.98),
                      title_text = 'Reviews',
                      font_size=fig_font_size,
                      xaxis_title="name",
                      yaxis_title="Number of reviews",
                      clickmode='event+select',
                      plot_bgcolor=app_colors['layout'],
                      font = {'color':'white'},
                      hovermode='x')
    

    return [fig,radar,pie]

@app.callback(
        Output('cust_rating', 'children'),
        Output('sentiment', 'children'),
        Output('review', 'children'),
        Input("restaurant-dropdown", "value"),
        Input("graph", "hoverData"),
)
def GetHoverData(drop,hoverData):
    rest_data = rest_dict[drop]
    X = 12
    if hoverData != None : X = int(hoverData['points'][0]['x'])
    rest_data = rest_data[rest_data.index == X]
    # table_data = rest_data.transpose().reset_index()
    # table = html.Table(children=[
    #                              html.Thead(html.Tr(children=[html.Th(col) for col in table_data.columns.values],
    #                                                 style={'color':app_colors['text']}
    #                                                 )
    #                                         ),
    #                              html.Tbody([html.Tr(children=[html.Td(table_data) for table_data in d],
    #                                                  style={'color':app_colors['text']}
    #                                                  )
    #                                          for d in table_data.values.tolist()])
    #                             ])

    review = rest_data['review']
    cust_rating = rest_data['cust_rating']
    sentiment = rest_data['sentiment']
    return [cust_rating,sentiment,review]


if __name__ == '__main__':
    app.run_server(debug=True,port = 8020)#mode = "inline")