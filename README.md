# Autonomous Agents and Multi-Agent Systems' Project
## Snake Royale

### Group 64

| Number | Name              | User                                  | Email                                            |
| -------|-------------------|---------------------------------------|--------------------------------------------------|
| 84699  | André Santos      | <https://github.com/Andregss97>       | <mailto:andre.s.dos.santos@tecnico.ulisboa.pt>   |
| 84721  | Gonçalo Cruz      | <https://github.com/Cruziper>         | <mailto:goncalo.garcia.cruz@tecnico.ulisboa.pt>  |
| 79730  | João Silva        | <https://github.com/Vadstena>         | <mailto:jonasprs@hotmail.com>                    |

- 4 cobras em busca de fruta, que procuram crescer à medida que se alimentam (1 px por fruta), com o objetivo de não chocarem umas com as outras;

- para além da fruta espalhada pelo board teríamos também:

    - cubos de gelo que congelariam a ação de todas as cobras adversárias, temporariamente;

    - bombas que retirariam 1 ponto a quem a capturasse e 4 a todas as cobras adversárias;

- no centro de um tabuleiro existe um " food dispenser" com períodos de "cooldown" que distribui pontos por todas as cobras (s1, s2, s3,s4) que colaborassem na sua ativação, da seguinte forma:
    - (  8, -8, -8, -8); em que apenas uma colabora;

    - (  6,  6, -6, -6); em que duas colaboram;

    - (  3,  3,  3, -3); em que três colaboram;

    - (  1,  1,  1,  1); em que as quatro colaboram;

Apesar desta última tarefa ser passível de colaboração, não deixa de ser uma ação de interesse individual, pelo que o sistema será 100% competitivo.

As 4 cobras que idealizámos, para além de procurarem fruta, teriam as seguintes configurações:

s1 : prioriza o "food dispenser";

s2 : prioriza os cubos de gelo e as bombas;

s3 : opta sempre pela ação de maior reward (greedy);

s4 : procura apenas comida;

Se a comida acabar no tabuleiro, todas as cobras devem priorizar o "food dispenser". O jogo acaba quando uma das cobras atinge os 30 px.

As métricas seriam pontos acumulados, tamanho da cobra, fruta comida, ...
