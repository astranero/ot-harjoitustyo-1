# Arkkirehtuurikuvaus
## Rakenne
Seuraava kaavio havainnollistaa koodin rakennetta ja sen eri luokkien/moduulien yhteyksiä. Pakkausrakenne on seuraavanlainen:

```mermaid
flowchart TB
    subgraph ui
    Ui
    Display
    end

    ui -.-> Main

    Main -.- my_recordings

    subgraph my_recordings
    record_api.py
    records.json

    record_api.py -.- records.json
    end

    Main -.- api

    subgraph api
    api.py
    end
```
</br>

### Huomioitavaa
myutils.py sisältää yleisiä työkalu funktioita ja on importattu kaikkiin luokkiin ja moduuleihin

```mermaid
flowchart BT
    subgraph ui
    Ui
    Display
    end

    subgraph api
    api.py
    end

    subgraph my_recordings
    record_api    
    end

    myutils -.-> Main
    myutils -.-> Ui
    myutils -.-> Display
    myutils -.-> record_api
    myutils -.-> api.py
```

## Käyttöliittymä
Käyttöliittymän päätoimintaperiaate on, että käyttäjä voi tarkastella bussi-aikatauluja, joita hän on itse sovelluksen avulla etsinyt ja tallentanut.
Käyttäjälle tarjotaan myös mahdollisuutta muokata tekemisiään jälkikäteen.

Käyttöliittymä sisältää 3 päänäkymää.
- Etusivu näkymä
- Bussi-aikataulu näkymä
- Hallinta näkymä

### Etusivu näkymä
Tämä näkymä toimii sovelluksen kotivalikkona. Näkymä tarjoaa tietoa siitä, saako sovellus onnistuneesti yhteyden HSL-rajapintaan, paikallisen ajan, valikon siitä mitä käyttäjä haluaa seuraavaksi tehdä ja tallennetut bussi-aikataulut.

### Bussi-aikataulu näkymä
Tämä komponentti on vastuussa ainoastaan bussi-aikataulujen näyttämisestä.

### Hallinta näkymä
Tämä näkymä tarjoaa käyttäjälle mahdollisuuden hallinnoida tallennettuja bussi-aikatauluja, muokkaamalla ja poistamalla näitä jälkikäteen.


</br>
Näkymät voivat olla näkyvissä yksi kerrallaan tai samanaikaisesti. Käyttöliittymä ohjaa myös käyttäjää eri toiminnoissa eteenpäin vaihe kerrallaan,josta koostuu sovelluksen muut näkymät.

## Sovelluslogiikka
--
## Tietojen pysyväistallennus
Tiedot pysyväistallennetaan sovelluksen mukana tulevaan `records.json` tiedostoon. Tiedosto on sijoitettu `my_recordings` kansioon. Tallennuslogiikasta vastaa samassa kansiossa sijaitseva `records_api.py`. `records_api.py` on käytössä ainoastaan `Main` luokasta.

## Päätoiminnallisuudet
### Alkuvalikko
Kun käyttäjä käynnistää sovelluksen, etenee sovelluksen kontrolli seuraavasti:

```mermaid
sequenceDiagram
    participant Main
    participant Ui
    participant Display
    participant record_api
    actor Käyttäjä
    
    Note over Main: Sovellus tarkistaa käyttäjän komentorivi argumentit
    Note over Main: luo ui-olio
    Note over Main: luo display-olio

    Main->>Main: start()
    Note over Main: Hakee tallennetut aikataulut
    Main->>record_api: get_records_file()
    Note over Main: Näyttää olemassaolevat aikataulut
    Main->>Display: render_timetable_list()
    Main->>Ui: ask_action()
    Ui->>Käyttäjä: Pyytää käyttäjältä toimintoa
```
</br>
</br>

### Bussi-aikataulun hakeminen ja tallentaminen
Bussi-aikataulun hakeminen ja tallentaminen on jaettu kahteen vuokaavioon. 
Ensimmäisenä kuvataan bussi-akataulun hakemista ja toiseksi sen tallentamista pysyväistallennukseen.

### Aikataulun hakeminen
Kun käyttäjä hakee bussi-aikataulua, etenee sovelluksen kontrolli seuraavasti:

```mermaid
sequenceDiagram
    actor Käyttäjä
    participant Ui
    participant Main
    participant api
    participant Display
    
    Käyttäjä->>Ui: Valitsee "Add timetable"-toiminnon
    Ui-->>Main: toiminto
    Main->>Main: get_timetable()
    Main->>Ui: ask_search_word()
    activate Ui
    Ui-)Käyttäjä: Pyytää käyttäjältä bussipysäkille hakusanaa
    activate Käyttäjä
    Käyttäjä-->>Ui: Antaa bussipysäkille hakusanan
    deactivate Käyttäjä
    Ui-->>Main: hakusana
    deactivate Ui
    Main-)api: fetch_search_options(hakusana)
    activate api
    api-->>Main: JSON data: pysäkki vaihtoehtoja
    deactivate api
    Main->>Ui: choose_search_option(pysäkki vaihtoehdot)
    activate Ui
    Ui-)Käyttäjä: Pyytää käyttäjää valitsemaan tarjotuista bussi-pysäkki vaihtoehdoista
    activate Käyttäjä
    Käyttäjä-->>Ui: Antaa täsmällisen bussipysäkin
    deactivate Käyttäjä
    Ui-->>Main: bussipysäkki
    deactivate Ui
    Main->>Main: display_timetable()
    Main-)api: fetch_timetable(bussipysäkki)
    activate api
    api-->>Main: JSON data: aikataulu data
    deactivate api
    Main->>Display: render_timetable(aikataulu data)

```

#### Aikataulun tallentaminen
Kun käyttäjä tallentaa bussi-aikataulun, etenee sovelluksen kontrolli seuraavasti:

```mermaid
sequenceDiagram
    actor Käyttäjä
    participant Ui
    participant Main
    participant record_api
    participant records.json
    
    Ui->>Käyttäjä: Kysyy käyttäjältä tallenetaanko aikataulu
    activate Käyttäjä
    Käyttäjä->>Ui: Valitsee "yes"
    deactivate Käyttäjä
    Ui-->>Main: toiminto
    Main->>Main: save_timetable() 
    Main->>Ui: get_timetable_info()
    activate Ui
    Ui-->>Main: Aikataulu informaatio
    deactivate Ui
    Main->>Ui: get_timetable_custom_name()
    activate Ui
    Ui->>Käyttäjä: Kyysyy käyttäjältä bussi-aikataululle nimeä
    activate Käyttäjä
    Käyttäjä-->>Ui: Antaa nimen
    deactivate Käyttäjä
    Ui-->>Main: Aikataulu nimi
    deactivate Ui
    Note over Main: Luodaan tallennusta varten data objekti 
    Main->>record_api: save_timetable(data)
    record_api->>records.json: get_records_file()
    activate records.json
    records.json-->>record_api: Nykyinen tallennuksen
    deactivate records.json
    Note over record_api: Jos aikataulu on olemassa, niin korvataan vanha uudella
    Note over record_api: Luodaan uusi aikataulu
    record_api->>records.json: Kirjoitetaan records.json tiedostoon uusi aikataulu kirjaus.



```