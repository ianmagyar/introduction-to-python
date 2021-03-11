## Domáca úloha 1 <a name="h1"></a>

Na úložisku pre odovzdávanie zadaní nájdete Python skript s názvom `h01.py`, ktorý obsahuje kód jednoduchej funkcie. Vašou úlohou je vytvoriť k funkcii vývojový diagram. Vývojový diagram nahrajte ako PDF súbor `h01.pdf` (za nesprávny formát súboru sa stiahne pol boda), na jeho vytvorenie môžete použiť ľubovoľný nástroj, napr. [draw.io](https://www.draw.io). V dokumente uveďte meno funkcie alebo číslo úlohy.

Ak počas riešenia spolupracujete so spolužiakom, jeho/jej meno uveďte v hlavičke skriptu `h01.py`. V hlavičke tiež uveďte zdroje, ktoré ste použili pri vypracovaní riešenia, ako aj približný čas, ktorý ste potrebovali na vypracovanie domácej úlohy.

**Poznámka:** Ak funkcia má parametre, tie nemusíte zadefinovať zvlášť vo vývojovom diagrame, môžete ich považovať za zadefinované. Ak sa ale vo funkcii načíta vstup od používateľa, tento krok musí mať príslušný blok.


## Domáca úloha 2 <a name="h2"></a>

Na úložisku pre odovzdávanie zadaní nájdete Python skript s názvom `h02.py`, ktorý obsahuje popis troch zoznamov a jednej lambda výrazu. Vašou úlohou je vygenerovať zoznamy pomocou list comprehension na základe zadanej špecifikácie (riadky 10, 14, 18), a zadefinovať lambda výraz podľa špecifikácie (riadok 22). Ak pri generovaní zoznamov potrebujete vytvoriť pomocné premenné (napríklad potrebujete vygenerovať zoznam kombinácií prvkov dvoch zoznamov, alebo hľadáte isté písmená v stringu), môžete tak urobiť ľubovoľným spôsobom.

Ak počas riešenia spolupracujete so spolužiakom, jeho/jej meno uveďte v hlavičke skriptu `h02.py`. V hlavičke tiež uveďte zdroje, ktoré ste použili pri vypracovaní riešenia, ako aj približný čas, ktorý ste potrebovali na vypracovanie domácej úlohy.


## Domáca úloha 3 <a name="h3"></a>

Na úložisku pre odovzdávanie zadaní nájdete Python skript s názvom `h03.py`, ktorý obsahuje deklaráciu generátora alebo funkcie pre implementáciu vybraného triediaceho algoritmu. Vašou úlohou je implementovať algoritmus ako generátor, resp. funkciu. Každý generátor a funkcia má dva parametre:

* `lst` - zoznam hodnôt, ktoré potrebujete zoradiť. Upravujte priamo tento zoznam, a generátory majú vracať tento zoznam ako medzivýsledok.
* `ascending` - hodnota určí smer zoradenia. Ak hodnota je `True`, chceme zoradiť od najmenšieho prvko po najväčší, v prípade `False` naopak. **Funkcionalitu môžete implementovať cez funkciu `reverse` len v prípade algoritmov radix a bucket sort.**

Vaše riešenia budú hodnotené automatickým testom, práve preto musíte dodržať formu implementácie a spôsobu získania medzivýsledkov. Za správny výsledok dostanete 0,5 boda, za správne medzivýsledky 0,5 b; test pobeží dvakrát, raz s `ascending=True`, raz s `ascending=False`. Skript obsahuje aj funkciu `main` s volaním funkcie a výpismi, ktoré sa budú kontrolovať. Skript takisto obsahuje ukážku pre medzivýsledky a správny výstup. Pri riešení môžete používať ľubovoľné štandardné funkcie Pythonu (okrem `sort`, resp. `sorted` a `reverse`, resp. `reversed` ak to nie je explicitne povolené).

Niekoľko poznámok k jednotlivým algoritmom:

* **selection sort** - algoritmus implementujte ako generátor, ktorý vracia medzivýsledok po každom iteratívnom kroku; efekt parametra `ascending` musíte zohľadniť už v medzivýsledkoch.
* **bubble sort** - algoritmus implementujte ako generátor, ktorý vracia medzivýsledok po každom iteratívnom kroku; efekt parametra `ascending` musíte zohľadniť už v medzivýsledkoch.
* **insertion sort** - algoritmus implementujte ako generátor, ktorý vracia medzivýsledok po každom iteratívnom kroku; efekt parametra `ascending` musíte zohľadniť už v medzivýsledkoch.
* **quick sort** - algoritmus implementujte ako funkciu; v skripte nájdete aj pomocnú funkciu `partition`, ktorá sa zavolá pre zoradenie hodnôt podľa pivotu (menšie hodnoty doľava, väčšie doprava); ako pivot použite poslednú hodnotu v zozname (v časti zoznamu), pred každým volaním funkcie `partition` uložte hodnoty parametrov `low` a `high` ako n-ticu (tuple) do zoznamu `partition_called_with`; pri hodnotení sa kontroluje aj hodnota zoznamu.
* **merge sort** - algoritmus implementujte ako funkciu; vo funkcii rozdeľte zoznam na dve časti v strede, t.j. `len(lst) // 2`; pred každým volaním funkcie `merge_sort` (okrem prvého volania) uložte hodnotu polovičného bodu do zoznamu `merge_sort_called_with`; pri hodnotení sa kontroluje aj hodnota zoznamu.
* **bucket_sort** - algoritmus implementujte ako funkciu, pri zoradení zoznamov v jednotlivých bucketoch **môžete** použiť funkciu `sort` aj s parametrom `reverse`, zoradenie prvkov v samotnom zozname `lst` ale musíte vyriešiť bez nich (konkatenácia bucketov); použite 10 bucketov, rozdelenie do bucketov riešte cez `10 * number`.
* **radix sort** - algoritmus implementujte ako generátor, ktorý vracia medzivýsledky po každej iterácii, teda po zavolaní pomocnej funkcie `counting_sort`; pre implementáciu efektu parametra `ascending` **môžete** použiť funkciu `reverse` ale až na konci vykonávania (viď príklad v skripte).

## Domáca úloha 4 <a name="h4"></a>

Na úložisku pre odovzdávanie zadaní nájdete Python skript s názvom `h04.py`, ktorý obsahuje jednoduchú funkciu a jej krátky popis. Vašou úlohou je upraviť kód funkcie tak, aby splnila špecifikáciu uvedenú v komentároch, a zároveň ošetriť chyby ktoré môžu vyskytnúť počas vykonávania programu. Kód teda potrebujete rozšíriť nasledovne:

1. skontrolovať hodnotu vstupných parametrov podľa špecifikácie (napr. správny typ, správny formát, platná hodnota); ak podmienky nie sú splnené, vygenerujte chybu s príslušnou chybovou správou.
2. otestovať a v prípade potreby doladiť kód aby spĺňal špecifikáciu - kód môže obsahovať chyby, ktoré úplne znemožnia jeho správny beh; unit testy nemusíte písať, stačí ak kód otestujete manuálne na rôznych vstupoch, aby ste odhalili možné chyby.
3. ošetriť možné výnimky - všetky kódy sa spoliehajú na platnosť niektorých predpokladov na vstup alebo využívajú štandardné funkcie jazyka Python, ktoré môžu spôsobiť výnimku počas behu programu. Identifikujte tieto možné chyby a ošetrite ich blokom `try - catch` alebo kontrolou hodnôt ešte pred ich použitím. V oboch prípadoch vygenerujte chybu s príslušnou chybovou správou (nepoužívajte iba štandardné výpisy z Pythonu).
