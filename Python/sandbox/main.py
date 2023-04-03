class Artificial_Input:

    def __init__(self):

        self.Holding = [];
        self.Reading = 0;

        self.Production = False;

    def add_input(self, new_input, split_lines=True):

        Appending = None;

        if type(new_input) is str and split_lines:

            Appending = new_input.split("\n");

        elif type(new_input) is list:

            Appending = new_input;

        else:

            raise Exception("Given value is not a string or list!")

        self.Holding += Appending;

    def read(self):

        if not self.Production:

            Returning = self.Holding[self.Reading];
            self.Reading += 1;

            return Returning;
        
        else:

            return input();

Custom_Input = Artificial_Input();

Custom_Input.Production = True;

Custom_Input.add_input('''5
Produkt1 2222888
NowyProdukt 123333
Chleb 9999999
Produkt1 2222888
ProduktTestowy 6281732
1''')

# UWAGA!
# W zadaniu wykorzystaj samodzielnie zaimplementowane sortowanie przez wstawianie.
# Rozwiązania implementujące inne sortowania zostaną wyzerowane.
# ___
# W pewnym sklepie osiedlowym pracuje starsza pani, która zapisuje wszystkie produkty wraz z ich kodami w
# papierowym zeszycie. Często ma problem z tym, aby znaleźć odpowiedni produkt na liście i sprawia jej to mnóstwo kłopotu.
# Jako, że jej syn to Twój bliski kolega, poprosił Cię, abyś napisał program, który ułatwi codzienne przeszukiwanie
# produktów.
# Program powinien przyjmować listę produktów, a następnie posortować ją w zależności od wyboru użytkownika -
# alfabetycznie lub względem kodów (od największego do najmniejszego). Niestety, zdarza się, że dwa produkty mogą
# mieć tę samą nazwę lub/i ten sam kod co inne, powinieneś to uwzględnić.
# Wejście
# W pierwszej linii wejścia znajduje się liczba n oznaczająca liczbę linii, w których znajdą się opisy produktów. Opis
# produktu składa się z nazwy produktu p - jednowyrazowego napisu oraz kodu k - w postaci liczby całkowitej. W ostatniej
# linii znajduje się liczba 0, jeżeli próbki mają być uszeregowane względem nazw, lub liczba 1 jeśli względem kodu.
# Wyjście
# Na wyjściu program powinien wypisywać nazwy oraz kody (oddzielone spacją) produktów (każdy produkt oddzielony znakiem nowej linii)
# w odpowiedniej kolejności (wg. nazw - alfabetycznie, wg. kodu - malejąco).
# Podczas sortowania względem nazw w przypadku takiej samej nazwy, decyduje kod i odwrotnie.

n = int(Custom_Input.read())

products = []

for i in range(n):

    rawInfo = Custom_Input.read().split(' ')
    products.append({'name': rawInfo[0], 'id': int(rawInfo[1])})

sortType = int(Custom_Input.read())

def insertSort(rawArr):

    arr = rawArr.copy()

    if (n := len(arr)) <= 1: return
    
    for i in range(1, n):
         
        key = arr[i]
        j = i-1

        while j >= 0 and key < arr[j]:
                
            arr[j+1] = arr[j]
            j -= 1

        arr[j+1] = key

    return arr

def findProduct(prop, val):

    for v in products:

        if v.get(prop) == val:

            return v
        
productProp = (sortType == 0 and "id") or "name"

listed = list(map(lambda product: product.get(productProp), products))
sorted = insertSort(listed)

if sortType == 0: sorted.reverse()

for v in sorted:

    found = findProduct(productProp, str(v))

    print(f"{found['name']} {str(found['id'])}")