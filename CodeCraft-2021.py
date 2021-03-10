from utils import data_util, setting_util


# 暂时模拟输入逐行读取txt文本
def process_data_txt(data_path):
    f = open(data_path)
    line = f.readline()
    index = 0
    # 循环读取文件
    while line:
        # 第一个输入的是服务器的数量
        if index == 0:
            server_size = int(line.strip())
            server_list = data_util.get_server_txt(file=f, server_size=server_size)
        elif index == 1:
            vr_size = int(line.strip())
            vr_list = data_util.get_vr_txt(file=f, vr_size=vr_size)
        elif index == 2:
            day_size = int(line.strip())
            day_list = data_util.get_day_txt(file=f, day_size=day_size)
        line = f.readline()
        index += 1

    # 核心算法处理


    # 关闭文件流
    f.close()


if __name__ == "__main__":
    process_data_txt(setting_util.DATA_PATH)
