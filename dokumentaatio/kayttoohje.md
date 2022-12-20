# Käyttöohje

Lataa projektin viimeisimmän releasen lähdekoodi valitsemalla Assets-osion alta Source code.

## Ohjelman käynnistäminen
Ennen ohjelman käynnistämistä, asenna riippuvuudet komennolla:

```bash
poetry install
```

Nyt ohjelman voi käynnistää komennolla:

```
poetry run invoke start
```

## Pelaaminen

Peli käynnistyy välittömästi ohjelman käynnistyessä. 

Pelaaja 1 liikkuu W- ja S-näppäimistä, kun taas Pelaaja 2 liikkuu nuolinäppäimistä.
Tarkoituksena on pitää pallo menemästä oman mailan ohi maaliin, ja saada se toisen pelaajan maaliin.
Kun toinen pelaajista saa 10 pistettä, tämä pelaaja voittaa ja peli päättyy.
Pelin voi missä tahansa vaiheessa käynnistää uudelleen R-näppäimellä.
