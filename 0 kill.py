# from dateutil.relativedelta import relativedelta
# from datetime import datetime
# import re
# import pandas as pd

# def ConvertDate(ago):
#     try: 
#         value, unit = re.search(r'(\d+) (\w+) ago', ago).groups()
#         if not unit.endswith('s'):
#             unit += 's'
#         delta = relativedelta(**{unit: int(value)})
#         return (datetime.now() - delta)
#     except: 
#         pass
#     try:
#         return pd.to_datetime(ago)
#     except:
#         return ''

# print(ConvertDate("Jan 04, 2020"))
import pandas as pd

pd.read_csv('reviews.csv').drop_duplicates().to_csv('reviews.csv',index= False,sep="~")
