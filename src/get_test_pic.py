import shutil
import os

# 源 CSV 文件路径
csv_file_path = '/home/radiance/ego4d_dealt_data/medium_train_output_0104.csv'

# 目标文件夹路径
destination_folder = '/home/radiance/ego4d_dealt_data/medium_data_test_0112'

# 确保目标文件夹存在
if not os.path.exists(destination_folder):
    os.makedirs(destination_folder)

# 读取 CSV 文件并处理每一行
with open(csv_file_path, 'r') as file:
    for line in file:
        # 从每行中提取文件路径
        file_path = line.split(',')[0].strip()
        if os.path.exists(file_path):
            # 提取文件名
            file_name = os.path.basename(file_path)
            # 构建目标文件路径
            destination_file_path = os.path.join(destination_folder, file_name)
            # 复制文件
            shutil.copy(file_path, destination_file_path)

print("文件复制完成。")
