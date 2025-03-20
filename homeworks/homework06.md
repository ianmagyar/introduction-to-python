# Domáca úloha 6
Na úložisku pre odovzdávanie zadaní nájdete Python skript s názvom `h06.py`, ktorý obsahuje jednoduchú funkciu s funkciou pre jej testovanie. Vašou úlohou je implementovať testovaciu funkciu, a pomocou nej odhaliť a opraviť chyby v implementácii funkcie. Pri testovaní používajte kľúčové slovo `assert`.

Implementáciu funkcie otestujte na nasledovných vstupoch:

* nesprávny vstup (min. 3 testy) - v takýchto prípadoch funkcia väčšinou iba ukončí vykonávanie (cez return) alebo sa automaticky vygeneruje výnimka. Je na vás, či to necháte tak, alebo pridáte špeciálnu návratovú hodnotu pre indikáciu nesprávneho vstupu. Nesprávny vstup môže byť hodnota nesprávneho typu, alebo hodnota nespĺňajúca všetky predpoklady na vstup. Ak ponecháte generovanie chyby ako spracovanie nesprávneho vstupu, nezabudnite na správne overenie fungovania programu v testovacej funkcii.
* extrémny vstup - mali by reprezentovať hraničné situácie, kde implementácia môže mať problémy, napríklad malé a veľké vstupné hodnoty; typický príklad je spracovanie hodnoty 0 alebo prázdneho reťazca/zoznamu a pod. Pri niektorých funkciách extrémne prípady neexistujú.
* platné vstupy - otestujte návratovú hodnotu alebo účinok funkcie pre minimálne 10 platných vstupov.

Testy napíšte iba zavolaním funkcie a porovnaním vypočítanej a očakávanej návratovej hodnoty (použite kľúčové slovo `assert`). Príklad nájdete v ukážkovom kóde k prednáške 5. Testy vám môžu pomôcť pri odhalení chyby v implementácii. Prispôsobujte vždy implementáciu testom, a nie naopak!

## Štruktúra riešenia
Upravte priamo súbor `h06.py` podľa špecifikácie úlohy.

## Hodnotenie
Za domácu úlohu môžete získať maximálne 1 bod:

* 0,5 bodov získate za testovanie správnosti implementácie pre správne vstupy (minimálne 10 testov),
* 0,5 bodov získate za testovanie na neplatných a hraničných vstupoch.

## Deadline
Vaše riešenie nahrajte do 28. 3. 2025 (piatok), do 18:00.
