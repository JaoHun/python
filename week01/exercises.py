"""
第1周练习题（共10题）
说明：
- 带有 # TODO 的地方需要你补全代码
- 每道题都对应一个Agent开发中的实际场景
- 建议先独立尝试，再对照 solutions.py
- 运行方式：python exercises.py
"""


# ==================== 练习题1：变量与类型转换 ====================
"""
场景：从配置文件读取到的temperature是字符串"0.7"，需要转成数字参与计算
要求：将字符串 temperature_str 转换为浮点数，并打印其2倍的值
"""
def exercise_1():
    temperature_str = "0.7"
    # TODO: 将 temperature_str 转换为浮点数，赋值给 temperature
    temperature = float(temperature_str)
    result = temperature * 2
    print(f"练习题1结果: {result}")
    return result


# ==================== 练习题2：列表操作 ====================
"""
场景：管理对话历史，保留最近的5条消息
要求：如果消息超过5条，删除最旧的消息，然后返回更新后的列表
"""
def exercise_2():
    messages = ["msg1", "msg2", "msg3", "msg4", "msg5", "msg6"]
    # TODO: 如果 messages 长度超过5，删除第一个元素（最旧的）
    message_count = len(messages)
    if len(messages) > 5:
        messages.pop(0)  # pop(0) 删除索引为0的元素，即第一个
    print(f"练习题2结果: {messages}")
    return messages


# ==================== 练习题3：字典操作 ====================
"""
场景：合并默认配置和用户自定义配置
要求：将 user_config 中的值合并到 default_config 中（用户配置优先）
提示：可以用 update 方法，或者遍历 user_config
"""
def exercise_3():
    default_config = {
        "model": "gpt-3.5",
        "temperature": 0.5,
        "max_tokens": 1024
    }
    user_config = {
        "model": "gpt-4",
        "temperature": 0.8
    }
    # TODO: 将 user_config 合并到 default_config 中
    default_config.update(user_config)
    print(f"练习题3结果: {default_config}")
    return default_config


# ==================== 练习题4：字符串格式化 ====================
"""
场景：动态构建系统提示词
要求：根据 model_name 和 language 生成提示词：
      "你是一个由 {model_name} 驱动的AI助手，请用 {language} 回答。"
"""
def exercise_4():
    model_name = "GPT-4"
    language = "中文"
    # TODO: 使用 f-string 拼接提示词
    prompt = None
    print(f"练习题4结果: {prompt}")
    return prompt


# ==================== 练习题5：条件判断 ====================
"""
场景：根据HTTP状态码返回对应的处理策略
要求：
  - 200-299: 返回 "success"
  - 429: 返回 "rate_limited"
  - 500-599: 返回 "server_error"
  - 其他: 返回 "unknown"
"""
def exercise_5(status_code):
    # TODO: 根据 status_code 返回对应的策略字符串
    strategy = None
    print(f"练习题5结果({status_code}): {strategy}")
    return strategy


# ==================== 练习题6：循环与列表推导 ====================
"""
场景：批量处理用户问题，给每个问题加上序号前缀
要求：将 questions 中的每个问题转换为 "[序号] 问题内容" 的格式
提示：可以用 for 循环，也可以尝试列表推导式
"""
def exercise_6():
    questions = ["什么是AI？", "什么是Agent？", "什么是LLM？"]
    # TODO: 生成带序号的问题列表
    numbered_questions = []
    print(f"练习题6结果: {numbered_questions}")
    return numbered_questions


# ==================== 练习题7：文件读写 ====================
"""
场景：将对话记录保存到文件，然后从文件读取最后一条
要求：
  1. 将 lines 写入 "chat_history.txt"（每行一条）
  2. 读取文件，返回最后一行的内容（去掉末尾换行符）
"""
def exercise_7():
    lines = ["用户: 你好", "助手: 你好！", "用户: 谢谢"]
    # TODO: 写入文件并读取最后一行
    last_line = None
    print(f"练习题7结果: {last_line}")
    return last_line


# ==================== 练习题8：异常处理 ====================
"""
场景：安全地读取字典中的嵌套值
要求：从 response 中读取 "choices" -> 0 -> "message" -> "content"
      如果任何一层键不存在，返回 "内容获取失败"
提示：使用 try-except 捕获 KeyError
"""
def exercise_8():
    response = {
        "choices": [
            {"message": {"content": "这是AI的回答"}}
        ]
    }
    # TODO: 安全获取嵌套值，出错时返回 "内容获取失败"
    content = None
    print(f"练习题8结果: {content}")
    return content


# ==================== 练习题9：集合去重与判断 ====================
"""
场景：管理已注册的工具列表，避免重复注册
要求：
  1. 从 tool_list 中去除重复项
  2. 判断 "search" 是否在工具列表中，返回布尔值
"""
def exercise_9():
    tool_list = ["calculator", "search", "weather", "search", "calculator"]
    # TODO: 去重并判断 "search" 是否存在
    has_search = None
    print(f"练习题9结果: 去重后={set(tool_list)}, 是否有search={has_search}")
    return has_search


# ==================== 练习题10：综合应用 ====================
"""
场景：写一个简易的配置加载器
要求：
  1. 函数接收文件路径（文件内容格式：每行 "key=value"）
  2. 返回字典 {key: value}
  3. 如果文件不存在，返回空字典（不抛出异常）
  4. 跳过空行和以 # 开头的注释行
提示：需要结合文件读写、字符串分割、条件判断、异常处理
"""
def exercise_10(file_path):
    # TODO: 实现配置加载器
    config = {}
    print(f"练习题10结果: {config}")
    return config


# ==================== 测试运行 ====================
if __name__ == "__main__":
    print("=" * 50)
    print("开始运行练习题（注意：TODO部分需要你补全代码才能正确运行）")
    print("=" * 50)

    # 为了测试能通过，你可以先运行看看报错，然后补全代码
    try:
        exercise_1()
    except Exception as e:
        print(f"练习题1报错: {e}")

    try:
        exercise_2()
    except Exception as e:
        print(f"练习题2报错: {e}")

    try:
        exercise_3()
    except Exception as e:
        print(f"练习题3报错: {e}")

    try:
        exercise_4()
    except Exception as e:
        print(f"练习题4报错: {e}")

    try:
        exercise_5(200)
        exercise_5(429)
        exercise_5(500)
    except Exception as e:
        print(f"练习题5报错: {e}")

    try:
        exercise_6()
    except Exception as e:
        print(f"练习题6报错: {e}")

    try:
        exercise_7()
    except Exception as e:
        print(f"练习题7报错: {e}")

    try:
        exercise_8()
    except Exception as e:
        print(f"练习题8报错: {e}")

    try:
        exercise_9()
    except Exception as e:
        print(f"练习题9报错: {e}")

    try:
        # 先创建一个测试文件
        with open("test_config.txt", "w", encoding="utf-8") as f:
            f.write("# 这是注释\n")
            f.write("model=gpt-4\n")
            f.write("\n")
            f.write("temperature=0.7\n")
        exercise_10("test_config.txt")
        exercise_10("不存在的文件.txt")
    except Exception as e:
        print(f"练习题10报错: {e}")
