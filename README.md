# RideDiary
Käyttäjän on mahdollista pitää harrastus/treenipäiväkirjaa ratsastuksista sovelluksen avulla. Pienellä muokkauksella soveltuu myös muiden lajien kirjanpitoon.

## Dokumentaatio

[Käyttöohje](https://github.com/loeppoe/ot-harjoitustyo-ridediary/blob/master/dokumentaatio/kayttoohje.md)

[Vaatimusmäärittely](https://github.com/loeppoe/ot-harjoitustyo-ridediary/blob/master/dokumentaatio/maarittelydokumentti.md)

[Arkkitehtuurikuvaus](https://github.com/loeppoe/ot-harjoitustyo-ridediary/blob/master/dokumentaatio/arkkitehtuuri.md)

[Työaikakirjanpito](https://github.com/loeppoe/ot-harjoitustyo-ridediary/blob/master/dokumentaatio/tyoaikakirjanpito.md)


## Asennus

1.

```bash
poetry install
```

2. Käynnistä sovellus:

```bash
poetry run invoke start
```

## Komentorivitoiminnot

### Ohjelman suorittaminen

Ohjelman käynnistäminen:

```bash
poetry run invoke start
```

### Testaus

Testien suorittaminen:

```bash
poetry run invoke test
```

### Testikattavuus

Testikattavuusraportti:

```bash
poetry run invoke coverage-report
```

### Pylint

Tiedoston [.pylintrc](./.pylintrc) määrittelemät tarkistukset voi suorittaa komennolla:

```bash
poetry run invoke lint
```
