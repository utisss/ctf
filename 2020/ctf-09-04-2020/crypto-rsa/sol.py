# Endless Emails
from Crypto.Util.number import bytes_to_long, getPrime, long_to_bytes
import sage.all
from sage.arith.misc import crt

def RSA_encrypt(message):
    m = bytes_to_long(message)
    p = getPrime(1024)
    q = getPrime(1024)
    N = p * q
    e = 3
    c = pow(m, e, N)
    return N, e, c

n0 = 21535950278723542143495990305825384015385025846174689596808070552536195719915468911283189871461399776000803953073051637596669500657410805414359255448669540375729192345833152764312984404661486243716865034936571136687575182585206009930815358042714283969552328241982191294399192739563543598176027528099424119455992073104581807533865115931979189677108352168441610628076271085852566528292097846644761081307664593795096740309064217446262415981352755524662454529025158837320742183902126953525785707875187552144834834939288139584061262569859778639880001346196086994751188200834384743894621008900135427741197181203734737693559
e0 = 3
c0 = 11879753323708489085590043579646570901470646583560165748483945773940620329163177832355499681559100679715422367003124493960616742230522564277910155619527439211689739352658929531879859374021801430418545524226922474547347765121130764086689392119222118130354112613

n1 = 14206567819243706983107444331503055165509129821796220757463336994584394961080745451872052383121740276611530959893561877499636808085776473093147555283143805633063801846228161664804657271952313877702616983443555163168143316807079843348216083624470672074324345223206716474677186792048606556854944849031647010112712033677597525425233691946215150509647781646982576721037541384598084382333508714850633280099265812640053412218476763713689809608524352062811751729936573317840860693200952041533235865650810759775919167375944782597900812871563000385274796507429738904477843560133320101837109785159215135777069895794224649321919
e1 = 3
c1 = 11879753323708489085590043579646570901470646583560165748483945773940620329163177832355499681559100679715422367003124493960616742230522564277910155619527439211689739352658929531879859374021801430418545524226922474547347765121130764086689392119222118130354112613

n2 = 14923835646673941499176456436121306274827978582315653014899184323114540406777556711250941612645623508743934198168798191957052416353156606113009435607516509607885915598175713512938673985156210514593603073685511867861815040267514827681124457004283306266539193791061802316836713951994850775022828583450830284051043174330083146725818170448015364558368900345428426919462343176120698404793245096839494654167207341490907502083610932829316324980685765610754291807692066484746124036811531932488373397980152526629363751332139330898406917293710295390396310638077902727593852521288644561324412428726593491247603481532708327538201
e2 = 3
c2 = 11879753323708489085590043579646570901470646583560165748483945773940620329163177832355499681559100679715422367003124493960616742230522564277910155619527439211689739352658929531879859374021801430418545524226922474547347765121130764086689392119222118130354112613


x = crt([c0, c1, c2], [n0, n1, n2])
print(long_to_bytes(x.nth_root(3)))