# Domáca úloha 7
Na úložisku pre odovzdávanie zadaní nájdete skript s názvom `h07.py`, ktorý obsahuje definíciu dvoch tried `ClassA` a `ClassB`. Vašou úlohou je doplniť implementáciu triedy `ClassB`, a to nasledovne:

* upraviť definíciu triedy tak, aby `ClassB` bola podtriedou (dedila od) triedy `ClassA`,
* upraviť konštruktor triedy `ClassB` tak, aby volal konštruktor nadtriedy (teda konštruktor triedy `ClassA`),
* prepísať metódu `foo` v triede `ClassB` podľa úlohy v komentároch v skripte; definícia metódy musí obsahovať volanie metódy `foo` z nadtriedy.

Na konci skriptu nájdete testovacie objekty a volanie metód `foo` a `bar` nad nimi. Do komentárov napíšte, implementácia metódy z ktorej triedy sa zavolá na danom riadku, máte na to vyhradené miesto - odpovede napíšte namiesto `...`.

## Hodnotenie
* `ClassB` je podtriedou `ClassA` - 0,5b
* konštruktor triedy `ClassB` správne opravený - 0,5b
* metóda `foo` je prepísaná správne v `ClassB` - 0,5b
* správne odpovede pri volaniach metód - 0,5b
