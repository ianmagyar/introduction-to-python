# Programovanie v jazyku Python

**Programovanie v jazyku Python** je kurz programovania ponúkaný v letnom semestri prvého ročníka bakalárskeho štúdia pre študijný program Inteligentné systémy. Predmet nadväzuje na kurz [Základy algoritmizácie a programovania](https://kurzy.kpi.fei.tuke.sk/zap/). Venuje sa pokročilým témam programovania v jazyku Python, ako údajové štruktúry, základné algoritmy, návrh a analýza algoritmov, objektovo orientované programovanie, modelovania a vytvorenie simulácií. Úspešný absolvent predmetu je schopný napísať zložitejšie kódy, porozumieť kódom napísaným inými programátormi, namapovať problémy z rôznych domén na výpočtové problémy a vyhodnotiť navrhnuté riešenia.

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
Prednášky sú vo štvrtok o 13:30 v miestnosti L4 v budove PK7. Účasť na prednáške nie je povinná.

Cvičenia sú v pondelok o 9:10 (PK6_S02 - PC1), a v utorok o 7:30 (PK6_S02 - PC1), 9:10 (V4_147) a 10:50 (PK6_107 - PC16). Účasť na cvičeniach je povinná, študent môže mať maximálne tri neúčasti za semester. Neúčasť môžete nahradiť účasťou na inom cvičení po dohode s vyučujúcim alebo vypracovaním cvičenia pre daný týždeň a poslaním riešenia vyučujúcemu.

[Orgnizačné informácie o predmete nájdete v tomto dokumente.](lectures/Lecture-00.pdf)

|                               |                  Cvičenie                 |                           Prednáška                          |                        Termíny                          |
|:-----------------------------:|:-----------------------------------------:|:------------------------------------------------------------:|---------------------------------------------------------|
|  1. týždeň<br>12. 2. - 18. 2. |   [Nastavenie programátorského prostredia](labs/lab01-setting-up.ipynb)  |        [Syntax, jazykové konštrukty](lectures/Lecture-01.pdf)<br>([kód z prednášky](lectures/codes/lecture01.ipynb))        |            [Z1 publikované](assignments/Zadanie1.pdf)<br>[D1 publikovaná](assignments/homeworks/homework01.md)             |
|  2. týždeň<br>19. 2. - 25. 2. |          [Prvé programy v Pythone](labs/lab02-first-baby-steps.ipynb)          |         [Funkcie, rekurzia, generátory, lambda výrazy](lectures/Lecture-02.pdf)<br>([kód z prednášky](lectures/codes/lecture02.ipynb))         |             D1 odovzdávka<br>[D2 publikovaná](assignments/homeworks/homework02.md)             |
|  3. týždeň<br>26. 2. - 3. 3.  |               [Algoritmizácia](labs/lab03-functions-and-algorithmization.ipynb)              |                [Reťazce, zoznamy, n-tice, mapy](lectures/Lecture-03.pdf)<br>([kód z prednášky](lectures/codes/lecture03.ipynb))                |             D2 odovzdávka<br>[D3 publikovaná](assignments/homeworks/homework03.md)             |
|  4. týždeň<br>4. 3. - 10. 3.  | [Práca so základnými údajovými štruktúrami](labs/lab04-a-look-at-the-table.ipynb) |        Test1<br>[Testovanie, ladenie, výnimky a chyby](lectures/Lecture-04.pdf)<br>([kód z prednášky](lectures/codes/lecture04.ipynb))         |             D3 odovzdávka<br>[D4 publikovaná](assignments/homeworks/homework04.md)             |
|  5. týždeň<br>11. 3. - 17. 3. |                   [Wordle](labs/lab05-wordle.ipynb)                  | Zložitosť algoritmov, optimalizácia, dynamické programovanie |         Z1, D4 odovzdávka<br>Z2, D5 publikované         |
|  6. týždeň<br>18. 3. - 24. 3. |             Kedy na Jedličku?             |    Test 2<br>Úvod do objektovo orientovaného programovania   |             D5 odovzdávka<br>D6 publikovaná             |
|  7. týždeň<br>25. 3. - 31. 3. |             Wordle pomocou OOP            |                           Veľká Noc                          |                     D6 odovzdávka                       |
|  8. týždeň<br>1. 4. - 7. 4.   |                 Veľká Noc                 |                   Princípy OOP a metametódy                  |                     D7 publikovaná                      |
|  9. týždeň<br>8. 4. - 14. 4.  |     Modelovanie hry poker pomocou OOP     |                         OOP v Pythone                        |           Z2, D7 odovzdávka<br>Z3 publikované           |
| 10. týždeň<br>15. 4. - 21. 4. |           Výpočet hodnoti pi              |                Test 3<br>Jednoduché simulácie                |                     D8 publikovaná                      |
| 11. týždeň<br>22. 4. - 28. 4. |   Simulácia letu komára, návrh simulácií  |                Výpočtové modely a simulácie                  |           D8 odovzdávka<br>D9, D10 publikované          |
| 12. týždeň<br>29. 4. - 5. 5.  |          Vývoj hier v Pythone             |                   Vedecké výpočty v Pythone                  |                      D9 odovzdávka                      |
| 13. týždeň<br>6. 5. - 12. 5.  |            odovzdávanie zadaní            |                    Test 4<br>opravné testy                   |             Z3 odovzdávka<br>D10 odovzdávka             |

## Hodnotenie <a name="grading"></a>

Celkové hodnotenie predmetu je 100 bodov (40 + 60 bodov); študent musí získať viac ako polovicu bodov zo zápočtu a zo skúšky.

Zápočet sa skladá z dvoch častí: 10 domácich úloh po 1 bod, a 3 zadania za 10 bodov. Na vypracovanie domácich úloh majú študenti jeden týždeň (zadanie bude zverejnené týždeň pred termínom odovzdania), počas semestra môže študent odovzdať max. 2 domáce úlohy po deadline bez straty bodov, inak sa udeľuje maximálne 0,5 boda (ak študent odovzdá riešenie do konca daného týždňa). Zadanie 1 bude zverejnené v prvom, Zadanie 2 v piatom, a Zadanie 3 v deviatom týždni semestra. Deadline odovzdania domácich úloh a zadaní je v piatok 18:00.

Skúška má teoretickú a praktickú časť. Teoretická časť sa skladá zo štyroch testov, ktoré sa píšu počas semestra na prednáškach. Na skúške majú študenti možnosť znova napísať ľubovoľné časti, aby si vylepšili celkové hodnotenie (do úvahy sa berie lepšie napísaný test). Praktická časť sa skladá z jedného projektu na programovanie. Úloha bude zverejnená deň pred skúškou, študenti na skúške obhajujú už hotové riešenia a následne rozšíria svoje riešenia. Na skúške potrebujete získať viac ako polovicu bodov z oboch častí.

|        Zložka       | Body |
|:-------------------:|:----:|
|       10 úloh       |  10  |
|      3 zadania      |  30  |
|       4 testy       |  40  |
| programovacia úloha |  20  |

### Domáce úlohy <a name="homeworks"></a>
1. [ciele a očakávania](assignments/homeworks/homework01.md) (deadline 23. 2. 2024)
2. [funkcie](assignments/homeworks/homework02.md) (deadline 1. 3. 2024)
3. [použitie lambda výrazov a list comprehension](assignments/homeworks/homework03.md) (deadline 8. 3. 2024)
4. [ošetrenie chýb](assignments/homeworks/homework04.md) (deadline 15. 3. 2024)
5. písanie unit testov (deadline 22. 3. 2024)
6. vytvorenie triedy z UML diagramu (deadline 29. 3. 2024)
7. hierarchia tried a metametódy (deadline 12. 4. 2024)
8. generovanie grafov (deadline 26. 4. 2024)
9. použitie knižníc numpy a pandas (deadline 3. 5. 2024)
10. oprava DÚ (deadline 10. 5. 2024)

### Zadania <a name="assignments"></a>
Vypracované riešenie - skripty - nahrajte priamo do priečinka na Google Drive (**nevytvorte samostatný priečinok!**).

1. Šípky (deadline 15. 3. 2024)

    * [Znenie zadania](assignments/Zadanie1.pdf)
    * [Projekt s testmi](assignments/Assignment1.zip)

2. Ideme na teambuilding (deadline 12. 4. 2024)
3. *TBA* (deadline 10. 5. 2024)
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
