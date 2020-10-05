# HW Assignment #6 (Forcasting)
##### By: Jacob Ridlinghafer
###### 10/5/2020




First, I created a boxplot with all data from August- December then I truncated the y axis to find the value where outliers begin I found this to be 335 cfs (Figure 1), I decided I would find a way to ommitt this data from june - august 21st  because the summer is the part most affecting this drought. I grouped these by flow and described by year (code: x=yearly.groupby('year')['flow'].describe()). I found while looking at the table that I could use 2011-2019 but would rather not use data in 2017 and 2019 because they either had too high of a mean or a great standard deviation. I plotted weekly data using these years in a box plot (Figure 2) and saw that the data looks more uniform and compact at a lower flow value. The means of all these years was much too high because we are in a drought so I decided to find a mean quantile # that matched the mean 2020 flow for this period (june - august 21st). I found x3=yearly.groupby('year')['flow'].quantile(0.11).mean() to be extremely close to the mean of 47 cfs. so applied this to every week in the time period and got a nice looking plot that see Figure 3 that matches initially the flows of 40-60 cfs that we saw leading up to the first week of the semester in 2020.

Figure 1: Box plot that that shows portion of graph without outliers for months August - December (all years)

![](assets/Ridlinghafer_HW6-f1f6a827.png)


Figure 2: zoomed in on training period with observed


![](assets/Ridlinghafer_HW6-72b822e2.png)


Figure 3: zoomed in on testing period with observed


![](assets/Ridlinghafer_HW6-f895748d.png)


Figure 3: Weekly prediction using 2011-2019 at the 11 % quantile of those weeks data (2017 and 2018 were ommited because of unpredictable data)


![](assets/Ridlinghafer_HW6-df3944c2.png)


Figure 3: AR model t-1 v t


![](assets/Ridlinghafer_HW6-262ed3a7.png)


Figure 3: Weekly discharge prediction using linear regression


![](assets/Ridlinghafer_HW6-b4cbdd5f.png)






As, for my two-week forcast I utilized the same technique but I had a month extra data so I shifted my data to match that and ommitted June and instead used the period from (august - september 26th). This one was tricky though because no quantile number matched the mean 2020 flow so I useed the lowest I could 0 and found the percent error of quantile 0 and the mean 2020 flow. I found that 1- decimal-percent error to be ~ 0.915 and multiplied this by my 1 week and 2 week quantiles to get 65.57 & 63.93 respectively for my week 1 and 2 forecasts.
