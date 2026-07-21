"""
第1周基础语法演示
运行方式：python basics.py
建议：逐行取消注释运行，观察输出结果
"""

# ==================== 1. 变量与类型 ====================

# Agent开发中常见的变量定义
api_key = "sk-abc123"           # 字符串：API密钥
temperature = 0.7               # 浮点数：模型温度参数
max_tokens = 2048               # 整数：最大生成token数
is_streaming = True             # 布尔值：是否流式输出

# 类型转换（经常需要把数字转成字符串拼接）
temperature_str = str(temperature)
print(f"当前温度设置: {temperature_str}")


# ==================== 2. 列表（List）====================
# 用途：存储对话历史、消息记录

messages = [
    "你好",
    "请介绍一下自己",
    "你能做什么？"
]

# 常用操作
messages.append("谢谢")                 # 添加元素
last_message = messages[-1]             # 取最后一个
message_count = len(messages)           # 获取长度
print(f"消息数量: {message_count}, 最后一条: {last_message}")

# 遍历列表（处理批量消息）
for idx, msg in enumerate(messages):
    print(f"[{idx}] {msg}")


# ==================== 3. 字典（Dict）====================
# 用途：存储配置、API参数、JSON响应

config = {
    "model": "gpt-4",
    "api_key": "sk-xxxx",
    "temperature": 0.7,
    "max_tokens": 2048
}

# 常用操作
model_name = config["model"]            # 取值
config["timeout"] = 30                  # 添加新键值对
has_proxy = "proxy" in config           # 判断键是否存在
print(f"使用模型: {model_name}, 配置项数量: {len(config)}")

# 遍历字典（处理API返回的JSON）
for key, value in config.items():
    print(f"  {key} = {value}")


# ==================== 4. 字符串操作 ====================
# 用途：拼接提示词（Prompt）

system_prompt = "你是一个有用的AI助手。"
user_question = "Python的列表怎么使用？"

# 字符串拼接（Agent中非常常用）
full_prompt = f"系统指令: {system_prompt}\n用户问题: {user_question}"
print(full_prompt)

# 字符串分割（处理模型输出）
response = "思考: 用户问的是Python列表\n答案: 列表用方括号定义..."
parts = response.split("\n")
print(f"分割后的行数: {len(parts)}")


# ==================== 5. 条件判断 ====================
# 用途：根据API响应状态做不同处理

status_code = 200

if status_code == 200:
    print("请求成功")
elif status_code == 429:
    print("请求太频繁，需要限流")
elif status_code >= 500:
    print("服务器错误，稍后重试")
else:
    print(f"其他错误: {status_code}")


# ==================== 6. 文件读写 ====================
# 用途：读取配置文件、保存对话记录

# 写文件（保存日志）
with open("log.txt", "w", encoding="utf-8") as f:
    f.write("2024-01-01 10:00: 系统启动\n")
    f.write("2024-01-01 10:05: 收到用户请求\n")

# 读文件（读取配置）
with open("log.txt", "r", encoding="utf-8") as f:
    content = f.read()
    print("日志内容:")
    print(content)

# 逐行读取
with open("log.txt", "r", encoding="utf-8") as f:
    for line in f:
        print(f"行内容: {line.strip()}")


# ==================== 7. 异常处理 ====================
# 用途：处理API调用中的网络错误、超时等

def call_api(config):
    """模拟API调用"""
    if "api_key" not in config:
        raise ValueError("缺少API密钥")
    return {"status": "success", "data": "Hello"}

# 使用try-except捕获异常（Agent开发中必须掌握）
try:
    result = call_api({"api_key": "sk-test"})
    print(f"API返回: {result}")
except ValueError as e:
    print(f"参数错误: {e}")
except Exception as e:
    print(f"未知错误: {e}")
finally:
    print("无论成功与否，这里的代码都会执行（常用于清理资源）")


# ==================== 8. 集合（Set）====================
# 用途：去重、快速判断是否存在

tools = ["计算器", "搜索引擎", "计算器", "天气查询"]  # 有重复
unique_tools = set(tools)
print(f"去重后的工具: {unique_tools}")

# 判断工具是否已注册
if "搜索引擎" in unique_tools:
    print("搜索引擎工具已注册")


# ==================== 9. 综合小例子 ====================
# 模拟一个简单的消息管理器（Agent中核心组件）

class SimpleMemory:
    """简易对话记忆"""
    def __init__(self):
        self.messages = []

    def add(self, role, content):
        """添加一条消息"""
        self.messages.append({"role": role, "content": content})

    def get_all(self):
        """获取所有消息"""
        return self.messages

    def get_last(self, n=1):
        """获取最后n条消息"""
        return self.messages[-n:]

    def clear(self):
        """清空记忆"""
        self.messages = []

# 使用示例
memory = SimpleMemory()
memory.add("user", "你好")
memory.add("assistant", "你好！有什么可以帮你的？")
print(f"当前对话轮数: {len(memory.get_all())}")
