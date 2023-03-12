def time_to_ts(line):
    sh,sm,ss = line.split(':')
    h,m,s = map(int, (sh,sm,ss))
    return h * 60*60 + m * 60 + s

def ts_to_time(ts):
    h = ts // 3600
    m = (ts % 3600) // 60
    s = ts % 60
    return f"{h:02d}:{m:02d}:{s:02d}"

a = time_to_ts(input())
b = time_to_ts(input())
c = time_to_ts(input())

lameround = lambda x: int(x+0.5)

def solve(a,b,c):
    if c < a:
        c += 24 * 3600  # add 24 hours
    return lameround(b + (c - a) / 2) % (24 * 3600)

ans = solve(a,b,c)
print(ts_to_time(ans))