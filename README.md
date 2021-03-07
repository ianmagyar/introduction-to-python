# Programovanie v jazyku Python

**Programovanie v jazyku Python** je kurz programovania ponúknutý v letnom semestri prvého a druhého ročníku bakalárskeho štúdia pre študijný program Inteligentné systémy. Predmet nadväzuje na kurz [Základy algoritmizácie a programovania](https://kurzy.kpi.fei.tuke.sk/zap/). Venuje sa pokročilým témam programovania v jazyku Python, ako údajové štruktúry, základné algoritmy, návrh a analýza algoritmov, objektovo orientované programovanie, modelovania a vytvorenie simulácií. Úspešný absolvent predmetu je schopný napísať zložitejšie kódy, porozumieť kódom napísaným inými programátormi, namapovať problémy z rôznych domén na výpočtové problémy a vyhodnotiť navrhnuté riešenia.

Informačný list predmetu je dostupný na [školskom portáli](https://maisportal.tuke.sk/portal/studijneProgramy.mais).

Vyučujúci predmetu: [Ing. Ján Magyar](http://www.cloudai.sk/people-janmagyar/).

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

Prednášky sú vo štvrtok o 13:30 v miestnosti A204 v hlavnej budove. Účasť na prednáške nie je povinná.

Cvičenia sú v pondelok o 9:10 (PK6_S02 - PC1) a 15:10 (PK6_108 - PC17), a v utorok o 9:10 (PK6_107 - PC16). Účasť na cvičeniach je povinná, študent môže mať maximálne tri neúčasti za semester. Neúčasť môžete nahradiť účasťou na inom cvičení po dohode s vyučujúcim alebo vypracovaním cvičenia pre daný týždeň a poslaním riešenia vyučujúcemu.

|           Týždeň           |                            Prednáška                            |                         Cvičenie                        |               Termíny               |
|:--------------------------:|:---------------------------------------------------------------:|:-------------------------------------------------------:|:-----------------------------------:|
| 1. týždeň<br>15. 2. - 21. 2.  | [Organizácia predmetu](lectures/Lecture-00.pdf)<br>[Syntax, základné jazykové konštrukty, vývojové diagramy](lectures/Lecture-01.pdf) ([kódy](lectures/codes/lecture01.ipynb))        | Úvod, [nastavenie programátorského rozhrania](labs/lab00-setting-up.ipynb)<br>[prvé programy](labs/lab01-first-baby-steps.ipynb)             |[DÚ1 publikovaná](assignments/homeworks.md#h1)<br>[Z1 publikované](assignments/assignment1.zip)      |
| 2. týždeň<br>22. 2. - 28. 2.  | [Funkcie, rekurzia, lambda výrazy](lectures/Lecture-02A.pdf)<br>[Reťazce, zoznamy, n-tice, mapy](lectures/Lecture-02B.pdf) ([kódy](lectures/codes/lecture02.ipynb)) | [Algoritmizácia](labs/lab02-functions-and-algorithmization.ipynb)  | DÚ1 odovzdanie<br>[DÚ2 publikovaná](assignments/homeworks.md#h2)      |
| 3. týždeň<br>1. 3. - 7. 3.    | Test 1 ([ukážka](tests/T1-sample.pdf))<br>[Zložitosť algoritmov, triedenie a vyhľadávanie](lectures/Lecture-03.pdf)           | [Práca so základnými údajovými štruktúrami](labs/lab03-a-look-at-the-table.ipynb)               | DÚ2 odozvdanie<br>[DÚ3 publikovaná](assignments/homeworks.md#h3)      |
| 4. týždeň<br>8. 3. - 14. 3.   | Testovanie, ladenie, výmiky a chyby                             | [Flip hats problém](labs/lab04-flipping-hats.ipynb)                                       | DÚ3 odozvdanie<br>DÚ4 publikovaná      |
| 5. týždeň<br>15. 3. - 21. 3.  | Optimalizácia, dynamické programovanie                          | Defenzívne programovanie                                | DÚ4 odovzdanie<br>DÚ5 publikovaná      |
| 6. týždeň<br>22. 3. - 28. 3.  | Test 2<br>Údajové štruktúry                                        | Kedy na Jedličku?                                       | DÚ5 odovzdanie                      |
| 7. týždeň<br>29. 3. - 4. 4.   | Objektovo orientované programovanie 1                           | Hašovacia tabuľka | Z1 odovzdanie<br>DÚ6 publikovaná       |
| 8. týždeň<br>5. 4. - 11. 4.   | Veľká Noc                                                       | Veľká Noc                                               | DÚ6 odovzdanie<br>Z2, DÚ10 publikované |
| 9. týždeň<br>12. 4. - 18. 4.  | Objektovo orientované programovanie 2                           | Objektové riešenie zadania 1                            | DÚ7 publikovaná                     |
| 10. týždeň<br>19. 4. - 25. 4. | Test 3<br>Výpočtové modely a simulácia 1                           | Výpočet hodnoty pi                                      | DÚ7 odovzdanie<br>DÚ8 publikovaná      |
| 11. týždeň<br>26. 4. - 2. 5.  | Výpočtové modely a simulácia 2                                  | Simulácia letu komára                                   | DÚ8 odovzdanie<br>DÚ9 publikovaná      |
| 12. týždeň<br>3. 5. - 9. 5.   | Test 4<br>Pokročilé témy v programovaní v Pythone                  | Simulácia nástupu pasažierov do lietadla                | DÚ9 odovzdanie                      |
| 13. týždeň<br>10. 5. - 16. 5. | -                                                               | konzultácie                                             | Z2 odovzdanie<br>DÚ10 odovzdanie       |

## Hodnotenie <a name="grading"></a>

Celkové hodnotenie predmetu je 100 bodov (40 + 60 bodov); študent musí získať viac ako polovicu bodov zo zápočtu a zo skúšky.

Zápočet sa skladá z dvoch častí: 10 domácich úloh po 2 body, a 2 zadania za 10 bodov. Na vypracovanie domácich úloh majú študenti jeden týždeň (zadanie bude zverejnené týždeň pred termínom odovzdania), počas semestra môže študent odovzdať max. 2 domáce úlohy po deadline bez straty bodov, inak sa udeľuje maximálne 1 bod (ak študent odovzdá riešenie do konca daného týždňa). Zadanie 1 bude zverejnené v prvom, Zadanie 2 v ôsmom týždni. Deadline pre domáce úlohy a zadania je v piatok 18:00.

Skúška má teoretickú a praktickú časť. Teoretická časť sa skladá zo štyroch testov, ktoré sa píšu počas semestra na prednáškach. Na skúške majú študenti možnosť znova napísať ľubovoľné časti aby si vylepšili celkové hodnotenie (do úvahy sa berie lepšie napísaný test). Praktická časť sa skladá z jedného projektu na programovanie. Úloha bude zverejnená deň pred skúškou, študenti na skúške obhajujú už hotové riešenia a následne rozšíria svoje riešenia. Na skúške potrebujete získať viac ako polovicu bodov na oboch častiach.

|        Zložka       | Body |
|:-------------------:|:----:|
|       10 úloh       |  20  |
|      2 zadanie      |  20  |
|       4 testy       |  40  |
| programovacia úloha |  20  |

Priebežné hodnotenie nájdete [tu](https://docs.google.com/spreadsheets/d/1zLwBEhnHpFwMagCywvC5Kt8dV10khDAKRXRIBCkh2P0/edit?usp=sharing).

### Domáce úlohy <a name="homeworks"></a>
1. [vývojové diagramy](assignments/homeworks.md#h1) (deadline 26. 2. 2021)
2. [list comprehensions a lambda výrazy](assignments/homeworks.md#h2) (deadline 5. 3. 2021)
3. [triediace algoritmy a generátory](assignments/homeworks.md#h3) (deadline 12. 3. 2021)
4. práca s chybami a výnimkami, ladenie kódu (deadline 19. 3. 2021)
5. unit testy (deadline 26. 3. 2021)
6. dynamické programovanie (deadline 9. 4. 2021)
7. vytvorenie triedy z UML diagramu (deadline 23. 4. 2021)
8. výpočet konštánt (deadline 30. 4. 2021)
9. biased random walk (deadline 7. 5. 2021)
10. grafické rozhranie pre zadanie 2 (deadline 14. 5. 2021)

### Zadania <a name="assignments"></a>
1. Algoritmické riešenie vybraných úloh (deadline 2. 4. 2021)
    * [Čakáme a čakáme](assignments/Znenie1-1.pdf)
    * [Fold, Check, Call, Raise...](assignments/Znenie1-2.pdf)
    * [projekt riešenia](assignments/assignment1.zip)

2. Simulácia účinku protiepidemiologických opatrení (deadline 14. 5. 2021)

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

[![Watch the video](https://img.youtube.com/vi/ZXsQAXx_ao0/0.jpg)](https://www.youtube.com/watch?v=ZXsQAXx_ao0)

