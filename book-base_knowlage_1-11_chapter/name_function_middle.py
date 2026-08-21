def get_formatted_name(first, last, middle=""):
    # 将middle位置形参移到末尾，并默认为空 ""
    """生成格式规范的名字"""
    if middle == "":
        full_name = f"{first} {last}"
    else:
        full_name = f"{first} {middle} {last}"
    return full_name.title()
