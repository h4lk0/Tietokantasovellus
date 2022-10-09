# Lippukunnan varastonhallinta- ja lainaustyökalu
Harjoitustyö syksyn 2022 Tietokantasovellus-kurssille (HY)

## Välipalautus 9.10.
- Sovelluksen etusivulle pääsee [tästä](https://tsoha-lpkvarasto.herokuapp.com/)
- Sovellukseen voi luoda uusia käyttäjiä
- Kirjautunut käyttäjä näkee varaston inventaarion ja voi tehdä uusia lainoja
- Omalla sivullaan käyttäjä voi tutkia omia lainojaan ja palauttaa tavaroita
- Ylläpitäjä voi nähdä kaikki lainat

Sovellusta voi testata testitunnuksilla

| Käyttäjä | Salasana | Ylläpitäjä |
|----------|----------|------------|
|testiadmin| heko1934 |  kyllä     |
|  testi1  | salasana |   ei       |

## Tilanne 25.9.2022
- Sovelluksen etusivulle pääsee [tästä](https://tsoha-lpkvarasto.herokuapp.com/) **HUOM!** Kirjautuminen tai rekisteröinti ei vielä toimi
- Alustavaa versiota kirjautumisen jälkeisestä etusivusta pääsee tarkastelemaan [tästä](https://tsoha-lpkvarasto.herokuapp.com/frontpage)
- Tietokannan taulut on luotu ja niiden alustava sisältö on valmis
- Nettisivua on aloitettu
- **PUUTTUU**: kaikki käyttäjätunnuksiin liittyvät funktiot

## Alustava kuvaus 11.9.2022
Sovelluksen avulla on tarkoitus ylläpitää tietokantaa lippukunnan varastossa sijaitsevista varusteista.

**Käyttäjä** pystyy
- Näkemään listan varaston tavaroista ja ovatko ne lainassa
- Lainaamaan ja palauttamaan varusteita
- Tutkailemaan omia lainojaan

**Ylläpitäjä** pystyy lisäksi
- Lisäämään ja poistamaan tavaroita tietokannasta
- Näkemään kaikki lainat
