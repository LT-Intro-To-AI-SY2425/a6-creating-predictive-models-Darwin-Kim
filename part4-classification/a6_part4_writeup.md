# Part 4 - Classification Writeup

After completing `a6_part4.py` answer the following questions

## Questions to answer

1. Comment out the StandardScaler and re-run your test. How accurate is the model? Why is that?

The model is much less accurate, because it is being skewed by the fact that all of the different variables have different ranges

2. How accurate is the model with the StandardScaler? Is this model accurate enough for the given use case? Explain.

Yes, I'd say the model is accurate enough. 

3. Looking at the predicted and actual results, how did the model do? Was there a pattern to the inputs that the model was incorrect about?

Most errors were in the middle of the age range.

4. Would a 34 year old Female who makes 56000 a year buy an SUV according to the model? Remember to scale the data before running it through the model.

According to the modle, no, she will not.