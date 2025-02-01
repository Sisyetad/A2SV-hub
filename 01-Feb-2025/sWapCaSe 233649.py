# Problem: sWapCaSe - https://www.hackerrank.com/challenges/swap-case/problem?isFullScreen=true

def swap_case(s):
    result=""
    for i in s:
        if ord(i)>=ord('a') and ord(i)<ord('z'):
            result+=chr(ord(i)-32)
        elif ord(i)>=ord('A') and ord(i)<=ord('Z'):
            result+=chr(ord(i)+32)
        else:
            result+=i
    return result

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)