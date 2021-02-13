import pandas as pd

def GetData():
    df = pd.read_csv("https://github.com/AbshkPskr/Zomato-Analysis/blob/master/Text%20and%20emotion%20Analysis/final.csv?raw=true",
                 index_col='Unnamed: 0')
                #  names = ['name','rating','date','cust_rating','review','sentiment','emotion']).drop_duplicates()

    rest_names = df.groupby('name').count().sort_values('rating',ascending = False).head(20).index.to_list()
    df = df[df.name.isin(rest_names)]
    df['rating'] = df['rating'].astype('float')
    df['date'] = pd.to_datetime(df['date'])
    df['cust_rating'] = df['cust_rating'].astype('float')
    df['review'] = df['review'].astype('string')
    df['sentiment'] = df['sentiment'].astype('float').round(2)

    rest_dict = {}
    for drop in rest_names:
        rest =  df[df.name == drop].sort_values('date')#[-400:]
        rest['date'] = rest['date'].astype('string')
        rest = rest[pd.notna(rest['review'])]
        rest['smooth_sentiment'] = rest['sentiment'].rolling(int(len(rest)/30)).mean()
        rest['smooth_cust_rating'] = (rest['cust_rating']/10).rolling(int(len(rest)/40)).mean()
        rest = rest[pd.notna(rest['smooth_sentiment'])]
        rest = rest.set_index(i for i in range(len(rest)))
        rest_dict[drop] = rest

    return rest_dict
