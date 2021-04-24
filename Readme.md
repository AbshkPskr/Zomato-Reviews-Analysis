# Zomato Review Analysis
A Dashboard demonstrating Sentimental and Emotional analysis of top rated restaurants reviews located in NCR.

The data is Scraped form [zomato website](https://www.zomato.com/ncr/top-restaurants) using BeautifulSoup and web scraping techniques.The application is build using [dash](https://plotly.com/dash/) (a python library used to build interactive dashboard applications) which uses ploty.js as frontend to generate vizualizations. The project is deployed on pythonanywhere. Watch the live demo [here](http://abshkpskr211.pythonanywhere.com/).

![ZRA](https://github.com/AbshkPskr/Zomato-Reviews-Analysis/raw/master/Images/Dashboard.png)

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

| Plugin | README |
| ------ | ------ |
| **Line chart** - Shows the rolling mean of sentiment and customer rating. The uprise in the line represents the series of consecutive positive reviews and downfall represents the consecutive negative reviews. | <p align="center"><img src="https://github.com/AbshkPskr/Zomato-Reviews-Analysis/raw/master/Images/Line%20Chart.png" width="100%"></p> |
| **Review Text data** | <p align="center"><img src="https://github.com/AbshkPskr/Zomato-Reviews-Analysis/raw/master/Images/Rating%20Sentiment.png" width="100%"></p> |
| **Radar chart** | <p align="center"><img src="https://github.com/AbshkPskr/Zomato-Reviews-Analysis/raw/master/Images/Emotion.png" width="100%"></p> |
| **Pie Chart** | <p align="center"><img src="https://github.com/AbshkPskr/Zomato-Reviews-Analysis/raw/master/Images/Pie.png" width="100%"></p> |
| **Word Cloud** | <p align="center"><img src="https://github.com/AbshkPskr/Zomato-Reviews-Analysis/raw/master/Images/WordCloud.png" width="100%"></p> |

### Scope of functionalities
Similarly more vizualizations can be created to demonstrate trends. Worldcloud can be utilized to show which dish has been critisized and which are liked the most by analizing the reviews separately for positive and negative sentiment and emotions.
### Example of use
### Project status
### Sources