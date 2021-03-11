from utils import data_util, setting_util

# 当前购买的服务器信息：server_id - server
SERVER_LIST = {}
# 当前用户存在的虚拟机信息 vr_id - vr
VR_LIST = {}
# 当前开机服务器：server_id - bool
SERVER_RUN_LIST = {}
# 记录服务器的剩余信息：server_id - rest_server
REST_SERVER_LIST = {}
# 记录服务器上运行的虚拟机信息：server_id - [vr_ids]
SERVER_VR = {}
# 成本费用
SERVER_COST, DAY_COST, TOTAL_COST = 0, 0, 0

# 虚拟机根据类型查找对应的虚拟机机型（主要为了减少每次查询所需的遍历时间） vr_type - vr
VR_TYPE_DICT = {}


# 提取全部天的所有操作
def extract_op_days(day_list):
    op_list = []
    for day in day_list:
        op_list += day.op_list
    return op_list


# 用户对虚拟机操作
# 添加服务器
def add_VR(server_list, vr_list, vr_type, vr_id):
    vr = VR_TYPE_DICT[vr_type]
    # 选择所部署的服务器ID
    server_id = choose_Server(vr)

    # 服务器减去当前虚拟机的消耗放入 REST_SERVER_LIST
    server = REST_SERVER_LIST[server_id]
    server.cpu -= vr.cpu
    server.memory -= vr.memory
    if vr.is_double:
        server.A_cpu -= int(vr.cpu / 2)
        server.B_cpu -= int(vr.cpu / 2)
        server.A_memory -= int(vr.A_memory / 2)
        server.B_memory -= int(vr.B_memory / 2)
    REST_SERVER_LIST[server_id] = server

    # 虚拟机列表中增加虚拟机
    VR_LIST[vr_id] = vr

    # 在SERVER_VR中增加使用关系
    if server_id not in SERVER_VR:
        SERVER_VR[server_id] = []
    vr_ids = SERVER_VR[server_id]
    vr_ids.append(vr_id)
    SERVER_VR[server_id] = vr_ids


# 删除服务器
def del_VR(vr_id):
    # TODO 实施删除的具体操作方案

    # 从 VR_LIST 删除虚拟机
    VR_LIST.pop(vr_id)
    # 如果当前的服务器没有部署虚拟机，则关闭-更改SERVER_RUN_LIST的状态
    free_server = SERVER_VR.keys() ^ SERVER_RUN_LIST.keys()
    for server_id in free_server:
        SERVER_RUN_LIST[server_id] = False


# 在服务器中分配虚拟机资源
def choose_Server(vr):
    # 先从当前的剩余服务器列表中查找可部署
    for rest_server in REST_SERVER_LIST:
        if rest_server.cpu < vr.cpu or rest_server.memory < vr.memory:
            continue
        if vr.is_double:
            if rest_server.A_cpu < int(vr.cpu / 2) or rest_server.B_cpu < int(vr.cpu / 2) or rest_server.A_memory < int(
                    vr.memory / 2) or rest_server.B_memory < int(vr.memory / 2):
                continue

    # TODO 核心选择方案
    # 当前所剩没有合适的服务器，需要重新购置服务器。
    # 两种思路，
    # 第一种是把根据每天的请求来进行每天的决策，进行选择购买的服务器（实现简单）贪心算法
    # 第二种是需要从全局来看，先算出需要购买哪几个服务器，再根据每天成本均衡进行购买

    # TODO 返回选择的服务器ID：server_id
    return 0


# 暂时模拟输入逐行读取txt文本
def process_data_txt(data_path):
    f = open(data_path)
    line = f.readline()
    index = 0
    # 循环读取文件
    while line:
        # 第一个输入的是服务器类型
        if index == 0:
            server_size = int(line.strip())
            server_list = data_util.get_server_txt(file=f, server_size=server_size)
        # 第二个输入的为虚拟机类型
        elif index == 1:
            vr_size = int(line.strip())
            vr_list, vr_type_dict = data_util.get_vr_txt(file=f, vr_size=vr_size)
            VR_TYPE_DICT.update(vr_type_dict)
        # 第三个输入用户操作行为
        elif index == 2:
            day_size = int(line.strip())
            day_list = data_util.get_day_txt(file=f, day_size=day_size)
        line = f.readline()
        index += 1

    # TODO 核心算法处理

    # 关闭文件流
    f.close()


if __name__ == "__main__":
    process_data_txt(setting_util.DATA_PATH)
