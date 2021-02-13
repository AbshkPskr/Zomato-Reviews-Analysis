import numpy as np
import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output
import plotly.graph_objs as go
from wordcloud import WordCloud, STOPWORDS
import Get_Data

# from jupyter_dash import JupyterDash

rest_dict = Get_Data.GetData()
rest_names = list(rest_dict.keys())

# external_css = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__)#,external_stylesheets=external_css)
    
app_styling = {
    'background': '#1e2130',
    'layout': '#161a28',
    'text':'#000000',
    'text-shadow':'2px 2px 5px #0A76BA',
    'box-shadow':'4px 4px 5px #0E1017',
}

#'border':'1px solid grey',
heading_style = {'text-align': 'center','color':'White','font-size':'50px','text-shadow': app_styling['text-shadow']}
dropdown_label_style = {'width':'10%','height':'40px','line-height': '35px','float':'left','color':'white',
                        'font-size':'20px','text-shadow': app_styling['text-shadow'],'text-align':'center'}
dropdown_div_style = {'width':'85%','height':'40px','float':'right','color':'black'}
graph_style = {'width': '70%','float': 'left'}
figure_text_style={'text-shadow': app_styling['text-shadow'],'box-shadow': app_styling['box-shadow']}
radar_style = {'width' : '49%','float': 'left','text-shadow': app_styling['text-shadow'],'box-shadow': app_styling['box-shadow']}
Pie_style = {'width' : '49%','float': 'right','text-shadow': app_styling['text-shadow'],'box-shadow': app_styling['box-shadow']}
head_style = {'font-size':'20px','text-align':'center','text-shadow': app_styling['text-shadow'],'margin':'5%'}
text_style = {'font-size':'50px','text-align':'center','text-shadow': app_styling['text-shadow']}
rating_div_style = {'width': '50%','float': 'left','color':'white','height':'120px','background-color':app_styling['layout'],'box-shadow': app_styling['box-shadow']}
Sentiment_div_style = {'width': '49%','float': 'right','color':'white','height':'120px','background-color':app_styling['layout'],'box-shadow': app_styling['box-shadow']}
review_div_style = {'height':'282.5px','overflow-y':'scroll','background-color':app_styling['layout'],'box-shadow': app_styling['box-shadow']}
review_text_style = {'width': '86%','font-size':'17px','text-align':'centre','color':'white','margin':'3% 5%'}
Wordcloud_div_style = {'height':'282.5px','background-color':app_styling['layout'],'box-shadow': app_styling['box-shadow']}
wordcloud_image_style = {'height':'100%', 'width':'100%'}
graph_hover_data_style = {'width': '29%','float': 'right'}
gap_div = html.Div(style={'height':'15px','clear':'both'})

