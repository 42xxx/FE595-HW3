import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer


def best_worst_idea(path, n):
    combined_df = pd.read_csv(path)
    sentiment = []
    analyzer = SentimentIntensityAnalyzer()
    for k in combined_df["Purpose"]:
        vs = analyzer.polarity_scores(k)
        sentiment.append(vs["compound"])
    combined_df['sentiment'] = sentiment
    sen_rank = combined_df.sort_values('sentiment', ascending=False)
    best_purp = sen_rank[:n]['Purpose']
    worst_purp = sen_rank[-n:]['Purpose']
    print("the best business idea is", '\n', best_purp, '\n')
    print("the worst business idea is", '\n', worst_purp)


if __name__ == "__main__":
    best_worst_idea("./data/combineddf.csv", 1)
