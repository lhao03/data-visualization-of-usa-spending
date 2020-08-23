# Submission for Hack for the People 2020 

### Why
I wanted to challenge myself and create a project that was not about the environment or climate change. So I picked to target a sociocultural/economic issue and thus I created a data visualization app to help myself and others see how spending on certain categories can impact incarceration rates in the USA.

### How
First you need data for a data visualization, so I went hunting for data. The data I gathered were in all sorts of formats, like csv, excel, or a mix of the both. I spent most of my time cleaning and manipulating data with pandas and pyspark. The data is then visualised with Dash Plotly. Finally I implemented linear regression with a tensorflow model to predict the total incarceration population based on these features: ['total','elementary_and_secondary_edu','higher_edu' ,
            'public_welfare','health_and_hospitals','highways',
            'police','all_other','population_thousands',
            'year','hispanic','white',
            'black','asian','indigneous']. 
 My first model in which I normalised all the features and one-hot encoded the states produced acceptable results, an absolute error of 14000 to 15000, and most total correctional populations are in the 10000 range to 500000 range. However, I was not able to reproduce the same input with user defined values, (I did not know how to normalise and one-hot encode user defined values), so I had to resort to using only user defined values. This lead to an absolute error of about 40000, which is not the best, but I know the reasons behind this increase in error. 

## What I'd do next time
I would use alot more data and use more categorical features such as race, gender, and state politcal affiliation, and this also leads on to my second point that I would one-hot these values. Furthermore I would normalise these values as well. 

### links to data
- [USA Spending](https://state-local-finance-data.taxpolicycenter.org/pages.cfm)
- [USA Race Demographs for 2017 from Census](https://www.governing.com/gov-data/census/state-minority-population-data-estimates.html)
- [USA Incarceration Data](https://www.bjs.gov/)


