import pandas as pd

if __name__ == '__main__':
    """读取 excel"""
    filename = "buybackVehicleQualityMaintainTemplate.xlsx"
    xl = pd.ExcelFile(filename)

    df1 = xl.parse("Sheet1")

    print(df1.columns)
    for head in df1.head():
        print(head)

    for index, row in df1.iterrows():
        print(f"Processing row {index} in sheet")
        print(row)

    # print(df1)
    xl.close()