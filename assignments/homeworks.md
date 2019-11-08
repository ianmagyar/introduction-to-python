## Domáca úloha 1 <a name="h1"></a>

Na úložisku pre odovzdávanie zadaní nájdete Python skript s názvom `h01.py`, ktorý obsahuje kód jednoduchej funkcie. Vašou úlohou je vytvoriť k funkcii vývojový diagram a napísať špecifikáciu. Vývojový diagram nahrajte ako PDF súbor `h01.pdf`, na jeho vytvorenie môžete použiť ľubovoľný nástroj, napr. [draw.io](https://www.draw.io). Špecifikáciu funkcie napíšte do skriptu s nasledovným obsahom:

* krátky popis funkcie a jej fungovania
* popis vstupných parametrov (ak sú) - typ, význam, predpoklady
* popis návratovej hodnoty (ak je) - typ, význam.

Ak počas riešenia ste spolupracovali so spolužiakom, uveďte jeho/jej meno v hlavičke skriptu.

## Domáca úloha 2 <a name="h2"></a>

Na úložisku pre odovzdávanie zadaní nájdete Python skript s názvom `h02.py`, ktorý obsahuje popis troch zoznamov a jednej lambda funkcie. Vašou úlohou je doplniť list comprehension pre generovanie špecifikovaných zoznamov (riadky 10, 14, 18) a napísať lambda funkciu (riadok 22).

## Domáca úloha 3 <a name="h3"></a>

Na úložisku pre odovzdávanie zadaní nájdete Python skript s názvom `h03.py`, ktorý obsahuje definíciu funkcie pre niektorý triediaci algoritmus. Vašou úlohou je implementovať túto funkciu. Funkcia má dva parametre:

* lst — zoznam čísel (alebo iných porovnávateľných hodnôt)
* ascending — parameter typu boolean, ktorý určuje, či čísla chceme zoradiť vzostupne (od najmenšieho po najväčšie; True) alebo zostupne (od najväčšieho po najmenšie; False).

## Domáca úloha 4 <a name="h4"></a>

Na úložisku pre odovzdávanie zadaní nájdete Python skript s názvom `h04.py`, ktorý obsahuje jednu funkciu. Vašou úlohou je ošetriť niektoré možné chyby v tejto funkcii. Ako prvé máte napísať kód pre kontrolu predpokladov pre vstupné parametre, v druhej úlohe máte ošetriť možnú chybu pomocou konštruktu try-except.

## Domáca úloha 5 <a name="h5"></a>

Na úložisku pre odovzdávanie zadaní nájdete Python skript s názvom `h05.py`, ktorý obsahuje dve funkcie. Funkcia `load_balance` je mock funkcia a emuluje načítavanie dát z databázy. V systémoch, ktoré pracujú s databázou je načítavanie kritický bod vo funkčnosti programu, keďže zvyčajne trvá dlhší čas. Vašou úlohou je využiť memoizáciu pre zvýšenie efektivity funkcie `get_balances`. Funkcia má jeden parameter - zoznam mien. Funkcia následne zavolá `load_balance` s každým menom - pre simuláciu náročnosti načítavania z databázy funkcia `load_balance` počká 3 sekundy a až potom vráti náhodné číslo.

Pridajte premennú typu dictionary (reprezentuje tabuľku s čiastočnými výsledkami) do funkcie `get_balances` a následne upravte for cyklus tak, aby suma sa načítala priamo z tabuľky ak tá obsahuje hodnotu pod kľúčom `name`. Ak taký kľúč v tabuľke neexistuje, zavolajte funkciu `load_balance` a pridajte dvojicu kľúč-hodnota (`name` a `balance`) do tabuľky.

## Domáca úloha 6 <a name="h6"></a>

Na úložisku pre odovzdávanie zadaní nájdete Python skript s názvom `h06.py`, ktorý obsahuje deklaráciu štyroch funkcií. Vašou úlohou je vytvoriť funkčnú implementáciu hašovania, pričom funkcie by mali definovať nasledujúcu funkcionalitu:

* **hash_function(number)** - vstupom je číslo, funkcia vráti hash hodnotu pre dané číslo; pri implementácii môžete použiť ľubovoľný algoritmus
* **add_number(table, number)** - funkcia pridá číslo `number` do hash tabuľky v premennej `table`; pri pridávaní najprv určte hash hodnotu čísla `number`, a pridajte číslo do príslušného bucketu v tabuľke; funkcia nevracia žiadnu hodnotu
* **has_number(table, number)** - funkcia zistí, či číslo `number` sa nachádza v tabuľke `table`; najprv určte hash hodnotu čísla `number`, a vyhľadávajte iba v príslušnom buckete; funkcia vráti `True` ak našla `number`, v opačnom prípade vráti `False`
* **delete_number(table, number)** - funkcia vymaže číslo `number` z tabuľky `table`, ak tabuľka obsahuje číslo; najprv určte hash hodnotu čísla `number`, a aktualizujte príslušný bucket (ak potrebné)
* **test_hashing()** - funkcia slúži na testovania Vášho riešenia, nie je potrebné ju upravovať
