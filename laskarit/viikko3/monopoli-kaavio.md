```mermaid
 classDiagram
      Peli "1" --> "1" Pelilauta
	Peli "1" --> "2" Noppa
	Peli "1" --> "2...8" Pelaaja
	Pelilauta "1" --> "40" Peliruutu
	Peliruutu "1" --> "*" Pelinappula
	Peliruutu "*" --> "1" Toiminto
	Kortti "1" --> "1" Toiminto
	Pelaaja "1" --> "1" Pelinappula
	Sattuma_yhteismaa "1" --> "1" Kortti	

	Peliruutu : +Peliruutu seuraava
	Peliruutu : +String tuomio
	Peli : +Peliruutu aloitus
	Peli : +Peliruutu vankila

	Peliruutu <|-- Aloitusruutu
	Peliruutu <|-- Vankila
	Peliruutu <|--  Sattuma_yhteismaa
	Peliruutu <|-- Asema_laitos
	Peliruutu <|-- Normaali

	Sattuma_yhteismaa : +Kortti kortti
	Normaali : +Pelaaja omistaja
	Pelaaja : +int rahaa
	

      class Peli{
      }
```
