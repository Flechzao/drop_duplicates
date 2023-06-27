import argparse
import pandas as pd

# 创建一个命令行参数解析器
parser = argparse.ArgumentParser(description='比较两个Excel文件并根据指定的列名输出新增行')

# 添加命令行参数
parser.add_argument('file1', type=str, help='第一个Excel文件')
parser.add_argument('file2', type=str, help='第二个Excel文件')
parser.add_argument('-c', '--column', type=str, help='要比较的列名', required=True)

# 解析命令行参数
args = parser.parse_args()

# 读取两个Excel文件，将数据加载到数据框中
df1 = pd.read_excel(args.file1)
df2 = pd.read_excel(args.file2)

# 创建一个新的空数据框，用于保存新增行
df_output = pd.DataFrame(columns=df1.columns)

# 遍历df2中的每一行，根据自定义列查找是否在df1中
for index, row in df2.iterrows():
    if row[args.column] not in df1[args.column].values:
        df_output = pd.concat([df_output, pd.DataFrame(row).transpose()], ignore_index=True)

# 将新增行输出到一个新的Excel文件
df_output.to_excel('output.xlsx', index=False)

print("新增行已输出到output.xlsx文件中")
