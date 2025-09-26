import sys

def main():
    tokens = sys.stdin.read().split()
    case_no = 1

    for n in tokens:
        if n == '0':
            break
        while True:
            if len(n) % 2 == 1:
                break
            
            sb = []

            ok = True
            for i in range(0, len(n), 2):
                cnt_ch = n[i]
                dig_ch = n[i+1]

                if not cnt_ch.isdigit() or not dig_ch.isdigit():
                    ok = False
                    break
                cnt = int(cnt_ch)
                if cnt == 0:
                    ok = False
                    break
                sb.append(dig_ch * cnt)
            if not ok:
                break
            prev = "".join(sb)

            if prev == n:
                break
            
            n = prev
        print(f"Test {case_no}: {n}")
        case_no += 1

main()