from collections import OrderedDict

def analyze_text(input_str):
    char_counts = {}
    for char in input_str:
        if not char.isalpha():
            continue
        lower_char = char.lower()
        char_counts[lower_char] = char_counts.get(lower_char, 0) + 1
    sorted_items = sorted(char_counts.items(), key=lambda x: (-x[1], x[0]))
    return OrderedDict(sorted_items)


if __name__ == "__main__":
    print("文本字符频率分析器")
    print("提示: 尝试输入中英文文章片段")
    user_input = input("请输入一段文本：")

    if not user_input:
        print("输入的字符串为空，无法分析。")
    else:
        result = analyze_text(user_input)
        print("字符频率降序排列：")
        for char, count in result.items():
            print(f"'{char}': {count}次")
