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
          ball
          is_over
      }
