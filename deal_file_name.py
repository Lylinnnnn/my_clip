import os
import csv

# CSV 文件路径
csv_file_path = 'small_train_output_0112.csv'
# 修改后的 CSV 文件路径
modified_csv_file_path = 'modified_small_train_output_0112.csv'

# 替换路径
old_path_prefix = '/home/radiance/ego4d_dealt_data/frame_output_dir_1'
new_path_prefix = '/root/autodl-tmp'

# 用于存储修改后的行
modified_rows = []

# 读取 CSV 文件
with open(csv_file_path, 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        # 替换文件路径
        new_path = row[0].replace(old_path_prefix, new_path_prefix)
        row[0] = new_path

        # 检查新路径下的文件是否存在
        if os.path.exists(new_path):
            # 如果存在，则保留整行数据
            modified_rows.append(row)

# 写入修改后的 CSV 文件
with open(modified_csv_file_path, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(modified_rows)

print("CSV 文件处理完成。")
