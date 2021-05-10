# Zomato Review Analysis
A Dashboard demonstrating Sentimental and Emotional analysis of top rated restaurants reviews located in NCR.

The data is Scraped form [zomato website](https://www.zomato.com/ncr/top-restaurants) using BeautifulSoup and web scraping techniques.The application is build using [dash](https://plotly.com/dash/) (a python library used to build interactive dashboard applications) which uses ploty.js as frontend to generate vizualizations. The project is deployed on pythonanywhere. Watch the live demo [here](http://abshkpskr211.pythonanywhere.com/).

![ZRA](https://github.com/AbshkPskr/Zomato-Reviews-Analysis/raw/master/Images/Dashboard.png)

For sentimental and emotional analysis source code please refer to [Ipython notebook](https://github.com/AbshkPskr/Zomato-Reviews-Analysis/blob/master/Text%20and%20emotion%20Analysis/z_graphs.ipynb).

## Packages used
- Pandas
- Plotly
- Dash
- BeautifulSoup
- TextBlob
- DeepEmoji
- WordCloud

## Illustrations
All the restaurants are listed in a drop down menu. Seleting a particular restaurant will generate following vizualizations.

| Description | Visualization |
| ------ | ------ |
| **Line chart** - Shows the rolling mean of sentiment and customer rating. The uprise in the line represents the series of consecutive positive reviews and downfall represents the consecutive negative reviews. | <p align="center"><img src="https://github.com/AbshkPskr/Zomato-Reviews-Analysis/raw/master/Images/Line%20Chart.png" width="100%"></p> |
| **Review Text data** - By hovering mouse on the line chart we can see rating given by the customer, the sentiment related to the review and the review text. | <p align="center"><img src="https://github.com/AbshkPskr/Zomato-Reviews-Analysis/raw/master/Images/Rating%20Sentiment.png" width="100%"></p> |
| **Radar chart** - Represents the emotional analysis of all the reviews, performed using deepemoji. | <p align="center"><img src="https://github.com/AbshkPskr/Zomato-Reviews-Analysis/raw/master/Images/Emotion.png" width="100%"></p> |
| **Pie Chart** - Shows the percentage share of people sentiment towards restaurant. It shows number of positive, negative and neutral sentiment.| <p align="center"><img src="https://github.com/AbshkPskr/Zomato-Reviews-Analysis/raw/master/Images/Pie.png" width="100%"></p> |
| **Word Cloud** - A jumbled representation of all of the words used in reviews. The font size represents the frequency of the words. Words with bigger size are frequently used by the customer in the reviews. | <p align="center"><img src="https://github.com/AbshkPskr/Zomato-Reviews-Analysis/raw/master/Images/WordCloud.png" width="100%"></p> |

### Scope of functionalities
- As we can see the downward trend of reviews and ratings, each review text can be read separately and the problem can be seen without searching the whole database.
- With the help of these graphs negative reviews can be collected separately and words analysis can be done to address the exact problem.
- In this case it can be a dish or issue with the delivery, whichever the reason is, it can be identified and reasonable steps could be taken to rectify it.
- Similarly more vizualizations can be created to demonstrate trends. 
- With emotional analysis and sentimental analysis on a range of dishes, the most popular and most critisized dish can also be identified.
- Worldcloud can be utilized to show which dish has been critisized and which are liked the most by analizing the reviews separately for positive and negative sentiment and emotions.

### Sources
- Scraping - https://pypi.org/project/beautifulsoup4/
- Sentimental Analysis - https://pypi.org/project/textblob/
- Emotional Analysis - https://github.com/AbshkPskr/Emotion-recognition
- Text2Emotion - https://pypi.org/project/text2emotion/
- DeepEmoji - https://github.com/huggingface/torchMoji
- Dashboard - https://plotly.com/dash/
- WordCloud - https://pypi.org/project/wordcloud/