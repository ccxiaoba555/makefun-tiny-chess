import json,os,time,random,zlib,urllib.request as u
T=10**9
H=os.getenv("MAKEFUN_ENV_URL")
def P(p,b):
 q=u.Request(H+p,data=json.dumps(b).encode());return json.load(u.urlopen(q))
Z=dict(P=100,N=320,B=330,R=500,Q=900,K=0)
K=[-33,-31,-18,-14,14,18,31,33]
I=[-17,-16,-15,-1,1,15,16,17]
D=[-17,-15,15,17]
R=[-16,-1,1,16]
TT={}
HI={}
KI={}
KS=[4,116]
random.seed(20261122)
ZR=[random.getrandbits(64) for _ in range(1550)]
PI={p:i for i,p in enumerate('PNBRQKpnbrqk')}
ZH=0
BK='f49a5bd2d404d8dde5d4fcc7bcb1c3474c45b1c3688654b7b5e61dd2d1e294c90ae4d6cb5946d4c68c38b4d1e2baccd2c3d504e95af3e565fd40g1f3c3f198c1g5c500fdh7h60b95ccf1d3ded25fe7e5e32aa0b1c3cce0b1e7e594a813b1c3ea871fg1f33328cab8c615be0cg1f3157cc9g1f3e5eda9g1f3f3721eg1f3ed406ce4g3b34d0fb1c3b47351f1c44b8ad2g1f3922507b8d75e8e17h2h35244f8e2e3c865b5f1c40480aae2e4ab42fbc8e6075800g1f3def7d5b8d7c0ea13a2a3a9472db1c31686f5c1f45e9622d1b3236caec4d5a130dde1g187f3d5d7d5962705b1d2ef54d4c4d51880cae6d5c1262cc3e4664983e2e3bbf9c2d5d4c6b987c4d5673c86d2d39be59be7e54d6f6db1c362a57cb8c6'
TM=0
PM=[0,0,0,0,0,0,0,0,50,50,50,50,50,50,50,50,10,10,20,30,30,20,10,10,5,5,10,25,25,10,5,5,0,0,0,20,20,0,0,0,5,-5,-10,0,0,-10,-5,5,5,10,10,-20,-20,10,10,5,0,0,0,0,0,0,0,0]
NM=[-50,-40,-30,-30,-30,-30,-40,-50,-40,-20,0,0,0,0,-20,-40,-30,0,10,15,15,10,0,-30,-30,5,15,20,20,15,5,-30,-30,0,15,20,20,15,0,-30,-30,5,10,15,15,10,5,-30,-40,-20,0,5,5,0,-20,-40,-50,-40,-30,-30,-30,-30,-40,-50]
NE=[-50,-40,-30,-30,-30,-30,-40,-50,-40,-20,0,0,0,0,-20,-40,-30,0,10,15,15,10,0,-30,-30,5,15,20,20,15,5,-30,-30,0,15,20,20,15,0,-30,-30,5,10,15,15,10,5,-30,-40,-20,0,5,5,0,-20,-40,-50,-40,-20,-30,-30,-20,-40,-50]
BM=[-20,-10,-10,-10,-10,-10,-10,-20,-10,0,0,0,0,0,0,-10,-10,0,5,10,10,5,0,-10,-10,5,5,10,10,5,5,-10,-10,0,10,10,10,10,0,-10,-10,10,10,10,10,10,10,-10,-10,5,0,0,0,0,5,-10,-20,-10,-10,-10,-10,-10,-10,-20]
RM=[0,0,0,0,0,0,0,0,5,10,10,10,10,10,10,5,-5,0,0,0,0,0,0,-5,-5,0,0,0,0,0,0,-5,-5,0,0,0,0,0,0,-5,-5,0,0,0,0,0,0,-5,-5,0,0,0,0,0,0,-5,0,0,0,5,5,0,0,0]
QM=[-20,-10,-10,-5,-5,-10,-10,-20,-10,0,0,0,0,0,0,-10,-10,0,5,5,5,5,0,-10,-5,0,5,5,5,5,0,-5,0,0,5,5,5,5,0,-5,-10,5,5,5,5,5,0,-10,-10,0,5,0,0,0,0,-10,-20,-10,-10,-5,-5,-10,-10,-20]
KM=[-30,-40,-40,-50,-50,-40,-40,-30,-30,-40,-40,-50,-50,-40,-40,-30,-30,-40,-40,-50,-50,-40,-40,-30,-30,-40,-40,-50,-50,-40,-40,-30,-20,-30,-30,-40,-40,-30,-30,-20,-10,-20,-20,-20,-20,-20,-20,-10,20,20,0,0,0,0,20,20,20,30,10,0,0,10,30,20]
KE=[-50,-40,-30,-20,-20,-30,-40,-50,-30,-20,-10,0,0,-10,-20,-30,-30,-10,20,30,30,20,-10,-30,-30,-10,30,40,40,30,-10,-30,-30,-10,30,40,40,30,-10,-30,-30,-10,20,30,30,20,-10,-30,-30,-30,0,0,0,0,-30,-30,-50,-30,-30,-30,-30,-30,-30,-50]
VT=dict(P=(PM,PM,82,94,0),N=(NM,NE,337,281,1),B=(BM,BM,365,297,1),R=(RM,RM,477,512,2),Q=(QM,QM,1025,936,4),K=(KM,KE,0,0,0))
J=lambda q,w:((7-(q>>4))if w else(q>>4))*8+(q&7)
MG=EG=PH=UB=VB=0
def A(b,s,w):
 n1='N' if w else'n';k1='K' if w else'k';d1='BQ' if w else'bq';r1='RQ' if w else'rq'
 for d in(15,17):
  t=s-d if w else s+d
  if not t&136 and b[t]=='Pp'[not w]:return 1
 for d in K+I:
  t=s+d
  if not t&136 and b[t]==(n1 if d in K else k1):return 1
 for d in D+R:
  t=s+d
  while not t&136:
   c=b[t]
   if c!='.':
    if c in(d1 if d in D else r1):return 1
    break
   t+=d
 return 0
