# Käyttöohjeet
Sovellus on terminaalissa käytettävä komentorivi-sovellus. Sovellusta käytetään sen tekstikäyttöliittymän avulla.

## Lataus
Lataa projekti kohdasta releases.

## Asennus ja käynnistys
Mene bussitt-app hakemiston sisään. Jos olet samassa kansiossa mistä löytyy src kansio ja pyproject.toml, asenna riippuvuudet.
```
poetry install
```

Käynnistä sovellus
```
poetry run invoke start
```


## Käyttö
### Lisää aikataulu
1. Lisää uusi aikataulu valitsemalla add timetable
2. Sovellus kysyy bussipysäkille nimeä. 
Bussipysäkin nimi voi olla sen nimi tai tunnistekoodi. Esim kamppi tai h1249.
3. Sovellus antaa annettua hakusanaa vastaavat bussipysäkki vaihtoehdot. Valitse jokin vaihtoehdoista. (Jatkossa bussipysäkkiä kohtaan on enemmän tietoa helpottamaan valintaa.)
4. Sovellus näyttää valitun aikataulun tiedot ja 10 seuraavaa lähtevää bussia hakuhetkestä alkaen.
5. Sovellus kysyy haluatko tallentaa aikataulun.
6. Jos valitsit kyllä, sovellus kysyy nimeä aikataululle, jonka jälkeen bussiaikataulu tallennetaan ja näkymä siirtyy takaisin kotivalikkoon.

### Katso aikataulua
1. Jos sinulta löytyy tallennettuja aikatauluja, niin voit valita tarkastella niitä valitsemalla view timetable.
2. Sovellus kysyy tarkennusta mitä aikataulua haluat katsella nimen perusteella
3. Valitse haluamasi vaihtoehto

### Hallinnoi aikataulua
1. Jos sinulla sinulta löytyy tallennettuja aikatauluja, voit valita manage timetables ja sovellus tarjoaa vaihtoehdon poistaa tai uudelleen nimetä valitsemasi aikataulu.
2. Jos valitsis delete timetable, sovellus tarjoaa aikataulu vaihtoehdot jonka voit poistaa.
3. Jos valitsit rename timetable, sovellus tarjoaa aikataulu vaihtoehdot joita voit uudelleen nimetä. Valinnan jälkeen sovellus kysyy uutta nimeä aikataululle.

### Poistuminen
1. Valitse Quit


