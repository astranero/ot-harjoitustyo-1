# Tehtävä 1: Monopoli

```mermaid
classDiagram
    class Noppa
    class Pelaaja
    class Pelinappula
    class Pelilauta
    class Ruutu

    Pelaaja : +Pelinappula pelinappula
    Ruutu : +Ruutu seuraava_ruutu
    Pelinappula : +Ruutu sijainti
```