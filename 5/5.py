from collections import defaultdict
import re

P1 = defaultdict(int)
P2 = defaultdict(int)
for line in open("input.txt"):
    x1,y1,x2,y2 = list(map(int, re.compile("\d+").findall(line)))

    dx = x2-x1
    dy = y2-y1

    for i in range(1+max(abs(dx),abs(dy))):
        x = x1+(1 if dx>0 else (-1 if dx<0 else 0))*i
        y = y1+(1 if dy>0 else (-1 if dy<0 else 0))*i
        if dx==0 or dy==0:
            P1[(x,y)] += 1
        P2[(x,y)] += 1

print(len([k for k in P1 if P1[k]>1]))
print(len([k for k in P2 if P2[k]>1])) 