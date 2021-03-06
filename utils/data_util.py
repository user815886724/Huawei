# 自定义服务器类
class Server:
    def __init__(self, server_str):
        server_str = server_str.strip().strip('(').strip(')')
        (server_model, cpu, memory, hardware_cost, day_cost) = server_str.split(",")
        self.server_model = server_model
        self.cpu = int(cpu)
        self.A_cpu = int(cpu) / 2
        self.B_cpu = int(cpu) / 2
        self.memory = int(memory)
        self.A_memory = int(memory) / 2
        self.B_memory = int(memory) / 2
        self.hardware_cost = int(hardware_cost)
        self.day_cost = int(day_cost)


# 自定义虚拟机类
class Virtual_Server:
    def __init__(self, vr_str):
        vr_str = vr_str.strip().strip('(').strip(')')
        (vr_name, cpu, memory, is_double) = vr_str.split(",")
        self.vr_name = vr_name
        self.cpu = int(cpu)
        self.memory = int(memory)
        self.is_double = bool(is_double)


# 自定义天数存放操作类
class Days_Op:
    def __init__(self, op_list):
        self.op_list = op_list
        self.size = len(op_list)


# 自定义操作类
class Operators:
    def __init__(self, op_str):
        op_str = op_str.strip().strip('(').strip(')')
        try:
            (operator, vr, vr_id) = op_str.split(",")
            self.operator = operator.strip()
            self.vr = vr.strip()
            self.vr_id = int(vr_id)
        except ValueError:
            (operator, vr_id) = op_str.split(",")
            self.operator = operator.strip()
            self.vr_id = int(vr_id)


# 从txt中读取服务器信息，返回服务器列表
def get_server_txt(file, server_size):
    server_list = []
    for i in range(server_size):
        server_str = file.readline()
        server = Server(server_str)
        server_list.append(server)
    return server_list


# 从txt中获得虚拟服务器的信息，返回虚拟服务器的列表和具体需要返回的类型对应的查找列表
def get_vr_txt(file, vr_size):
    vr_type_dict = {}
    vr_list = []
    for i in range(vr_size):
        vr_str = file.readline()
        vr = Virtual_Server(vr_str)
        vr_list.append(vr)
        vr_type_dict[vr.vr_name] = vr
    return vr_list, vr_type_dict


# 从txt中获得每天的操作序列，返回操作列表
def get_day_txt(file, day_size):
    days = []
    for i in range(day_size):
        op_list = []
        op_size = int(file.readline())
        for j in range(op_size):
            op_str = file.readline()
            op = Operators(op_str)
            op_list.append(op)
        day = Days_Op(op_list)
        days.append(day)
    return days


# 扩容的策略
def expansion_info(expansion_size):
    print("(purchase, %d)" % expansion_size)


# 购买信息输出
def buy_info(server_name, server_num):
    print("(%s, %d)" % (server_name, server_num))


# 转移虚拟机个数信息
def migrate_size_info(migrate_size):
    print("(migration, %d)" % migrate_size)


# 转移虚拟机信息
def migrate_info(vr_id, server_id, server_node=None):
    if server_node is None:
        print("(%s, %s)" % (vr_id, server_id))
    else:
        print("(%s, %s, %s)" % (vr_id, server_id, server_node))


# 部署当前请求的虚拟机
def deploy_vr_info(server_id, server_node=None):
    if server_node is None:
        print("(%s)" % server_id)
    else:
        print("(%s, %s)" % (server_id, server_node))

