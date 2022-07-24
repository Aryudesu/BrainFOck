def getchar(num):
    try:
        return chr(num)
    except Exception:
        return ""


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
        elif S[idx] == ".":
            print(getchar(mem[ptr]), end="")
        elif S[idx] == ",":
            print("\n Input Char > ", end="")
            mem[ptr] = ord(input()[0])
        elif S[idx] == "[":
            if mem[ptr] == 0:
                c = 0
                while True:
                    idx += 1
                    if idx == Slen:
                        print("Error")
                        return
                    if S[idx] == "[":
                        c += 1
                    elif S[idx] == "]":
                        if c == 0:
                            break
                        c -= 1
        elif S[idx] == "]":
            if mem[ptr]:
                c = 0
                while True:
                    idx -= 1
                    if idx < 0:
                        print("Error")
                        return
                    if S[idx] == "]":
                        c += 1
                    elif S[idx] == "[":
                        if c == 0:
                            break
                        c -= 1
        idx += 1
    print("")
    return


FileName = input()
S = ""
with open(FileName) as f:
    S = f.read()
bf(S)
