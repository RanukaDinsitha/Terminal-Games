import curses
import random
import time

def main(s):
    curses.curs_set(0)
    s.nodelay(1)
    s.timeout(1)
    h, w = s.getmaxyx()
    p1, p2, bx, by, dx, dy, s1, s2 = h//2-2, h//2-2, w//2, h//2, random.choice([-1,1]), random.choice([-1,1]), 0, 0
    
    while True:
        s.clear()
        k = s.getch()
        if k in [ord('w'), ord('W'), ord('k'), ord('K'), curses.KEY_UP] and p1 > 0: p1 -= 1
        elif k in [ord('s'), ord('S'), ord('j'), ord('J'), curses.KEY_DOWN] and p1 < h-6: p1 += 1
        elif k in [ord('q'), ord('Q'), 27]: break
        
        if by < p2+2 and p2 > 0: p2 -= 1
        elif by > p2+2 and p2 < h-6: p2 += 1
        
        bx, by = bx+dx, by+dy
        if by <= 0 or by >= h-1: dy *= -1
        if bx == 3 and p1 <= by < p1+5: dx, bx = 1, 4
        elif bx == w-4 and p2 <= by < p2+5: dx, bx = -1, w-5
        
        if bx <= 0: s2, bx, by, dx, dy = s2+1, w//2, h//2, 1, random.choice([-1,1])
        elif bx >= w-1: s1, bx, by, dx, dy = s1+1, w//2, h//2, -1, random.choice([-1,1])
        
        try:
            s.addstr(0, w//4, str(s1))
            s.addstr(0, 3*w//4, str(s2))
            for i in range(5): s.addstr(p1+i, 2, '|'); s.addstr(p2+i, w-3, '|')
            s.addstr(int(by), int(bx), 'O')
            for i in range(0, h, 2): s.addstr(i, w//2, '|')
        except: pass
        
        s.refresh()
        time.sleep(0.02)

curses.wrapper(main)