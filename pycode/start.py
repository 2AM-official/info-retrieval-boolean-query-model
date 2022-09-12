import csv
from search_system import InfoSystem

def main():
    tweet_csv_filename = "../data/tweets.csv"
    list_of_tweets = []
    with open(tweet_csv_filename, "r") as f:
        csv_reader = csv.reader(f, delimiter=",")
        for i, row in enumerate(csv_reader):
            if i == 0:
                continue
            timestamp = int(row[0])
            tweet = str(row[1])
            list_of_tweets.append((timestamp, tweet))
    
    # remove the effect of useless word
    stop_words = ['is', 'a', 'for', 'the', 'of']
    info_system = InfoSystem(list_of_tweets, stop_words)
    query = "neeva & special & his & in"
    results = info_system.process_query(query)

    #return the top 5 most recent tweets instead of a single tweet
    tweets = []
    if len(results) > 0:
        if len(results) < 5:
            for result in results:
                timestamp, tweet = list_of_tweets[result]
                tweets.append(tweet)
                print(timestamp, tweet)
        else:
            for i in range(len(results)-1, len(results)-6, -1):
                timestamp, tweet = list_of_tweets[results[i]]
                tweets.append(tweet)
                print(timestamp, tweet)
    else:
        print("There are no suitable query tweets")
    print("Success!")
    return tweets

if __name__ == "__main__":
    main()