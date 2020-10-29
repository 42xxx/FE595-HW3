import pandas as pd
import numpy as np


# merage all of the files

# for Sharize's txt file.
def txt_file(path):
    f = open(path)  # Sharize
    line = f.read()
    text = line.strip("['").strip("']").split("', '")
    odd = np.arange(-1, 100, 2)
    even = np.arange(0, 100, 2)
    name = []
    for i in even:
        name.append(text[i])
    purpose = []
    for j in odd[1:]:
        purpose.append(text[j])
    dfS = pd.DataFrame(name)
    dfS['Purpose'] = purpose
    dfS.columns = ['Name', 'Purpose']
    return dfS

# for Minghao, Yuwen, Fangchi's csv file
def csv_file(path):
    df = pd.read_csv(path)
    for i in range(len(df['Name'])):
        if df['Name'][i][:4] == 'Name':
            df['Name'][i] = df['Name'][i][5:]
            df['Purpose'][i] = df['Purpose'][i][8:]
    if df.shape[1] == 3:
        df.drop(df.columns[0], axis=1, inplace=True)
    return df


def meragedf(dfName: list):
    df = pd.concat(dfName, axis=0)
    df = df.drop_duplicates()
    df.reset_index(drop=True, inplace=True)
    df.to_csv('./data/combineddf.csv', index=False)
    return df


# output meraged dataframe

if __name__ == "__main__":
    dfS = txt_file("./data/shiraz.txt")
    dfM = csv_file("./data/companies_data.csv")
    dfF = csv_file("./data/A2_result.csv")
    dfY = csv_file("./data/collected_info (1).csv")
    combined_df = meragedf([dfS, dfF, dfM, dfY])
    print(combined_df)
