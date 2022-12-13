# OT-Harjoitustyö

(Nimi: Bussitt) Sovelluksen avulla käyttäjän on mahdollista nähdä tietokoneen terminaalista toivomansa pysäkin seuraavat 10 lähtevää bussia tarkastelu hetkestä alkaen. Käyttäjä voi myös tallentaa pysäkin muistiin seuraavaa käyttö kertaa varten. Näin hän voi nopeasti nähdä hänen suosikki pysäkkien lähtevät bussit yhdellä komennolla. Sovelluksessa voi myös hallinnoida omia bussi-aikataulu näkymiä lisäämällä, nimeämällä ja poistamalla niitä. 

Sovellus käyttää HSL:n tarjoamaa rajapintaa Helsingin julkisesta liikenteestä.

## Huomio Python-versiosta
Sovelluksen toiminta on testattu Python-versiolla 3.8. Etenkin vanhempien Python-versioiden kanssa saattaa ilmentyä ongelmia.

## Julkaistu versio
- [Release](https://github.com/sutigit/ot-harjoitustyo/releases)


## Käyttöohjeet
- [Käyttöohje](https://github.com/sutigit/ot-harjoitustyo/blob/master/bussitt-app/dokumentaatio/kayttoohjeet.md)

## Dokumentaatio

- [Vaatimusmäärittely](https://github.com/sutigit/ot-harjoitustyo/blob/master/bussitt-app/dokumentaatio/vaatimusmaarittely.md)
- [Tuntikirjanpito](https://github.com/sutigit/ot-harjoitustyo/blob/master/bussitt-app/dokumentaatio/tuntikirjanpito.md)
- [Arkkitehtuuri](https://github.com/sutigit/ot-harjoitustyo/blob/master/bussitt-app/dokumentaatio/arkkitehtuuri.md)
- [Changelog](https://github.com/sutigit/ot-harjoitustyo/blob/master/bussitt-app/dokumentaatio/changelog.md)
- [Release](https://github.com/sutigit/ot-harjoitustyo/releases)

## Komentorivitoiminnot

### Sovelluksen asennus ja käynnistys

Lataa sovellus kohdasta releases ja pura tiedosto haluamaasi hakemistoon.

Mene hakemistoon terminaalissa.

Varmista että poetry on asennettu suorittamalla komento
```
poetry --version
```

Varmista että python3 versio on korkeampi kuin 3.8 komennolla
```
python3 --version
```

Mene Bussitt-app hakemiston sisään 
```
cd Bussitt-app
```

Suorita 
```
poetry install
```

Asennuksen jälkeen ohjelman voi käynnistää komennolla 
```
poetry run invoke start
```



### Sovelluksen testaus

Suorita testit komennolla

```
poetry run invoke test
```

### Sovelluksen testikattavuus

Generoi sovelluksen testikattavuus komennolla

```
poetry run invoke report
```
Raportti generoituu htmlcov-hakemistoon
