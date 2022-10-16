# Lippukunnan varastonhallinta- ja lainaustyökalu
Harjoitustyö syksyn 2022 Tietokantasovellus-kurssille (HY)

Sovelluksen tarkoitus on ylläpitää tietokantaa partiolippukunnan varastossa säilöttävistä varusteista ja niiden lainoista.

Käyttäjätunnuksen tehtyään **käyttäjä** voi:
- Näkemään listan varaston tavaroista ja ovatko ne lainassa
- Lainaamaan ja palauttamaan varusteita
- Tutkailemaan omia lainojaan

**Ylläpitäjä** pystyy lisäksi
- Näkemään kaikki lainat
- Merkitsemään kaikki tavarat palautetuksi

Sovellusta voi testata [Herokussa](https://tsoha-lpkvarasto.herokuapp.com/).

Sovelluksesta löytyy valmiiksi seuraavat testitunnukset

| Käyttäjä | Salasana | Ylläpitäjä |
|----------|----------|------------|
|testiadmin| heko1934 |  kyllä     |
|  testi1  | salasana |   ei       |

## Jatkokehitysideoita
- Tavaroita voi lainata useamman kerralla
- Ylläpitäjä voi merkitä yksittäisiä tavaroita palautetuksi
- Ylläpitäjä voi lisätä ja poistaa tavaroita tietokannasta
