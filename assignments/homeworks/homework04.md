# Domáca úloha 4
Na úložisku pre odovzdávanie zadaní nájdete Python skript s názvom `h04.py`, ktorý obsahuje jednoduchú funkciu a jej krátky popis. Kód je ale napísaný optimisticky, teda predpokladá, že vstupy vždy budú spĺňať požadované predpoklady, alebo obsahuje drobnú implementačnú chybu. Vašou úlohou je opraviť funkciu tak, aby ste predišli generickým chybám a výnimkám. Chybám môžete predísť buď cez použitie konštruktu `try-except` alebo kontrolou hodnôt pred použitím operácie, ktorá môže spôsobiť chybu.

Pri špecifikácii funkcie nájdete aj položku TODO, ktorá načrtne, aké kontroly a zmeny potrebujete v kóde urobiť, ako aj nápady, na ktoré možné chyby sa môžete zamerať.

Kód teda potrebujete rozšíriť nasledovne:

1. skontrolovať hodnotu vstupných parametrov podľa špecifikácie (správny typ, správny formát, platná hodnota); ak podmienky nie sú splnené, vygenerujte chybu s príslušnou chybovou správou.
2. otestovať a v prípade potreby doladiť kód aby spĺňal špecifikáciu - kód môže obsahovať chyby, ktoré úplne znemožnia jeho správny beh (napr. zle nastavené limity pri for cykle); unit testy nemusíte písať, stačí ak kód otestujete manuálne na rôznych vstupoch, aby ste odhalili možné chyby.
3. ošetriť možné výnimky - kód sa môže spoliehať na platnosť niektorých predpokladov na vstup alebo využíva štandardné funkcie jazyka Python, ktoré môžu spôsobiť výnimku počas behu programu. Identifikujte tieto možné chyby a ošetrite ich blokom `try - except` alebo kontrolou hodnôt ešte pred ich použitím. V oboch prípadoch vygenerujte chybu s príslušnou chybovou správou (nepoužívajte iba štandardné výpisy z Pythonu).

## Štruktúra riešenia
Upravte priamo súbor `h04.py` podľa špecifikácie úlohy.

## Hodnotenie
Za domácu úlohu môžete získať maximálne 1 bod:

* 0,5 bodov získate za kontrolu vstupných hodnôt,
* 0,5 bodov získate za spracovanie a generovanie chýb.

## Deadline
Vaše riešenie nahrajte do 17. 3. 2023 (piatok), do 18:00.

