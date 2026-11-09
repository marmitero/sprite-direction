# P1 — Guia de direção artística (padrão aprovado)

**Estado:** P1 concluída em 09/11/2026, direção artística aprovada e congelada. As referências são moodboards conceituais, não sprites utilizáveis. P2 ainda não iniciada, aguardando autorização. Ver [termo P1](P1_APPROVAL.md).

## 1. Identidade visual

- MMORPG 2D isométrico 2:1; fantasia medieval sombria com personagens pixel art chibi.
- Estilo próprio, sem copiar personagens, cenários, UI ou símbolos de Diablo II/Mu Online.
- Silhuetas expressivas e legíveis no zoom nativo; contraste médio/alto, materiais reconhecíveis, texturas contidas.
- Iluminação pintada no sprite: luz principal difusa de alto-esquerda em coordenadas de tela; iluminação de efeitos dinâmicos pertence às camadas VFX, não é incorporada no corpo-base.
- Contorno externo seletivo de 1 pixel lógico (2 apenas quando a silhueta ou o tamanho justificarem); clusters coerentes, evitar ruído e dithering excessivo.
- Proibir filtros de suavização, antialiasing subpixel, gradientes borrados e alterações de tamanho da cabeça entre orientações.
- Personagens humanos devem manter anatomia compatível com equipamento modular. Cabeça chibi ~30–35% da altura corporal como alvo estético **a validar por piloto**, não especificação fechada.

## 2. Paleta técnica inicial

Fonte legível por máquina: [palette.p1.json](palette.p1.json). Os valores HEX são uma proposta de tons-base e não limitam cores auxiliares de sombra/realce. Tons neutros, terrosos e metálicos sustentam o cenário; azul, violeta, verde e brasa marcam habilidades sem dominar a leitura. Manter no máximo 3–5 faixas de valor por material por cluster local, com exceções justificadas.

## 3. Escala proposta, não congelada

- Grade isométrica: diamond 64×32 pixels (razão 2:1) **como referência dos documentos da cidade**.
- Para dimensionamento inicial, corpo humanoide de aproximadamente 40–48 px de altura visível, não necessariamente mesmo tamanho do canvas. Pequenos inimigos ~32–48 px; grandes ~64–96 px; edifícios ultrapassam vários tiles.
- Canvas experimental do corpo humanoide: 64×64 px **somente como ponto de partida de testes**, com expansão para golpe, arma e capa sem recortar. **Não** impor 48×48/64×64 a animações de efeitos grandes.
- A regra determinante é a relação personagem vs tile e ponto de contato no chão, não a ocupação integral da célula.
- Um pixel de arte equivale a um pixel do atlas; teste no scale 1×, 2× e 3× com nearest-neighbor. Nada de redimensionar sprites com interpolação bilinear.
- Primeira cidade 96×96 tiles lógicos; área de caça 160×160. Ambas são grades-alvo documentais, não arquivos já montados.

## 4. Direções (CONTRATO CANÔNICO)

Ordem técnica única e obrigatória no atlas: `N, NE, E, SE, S, SW, W, NW`. Em coordenadas de tela, N = parte superior, E = direita; S = parte inferior; W = esquerda. NE = diagonal superior direita; SE = diagonal inferior direita; SW inferior esquerda; NW superior esquerda. Não inverter rótulos (ex.: NO/SO são aliases de apresentação, mas os IDs de runtime são sempre NW/SW). Não espelhar automaticamente anatomia, sombras direcionais, armas ou acessórios assimétricos.

Representar orientações próprias do mesmo modelo sem alterar roupa, cor, escala, comprimento de membros ou posicionamento do apoio.

## 5. Ancoragem e perspectivas

