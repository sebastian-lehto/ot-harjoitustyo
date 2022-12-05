[työaikakirjanpito](https://github.com/sebastian-lehto/ot-harjoitustyo/blob/master/dokumentaatio/tuntikirjanpito.md)

[vaativuusmäärittely](https://github.com/sebastian-lehto/ot-harjoitustyo/blob/master/dokumentaatio/vaatimusmaarittelu.md)

[changelog](https://github.com/sebastian-lehto/ot-harjoitustyo/blob/master/dokumentaatio/changelog.md)

[arkkitehtuuri](https://github.com/sebastian-lehto/ot-harjoitustyo/blob/master/dokumentaatio/arkkitehtuuri.md)

[release viikko 5](https://github.com/sebastian-lehto/ot-harjoitustyo/releases/tag/viikko5)

--

## Asennus

1. Asenna riippuvuudet komennolla:

```bash
poetry install
```

2. Käynnistä sovellus komennolla:

```bash
poetry run invoke start
```

## Komentorivitoiminnot

### Ohjelman suorittaminen

Ohjelman pystyy suorittamaan komennolla:

```bash
poetry run invoke start
```

### Testaus

Testit suoritetaan komennolla:

```bash
poetry run invoke test
```

### Testikattavuus

Testikattavuusraportin voi generoida komennolla:

```bash
poetry run invoke coverage-report
```

Raportti generoituu _htmlcov_-hakemistoon.
