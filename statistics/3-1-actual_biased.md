[Think Stats Chapter 3 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2004.html#toc31) (actual vs. biased)

>> The mean of actual data: 1.024 children under 18 per household. While the mean of childrens' observations: 2.404 
children under 18 per household. In the latter biased sample, we only surveyed children - meaning we excluded all 
households that have 0 children since there's no children to survey. So in the former, our unbiased sample, we see a 
much higher probability for multiple children per household and a 0.0 probability of 0 children per household
under the age of 18.

### Further insights into this question

We're comparing data from two groups. In one group, we analyze this pregnancy dataset provided and see how many children
are in each household. In another group, we survey children and ask how many children are in their family. Note in this
second group, it's impossible to receive a value of 0 because we're asking children - so the minimum value must be 1 
since the child we're surveying is included.

In our BiasedPMF function, when we modify the item in place by multiplying (from a row) the probability of a certain
 number of children in a household by the probability of that outcome occurring, we get a 0 result. We then normalize
 those results and now have a 0% chance that there's 0 children in the household - hence a biased result from only
 surveying children.

!(Children household survey)[../img/children_household_survey.png]

Based on the graph above, we can see a much higher probability (actual data) that nearly half of households from our
 pregnancy dataset have 0 children under the age of 18. However, childrens' observations also think there's more 
 children per households under 18 than the pregnancy dataset shows.

```
resp = nsfg.ReadFemResp()
actual_under_18_per_household = resp.numkdhh # this works!
pmf = thinkstats2.Pmf(actual_under_18_per_household, label="actual")
actual_under_18_per_household.mean()
```

```
def BiasPmf(pmf, label):
    new_pmf = pmf.Copy(label=label) # make a copy of our unbiased pmf data
    for x, p in pmf.Items():
        new_pmf.Mult(x, x) # modifies the item in place
    new_pmf.Normalize() # normalize so sum of probabilities is 1
    return new_pmf
    
biased_pmf = BiasPmf(pmf, label="children's observations")
thinkplot.PrePlot(2)
thinkplot.Pmfs([pmf, biased_pmf])
thinkplot.Show(title="Actual versus Childrens' Observations of Children in Household Under 18", xlabel='children under 18 in household', ylabel='PMF')    
```

```
thinkstats2.Pmf(actual_under_18_per_household).Mean()
BiasPmf(pmf, label="children's observations").Mean()
```