# Programovanie v jazyku Python

**Programovanie v jazyku Python** je kurz programovania ponúkaný v letnom semestri prvého ročníka bakalárskeho štúdia pre študijný program Inteligentné systémy. Predmet nadväzuje na kurz [Základy algoritmizácie a programovania](https://kurzy.kpi.fei.tuke.sk/zap/). Venuje sa pokročilým témam programovania v jazyku Python, ako údajové štruktúry, základné algoritmy, návrh a analýza algoritmov, objektovo orientované programovanie, modelovania a vytvorenie simulácií. Úspešný absolvent predmetu je schopný napísať zložitejšie kódy, porozumieť kódom napísaným inými programátormi, namapovať problémy z rôznych domén na výpočtové problémy a vyhodnotiť navrhnuté riešenia.

Informačný list predmetu je dostupný na [školskom portáli](https://maisportal.tuke.sk/portal/studijneProgramy.mais).

Prednášajúci predmetu: [Ing. Ján Magyar, PhD.](https://cit.fei.tuke.sk/people-janmagyar/).

Cvičiaci predmetu:

* Bc. Veronika Kapcalová
* Bc. Yehor Nepokrytyi

## Obsah
1. [Plán prednášok a cvičení](#plan)
2. [Hodnotenie](#grading)
    1. [Domáce úlohy](#homeworks)
    2. [Zadania](#assignments)
    <!--3. [Skúška](#exam)-->
3. [Odporúčaná literatúra](#textbooks)
4. [Etický kódex](#collaboration)

## Plán prednášok a cvičení <a name="plan"></a>
Prednášky sú vo štvrtok o 13:30 v miestnosti L4 v budove PK7. Účasť na prednáške nie je povinná.

Cvičenia sú v pondelok o 9:10 (PK6_S02 - PC1), a v utorok o 7:30 (PK6_S02 - PC1), 9:10 (V4_147) a 10:50 (PK6_107 - PC16). Účasť na cvičeniach je povinná, študent môže mať maximálne tri neúčasti za semester. Neúčasť môžete nahradiť účasťou na inom cvičení po dohode s vyučujúcim alebo vypracovaním cvičenia pre daný týždeň a poslaním riešenia vyučujúcemu.

[Orgnizačné informácie o predmete nájdete v tomto dokumente.](lectures/Lecture-00.pdf)

|                               |                  Cvičenie                 |                           Prednáška                          |                        Termíny                          |
|:-----------------------------:|:-----------------------------------------:|:------------------------------------------------------------:|---------------------------------------------------------|
|  1. týždeň<br>10. 2. - 16. 2. |   [Nastavenie programátorského prostredia](labs/lab01-setting-up.ipynb)  |                  [Syntax, jazykové konštrukty](lectures/Lecture-01.pdf) <br> ([kód z prednášky](lectures/codes/lecture01.ipynb))                 |            Z1 publikované<br>[D1 publikovaná](homeworks/homework01.md)             |
|  2. týždeň<br>17. 2. - 23. 2. |          Prvé programy v Pythone          |         Funkcie, rekurzia, generátory, lambda výrazy         |                     D2 publikovaná                      |
|  3. týždeň<br>24. 2. - 2. 3.  |               Algoritmizácia              |                Reťazce, zoznamy, n-tice, mapy                |           D1, D2 odovzdávka<br>D3 publikovaná           |
|  4. týždeň<br>3. 3. - 9. 3.   | Práca so základnými údajovými štruktúrami |          Test1<br>Údajové štruktúry, numpy a pandas          |             D3 odovzdávka<br>D4 publikovaná             |
|  5. týždeň<br>10. 3. - 16. 3. |             Kedy na Jedličku?             |             Testovanie, ladenie, výnimky a chyby             |           Z1, D4 odovzdávka<br>D5 publikované           |
|  6. týždeň<br>17. 3. - 23. 3. |                   Wordle                  | Zložitosť algoritmov, optimalizácia, dynamické programovanie |           D5 odovzdávka<br>Z2, D6 publikované           |
|  7. týždeň<br>24. 3. - 30. 3. |           Monte Carlo simulácie           |                 Výpočtové modely a simulácia                 |                      D6 odovzdávka                      |
|  8. týždeň<br>31. 3. - 6. 4.  |             Wordle pomocou OOP            | Test 2<br>Úvod do objektovo orientovaného programovania, princípy |                D7 publikovaná                      |
|  9. týždeň<br>7. 4. - 13. 4.  |          Modelovanie a simulácia          |                         OOP v Pythone                        |           Z2, D7 odovzdávka<br>D8 publikovaná           |
| 10. týždeň<br>14. 4. - 20. 4. |             Vývoj hry v pygame            |                           Veľká Noc                          |             D8 odovzdávka<br>Z3 publikované             |
| 11. týždeň<br>21. 4. - 27. 4. |                 Veľká Noc                 |                   Test 3<br>Návrhové vzory                   |                   D9, D10 publikované                   |
| 12. týždeň<br>28. 4. - 4. 5.  |             Vývoj hry v pygame            |                       *štátny sviatok*                       |                      D9 odovzdávka                      |
| 13. týždeň<br>5. 5. - 11. 5.  |             Vývoj hry v pygame            |                        Návrhové vzory                        |             Z3 odovzdávka<br>D10 odovzdávka             |
| 14. týždeň<br>12. 5. - 18. 5. |            odovzdávanie zadaní            |                    Test 4<br>opravné testy                   |                                                         |

## Hodnotenie <a name="grading"></a>

Celkové hodnotenie predmetu je 100 bodov (40 + 60 bodov); študent musí získať viac ako polovicu bodov zo zápočtu a zo skúšky.

Zápočet sa skladá z dvoch častí: 10 domácich úloh po 1 bod, a 3 zadania za 10 bodov. Na vypracovanie domácich úloh majú študenti jeden týždeň (zadanie bude zverejnené týždeň pred termínom odovzdania), počas semestra môže študent odovzdať max. 2 domáce úlohy po deadline bez straty bodov, inak sa udeľuje maximálne 0,5 boda (ak študent odovzdá riešenie do konca daného týždňa). Zadanie 1 bude zverejnené v prvom, Zadanie 2 v šiestom, a Zadanie 3 v desiatom týždni semestra. Deadline odovzdania domácich úloh a zadaní je v piatok 18:00.

Skúška má teoretickú a praktickú časť. Teoretická časť sa skladá zo štyroch testov, ktoré sa píšu počas semestra na prednáškach. Na skúške majú študenti možnosť znova napísať ľubovoľné časti, aby si vylepšili celkové hodnotenie (do úvahy sa berie lepšie napísaný test). Praktická časť sa skladá z jedného projektu na programovanie. Na skúške potrebujete získať viac ako polovicu bodov z oboch častí.

|        Zložka       | Body |
|:-------------------:|:----:|
|       10 úloh       |  10  |
|      3 zadania      |  30  |
|       4 testy       |  40  |
| programovacia úloha |  20  |

### Domáce úlohy <a name="homeworks"></a>
1. [ciele a očakávania](homeworks/homework01.md) (deadline 28. 2. 2025)
2. funkcie (deadline 28. 2. 2025)
3. použitie lambda výrazov a list comprehension (deadline 7. 3. 2025)
4. numpy a pandas (deadline 14. 3. 2025)
5. ošetrenie chýb (deadline 21. 3. 2025)
6. písanie unit testov (deadline 28. 3. 2025)
7. vytvorenie triedy z UML diagramu (deadline 11. 4. 2025)
8. hierarchia tried a prepisovanie metód (deadline 18. 4. 2025)
9. implementácia návrhového vzoru (deadline 2. 5. 2025)
10. oprava DÚ (deadline 9. 5. 2025)

### Zadania <a name="assignments"></a>
Vypracované riešenie - skripty - nahrajte priamo do priečinka na Google Drive (**nevytvárajte samostatný priečinok!**).

1. Ohlásená doba meškania sa môže zmeniť (deadline 14. 3. 2025)
2. *TBA* (deadline 11. 4. 2025)
3. *TBA* (deadline 9. 5. 2025)

<!--### Skúška <a name="exam"></a>-->

## Odporúčaná literatúra <a name="textbooks"></a>

* GUTTAG, J. V.: Introduction to Computation and Programming Using Python. Revised and expanded edition, MIT Press, 2013 ([link](https://doc.lagout.org/programmation/python/Introduction%20to%20Computation%20and%20Programming%20using%20Python%20%28rev.%20ed.%29%20%5BGuttag%202013-08-09%5D.pdf))
* CORMEN, T. H. – LEISERSON, C. E. – RIVEST, R. L. – STEIN, C.: Introduction to Algorithms. 3rd edition, MIT Press, 2009 ([link](https://ms.sapientia.ro/~kasa/Algorithms_3rd.pdf))
* RASCHKA, S.: Python Machine Learning. 1st edition, Packt Publishing, 2015 ([link](https://www.amazon.com/Python-Machine-Learning-scikit-learn-TensorFlow-ebook/dp/B0742K7HYF))
* CHUN, W. J.: Core Python Programming. 2nd Edition, Prentice Hall, 2006 ([link](https://www.amazon.com/Core-Python-Programming-Wesley-Chun/dp/0132269937))
* McKINNEY, W.: Python for Data Analysis: Data Wrangling with Pandas, Numpy, and IPython. 2nd Edition, O’Reilly Media, 2017 ([link](https://www.amazon.com/Python-Data-Analysis-Wrangling-IPython/dp/1491957662))
* SEVERANCE, C.: Python for Everybody: Exploring Data in Python 3. 1st edition, CreateSpace Independent Publishing Platform, 2016 ([link](https://www.amazon.com/Python-Everybody-Exploring-Data/dp/1530051126))
* JAWORSKI, M. - ZIADÉ, T.: Expert Python Programming. 4th edition, Packt Publishing Ltd, 2021. ([link](https://www.packtpub.com/product/expert-python-programming-fourth-edition/9781801071109))
* PHILLIPS, D.: Python 3 object oriented programming. 3rd edition, Packt Publishing Ltd, 2018. ([link](https://www.packtpub.com/product/python-3-object-oriented-programming-third-edition/9781789615852))

Ďalšie zdroje sú dostupné na [web stránke MIT kurzu 6.00](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-00-introduction-to-computer-science-and-programming-fall-2008/index.htm).

## Etický kódex <a name="collaboration"></a>
Študenti môžu spolupracovať pri riešení **zadaní a domácich úloh počas semestra**, pričom sú povinní uviesť mená spolupracujúcich študentov. **Spolupráca pri testoch a na skúške je zakázaná.**

Tieto pravidlá vychádzajú z predpokladu, že študenti sú na predmete pretože si chcú osvojiť náplň kurzu. Spolupráca spočíva v spoločnom riešení problému kde každý spolupracujúci študent pomáha pri riešení. Zdieľanie už hotových riešení spolužiakom **nie je** spolupráca. Cieľom zadaní je pomôcť študentom precvičiť si princípy a metódy programovania, k čomu je nevyhnutná zodpovedajúca miera pochopenia daných konceptov. Od každého študenta sa očakáva že je schopný svoje zadanie obhájiť a rozšíriť pod dohľadom vyučujúceho.
