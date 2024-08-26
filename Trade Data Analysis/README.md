In this script we compare same type of data, namely import volumes for EU 27, from two different sources, A and B.

Source A: First we retrieve data from an EU comission API. It's weekly a data and the week numbers (the only type of date indication available through an API) are assigned 
according to an agricultural marketing year (Week 1 is the beggining of July). To be able to compare it with source B, we turn data into monthly and change week numbers 
to a calendar year. Then data gets stored into a dataframe. 

Source B: We retrieve monthly data from a database and store into a second dataframe. 

Then we perform merging, and pair relevant products from both dataframes to display them on charts to explore the correlation (or the absence of it). 