def G(b,w,c,e,z=0):
 m=[]
 for s,p in enumerate(b):
  if p=='.':continue
  n=ord(p);u=n<91
  if u!=w:continue
  q=n if u else n-32
  if q==80:
   d=32*w-16;f=s+d
   if not z and not f&136 and b[f]=='.':
    m+=[(s,f,'Q')] if f>>4==7*w else[(s,f,'')]
    x=s+2*d
    if s>>4==6-5*w and b[x]=='.':m.append((s,x,''))
   for y in(15,17)if w else(-15,-17):
    t=s+y
    if t&136:continue
    o=b[t]
    if o!='.' and o.isupper()!=w:m+=[(s,t,'Q')] if t>>4==7*w else[(s,t,'')]
    elif t==e:m.append((s,t,''))
  elif q==78 or q==75:
   for d in K if q==78 else I:
    t=s+d
    if not t&136 and(b[t]=='.' and not z or b[t]!='.' and b[t].isupper()!=w):m.append((s,t,''))
  else:
   for d in D if q==66 else R if q==82 else D+R:
    t=s+d
    while not t&136:
     o=b[t]
     if o=='.':
      if not z:m.append((s,t,''))
     else:
      if o.isupper()!=w:m.append((s,t,''))
      break
     t+=d
 for y,r,k,t,j in((1,'K',4,6,5),(1,'Q',4,2,3),(0,'k',116,118,117),(0,'q',116,114,115)):
  if not z and w==y and r in c and b[j]=='.' and b[t]=='.' and(r in'Kk' or b[k-3]=='.') and not A(b,k,not w) and not A(b,j,not w) and not A(b,t,not w):m.append((k,t,''))
 return m
