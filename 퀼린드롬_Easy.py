import sys

def make_map():
    m = {}
    m['A'] = 'A'
    m['E'] = '3'
    m['3'] = 'E'
    m['H'] = 'H'
    m['I'] = 'I'
    m['M'] = 'M'
    m['O'] = 'O'
    m['S'] = '2'
    m['2'] = 'S'
    m['T'] = 'T'
    m['U'] = 'U'
    m['V'] = 'V'
    m['W'] = 'W'
    m['X'] = 'X'
    m['Y'] = 'Y'
    m['Z'] = '5'
    m['5'] = 'Z'
    m['b'] = 'd'
    m['d'] = 'b'
    m['i'] = 'i'
    m['l'] = 'l'
    m['m'] = 'm'
    m['n'] = 'n'
    m['o'] = 'o'
    m['p'] = 'q'
    m['q'] = 'p'
    m['r'] = '7'
    m['7'] = 'r'
    m['u'] = 'u'
    m['v'] = 'v'
    m['w'] = 'w'
    m['x'] = 'x'
    m['0'] = '0'
    m['1'] = '1'
    m['8'] = '8'
    return m

def is_small_alpha(c):
    return 'a' <= c <= 'z'

def is_big_alpha(c):
    return 'A' <= c <= 'Z'

def main():
    s = sys.stdin.readline().rstrip('\n')

    m = make_map()
    n = len(s)
    avail = True

    sl_parts = []
    sr_parts = []

    for i in range((n+1) // 2):
        l = s[i]
        r=  s[n - 1 -i]

        ll = [l]
        if is_small_alpha(l):
            ll.append(chr(ord(l) - ord('a') + ord('A')))
        elif is_big_alpha(l):
            ll.append(chr(ord(l) - ord('A') + ord('a')))

        rr = [r]
        if is_small_alpha(r):
            rr.append(chr(ord(r) - ord('a') + ord('A')))
        elif is_big_alpha(r):
            rr.append(chr(ord(r) - ord('A') + ord('a')))
        
        matched = False

        for c in ll:
            if c in m:
                cc = m[c]
                for t in rr:
                    if cc == t:
                        matched = True
                        sl_parts.append(c)
                        if i != n-1-i:
                            sr_parts.append(cc)
                        break
            if matched:
                break
        if not matched:
            avail = False
            break
    if not avail:
        print(-1)
    else:
        result = ''.join(sl_parts) + ''.join(reversed(sr_parts))
        print(result)

main()