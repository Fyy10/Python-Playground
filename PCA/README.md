# Principal Component Analysis

This is a python implementation of principal component analysis (PCA) in the field of image searching.

这是主元分析法在图像检索领域的一个python实现。

All of the codes are used for the comprehensive curricular designing in UESTC.

所有的代码都被用于UESTC的综合课程设计。

# Datasets

[CIFAR10](https://www.cs.toronto.edu/~kriz/cifar.html) and [DomainNet](http://ai.bu.edu/M3SDA/) are used in this project.

在这个项目中使用了[CIFAR10](https://www.cs.toronto.edu/~kriz/cifar.html)和[DomainNet](http://ai.bu.edu/M3SDA/)这两个数据集。

# Usage

Install requirements.

安装依赖包。

```shell script
pip install -r requirements.txt
```

To search for similar images, simply type the command below in your terminal.

搜索相似图片时，只需要在终端中输入以下命令。

```shell script
python main.py --filename yourfilename
```

`yourfilename` is the name of your image file in the same directory of `main.py` (suffix included).

`yourfilename`是与`main.py`同一目录中的图片文件名（包含后缀）。

For further information of arguments, please type the following command.

输入以下命令以获得更详细的参数表。

```shell script
python main.py -h
```
