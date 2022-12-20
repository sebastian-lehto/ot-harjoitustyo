## Luokkakaavio
```mermaid
 classDiagram
      Ball "1" --> "1" Game
      class Ball {
          x
          y
          x_speed
          y_speed
      }
      class Game {
          p1score
          p2score
          p1y
          p2y
          ball
          is_over
      }
```
## Pelin etenemisen sekvenssikaavio
```mermaid
sequenceDiagram
  actor User
  participant Index
  participant Game
  participant Ball
  User->>Index: Starts game
  Index->>Game: tick()
  Game->>Ball: move()
  Game->>Ball: flip_y()
  Game->>Ball: flip_x()
  Game->>Ball: reset()
```

Pelin käynnistyessä suoritetaan Index-luokan main-metodi alustaa tarvittavat muuttujat, ja aloittaa while-silmukan suorituksen,
jossa kutsutaan jatkuvasti Game-olion tick-metodia ja pelin osat piirretään ruudulle Game-olion tietojen perusteella.
Pallon osuessa "kattoon" tai "lattiaan" kutsutaan pallon flip_y-metodia, pallon osuesssa mailaan taas kutsutaan flip_x-metodia.
Kun toinen pelaajista tekee maalin, kutsutaan Game-olion reset-metodia.
