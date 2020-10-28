import pandas as pd


def find_common(path, n):
    combined_df = pd.read_csv(path)
    voc = ' '.join(text for text in combined_df['Purpose'])
    voc = voc.split()
    counts = pd.value_counts(voc).sort_values(ascending=False)
    print(counts[:n])


if __name__ == "__main__":
    find_common("./data/combineddf.csv", 10)
