
def Pandas_Read_Excel(path_file):
    ''' Pandas 读取Excel
        需要安装openpyxl模块
        是否使用第一行作为表头
        :param: xlsx文件路径
        :return: DataFrame矩阵
    '''
    from pandas import read_excel
    df = read_excel(path_file, header=None) # 不使用表头！！
    # print(df.shape)      # 显示行数和列数
    return df

def 区间统计(data):
    ''' 统计多维数组内元素，在指定区间内的频数
    :param: 多维数组
    :print: 区间统计数据结果
    :return: 【横轴list】, 【对应频数List】
    '''
    import pandas as pd
    import numpy as np
    # data = np.random.random((10,10))  #[0,1)随机数组
    data_1 = data.flatten()             #变一维数组；因pd.cut参数要求
    sum_data = pd.cut(data_1, bins=[x for x in np.arange(0, 1.1, 0.1)])
        # Range(0, 1.0, 0.1)            参数必须是int
        # np.arange(0, 1.1, 0.1)        小数列表;注意右侧不含！
    print(sum_data.value_counts())      #输出区间+对应频数 二维数组计数？
    #横轴标签List
    Xlabels = [str(round(i,1)) + '-' + str(round(i+0.1,1)) for i in np.arange(0, 1, 0.1)]
        #需要round()保留1位小数
    #y轴=对应频数list
    Ycount = sum_data.value_counts().values
    return Xlabels, Ycount
def BarとPie_Plot(Ycount, Xlables):
    '''绘图
    :param Ycount:
    :param Xlables:
    :return:
    '''
    from matplotlib import pyplot as plt
    plt.figure(figsize=(18, 8))  # 设定窗口大小
    plt.subplot(1, 2, 1)
    plt.title("Bar")
    plt.bar(Xlables, Ycount)    #柱形图
    plt.subplot(1,2,2)
    plt.pie(Ycount, labels=Xlables, shadow=True) #饼图
    plt.title("Pie Chart")
    # plt.savefig('./fig/test.png')    #保存图片
    plt.show()

if __name__ == '__main__':
    m1_df = Pandas_Read_Excel("D:\Documents\GitHub\GH01\m1.xlsx")
    print("m1数组尺寸", m1_df.shape)
    m2_df = Pandas_Read_Excel("D:\Documents\GitHub\GH01\m2.xlsx")
    print("m2数组尺寸", m2_df.shape)
    df_mulp = m1_df.dot(m2_df)      #矩阵乘法
    print("相乘后矩阵尺寸", df_mulp.shape)
    # df_mulp.to_csv('res.csv')     # 另存为CSV

    nmp = m1_df.to_numpy()     #DataFrame转为numpy.ndarray
    x,y = 区间统计(nmp)         #获取x,y数据
    BarとPie_Plot(y, x)        #绘图