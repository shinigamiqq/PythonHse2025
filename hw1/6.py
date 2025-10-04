import re


def get_important_messages(list_messages: list) -> list:

    pattern = re.compile(r"(кр|дедлайн|дз|домашнее задание|контрольная работа)", re.IGNORECASE)
    result = set()
    for msg in list_messages:
        if pattern.search(msg):
            result.add(msg)
    return sorted(result)

exec(input())