- Pivô do personagem no solo, à projeção central entre os pés (mesmo pixel lógico de origem ao longo de toda animação).
- Oscilação do corpo dentro do frame é deliberada; o pivô do mundo não acompanha bob vertical aparente.
- Separar *root motion* (posição real no mapa controlada pela engine) de deformação/deslocamento aparente no atlas.
- Para tiles: largura vetorial de referência 64px e altura de losango 32px; paredes, telhados e props têm extensão vertical independente do tile-base.
- Ordenação base por profundidade de contato no chão; camadas de telhado, vegetação e objetos podem ocultar parcialmente jogadores sem apagar sprites.
- O sentido lateral de arma, escudo, ombreira e cabelo tem de ser registrado em cada direção; não depender de ordem de camada fixa para tudo.

## 6. Arquitetura modular de arte

Corpo-base com roupa íntima medieval discreta e opaca, sem arma, túnica, elmo ou armadura fixos. Variantes equipáveis: `hair`, `head`, `chest`, `shoulders`, `arms`, `hands`, `legs`, `feet`, `back`, `main_hand`, `off_hand`, `accessories`.

Todas as camadas seguem mesma animação, mesmo frame e mesmo pivô; posições por frame podem ter ajustes locais de arma e mão. Coleta de âncoras `head`, `left_hand`, `right_hand`, `back`, `ground` será requisito da P2; arte P1 não promete funcionamento do sistema.

## 7. Amostras-piloto a validar

1. **Humanoide neutro/espadachim**: personagem sem roupa fixa de classe, oito poses coerentes de Idle em ângulos principais, uma pose com armadura ilustrativa separada.
2. **Goblin**: pequeno, pele verde e postura curvada; oito vistas em escala consistente e arma bem posicionada.
3. **Ferreiro**: pose de trabalho vista isométrica, bigorna e martelo em componentes separados para futura animação de 40 frames.
4. **Ambiente**: tile 64×32 de pedra e terra, bloco de parede, árvore, prop de oficina e um canto de rua.

**Importante:** moodboards de IA não devem ser recortados e chamados de sprites funcionais sem refazer e validar os frames. Eles podem conter textos, tamanhos ou direcionamentos incorretos; somente este guia e os schemas canônicos controlam a execução.

## 8. Animação, fluidez e recontagem autorizada

O usuário autorizou recálculos e correções de frames quando melhorarem a fluidez ou o funcionamento. Regra:
- As linhas de animação e suas fases (antecipação, ação, impacto, recuperação e loop) têm precedência sobre totais declarados que não conferem.
- Não adicionar frames como preenchimento aritmético. Uma alteração exige motivo visual/técnico, antes/depois, duração/FPS, amostra e QA da nova versão.
- Caso um ciclo de corrida exija frames intermediários, acrescentar somente onde o movimento apresenta artefatos verificáveis, sincronizando todos os overlays da ação.
- Nunca interpolar por filtros que destruam pixel art; movimentos de armas, projéteis e VFX podem usar pontos de encaixe e eventos independentes.
- Registros obrigatórios: `docs/art-direction/FRAME_RECONCILIATION.md`, manifestos e notas de QA.
- Não transformar hold de VFX em novos frames corporais sem mudança documentada de escopo.

## 9. Critérios de aceite P1 (aceite visual; testes de runtime em etapas posteriores)

- [x] Direção artística de humanoide aprovada conceitualmente; sprite funcional 1× ainda não gerado.
- [x] Referência estética de inimigo aceita; oito vistas funcionais ainda precisam ser geradas e testadas.
- [x] Referência estética de NPC/objetos aceita; sprites de runtime ainda pendentes.
- [x] Referência estética de cenário/prop aprovada; tiles funcionais ainda pendentes.
- [x] Paleta, sombreamento, perspectiva e faixas de escala documentadas e congeladas como baseline.
- [x] Aceite veio de declaração expressa do usuário, não de selos nos moodboards.
- [ ] Autorização para iniciar P2 — ainda não concedida.

**Resultado:** direção visual homologada e P1 encerrada; assets funcionais e execução de P2 continuam pendentes.
