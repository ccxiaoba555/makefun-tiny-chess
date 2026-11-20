import json,os,urllib.request as u
H=os.environ["MAKEFUN_ENV_URL"]
B='abcdefgh';T=10**9
def P(p,b):
 q=u.Request(H+p,data=json.dumps(b).encode(),headers={"content-type":"application/json"});return json.load(u.urlopen(q))
Z={'P':100,'N':320,'B':330,'R':500,'Q':900,'K':0}
K=[-33,-31,-18,-14,14,18,31,33]
I=[-17,-16,-15,-1,1,15,16,17]
D=[-17,-15,15,17]
R=[-16,-1,1,16]
def A(b,s,w):
 for d in(15,17):
  t=s-d if w else s+d
  if not t&136 and b[t]==('P' if w else 'p'):return 1
 for d in K+I:
  t=s+d
  if not t&136 and b[t]==(('N' if d in K else'K') if w else('n' if d in K else'k')):return 1
 for d in D+R:
  t=s+d
  while not t&136:
   c=b[t]
   if c!='.':
    if c.isupper()==w and(c.upper() in'BQ' if d in D else c.upper() in'RQ'):return 1
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
    m+=[(s,f,'Q')] if f>>4==(7*w) else[(s,f,'')]
    x=s+2*d
    if(s>>4)==(6-5*w) and b[x]=='.':m.append((s,x,''))
   for y in((15,17) if w else(-15,-17)):
    t=s+y
    if t&136:continue
    o=b[t]
    if o!='.' and o.isupper()!=w:m+=[(s,t,'Q')] if t>>4==(7*w) else[(s,t,'')]
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
 for z in((1,'K',4,6,5),(1,'Q',4,2,3),(0,'k',116,118,117),(0,'q',116,114,115)):
  y,r,k,t,j=z
  if w==bool(y) and r in c and b[j]=='.' and b[t]=='.' and(r in'Kk' or b[k-3]=='.') and not A(b,k,not w) and not A(b,j,not w):m.append((k,t,''))
 return m
def M(b,m,w,c,e):
 n=b[:];f,t,r=m;p=n[f];n[f]='.';n[t]=(r.upper() if w else r.lower()) if r else p
 if p.upper()=='P' and t==e and b[t]=='.':n[t-16 if w else t+16]='.'
 if p.upper()=='K' and abs(t-f)==2:
  x=(119 if t>f else 112) if not w else(7 if t>f else 0);n[(f+t)//2]=n[x];n[x]='.'
 c=''
 if n[4]=='K' and n[7]=='R':c+='K'
 if n[4]=='K' and n[0]=='R':c+='Q'
 if n[116]=='k' and n[119]=='r':c+='k'
 if n[116]=='k' and n[112]=='r':c+='q'
 return n,c,(f+t)//2 if p.upper()=='P' and abs(t-f)==32 else-1
def L(b,w,c,e):
 return[z for m in G(b,w,c,e) for z in[(m,)+M(b,m,w,c,e)] if not A(z[1],z[1].index('K' if w else'k'),not w)]
def E(b):
 s=0
 for q,p in enumerate(b):
  if p=='.':continue
  v=Z[p.upper()];f=q&7;r=q>>4;a=0
  if p.upper()=='P':a=(r if p.isupper() else 7-r)*8
  elif p.upper() in'NB':a=(3-abs(f-3)-abs(r-3))*8
  s+=v+a if p.isupper() else-(v+a)
 return s
N=[0]
def Q(b,w,c,e,a,l):
 N[0]+=1
 if N[0]>25000:raise StopIteration
 s=E(b) if w else-E(b)
 if s>=l:return l
 if s>a:a=s
 for m,n,x,y in L(b,w,c,e):
  if b[m[1]]=='.' and not(b[m[0]].upper()=='P' and m[1]==e):continue
  v=-Q(n,not w,x,y,-l,-a)
  if v>=l:return l
  if v>a:a=v
 return a
def S(b,w,c,e,d,a,l):
 N[0]+=1
 if N[0]>25000:raise StopIteration
 if d==0:return Q(b,w,c,e,a,l)
 m=L(b,w,c,e)
 if not m:return-99999 if A(b,b.index('K' if w else'k'),not w) else 0
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
 w=g[1]=='w';c=g[2] if g[2]!='-' else'';e=-1
 if g[3]!='-':e=(int(g[3][1])-1)*16+B.index(g[3][0])
 return b,w,c,e
def C(f,l):
 b,w,c,e=F(f);o=l[0];t=-T;N[0]=0
 for v in l:
  a=B.index(v[0])+(int(v[1])-1)*16;d=B.index(v[2])+(int(v[3])-1)*16;r=v[4:]
  n,x,y=M(b,(a,d,r),w,c,e)
  if A(n,n.index('K' if w else'k'),not w):continue
  try:s=-S(n,not w,x,y,2,-T,T)
  except StopIteration:s=-99998
  if s>t:t=s;o=v
 return o
while 1:
 g=P('/game',{})
 if g['status']=='done':break
 while g['status']=='your_move':g=P('/move',{'game':g['game'],'move':C(g['fen'],g['legal_moves'])})
