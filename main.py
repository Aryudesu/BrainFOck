from error import NoBracketsError, PointerError
from importFile import file_check


# 文字コードに対応する文字を返す
def getchar(num):
    try:
        return chr(num)
    except Exception:
        return ""


# 対応のインデックス検索
def search_next_index(S, Slen, idx, c):
    co = 0
    cnt = 1 if c == "[" else -1
    ec = "]" if c == "[" else "["
    while True:
        idx += cnt
        if idx < 0 or idx >= Slen:
            raise NoBracketsError()
        if S[idx] == c:
            co += 1
        elif S[idx] == ec:
            if co == 0:
                break
            co -= 1
    return idx


def bf(S):
    Slen = len(S)
    idx = 0
    mem = [0]
    memlen = 1
    ptr = 0
    while idx < Slen:
        if S[idx] == "+":
            mem[ptr] += 1
        elif S[idx] == "-":
            mem[ptr] -= 1
        elif S[idx] == ">":
            ptr += 1
            if ptr == memlen:
                mem.append(0)
                memlen += 1
        elif S[idx] == "<":
            ptr -= 1
            if ptr < 0:
                raise PointerError()
        elif S[idx] == ".":
            print(getchar(mem[ptr]), end="")
        elif S[idx] == ",":
            print("\n Input Char > ", end="")
            mem[ptr] = ord(input()[0])
        elif S[idx] == "[" and mem[ptr] == 0:
            idx = search_next_index(S, Slen, idx, "[")
        elif S[idx] == "]" and mem[ptr]:
            idx = search_next_index(S, Slen, idx, "]")
        idx += 1
    print("")
    return


print("FileName > ", end="")
file_name = input()
file_check(file_name)
f = open(file_name)
S = f.read()
bf(S)
