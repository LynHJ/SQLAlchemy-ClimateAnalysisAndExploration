# Climate Analysis And Exploration

![](https://img.shields.io/badge/Flask-1.1.2-informational?style=plastic&logo=appveyor)
![](https://img.shields.io/badge/SQLAlchemy-1.4.40-informational?style=plastic&logo=appveyor)
![](https://img.shields.io/badge/numpy-1.23.4-informational?style=plastic&logo=appveyor)
![](https://img.shields.io/badge/pandas-1.0.3-informational?style=plastic&logo=appveyor)
![](https://img.shields.io/badge/scipy-1.4.1-informational?style=plastic&logo=appveyor)


## Background

After having been working as a data analyst for 2 years, I have decided to have a long holiday vacation in Honolulu, Hawaii. To work out my trip planning, I think I need to do some climate analysis on the area. 

## Source

There is a sqlite database containing Hawaii's climate change in recent years and the data of weather stations in Hawaii.      

## Climate Analysis

![alt text](https://github.com/LynHJ/Sqlalchemy-Climate-Analysis-and-Exploration/blob/fa1724651f8ac36d435ef7ca1902a31aba8714b8/OutputData/precipitation.png)

##### Summary:

The rainfall pattern of Hawaii is quite clear. There are four times of heavy rain during a year (2016, 8, 23 ~ 2017, 8, 23). Most of the time, the amount of rainfall is below 25mm. If tourists can avoid traveling in specific months(Feb,May,Jul, and Oct, based on the photo above), they would have a great time in Hawaii.


![alt text](https://github.com/LynHJ/Sqlalchemy-Climate-Analysis-and-Exploration/blob/fa1724651f8ac36d435ef7ca1902a31aba8714b8/OutputData/station-histogram.png)

##### Summary:

According to the picture above,the distribution of temperature is a left-skewed-distribution.It indicates that most of the time in Hawaii, the temperature ranges around 22-26°C​ and ​​there is a cool weather period.


## Advanced Data Analysis1

§ Conduct an analysis :Is there a meaningful difference between the temperatures in June and December?  
  
0. There are some premises we need to go through to make sure the result of T-test is Statistically meaningful.  
1. Normal Distribution.->temperature is a normal distribution  
2. Independent variable.-> the weather condition in June won't affect the weather condition in December.  
3. Ｈomogeneity in the two groups of variance-> Run levene test  
4. Sample Size: The size of two gorups is different. ->Run unpaired T-test.   
5. H0:mean(June)=mean(December)  
&emsp;H1:mean(June)≠mean(December)

#### Summary for Advanced Data Analysis1

1. levene-test: p-value(0.001)<0.05  ->Heteroscedasticity in the two groups of variance, run adjusted T-test(equal_var=False).  
2. unpaired t-test result:p-value<0.05 ->Reject H0, The average temperature in June is differ than the average temperature in December.
  

## Advanced Data Analysis2

§ Based on my travel time period, I investigate the daily rainfall amount and temperature.
 
![alt text](https://github.com/LynHJ/Sqlalchemy-Climate-Analysis-and-Exploration/blob/450c53707646bbf2ac81fcbc325bc7352d6ccd37/OutputData/daily-normals.png)  

#### Summary for Advanced Data Analysis

1. The amount of precipitation is less than 10mm during the time period I have set.
2. According to the picture above,the temperature is stable. The temperature range is around 20°c to 28°c


### WeatherApp

![alt text](https://github.com/LynHJ/Sqlalchemy-Climate-Analysis-and-Exploration/blob/5b71fd4f3d2121b29013dfdfcf2d6b3c54a208fd/OutputData/app.png)

I use flask to do a simple web framework.
By excuting 'app.py',I can run the route to get basic weather data or input Start/End date to get specific time period weather data.

## Content:
```
Project  
├── AdvancedTempAnalysis1.ipynb
├── AdvancedTempAnalysis2.ipynb
├── ClimateAnalysis.ipynb
├── OutputData
│   ├── app.png
│   ├── daily-normals.png
│   ├── describe.png
│   ├── precipitation.png
│   ├── station-histogram.png
│   └── temperature.png
├── README.md
├── Resources
│   ├── hawaii_measurements.csv
│   └── hawaii_stations.csv
├── app.ipynb
├── app.py
├── hawaii.sqlite
├── requirements.txt

```

## Installation

pip install -r requirements.txt







