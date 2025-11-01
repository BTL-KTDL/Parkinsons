import pandas as pd
import numpy as np
import os

# Đọc dữ liệu Excel 
excel_path = "D07 - parkinsons.data.xlsx"
csv_path = "data.csv"

print(" Đọc file Excel...")
df = pd.read_excel(excel_path, sheet_name=1)
print(f" Đã đọc thành công: {df.shape[0]} hàng, {df.shape[1]} cột")

if 'name' in df.columns:
    df = df.drop(columns=['name'])
    print(" Đã loại bỏ cột 'name' (không cần cho phân tích).")

# Xuất ra CSV để nộp
df.to_csv(csv_path, index=False)
print(f" Đã lưu file CSV: {csv_path}")

# Đọc lại CSV để xử lý EDA
df = pd.read_csv(csv_path)
print("\n 5 dòng đầu tiên của dữ liệu:")
print(df.head(), "\n")

# Kích thước và chiều của dữ liệu 
print("a) Kích thước dữ liệu:")
print(" - Số hàng, cột:", df.shape)
print(" - Số chiều:", df.ndim)
print(" - Tổng số ô:", df.size, "\n")

# Kiểu dữ liệu của các thuộc tính
print("b) Kiểu dữ liệu của các thuộc tính:")
print(df.dtypes, "\n")

# Số lượng thực thể theo nhãn
label_col = "status"
if label_col in df.columns:
    print("c) Số lượng thực thể theo nhãn:")
    print(df[label_col].value_counts())
    print("\nTỷ lệ phần trăm mỗi nhãn:")
    print(df[label_col].value_counts(normalize=True).mul(100).round(2))
    print()
else:
    print(" Không tìm thấy cột nhãn 'status'! Kiểm tra lại dữ liệu.\n")

# Thống kê min/max/mean của các cột số
numeric_cols = df.select_dtypes(include=[np.number]).columns
print(f"d) Các cột số ({len(numeric_cols)} cột):\n", list(numeric_cols), "\n")

stats = pd.DataFrame({
    "min": df[numeric_cols].min(),
    "max": df[numeric_cols].max(),
    "mean": df[numeric_cols].mean().round(4)
})
stats_path = "numeric_columns_stats.csv"
stats.to_csv(stats_path)
print(f" Đã lưu thống kê numeric vào {stats_path}")

print("\n 5 dòng đầu tiên của bảng thống kê numeric:")
print(stats.head())

