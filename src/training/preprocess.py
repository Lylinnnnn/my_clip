import pandas as pd
from sklearn.model_selection import train_test_split
import re
import csv
import os


def clean_and_save_csv(input_file, output_file, encoding='utf-8', replacement_char=' '):
    # 定义一个正则表达式来匹配特定的非英文字符
    pattern = re.compile(r'#C |#O |# |@ |#unsure')

    base_dir = '/home/radiance/ego4d_dealt_data/frame_output_dir_1'

    with open(input_file, 'rb') as infile, open(output_file, 'w', encoding=encoding, newline='') as outfile:
        writer = csv.writer(outfile)
        for line_number, line in enumerate(infile, 1):
            try:
                decoded_line = line.decode(encoding)
                # 使用正则表达式替换特定字符
                cleaned_line = pattern.sub(replacement_char, decoded_line)

                # 移除开头和结尾的空格
                cleaned_line = cleaned_line.strip()

                # 使用csv模块来处理每一行
                reader = csv.reader([cleaned_line])
                for row in reader:
                    # 检查行是否为空
                    if not row:
                        continue

                    # 检查字段数量是否正确
                    expected_field_count = 2
                    if len(row) != expected_field_count:
                        continue

                    # 检查filepath和title是否缺失
                    filepath, title = row
                    if not filepath.strip() or not title.strip():
                        continue

                    # 检查文件是否存在
                    full_path = os.path.join(base_dir, filepath.strip())
                    if not os.path.exists(full_path):
                        continue

                    writer.writerow(row)

            except UnicodeDecodeError as e:
                corrected_line = (line[:e.start].decode(encoding) + replacement_char +
                                  line[e.end:].decode(encoding))
                print(f"Error in line {line_number}, position {e.start}: {line[e.start:e.end]}")
                writer.writerow([corrected_line])


def clean_and_split_csv(input_file, output_file_cleaned, output_file_train, output_file_test, train_size=0.8, random_state=42):
    # 首先清理 CSV 文件
    clean_and_save_csv(input_file, output_file_cleaned)

    # 读取清理后的 CSV 文件
    df = pd.read_csv(output_file_cleaned, sep=',')

    # 删除缺失值
    df = df.dropna()

    # 划分为训练集和测试集
    df_train, df_test = train_test_split(df, train_size=train_size, random_state=random_state)

    # 保存训练集和测试集
    df_train.to_csv(output_file_train, index=False)
    df_test.to_csv(output_file_test, index=False)

# 替换为您的文件路径
input_path = '/home/radiance/ego4d_dealt_data/dataset.csv'
output_cleaned_path = '/home/radiance/ego4d_dealt_data/dataset_cleaned_0104.csv'
output_train_path = '/home/radiance/ego4d_dealt_data/train_output_0104.csv'
output_test_path = '/home/radiance/ego4d_dealt_data/test_output_0104.csv'


clean_and_split_csv(input_path, output_cleaned_path, output_train_path, output_test_path)
