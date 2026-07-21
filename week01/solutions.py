"""
第1周练习题参考答案
建议：先独立完成 exercises.py，再对照此文件
"""


# ==================== 练习题1：变量与类型转换 ====================
def exercise_1():
    temperature_str = "0.7"
    temperature = float(temperature_str)  # 字符串转浮点数
    result = temperature * 2
    print(f"练习题1结果: {result}")
    return result


# ==================== 练习题2：列表操作 ====================
def exercise_2():
    messages = ["msg1", "msg2", "msg3", "msg4", "msg5", "msg6"]
    while len(messages) > 5:
        messages.pop(0)  # 删除第一个元素
    # 或者用：messages = messages[-5:]
    print(f"练习题2结果: {messages}")
    return messages


# ==================== 练习题3：字典操作 ====================
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
    default_config.update(user_config)  # 用户配置覆盖默认配置
    print(f"练习题3结果: {default_config}")
    return default_config


# ==================== 练习题4：字符串格式化 ====================
def exercise_4():
    model_name = "GPT-4"
    language = "中文"
    prompt = f"你是一个由 {model_name} 驱动的AI助手，请用 {language} 回答。"
    print(f"练习题4结果: {prompt}")
    return prompt


# ==================== 练习题5：条件判断 ====================
def exercise_5(status_code):
    if 200 <= status_code <= 299:
        strategy = "success"
    elif status_code == 429:
        strategy = "rate_limited"
    elif 500 <= status_code <= 599:
        strategy = "server_error"
    else:
        strategy = "unknown"
    print(f"练习题5结果({status_code}): {strategy}")
    return strategy


# ==================== 练习题6：循环与列表推导 ====================
def exercise_6():
    questions = ["什么是AI？", "什么是Agent？", "什么是LLM？"]
    # 方法1：for循环
    # numbered_questions = []
    # for idx, q in enumerate(questions, 1):
    #     numbered_questions.append(f"[{idx}] {q}")

    # 方法2：列表推导式（推荐）
    numbered_questions = [f"[{idx}] {q}" for idx, q in enumerate(questions, 1)]
    print(f"练习题6结果: {numbered_questions}")
    return numbered_questions


# ==================== 练习题7：文件读写 ====================
def exercise_7():
    lines = ["用户: 你好", "助手: 你好！", "用户: 谢谢"]
    # 写入文件
    with open("chat_history.txt", "w", encoding="utf-8") as f:
        for line in lines:
            f.write(line + "\n")

    # 读取最后一行
    with open("chat_history.txt", "r", encoding="utf-8") as f:
        all_lines = f.readlines()
        last_line = all_lines[-1].strip()

    print(f"练习题7结果: {last_line}")
    return last_line


# ==================== 练习题8：异常处理 ====================
def exercise_8():
    response = {
        "choices": [
            {"message": {"content": "这是AI的回答"}}
        ]
    }
    try:
        content = response["choices"][0]["message"]["content"]
    except (KeyError, IndexError):
        content = "内容获取失败"
    print(f"练习题8结果: {content}")
    return content


# ==================== 练习题9：集合去重与判断 ====================
def exercise_9():
    tool_list = ["calculator", "search", "weather", "search", "calculator"]
    unique_tools = set(tool_list)
    has_search = "search" in unique_tools
    print(f"练习题9结果: 去重后={unique_tools}, 是否有search={has_search}")
    return has_search


# ==================== 练习题10：综合应用 ====================
def exercise_10(file_path):
    config = {}
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line or line.startswith("#"):
                    continue
                if "=" in line:
                    key, value = line.split("=", 1)
                    config[key.strip()] = value.strip()
    except FileNotFoundError:
        pass  # 文件不存在返回空字典
    print(f"练习题10结果: {config}")
    return config


# ==================== 验证所有答案 ====================
if __name__ == "__main__":
    print("=" * 50)
    print("运行参考答案验证")
    print("=" * 50)

    assert exercise_1() == 1.4
    assert exercise_2() == ["msg2", "msg3", "msg4", "msg5", "msg6"]
    assert exercise_3() == {"model": "gpt-4", "temperature": 0.8, "max_tokens": 1024}
    assert exercise_4() == "你是一个由 GPT-4 驱动的AI助手，请用 中文 回答。"
    assert exercise_5(200) == "success"
    assert exercise_5(429) == "rate_limited"
    assert exercise_5(500) == "server_error"
    assert exercise_6() == ["[1] 什么是AI？", "[2] 什么是Agent？", "[3] 什么是LLM？"]
    assert exercise_7() == "用户: 谢谢"
    assert exercise_8() == "这是AI的回答"
    assert exercise_9() == True

    with open("test_config.txt", "w", encoding="utf-8") as f:
        f.write("# 这是注释\n")
        f.write("model=gpt-4\n")
        f.write("\n")
        f.write("temperature=0.7\n")
    assert exercise_10("test_config.txt") == {"model": "gpt-4", "temperature": "0.7"}
    assert exercise_10("不存在的文件.txt") == {}

    print("\n所有测试通过！")
