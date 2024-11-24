import pandas as pd
import yfinance as yf

# 定義股票代號和時間範圍
symbol = 'TSM'
start = '2024-07-31'
end = '2024-11-22'

# 下載股票數據
stock_df = yf.download(symbol, start, end)[['High', 'Low', 'Close']]

# 定義計算與前一天收盤價相比的漲跌幅和標籤
def calculate_changes_and_label(df):
    # 計算與前一天收盤價相比的漲跌幅百分比
    df['changes'] = df['Close'].pct_change() * 100  # 計算百分比變化
    
    # 根據漲跌幅設置標籤
    def label_change(change):
        if change > 1.5:
            return 1
        elif change < -1.5:
            return -1
        else:
            return 0
    
    # 套用標籤函式
    df['label'] = df['changes'].apply(label_change)
    return df

# 定義計算當天內部最高價和最低價的漲跌幅
def calculate_interior_change(df):
    # 計算當天內部漲跌幅百分比
    df['interior_change'] = (df['High'] - df['Low']) / df['Low'] * 100
    return df

# 使用函式處理數據
result_df = calculate_changes_and_label(stock_df)
result_df = calculate_interior_change(result_df)

# 將結果輸出為 CSV 檔案
output_file_1 = "/Users/chuhsiaochi/Desktop/113-1/text_mining/stock_changes_1.csv"
result_df.to_csv(output_file_1, index=True)

print(f"結果已保存到檔案：{output_file_1}")

# print(result_df)