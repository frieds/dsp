[Think Stats Chapter 5 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2006.html#toc50) (blue men)

>> 47,317,422 men in the United States of America are in the height range of 5'10" to 6'1" and therefore fit the 
minimum qualifications to be a part of the Blue Man Group.

```
import scipy.stats

mu = 178
sigma = 7.7
# loc keyword specifices the mean
# scale keyword specifies the standard deviation
# dist is a normal continous random variable object, which we can call methods upon to get more insights
dist = scipy.stats.norm(loc=mu, scale=sigma)
```

Let's convert 5'10" and 6'1 to centimeters
```
inches_in_a_foot = 12
cent_per_inch = 2.54
min_height = (5*inches_in_a_foot+10)*cent_per_inch # cm
max_height = (6*inches_in_a_foot+1)*cent_per_inch # cm
```

Let's find the probability a person is in the height range of 5'10" and 6'1"
```
proportion_blue_men_height = dist.cdf(max_height) - dist.cdf(min_height)
```

Let's multiply our proportion of people between 5'10" and 6'1" by the number of males in the USA
```
# US Population as of 2014
males_in_usa = 138053563

available_blue_men = males_in_usa * proportion_blue_men_height
available_blue_men
```