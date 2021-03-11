from utils import data_util, setting_util

# 服务器信息：server_id- server
SERVER_LIST = {}
# 虚拟机信息 vr_id - vr
VR_LIST = {}
# 当前开机服务器：server_id - bool
SERVER_RUN_LIST = {}
# 记录服务器的剩余信息：server_id - rest_server
REST_SERVER_LIST = {}
# 记录服务器上运行的虚拟机信息：server_id - [vr_ids]
SERVER_VR = {}
# 成本费用
SERVER_COST, DAY_COST, TOTAL_COST = 0, 0, 0


# 提取全部天的所有操作
def extract_op_days(day_list):
    op_list = []
    for day in day_list:
        op_list += day.op_list
    return op_list


# 用户对虚拟机操作
# 添加服务器
def add_VR(vr_type, vr_id):
    print()


# 删除服务器
def del_VR(vr_id):
    print()


# 在服务器中分配虚拟机资源
def choose_Server(vr_id):
    vr = VR_LIST[vr_id]
    for rest_server in REST_SERVER_LIST:
        if rest_server.cpu < vr.cpu or rest_server.memory < vr.memory:
            continue
        if vr.is_double:
            print()
        print()
    # 当前所剩没有合适的服务器，需要重新购置服务器。
    # 两种思路，一种是把根据每天的请求来进行每天的决策，进行选择购买的服务器（实现简单）
    # 第二种是需要从全局来看，先算出需要购买哪几个服务器，再根据每天成本均衡进行购买


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
