def serializer(email_addr: str):
    # check if input is full email address or just username
    if "@" in email_addr:
        email_addr_cleaned = email_addr.split("@")
        username = email_addr_cleaned[0]
    else:
        username = email_addr
    # cleanup username (removes dots)
    username = username.replace(".", "")

    return username


def generate_dot_trick(username: str):
    if len(username) <= 1:
        # stop recursion at the last character of the user name
        # 11 is the length of "X@gmail.com"
        yield username
    else:
        first, rest = username[0], username[1:]
        for sub in generate_dot_trick(rest):
            # with and without the dot after the first char
            yield first + '.' + sub
            yield first + sub


def add_suffix(lst: list, extra: bool = False):
    for s in lst:
        yield f"{s}@gmail.com"
        if extra:
            yield f"{s}@googlemail.com"


def save_to_file(lst: list):
    with open("result.txt", "w+") as f:
        for s in lst:
            f.write(f"{s}\n")


def print_result(lst: list):
    result_string = ""
    for s in lst:
        result_string += f"\n{s}"
    return result_string