app.layout = html.Div([
                       html.Div([
                                 html.H1("Zomato Review Analysis",style=heading_style),
                                 html.Div([html.Div('Select Restaurant', style=dropdown_label_style),
                                           html.Div(dcc.Dropdown(id='restaurant-dropdown',
                                                                 options=[{'label': i, 'value': i} for i in rest_names],
                                                                 value='PCO'),style=dropdown_div_style)
                                           ],
                                          ),
                                 gap_div,
                                 html.Div([
                                            html.Div( [
                                                        dcc.Graph(id='graph',style = figure_text_style),
                                                        gap_div, 
                                                        html.Div([
                                                                dcc.Graph(id='radar',style=radar_style),
                                                                dcc.Graph(id='pie',style=Pie_style),
                                                                ],
                                                                ),
                                                        ],
                                                        style=graph_style
                                                        ),
                                            html.Div([
                                                        html.Div([
                                                                html.Div([
                                                                        html.Div('Rating',style = head_style),
                                                                        html.Div(id='cust_rating',style=text_style)
                                                                        ],
                                                                        style=rating_div_style
                                                                        ),
                                                                html.Div([
                                                                        html.Div('Sentiment',style = head_style),
                                                                        html.Div(id='sentiment',style=text_style)
                                                                        ],
                                                                        style=Sentiment_div_style
                                                                        ),
                                                                  ],
                                                                 ),
                                                        gap_div,
                                                        html.Div([
                                                                    html.Div(id = 'review',style=review_text_style),
                                                                    ],
                                                                style = review_div_style
                                                                ),
                                                        gap_div,
                                                        html.Div(html.Img(id = 'wordcloud',style=wordcloud_image_style),
                                                                style = Wordcloud_div_style),
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
                      style = {'background-color':app_styling['background']}
                      )



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

    graph = go.Figure()
    graph.add_trace(go.Scatter(x=rest_data.index,
                             y=rest_data.smooth_sentiment,
                             mode='lines+markers',
                             text = rest_data.sentiment,
                             hovertemplate = 
                             "<b>%{text}</b>",
                             name='Sentiment',line=dict(color='green', width=2)))
    graph.add_trace(go.Scatter(x=rest_data.index,
                             y=rest_data.smooth_cust_rating,
                             text = rest_data.cust_rating,
                             hovertemplate = 
                             "<b>%{text}</b>",
                             mode='lines+markers',
                             name='Customer Rating',line=dict(color='red', width=2)))
    graph.update_layout(margin=dict(l=60,r=10,b=20,t=50,pad=0),
                      paper_bgcolor=app_styling['layout'], 
                      height= 350,
                      legend=dict(x=.01,y=.98),
                      title_text = 'Reviews',
                      font_size=fig_font_size,
                      xaxis_title="Number of reviews",
                      yaxis_title="Sentiment and rating with rolling mean",
                    #   gridcolor = 'Red',
                    #   clickmode='event+select',
                      xaxis = {'gridcolor':'grey'},
                      yaxis = {'gridcolor':'grey'},
                      plot_bgcolor=app_styling['layout'],
                      font = {'color':'white'},
                      hovermode='x'
                      )
    
    
    radar_data = rest_data.groupby('emotion').count()
    radar_emotion_count = np.log(radar_data.name).to_list()
    radar_emotion_count.append(radar_emotion_count[0])
    radar_emotion_types = radar_data.index.to_list()
    radar_emotion_types.append(radar_emotion_types[0])
    # radar_data.name = (radar_data.name - min(radar_data.name))/(max(radar_data.name) - min(radar_data.name))

    rating_data = rest_data.groupby('cust_rating').count()
    rating_count_list = np.log(rating_data.name).to_list()
    rating_count_list.append(rating_count_list[0])
    rating_num_list = [str(i)+".." for i in rating_data.index.to_list()]
    rating_num_list.append(rating_num_list[0])

    radar = go.Figure()
    radar.add_trace(go.Scatterpolar(r=radar_emotion_count,
                                    theta=radar_emotion_types,
                                    mode='lines+markers',fill='toself',
                                    line=dict(width=2,color='green')))
    # radar.add_trace(go.Scatterpolar(r=rating_count_list,
    #                             theta=rating_num_list,
    #                             mode='lines+markers',fill='toself',
    #                             line=dict(width=2,color='red')))
    
    radar.update_layout(margin=dict(l=50,r=50,b=30,t=50,pad=0),
                    paper_bgcolor=app_styling['layout'],
                    height= 350,
                    # legend=dict(x=.01,y=.98),
                    title_text = 'Emotions',
                    font_size=fig_font_size,
                    xaxis_title="none",
                    yaxis_title="Emotional value",
                    plot_bgcolor=app_styling['layout'],
                    font = {'color':'white'},
                    polar = dict(angularaxis = dict(tickfont = dict(size = 25)),
                                 radialaxis=dict(visible = True,
                                                 range = [0,max(np.log(radar_data.name).to_list())+1]
                                                 )
                                 ),
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
                      paper_bgcolor=app_styling['layout'],
                      height= 350,
                    #   legend=dict(x=.01,y=.98),
                      title_text = 'Reviews',
                      font_size=fig_font_size,
                      xaxis_title="name",
                      yaxis_title="Number of reviews",
                      clickmode='event+select',
                      plot_bgcolor=app_styling['layout'],
                      font = {'color':'white'},
                      hovermode='x')
    
    return [graph,radar,pie]

@app.callback(
        Output('cust_rating', 'children'),
        Output('sentiment', 'children'),
        Output('review', 'children'),
        Input("restaurant-dropdown", "value"),
        Input("graph", "hoverData"),
)
def GetHoverData(drop,hoverData):
    rest_data = rest_dict[drop]
    X = 100
    if hoverData != None : X = int(hoverData['points'][0]['x'])
    rest_data = rest_data[rest_data.index == X]
    review = rest_data['review']
    cust_rating = rest_data['cust_rating']
    sentiment = rest_data['sentiment']
    return [cust_rating,sentiment,review]

@app.callback(
        Output('wordcloud', 'src'),
        Input("restaurant-dropdown", "value"),
)
def CreateWordCloudImage(drop):
    rest_data = rest_dict[drop]
    reviews = rest_data[rest_data['sentiment']>.5].review.dropna()
    text = " ".join(rest_data.review.dropna())
    wca = WordCloud(relative_scaling = 1.0,stopwords = set(STOPWORDS)).generate(text)
    return wca.to_image()


if __name__ == '__main__':
    app.run_server(debug=True)#,port = 8020)#mode = "inline")