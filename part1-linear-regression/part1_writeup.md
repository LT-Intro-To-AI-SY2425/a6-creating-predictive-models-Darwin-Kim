# Part 1 - Linear Regression Writeup

After completing `a6_part1.py` answer the following questions

## Questions to answer

1. What is the r squared value?  What does this say about this linear regression model?

The r^2 value is a value that takes the distance between each point on the graph and the line of best fit, sprinkles it with math fairy dust, and spits out a value between -1 and 1. This tells you the correalation between the two models given that the line of best fit is in the optimal format for the graph(y=mx=b for linear relationships, y=a(x-h)^2+k for exponential, etc).

2. According to your model, what is the predicted systolic blood pressure for a person who is 42 years old?

According to the model, 137mmHg.

3. How accurate do you think this model's predictions are?  Do you think this model is accurate enough to reliably predict someone's blood pressure based on their age?  Why or why not?  And if not, what could improve the model?

I have a suspiscion that it could be improved by considering more variables, since the human body is normally more complex than plug in your age and get a value. However I understand that this is a coding class and is therefore not at all related to medical practice in any way, so for our use, yes, this data is acceptable.