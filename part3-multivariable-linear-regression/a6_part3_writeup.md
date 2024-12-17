# Part 3 - Multivariable Linear Regression Writeup

After completing `a6_part3.py` answer the following questions

## Questions to answer

1. What is the R Squared coefficient for your model? What does that mean about the model in relation to your data?

The R squared value is .86 . This tells me the correlation between the two x values combined and the resulting y value.

2. Is your model accurate? Why or why not?

Yes. The R squared value is well above the threshhold of .75, meaning the model is considered to be very accurate.

3. What does the model predict a 10-year-old car with 89000 miles is worth? What about a car that is 20 years old with 150000 miles?

For a ten year old car with 89,000 miles, the prediction is $8990.
For a 20 year old car with 150,000 miles, the prediction is $1064.

4. You may notice that some of your predicted results are negative. This is occurring when the value of age and the mileage of the car are very high. Why do you think this is happening?

Because the car is unrealistically old or has an unrealistic number of miles, meaning that the price will be unrealistic. For instance, for a 10 year old car, the price becomes negative when the milage reaches 252,000. This is far above the dataset, which could account for this lack of data.  