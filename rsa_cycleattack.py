from math import prod
import itertools
from Crypto.Util.number import long_to_bytes
from sympy import isprime

# From the itertools documentation/example
def powerset(iterable):
    "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)
    return itertools.chain.from_iterable(itertools.combinations(s, r) for r in range(len(s) + 1))

# From factordb
factors = [2, 3, 5, 17, 257, 641, 65537, 274177, 2424833, 6700417, 67280421310721, 1238926361552897,
           59649589127497217, 5704689200685129054721,
           7455602825647884208337395736200454918783366342657, (2 ** 256 + 1) // 1238926361552897,
           (2 ** 512 + 1) // 18078591766524236008555392315198157702078226558764001281]
assert 2 ** 1025 - 2 == prod(factors)

C = []
for ps in powerset(factors):
    v = prod(ps) + 1
    if isprime(v):
        C.append(prod(ps) + 1)
Ξ = prod(C)

e = 65537
n = 19432641663970228602454613256929114093476416053442925475633254245656442084676980241826420384564272629134502497370061822076575747111463173201148542655045316278398090385068205171950436581955137869549446126341817834795747752514975275682979945848335808044820464090400072255846712957548213211431401971264889339784897955377737194300284006994191233787440876463420303629452274099577492835935079361075653597959905476367002091347991422449318117611737507742564118800601798173432551133299810583835849178650967941773909728228411231512356877046766337695521576044469689255114306770909991892251764320328930944573509467143490908803761
ct = 8551704885740889744309755032987020101863512425625180888138627403607161304953822738993391680520345265592645043068662520708169366929781691169918381273362170488677392263413969108832923278482236586827429727875628949058487270602658158101694222209489370933673886258280620225153476785410966385368931064204410945415519061635281102269037222446346830867891096168098901223718236752069061291203478333728516036006116492418308443798004928728297236853940010607000975084059609420468736462697536417422456028629313022287791490911384316494423590462342695228344052791447804257706981132882707663376242387425202256065291974952961394903512

d = pow(e, -1, Ξ)
print (long_to_bytes(pow(ct,d,n)))