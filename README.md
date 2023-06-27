# drop_duplicates
compares two Excel files and outputs the newly added rows based on a specified column name.

# 功能介绍
用于比较两个 Excel 文件，并根据指定的列名输出新增行

# 使用方法
在运行脚本之前，您可以按照以下步骤使用它：

1.确保已安装以下Python库：pip install pandas。
2.将上述代码保存到一个名为drop_duplicates.py的文件中。
3.运行脚本 python compare_excel.py <file1> <file2> -c <column>  示例：python compare_excel.py file1.xlsx file2.xlsx -c "ProductID"

  <file1>: 要比较的第一个 Excel 文件
  
  <file2>: 要比较的第二个 Excel 文件
  
  <column>: 要在两个文件中比较的列名
