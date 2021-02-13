import pandas as pd

def GetData()
    df = pd.read_csv("https://raw.githubusercontent.com/AbshkPskr/Zomato-Analysis/master/reviews.csv",
                    names = ['name','rating','date','cust_rating','review','sentiment']).drop_duplicates()

    rest_names = df.groupby('name').count().sort_values('rating',ascending = False).head(20).index.to_list()
    df = df[df.name.isin(rest_names)]
    df['rating'] = df['rating'].astype('float')
    df['date'] = pd.to_datetime(df['date'])
    df['cust_rating'] = df['cust_rating'].astype('float')
    df['review'] = df['review'].astype('string')
    df['sentiment'] = df['sentiment'].astype('float').round(2)

    return df
