import nltk
import collections
from boolean import BooleanModel

class InfoSystem():
    def __init__(self, tweets, stop_words):
        if tweets == None:
            raise UserWarning('Corpus should not be none')
        self._stemmer = nltk.stem.PorterStemmer()
        self.tweets = tweets
        self.records = self.preprocess_tweets(stop_words)
        #print(self.records)
    
    def preprocess_tweets(self, stop_words):
        """
        :param stop_words: words that may not effect the query
        :return: a dict of words and its apperaing tweets timestamp
        """
        records = collections.defaultdict(list)
        for timestamp, tweet in self.tweets:
            for word in tweet.split():
                if word in stop_words:
                    continue
                word = self._stemmer.stem(word.lower())
                records[word].append(timestamp)
        return records
    
    def get_appearing_tweets(self, word):
        """
        :return: a list of tweets timestamp containing word
        """
        return [timestamps for timestamps in self.records[word] if timestamps != None]
    
    def process_query(self, query):
        """
        :param query: query want to be searched
        :return: answer
        """
        query = query.replace('(', '( ')
        query = query.replace(')', ' )')
        query = query.replace('!', '! ')
        query = query.split(' ')
        number_of_tweets = [i for i in range(1, len(self.tweets)+1)]

        result_stack = []
        query = collections.deque(self.parse_query(query))
        print(query)
        while query:
            token = query.popleft()
            result = []

            if token != '&' and token != '|' and token != '!':
                token = self._stemmer.stem(token)
                if token in self.records:
                    result = self.get_appearing_tweets(token)
                
            elif token == '&':
                right = result_stack.pop()
                left = result_stack.pop()
                result = BooleanModel.and_operation(left, right)
            
            elif token == '|':
                right = result_stack.pop()
                left = result_stack.pop()
                result = BooleanModel.or_operation(left, right)
            
            elif token == '!':
                right = result_stack.pop()
                result = BooleanModel.not_operation(right, number_of_tweets)
            result_stack.append(result)

        if len(result_stack) != 1:
            return None
        #print(result_stack)
        return result_stack.pop()
    
    def parse_query(self, query):
        """
        use Shunting Yard Algorithm to parse the query
        """
        rank = {}
        rank['!'] = 3
        rank['&'] = 2
        rank['|'] = 1
        rank['('] = 0
        rank[')'] = 0

        result = []
        operator_stack = []

        for token in query:
            if token == '(':
                operator_stack.append(token)
            
            elif token == ')':
                operator = operator_stack.pop()
                while operator != '(':
                    result.append(operator)
                    operator = operator_stack.pop()
            
            elif token in rank:
                if operator_stack:
                    prev_operator = operator_stack[-1]
                    while operator_stack and rank[prev_operator] > rank[token]:
                        result.append(operator_stack.pop())
                        if operator_stack:
                            prev_operator = operator_stack[-1]
                operator_stack.append(token)
            else:
                result.append(token.lower())

        while operator_stack:
            result.append(operator_stack.pop())
        return result
        
