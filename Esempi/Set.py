#Classe Set
#Classe Set -> insieme (senza ordine e senza duplicati)
#Gli elementi sono Immutable

s = set() #insieme vuoto
print("Set ", s)
s = set('Buongiorno') #parametro iterabile
print("Set ", s)

print("\nLunghezza")
i = len(s) #lunghezza dell'insieme
print("La lunghezza dell'insieme è ", i)

print("\nAggiunta elemento")
s.add('e') #aggiunge nell'insieme in una posizione qualsiasi e ritorna None
print("Set ", s)

print("\nRemove")
s.remove('r') #rimuove l'elemento dal set e ritorna None
print("Set ", s)
try:
    s.remove('x') #rimuovo elemento non presente
except Exception as e: print(e) #se non presente restituisce l'elemento non trovato
