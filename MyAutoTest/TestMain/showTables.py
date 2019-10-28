# @Time    : 2019/8/28 8:56
# @Author  : Libuda
# @FileName: showTables.py
# @Software: PyCharm
from matplotlib import pyplot as plt


class ShowTables:
    """
    测试结果可视化
    """

    def __init__(self):
        # 解决中文乱码
        plt.rcParams['font.sans-serif'] = ['SimHei']

<<<<<<< Updated upstream
    def draw_pie(self, no_test_num, test_pass_num, test_fail_num):
=======
    def draw_pie(self,no_test_num,test_pass_num,test_fail_num):

>>>>>>> Stashed changes
        """
        #饼状图
        # labeldistance，文本的位置离远点有多远，1.1指1.1倍半径的位置
        # autopct，圆里面的文本格式，%3.1f%%表示小数有三位，整数有一位的浮点数
        # shadow，饼是否有阴影
        # startangle，起始角度，0，表示从0开始逆时针转，为第一块。一般选择从90度开始比较好看
        # pctdistance，百分比的text离圆心的距离
        :param data:
        :return:
        """
        plt.title("测 试 结 果")
        labels = ['未测试', '测试通过', '测试未通过']
        colors = ['lightskyblue', 'yellowgreen', 'red']
        explode = (0, 0, 0)
        plt.pie([no_test_num, test_pass_num, test_fail_num], explode=explode, labels=labels, colors=colors,
                labeldistance=1.1, autopct="%2.1f%%", shadow=False, startangle=40, pctdistance=0.6)

        # 设置x,y轴一致
        plt.axis('equal')
        # 图例
        plt.legend()
        plt.show()


if __name__ == "__main__":
    showtables = ShowTables()
    showtables.draw_pie(20, 10, 2)
