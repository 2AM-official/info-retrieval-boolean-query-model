# info-retrieval-boolean-query-model
Boolean Query Model for Information Retrieval in Python

run the code:
1. cd in pycode floder (or it cannot find the data)
2. run the start.py 
3. change the query in main function and check the code
4. change the stop_words to avoid the affect of some useless words for example 'a, the'

I solve this problem by using Shunting Yard Algorithm and built a easy information retrieval boolean query model

Idea:
1. Preprocess the input tweets data: split by space, change to lowercase, use nltk.stem to stem the word
2. Build a dictionary(key: word in tweets, val: timestamps of the tweets containing the word
3. Preprocess the query: apply **Shunting Yard Algorithm** to the input query and output the needed query
4. Process the query by implementing different ways to handle '&','|' and '!'
5. Get the result tweets' timestamps and find the top 5 most recent tweets, print and add to the output
6. Return the output