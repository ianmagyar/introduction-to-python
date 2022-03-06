# Programovanie v jazyku Python

**Programovanie v jazyku Python** je kurz programovania ponúknutý v letnom semestri prvého ročníku bakalárskeho štúdia pre študijný program Inteligentné systémy. Predmet nadväzuje na kurz [Základy algoritmizácie a programovania](https://kurzy.kpi.fei.tuke.sk/zap/). Venuje sa pokročilým témam programovania v jazyku Python, ako údajové štruktúry, základné algoritmy, návrh a analýza algoritmov, objektovo orientované programovanie, modelovania a vytvorenie simulácií. Úspešný absolvent predmetu je schopný napísať zložitejšie kódy, porozumieť kódom napísaným inými programátormi, namapovať problémy z rôznych domén na výpočtové problémy a vyhodnotiť navrhnuté riešenia.

Informačný list predmetu je dostupný na [školskom portáli](https://maisportal.tuke.sk/portal/studijneProgramy.mais).

Vyučujúci predmetu: [Ing. Ján Magyar, PhD.](http://www.cloudai.sk/people-janmagyar/).

## Obsah
1. [Plán prednášok a cvičení](#plan)
2. [Hodnotenie](#grading)
    1. [Domáce úlohy](#homeworks)
    2. [Zadania](#assignments)
    <!--3. [Skúška](#exam)-->
3. [Odporúčaná literatúra](#textbooks)
4. [Etický kódex](#collaboration)

## Plán prednášok a cvičení <a name="plan"></a>

**Vzhľadom na pretrvávajúce opatrenia v súvislosti s pandémiou COVID-19 všetky prednášky a cvičenia sú online až do odvolania.**

Prednášky sú vo štvrtok o 13:30 v miestnosti L4 v budove PK7. Účasť na prednáške nie je povinná.

Cvičenia sú v pondelok o 9:10 (PK6_S02 - PC1) a 15:10 (PK6_108 - PC17), a v utorok o 9:10 (PK6_107 - PC16), 10:50 (PK6_107 - PC16) a 13:30 (V4 - V147). Účasť na cvičeniach je povinná, študent môže mať maximálne tri neúčasti za semester. Neúčasť môžete nahradiť účasťou na inom cvičení po dohode s vyučujúcim alebo vypracovaním cvičenia pre daný týždeň a poslaním riešenia vyučujúcemu.

[Orgnizačné informácie o predmete nájdete v tomto dokumente.](lectures/Lecture-00.pdf)

|                               |                           Prednáška                          |                  Cvičenie                 |                        Termíny                          |
|:-----------------------------:|:------------------------------------------------------------:|:-----------------------------------------:|---------------------------------------------------------|
|  1. týždeň<br>14. 2. - 20. 2. |        [Syntax, jazykové konštrukty, vývojové diagramy](lectures/Lecture-01.pdf)<br>([kód z prednášky](lectures/codes/lecture01.py))        |   [Nastavenie programátorského prostredia](labs/lab01-setting-up.ipynb)  |            [Z1 publikované](assignments/assignment1.zip)<br>[D1 publikovaná](assignments/homeworks/homework1.md)             |
|  2. týždeň<br>21. 2. - 27. 2. |         [Funkcie, rekurzia, generátory, lambda výrazy](lectures/Lecture-02.pdf)<br>([kód z prednášky](lectures/codes/lecture02.py))         |          [Prvé programy v Pythone](labs/lab02-first-baby-steps.ipynb)          |             D1 odovzdávka<br>[D2 publikovaná](assignments/homeworks/homework2.md)             |
|  3. týždeň<br>28. 2. - 6. 3.  |         [Reťazce, zoznamy, n-tice, mapy, polia, pandas](lectures/Lecture-03.pdf)<br>([kód z prednášky](lectures/codes/lecture03.ipynb))        |               [Algoritmizácia](labs/lab03-functions-and-algorithmization.ipynb)              |             D2 odovzdávka<br>[D3 publikovaná](assignments/homeworks/homework3.md)             |
|  4. týždeň<br>7. 3. - 13. 3.  |        Test1 ([ukážka](tests/T1-sample.pdf))<br>Testovanie, ladenie, výnimky a chyby         | [Práca so základnými údajovými štruktúrami](labs/lab04-a-look-at-the-table.ipynb) |             D3 odovzdávka<br>D4 publikovaná             |
|  5. týždeň<br>14. 3. - 20. 3. | Zložitosť algoritmov, optimalizácia, dynamické programovanie |          Defenzívne programovanie         |             D4 odovzdávka<br>D5 publikovaná             |
|  6. týždeň<br>21. 3. - 27. 3. |    Test 2<br>Úvod do objektovo orientovaného programovania   |             Flip hats problém             |                      D5 odovzdávka                      |
|  7. týždeň<br>28. 3. - 3. 4.  |             Objektovo orientované programovanie 1            |       Hašovacia tabuľka a ukážka OOP      |             Z1 odovzdávka<br>D6 publikovaná             |
|  8. týždeň<br>4. 4. - 10. 4.  |             Objektovo orientované programovanie 2            |        Objektové riešenie zadania 1       | D6 odovzdávka<br>D7 publikovaná<br>Z2 a D10 publikované |
|  9. týždeň<br>11. 4. - 17. 4. |                           Veľká Noc                          |             Postavy v 2D svete            |                      D7 odovzdávka                      |
| 10. týždeň<br>18. 4. - 24. 4. |                Test 3<br>Jednoduché simulácie                |                 Veľká Noc                 |                      D8 publikovaná                     |
|  11. týždeň<br>25. 4. - 1. 5. |                Výpočtové modely a simulácie 1                |        Let komára, návrh simulácií        |             D8 odovzdávka<br>D9 publikovaná             |
|  12. týždeň<br>2. 5. - 8. 5.  |                Výpočtové modely a simulácie 2                |  Simulácia nástupu pasažierov do lietadla |                      D9 odovzdávka                      |
|  13. týždeň<br>9. 5. - 15. 5. |                   Test 4<br>GUI v Pythone                    |            odovzdávanie zadaní            |             Z2 odovzdávka<br>D10 odovzdávka             |

## Hodnotenie <a name="grading"></a>

Celkové hodnotenie predmetu je 100 bodov (40 + 60 bodov); študent musí získať viac ako polovicu bodov zo zápočtu a zo skúšky.

Zápočet sa skladá z dvoch častí: 10 domácich úloh po 2 body, a 2 zadania za 10 bodov. Na vypracovanie domácich úloh majú študenti jeden týždeň (zadanie bude zverejnené týždeň pred termínom odovzdania), počas semestra môže študent odovzdať max. 2 domáce úlohy po deadline bez straty bodov, inak sa udeľuje maximálne 1 bod (ak študent odovzdá riešenie do konca daného týždňa). Zadanie 1 bude zverejnené v prvom, Zadanie 2 v ôsmom týždni semestra. Deadline pre domáce úlohy a zadania je v piatok 18:00.

Skúška má teoretickú a praktickú časť. Teoretická časť sa skladá zo štyroch testov, ktoré sa píšu počas semestra na prednáškach. Na skúške majú študenti možnosť znova napísať ľubovoľné časti aby si vylepšili celkové hodnotenie (do úvahy sa berie lepšie napísaný test). Praktická časť sa skladá z jedného projektu na programovanie. Úloha bude zverejnená deň pred skúškou, študenti na skúške obhajujú už hotové riešenia a následne rozšíria svoje riešenia. Na skúške potrebujete získať viac ako polovicu bodov na oboch častiach.

|        Zložka       | Body |
|:-------------------:|:----:|
|       10 úloh       |  20  |
|      2 zadanie      |  20  |
|       4 testy       |  40  |
| programovacia úloha |  20  |

[Stav priebežného hodnotenia nájdete tu](https://docs.google.com/spreadsheets/d/1owm8WAxbDqVk4_Di9CGoAzO9nlUqUYuhekkErW-PNc0/edit?usp=sharing).

### Domáce úlohy <a name="homeworks"></a>
1. [implementácia jednoduchej úlohy, vývojové diagramy](assignments/homeworks/homework1.md) (deadline 25. 2. 2022)
2. [generátory, použitie lambda výrazov a funkcie](assignments/homeworks/homework2.md) (deadline 4. 3. 2022)
3. [práca s knižnicami pandas a numpy, list comprehension](assignments/homeworks/homework3.md) (deadline 11. 3. 2022)
4. ošetrenie chýb (deadline 18. 3. 2022)
5. písanie unit testov (deadline 25. 3. 2022)
6. vytvorenie triedy z UML diagramu (deadline 8. 4. 2022)
7. hierarchia tried (deadline 15. 4. 2022)
8. generovanie grafov (deadline 29. 4. 2022)
9. implementácia simulácie (deadline 6. 5. 2022)
10. oprava DÚ/grafické rozhranie pre zadanie 2 (deadline 13. 5. 2022)

### Zadania <a name="assignments"></a>
1. Algoritmické riešenie vybraných úloh (deadline 1. 4. 2022)
    * [Čo máme na obed?](assignments/Znenie_1a.pdf)
    * [Wordle](assignments/Znenie_1b.pdf)
    * [projekt riešenia](assignments/assignment1.zip)

2. Simulácia (deadline 14. 5. 2022)

<!--### Skúška <a name="exam"></a>-->

## Odporúčaná literatúra <a name="textbooks"></a>

* GUTTAG, J. V.: Introduction to Computation and Programming Using Python. Revised and expanded edition, MIT Press, 2013 ([link](https://doc.lagout.org/programmation/python/Introduction%20to%20Computation%20and%20Programming%20using%20Python%20%28rev.%20ed.%29%20%5BGuttag%202013-08-09%5D.pdf))
* CORMEN, T. H. – LEISERSON, C. E. – RIVEST, R. L. – STEIN, C.: Introduction to Algorithms. 3rd edition, MIT Press, 2009 ([link](https://ms.sapientia.ro/~kasa/Algorithms_3rd.pdf))
* RASCHKA, S.: Python Machine Learning. 1st edition, Packt Publishing, 2015 ([link](https://www.amazon.com/Python-Machine-Learning-scikit-learn-TensorFlow-ebook/dp/B0742K7HYF))
* CHUN, W. J.: Core Python Programming. 2nd Edition, Prentice Hall, 2006 ([link](https://www.amazon.com/Core-Python-Programming-Wesley-Chun/dp/0132269937))
* McKINNEY, W.: Python for Data Analysis: Data Wrangling with Pandas, Numpy, and IPython. 2nd Edition, O’Reilly Media, 2017 ([link](https://www.amazon.com/Python-Data-Analysis-Wrangling-IPython/dp/1491957662))
* SEVERANCE, C.: Python for Everybody: Exploring Data in Python 3. 1st edition, CreateSpace Independent Publishing Platform, 2016 ([link](https://www.amazon.com/Python-Everybody-Exploring-Data/dp/1530051126))

Ďalšie zdroje sú dostupné na [web stránke MIT kurzu 6.00](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-00-introduction-to-computer-science-and-programming-fall-2008/index.htm).

## Etický kódex <a name="collaboration"></a>
Študenti môžu spolupracovať pri riešení **zadaní a domácich úloh počas semestra**, pričom sú povinní uviesť mená spolupracujúcich študentov. **Spolupráca pri testoch a na skúške je zakázaná.**

Tieto pravidlá vychádzajú z predpokladu, že študenti sú na predmete pretože si chcú osvojiť náplň kurzu. Spolupráca spočíva v spoločnom riešení problému kde každý spolupracujúci študent pomáha pri riešení. Zdieľanie už hotových riešení spolužiakom **nie je** spolupráca. Cieľom zadaní je pomôcť študentom precvičiť si princípy a metódy programovania, k čomu je nevyhnutná zodpovedajúca miera pochopenia daných konceptov. Od každého študenta sa očakáva že je schopný svoje zadanie obhájiť a rozšíriť pod dohľadom vyučujúceho.
