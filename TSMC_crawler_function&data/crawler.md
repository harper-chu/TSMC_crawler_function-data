INTRODUCTION:

本程式使用 Yahoo Finance 提供的股票數據，計算：

1. 與前一天收盤價相比的漲跌幅百分比（changes）。
2. 當天內部最高價與最低價的漲跌幅百分比（interior_change）。
3. 基於漲跌幅百分比的分類標籤（label）。

計算結果將存儲到一個 CSV 文件中，便於後續分析。

FUNCTION:

1. 計算漲跌幅：
   • changes：當天收盤價與前一天收盤價相比的漲跌幅百分比。
   • label：根據漲跌幅設定分類標籤：
   • 漲跌幅 > 1.5 → 1
   • 漲跌幅 < -1.5 → -1
   • -1.5 ≤ 漲跌幅 ≤ 1.5 → 0
2. 計算內部波動幅度：
   • interior_change：當天最高價與最低價的漲跌幅百分比。

ROWS&COLUMNS
輸出的 CSV 文件包含以下欄位：
• High：每日最高價。
• Low：每日最低價。
• Close：每日收盤價。
• changes：與前一天收盤價相比的漲跌幅百分比。
• label：基於漲跌幅的分類標籤。
• interior_change：當天內部最高價與最低價的漲跌幅百分比。
