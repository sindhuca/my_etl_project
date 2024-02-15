import pandas as pd

def read_csvfile():
    df = pd.read_csv("etl2py/stationary.csv")
    # print(df)

    read_csvfile.finl = []
    for index,row in df.iterrows():
        var1,var2,var3,var4 = row["PID"],row["PNAME"],row["QTY"],row["PRICE"]
        tupl_data = (var1,var2,var3,var4)
        # print(tupl_data)

        read_csvfile.finl.append(tupl_data)

    # print(read_csvfile.finl)
