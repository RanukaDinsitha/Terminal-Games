import sys,time,random
C,R=60,30
def clr():sys.stdout.write('\033[2J\033[H');sys.stdout.flush()
def rnd(sx,sy,t,h,ax,ay,sc):
 b=[[' ']*(C+2)for _ in range(R+2)]
 b[0][0],b[0][C+1],b[R+1][0],b[R+1][C+1]='┌','┐','└','┘'
 for i in range(1,C+1):b[0][i]=b[R+1][i]='─'
 for i in range(1,R+1):b[i][0]=b[i][C+1]='│'
 ss=' '+str(sc)+' ';sp=(C-len(ss))//2+1
 for i,c in enumerate(ss):b[0][sp+i]=c
 for r in range(1,R+1):
  for c in range(1,C+1):b[r][c]='·'
 if ax>=0:b[ay+1][ax+1]='❤'
 i=t
 while i!=h:b[sy[i]+1][sx[i]+1]='▓';i=(i+1)&1023
 b[sy[h]+1][sx[h]+1]='▓'
 clr()
 for row in b:sys.stdout.write(''.join(row)+'\n')
 sys.stdout.flush()
def go():
 a=["  ____                        ___                 _ "," / ___| __ _ _ __ ___   ___  / _ \__   _____ _ __| |","| |  _ / _` | '_ ` _ \ / _ \| | | \ \ / / _ \ '__| |","| |_| | (_| | | | | | |  __/| |_| |\ V /  __/ |  |_|"," \____|\__,_|_| |_| |_|\___| \___/  \_/ \___|_|  (_)"]
 s=(R-len(a))//2+1
 for i,l in enumerate(a):sys.stdout.write(f'\033[{s+i};{max(0,(C-len(l))//2+1)}H{l}')
 sys.stdout.flush()
def gi():
 try:
  import msvcrt
  if msvcrt.kbhit():
   c=msvcrt.getch()
   if c in(b'\xe0',b'\x00'):
    c2=msvcrt.getch()
    return{b'H':'UP',b'P':'DOWN',b'M':'RIGHT',b'K':'LEFT'}.get(c2)
   return c.decode('utf-8',errors='ignore')
 except:
  import select
  if select.select([sys.stdin],[],[],0)[0]:
   c=sys.stdin.read(1)
   if c=='\x1b':
    if select.select([sys.stdin],[],[],0.01)[0]:
     if sys.stdin.read(1)=='[':
      if select.select([sys.stdin],[],[],0.01)[0]:
       return{'A':'UP','B':'DOWN','C':'RIGHT','D':'LEFT'}.get(sys.stdin.read(1),'ESC')
    return'ESC'
   return c
sys.stdout.write('\033[?25l');sys.stdout.flush()
try:
 import msvcrt;import os;os.system('');os.system(f'mode con: cols={C+3} lines={R+4}')
except:
 import tty,termios;fd=sys.stdin.fileno();o=termios.tcgetattr(fd);tty.setcbreak(fd)
try:
 while 1:
  sx,sy=[0]*1024,[0]*1024;t=h=0;sx[0],sy[0]=C//2,R//2;xd,yd=1,0;ax=ay=-1;ov=sc=0
  while not ov:
   if ax<0:
    while 1:
     ax,ay=random.randint(0,C-1),random.randint(0,R-1);i=t;ok=1
     while i!=h:
      if sx[i]==ax and sy[i]==ay:ok=0;break
      i=(i+1)&1023
     if ok:break
     ax=-1
   nh=(h+1)&1023;sx[nh]=(sx[h]+xd)%C;sy[nh]=(sy[h]+yd)%R;h=nh
   if sx[h]==ax and sy[h]==ay:ax=-1;sc+=1
   else:t=(t+1)&1023
   i=t
   while i!=h:
    if sx[i]==sx[h]and sy[i]==sy[h]:ov=1;break
    i=(i+1)&1023
   rnd(sx,sy,t,h,ax,ay,sc)
   if ov:
    go()
    while 1:
     time.sleep(0.1)
     if gi():break
    break
   time.sleep(5.0/60.0);c=gi()
   if c:
    if c=='UP'and yd!=1:xd,yd=0,-1
    elif c=='DOWN'and yd!=-1:xd,yd=0,1
    elif c=='RIGHT'and xd!=-1:xd,yd=1,0
    elif c=='LEFT'and xd!=1:xd,yd=-1,0
    elif c in('ESC','q'):raise KeyboardInterrupt
    elif c=='h'and xd!=1:xd,yd=-1,0
    elif c=='l'and xd!=-1:xd,yd=1,0
    elif c=='j'and yd!=-1:xd,yd=0,1
    elif c=='k'and yd!=1:xd,yd=0,-1
    elif c=='a'and xd!=1:xd,yd=-1,0
    elif c=='d'and xd!=-1:xd,yd=1,0
    elif c=='s'and yd!=-1:xd,yd=0,1
    elif c=='w'and yd!=1:xd,yd=0,-1
except KeyboardInterrupt:pass
finally:
 sys.stdout.write('\033[?25h');sys.stdout.flush()
 try:termios.tcsetattr(fd,termios.TCSADRAIN,o)
 except:pass