def MK(b,m,w,c,e):
 global ZH,MG,EG,PH,UB,VB
 f,t,r=m;p=b[f];cap=b[t];epc='.'
 b[f]='.';b[t]=(r.upper() if w else r.lower()) if r else p
 if p.upper()=='P' and t==e and cap=='.':
  x=t+16-32*w;epc=b[x];b[x]='.'
 rf=-1
 if p.upper()=='K' and abs(t-f)==2:
  rf=(119 if t>f else 112)if not w else(7 if t>f else 0);b[(f+t)//2]=b[rf];b[rf]='.'
  KS[not w]=t
 elif p.upper()=='K':KS[not w]=t
 nc=(('K' if b[7]=='R' else'')+('Q' if b[0]=='R' else'') if b[4]=='K' else'')+(('k' if b[119]=='r' else'')+('q' if b[112]=='r' else'') if b[116]=='k' else'')
 ne=(f+t)//2 if p.upper()=='P' and abs(t-f)==32 else-1
 h=ZR[1536]^ZR[PI[p]*128+f]^ZR[PI[b[t]]*128+t]
 if cap!='.':h^=ZR[PI[cap]*128+t]
 if epc!='.':h^=ZR[PI[epc]*128+t+16-32*w]
 if rf>=0:
  q=(f+t)//2;rk='R' if w else 'r';h^=ZR[PI[rk]*128+rf]^ZR[PI[rk]*128+q]
 for i,k in enumerate('KQkq'):
  if (k in c)!=(k in nc):h^=ZR[1537+i]
 if e>=0:h^=ZR[1541+(e&7)]
 if ne>=0:h^=ZR[1541+(ne&7)]
 ZH^=h
 mt,et,vm,ve,pp=VT[p.upper()]
 fi=J(f,w);ti=J(t,w)
 s=1 if w else-1
 if r:
  nt,net,nvm,nve,npp=VT[r.upper()]
  dg=s*((nvm+nt[ti])-(vm+mt[fi]));de=s*((nve+net[ti])-(ve+et[fi]));dp=npp
 else:
  dg=s*(mt[ti]-mt[fi]);de=s*(et[ti]-et[fi]);dp=0
 du=dv=0
 if cap!='.':
  ct,cet,cvm,cve,cpp=VT[cap.upper()]
  ci=J(t,not w)
  dg+=s*(cvm+ct[ci]);de+=s*(cve+cet[ci]);dp-=cpp
  if cap in'Bb':
   if w:dv=-1
   else:du=-1
 if epc!='.':
  xi=J(x,not w)
  dg+=s*(82+PM[xi]);de+=s*(94+PM[xi])
 if rf>=0:
  q=(f+t)//2
  qi=J(q,w);ri=J(rf,w)
  dg+=s*(RM[qi]-RM[ri]);de+=s*(RM[qi]-RM[ri])
 if r in('B','b'):
  if w:du+=1
  else:dv+=1
 if du:
  d=25*((UB+du==2)-(UB==2));dg+=d;de+=d;UB+=du
 if dv:
  d=-25*((VB+dv==2)-(VB==2));dg+=d;de+=d;VB+=dv
 MG+=dg;EG+=de;PH+=dp
 return (p,cap,epc,rf,nc,ne,c,e,h,dg,de,dp,du,dv)
def UN(b,m,w,u):
 global ZH,MG,EG,PH,UB,VB
 f,t,r=m;p,cap,epc,rf,nc,ne,oc,oe,hd,dg,de,dp,du,dv=u
 ZH^=hd;MG-=dg;EG-=de;PH-=dp;UB-=du;VB-=dv
 b[f]=p;b[t]=cap
 if epc!='.':b[t+16-32*w]=epc
 if rf>=0:b[rf]=b[(f+t)//2];b[(f+t)//2]='.'
 if p.upper()=='K':KS[not w]=f
def E(b):
 p=min(PH,24);return (MG*p+EG*(24-p))//24
N=[0,0]
def Q(b,w,c,e,a,l,q,ply):
 N[0]+=1
 if N[0]>N[1] or(N[0]&1023==0 and time.time()>TM):raise StopIteration
 chk=A(b,KS[not w],not w)
 if not chk:
  s=E(b) if w else-E(b)
  if s>=l:return l
  if s>a:a=s
  if q<=0:return a
 legal=0
 for m in G(b,w,c,e,not chk):
  if not chk and b[m[1]]=='.' and m[1]!=e:continue
  u=MK(b,m,w,c,e)
  if A(b,KS[not w],not w):UN(b,m,w,u);continue
  legal+=1
  v=-Q(b,not w,u[4],u[5],-l,-a,q-1,ply+1)
  UN(b,m,w,u)
  if v>=l:return l
  if v>a:a=v
 if chk and not legal:return -99999+ply
 return a
def S(b,w,c,e,d,a,l,ply):
 N[0]+=1
 if N[0]>N[1] or(N[0]&1023==0 and time.time()>TM):raise StopIteration
 if d<=0:return Q(b,w,c,e,a,l,2,ply)
 key=(ZH,d)
 h=TT.get(key)
 a0,l0=a,l
 if h is not None:
  sc,fl,bm=h
  if fl==0:return sc
  if fl==1 and sc>=l:return sc
  if fl==2 and sc<=a:return sc
 chk=A(b,KS[not w],not w)
 if chk:d+=1
 m=G(b,w,c,e)
 def ord(mv):
  cap=b[mv[1]]
  s=0
  if h is not None and mv==h[2]:s=10**7
  elif cap!='.':s=Z[cap.upper()]*10-Z[b[mv[0]].upper()]
  elif mv in KI.get(ply,()):s=9000
  else:s=HI.get((b[mv[0]],mv[1]),0)
  return -s
 m.sort(key=ord)
 t=-T;bm=None;legal=0
 for i,mv in enumerate(m):
  cap=b[mv[1]]!='.' or mv[1]==e
  u=MK(b,mv,w,c,e)
  if A(b,KS[not w],not w):UN(b,mv,w,u);continue
  legal+=1
  if i==0:
   v=-S(b,not w,u[4],u[5],d-1,-l,-a,ply+1)
  elif i>=3 and d>=3 and not chk and not cap and not mv[2]:
   v=-S(b,not w,u[4],u[5],d-2,-a-1,-a,ply+1)
   if v>a:v=-S(b,not w,u[4],u[5],d-1,-l,-a,ply+1)
  else:
   v=-S(b,not w,u[4],u[5],d-1,-a-1,-a,ply+1)
   if a<v<l:v=-S(b,not w,u[4],u[5],d-1,-l,-a,ply+1)
  UN(b,mv,w,u)
  if v>t:t=v;bm=mv
  if t>a:a=t
  if a>=l:break
 if not legal:
  return -99999+ply if chk else 0
 fl=2 if t<=a0 else 1 if t>=l0 else 0
 TT[key]=(t,fl,bm)
 if t>=l and b[bm[1]]=='.':
  KI.setdefault(ply,[]).insert(0,bm);KI[ply]=KI[ply][:2]
  HI[(b[bm[0]],bm[1])]=HI.get((b[bm[0]],bm[1]),0)+d*d
 return t
def F(f):
 global ZH,MG,EG,PH,UB,VB
 b=['.']*128;g=f.split()
 for r,row in enumerate(g[0].split('/')):
  x=0
  for o in row:
   if o.isdigit():x+=int(o)
   else:b[(7-r)*16+x]=o;x+=1
 w=g[1]=='w';c=''if g[2]=='-'else g[2];e=-1
 if g[3]!='-':e=(int(g[3][1])-1)*16+ord(g[3][0])-97
 KS[0]=b.index('K');KS[1]=b.index('k')
 ZH=0;MG=0;EG=0;PH=0;UB=0;VB=0
 for q,p in enumerate(b):
  if p!='.':
   ZH^=ZR[PI[p]*128+q]
   mt,et,vm,ve,pp=VT[p.upper()];u=p.isupper()
   i=J(q,u)
   s=1 if u else-1
   MG+=s*(vm+mt[i]);EG+=s*(ve+et[i]);PH+=pp
   UB+=p=='B';VB+=p=='b'
 MG+=25*(UB==2);EG+=25*(UB==2);MG-=25*(VB==2);EG-=25*(VB==2)
 if not w:ZH^=ZR[1536]
 for i,k in enumerate('KQkq'):
  if k in c:ZH^=ZR[1537+i]
 if e>=0:ZH^=ZR[1541+(e&7)]
 return b,w,c,e
def C(f,l):
 global TM
 b,w,c,e=F(f);o=l[0];sc={}
 k='%06x'%(zlib.crc32((''.join(b)+('w' if w else 'b')+c+str(e)).encode())&0xffffff)
 i=BK.find(k)
 if i>=0 and i%10==0:
  v=BK[i+6:i+10]
  if v in l:return v
 TS=time.time();TM=TS+9
 for d in(1,2,3,4,5,6):
  if d==6 and time.time()-TS>1.5:break
  N[1]=(25e3,60e3,150e3,400e3,600e3,1200000)[d-1];N[0]=0;u=o;h=-T;ok=1
  l2=sorted(l,key=lambda v:-sc.get(v,0))
  for k,v in enumerate(l2):
   a=ord(v[0])-97+(int(v[1])-1)*16;j=ord(v[2])-97+(int(v[3])-1)*16;r=v[4:]
   uu=MK(b,(a,j,r),w,c,e)
   if A(b,KS[not w],not w):UN(b,(a,j,r),w,uu);continue
   try:
    if k==0:s=-S(b,not w,uu[4],uu[5],d-1,-T,-h,1)
    else:
     s=-S(b,not w,uu[4],uu[5],d-1,-h-1,-h,1)
     if s>h:s=-S(b,not w,uu[4],uu[5],d-1,-T,-h,1)
   except StopIteration:ok=0;UN(b,(a,j,r),w,uu);break
   UN(b,(a,j,r),w,uu)
   sc[v]=s
   if s>h:h=s;u=v
  if ok:o=u
  else:break
 return o
while(g:=P('/game',{}))['status']!='done':
 while g['status']=='your_move':g['move']=C(g['fen'],g['legal_moves']);g=P('/move',g)
