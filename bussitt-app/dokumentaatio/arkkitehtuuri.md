# Arkkirehtuurikuvaus
## Rakenne
Seuraava kaavio havainnollistaa koodin rakennetta ja sen eri tiedostojen yhteyksiä toisiinsa. Nuolen kulku suunta osoittaa missä import lause moduulille tapahtuu.

Koodin tiedosto rakenne on seuraavanlainen.

```mermaid
flowchart RL
    ui([ui.py]) --> main([main.py])
    display([display.py]) --> main([main.py])
    api{api} --> ui([ui.py])
```
</br>

```mermaid
flowchart RL
    query([query.py]) --> api{api}
```

</br>
</br>

### Huomioitavaa
myutils.py sisältää yleisiä työkalu funktioita. Jokainen seuraavista tiedostoista sisältää tämän tiedoston.

```mermaid
flowchart LR
    myutils([myutils.py]) --> main([main.py])
    myutils([myutils.py]) --> ui([ui.py])
    myutils([myutils.py]) --> display([display.py])
    myutils([myutils.py]) --> query([query.py])
```

## Käyttöliittymä