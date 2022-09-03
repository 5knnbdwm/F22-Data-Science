"""
project_1_1
"""
import pandas as pd

if __name__ == "__main__":
    csv_data = pd.read_csv('national/yob2021.txt')
    print(csv_data)
