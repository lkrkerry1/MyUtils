import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt

plt.rcParams["font.sans-serif"] = ["SimHei"]  # 用来正常显示中文标签
plt.rcParams["axes.unicode_minus"] = False  # 用来正常显示负号


def read_files():
    filelst = os.listdir("./scores/")
    datalst = {}
    col = []
    for file in filelst:
        df = pd.read_csv(os.path.join("./scores/", file), encoding="utf-8")
        print(df)
        arr = np.array(df)
        datalst[file[:-4]] = arr.tolist()
        col = df.columns.to_list()
    return col, datalst


def display(x_data, y_data, filename, yname):

    plt.plot(
        x_data, y_data, "b*--", alpha=0.5, linewidth=1, label="acc"
    )  #'bo-'表示蓝色实线，数据点实心原点标注
    ## plot中参数的含义分别是横轴值，纵轴值，线的形状（'s'方块,'o'实心圆点，'*'五角星   ...，颜色，透明度,线的宽度和标签 ，

    plt.legend()  # 显示上面的label
    plt.xlabel("月考序号")  # x_label
    plt.ylabel(yname)  # y_label

    # plt.ylim(-1,1)#仅设置y轴坐标范围
    plt.savefig(filename)
    plt.close()


def main():
    col, flst = read_files()
    for key, red in flst.items():
        reduced_list = zip(*red)
        reduced_list = tuple(reduced_list)
        print(reduced_list)
        for i in range(1, len(reduced_list)):
            display(
                reduced_list[0],
                reduced_list[i],
                os.path.join("./output/", "{}{}.png".format(key, col[i])),
                col[i],
            )


if __name__ == "__main__":
    main()
