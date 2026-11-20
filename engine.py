import json,os,urllib.request as u
T=10**9
H=os.getenv("MAKEFUN_ENV_URL")
def P(p,b):
 q=u.Request(H+p,data=json.dumps(b).encode());return json.load(u.urlopen(q))
Z=dict(P=100,N=320,B=330,R=500,Q=900,K=0)
K=[-33,-31,-18,-14,14,18,31,33]
I=[-17,-16,-15,-1,1,15,16,17]
D=[-17,-15,15,17]
R=[-16,-1,1,16]
def A(b,s,w):
 for d in(15,17):
  t=s-d if w else s+d
  if not t&136 and b[t]=='Pp'[not w]:return 1
 for d in K+I:
  t=s+d
  if not t&136 and b[t].upper()==('N' if d in K else'K')and b[t].isupper()==w:return 1
 for d in D+R:
  t=s+d
  while not t&136:
   c=b[t]
   if c!='.':
    if c.isupper()==w and(u:=c.upper())in('BQ' if d in D else'RQ'):return 1
    break
   t+=d
 return 0
def G(b,w,c,e):
 m=[]
 for s,p in enumerate(b):
  if p=='.' or p.isupper()!=w:continue
  q=p.upper()
  if q=='P':
   d=32*w-16;f=s+d
   if not f&136 and b[f]=='.':
    m+=[(s,f,'Q')] if f>>4==7*w else[(s,f,'')]
    x=s+2*d
    if s>>4==6-5*w and b[x]=='.':m.append((s,x,''))
   for y in(15,17)if w else(-15,-17):
    t=s+y
    if t&136:continue
    o=b[t]
    if o!='.' and o.isupper()!=w:m+=[(s,t,'Q')] if t>>4==7*w else[(s,t,'')]
    elif t==e:m.append((s,t,''))
  elif q in'NK':
   for d in K if q=='N' else I:
    t=s+d
    if not t&136 and(b[t]=='.' or b[t].isupper()!=w):m.append((s,t,''))
  else:
   for d in D if q=='B' else R if q=='R' else D+R:
    t=s+d
    while not t&136:
     o=b[t]
     if o=='.':m.append((s,t,''))
     else:
      if o.isupper()!=w:m.append((s,t,''))
      break
     t+=d
 for y,r,k,t,j in((1,'K',4,6,5),(1,'Q',4,2,3),(0,'k',116,118,117),(0,'q',116,114,115)):
  if w==y and r in c and b[j]=='.' and b[t]=='.' and(r in'Kk' or b[k-3]=='.') and not A(b,k,not w) and not A(b,j,not w) and not A(b,t,not w):m.append((k,t,''))
 return m
def M(b,m,w,c,e):
 n=b[:];f,t,r=m;p=n[f];n[f]='.';n[t]=(r.upper() if w else r.lower()) if r else p
 if p.upper()=='P' and t==e and b[t]=='.':n[t+16-32*w]='.'
 if p.upper()=='K' and abs(t-f)==2:
  x=(119 if t>f else 112)if not w else(7 if t>f else 0);n[(f+t)//2]=n[x];n[x]='.'
 c=(('K' if n[7]=='R' else'')+('Q' if n[0]=='R' else'') if n[4]=='K' else'')+(('k' if n[119]=='r' else'')+('q' if n[112]=='r' else'') if n[116]=='k' else'')
 return n,c,(f+t)//2 if p.upper()=='P' and abs(t-f)==32 else-1
def L(b,w,c,e):
 return[z for m in G(b,w,c,e) for z in[(m,)+M(b,m,w,c,e)] if not A(z[1],z[1].index('Kk'[not w]),not w)]
def E(b):
 s=0;u=0;v=0
 for q,p in enumerate(b):
  if p=='.':continue
  y=p.upper();x=Z[y];f=q&7;r=q>>4;a=0
  if y=='P':a=(r if p.isupper() else 7-r)*8
  elif y in'NB':a=24-8*abs(f-3)-8*abs(r-3)
  elif y in'RQ':a=12-4*abs(f-3)-4*abs(r-3)+(12 if y=='R' and r==(6 if p.isupper() else 1)else 0)
  u+=p=='B';v+=p=='b'
  s+=x+a if p.isupper() else-x-a
 return s+25*((u==2)-(v==2))
N=[0,0]
def S(b,w,c,e,d,a,l):
 N[0]+=1+(d==0)
 if N[0]>N[1]:raise StopIteration
 if d<=0:
  s=E(b) if w else-E(b)
  if s>=l:return l
  if s>a:a=s
  if d==-2:return a
  for m,n,x,y in L(b,w,c,e):
   if b[m[1]]=='.' and m[1]!=e:continue
   v=-S(n,not w,x,y,d-1,-l,-a)
   if v>=l:return l
   if v>a:a=v
  return a
 m=L(b,w,c,e)
 if not m:return-99999 if A(b,b.index('Kk'[not w]),not w) else 0
 m.sort(key=lambda x:-Z.get(b[x[0][1]].upper(),0))
 t=-T
 for o,n,x,y in m:
  v=-S(n,not w,x,y,d-1,-l,-a)
  if v>t:t=v
  if t>a:a=t
  if a>=l:break
 return t
def F(f):
 b=['.']*128;g=f.split()
 for r,row in enumerate(g[0].split('/')):
  x=0
  for o in row:
   if o.isdigit():x+=int(o)
   else:b[(7-r)*16+x]=o;x+=1
 w=g[1]=='w';c=''if g[2]=='-'else g[2];e=-1
 if g[3]!='-':e=(int(g[3][1])-1)*16+ord(g[3][0])-97
 return b,w,c,e
def C(f,l):
 b,w,c,e=F(f);o=l[0]
 for d in(1,2,3):
  N[1]=(12e3,2e4,4e4)[d-1];N[0]=0;u=o;h=-T;ok=1
  for v in l:
   a=ord(v[0])-97+(int(v[1])-1)*16;j=ord(v[2])-97+(int(v[3])-1)*16;r=v[4:]
   n,x,y=M(b,(a,j,r),w,c,e)
   if A(n,n.index('Kk'[not w]),not w):continue
   try:s=-S(n,not w,x,y,d,-T,T)
   except StopIteration:ok=0;break
   if s>h:h=s;u=v
  if ok:o=u
  if not ok or(d==2 and N[0]>8000):break
 return o
while(g:=P('/game',{}))['status']!='done':
 while g['status']=='your_move':g['move']=C(g['fen'],g['legal_moves']);g=P('/move',g)
