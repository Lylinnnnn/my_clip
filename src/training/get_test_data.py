import pandas as pd

# 文件路径
train_path = '/home/radiance/ego4d_dealt_data/train_output_0104.csv'
test_path = '/home/radiance/ego4d_dealt_data/test_output_0104.csv'

# 读取文件
df_train = pd.read_csv(train_path)
df_test = pd.read_csv(test_path)

# 随机选择80行训练数据和20行测试数据
df_train_sample = df_train.sample(n=8000)
df_test_sample = df_test.sample(n=2000)

# 将抽取的数据保存为新文件
df_train_sample.to_csv('/home/radiance/ego4d_dealt_data/small_train_output_0112.csv', index=False)
df_test_sample.to_csv('/home/radiance/ego4d_dealt_data/small_test_output_0112.csv', index=False)
