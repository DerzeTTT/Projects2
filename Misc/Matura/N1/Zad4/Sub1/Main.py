Reading = [Line for Line in open('../liczby.txt', 'r').read().split("\n") if Line != ''];
Holding = [];

def Parse_Num(Line):

    Listed = list(Line);

    if Listed[0] == Listed[-1]:

        Holding.append(Line);

for v in Reading:

    Parse_Num(v);

print(len(Holding), Holding[0]);