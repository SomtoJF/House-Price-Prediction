# House Price Prediction
The linear regression model was used to perform the predictions of median home prices [MEDV]
Programmed solely using Python Programming Language.

The project was carried out by;
1. Gathering/collecting the data.
While buliding the model scikitlearn's inbuilt load_boston dataset was used. There wasnt any data cleaning to be done since the data had no null values and/or anomalies.
2. Exploratory Data Analysis in which I used a combination of matplotlib.pyplot and seaborn to plot a correlation heatmap (It is present in the code but commented out) which I used to observe the values which most affected the MEDV.
3. Model Building Using linear regressing algorithm. I fitted the model which i then used to get my 'b' and 'm' values which represent y-intercept and slope respectively.
   
Note that i used the mean_absolute_error (MAE) method for evaluation. The mean absolute error was 4.00 
