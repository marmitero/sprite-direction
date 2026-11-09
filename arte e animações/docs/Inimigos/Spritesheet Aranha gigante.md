# INIMIGO ARANHA GIGANTE — SPRITESHEET COMPLETA EM 8 DIREÇÕES

Crie um conjunto completo de spritesheets para uma **Aranha Gigante de RPG 2D isométrico, inspirado em Diablo II, com estética Pixel Art Chibi e fantasia medieval sombria**.

A Aranha Gigante deve ser um inimigo de porte médio a grande, com aparência ameaçadora, movimentos aracnídeos realistas e comportamento predatório. Apesar das proporções chibi, deve transmitir perigo, agilidade e uma sensação inquietante através de seus movimentos.

O inimigo deve possuir **8 patas articuladas, abdômen volumoso, presas venenosas, múltiplos olhos brilhantes e pequenas estruturas de pelos ou espinhos** distribuídos pelo corpo.

Sua coloração principal deve utilizar tons de preto, marrom-escuro e roxo profundo, com detalhes avermelhados ou esverdeados nas articulações e no abdômen.

O objetivo é produzir animações extremamente fluidas, expressivas e prontas para gameplay real, com movimentação independente das patas, ataques físicos, habilidades de veneno e lançamento de teias.

## 1. SISTEMA DE 8 DIREÇÕES

Produzir todas as animações corporais em oito direções:

1. Norte (N) — Costas
2. Nordeste (NE) — Diagonal superior direita
3. Leste (E) — Lateral direita
4. Sudeste (SE) — Diagonal inferior direita
5. Sul (S) — Frente
6. Sudoeste (SW) — Diagonal inferior esquerda
7. Oeste (W) — Lateral esquerda
8. Noroeste (NW) — Diagonal superior esquerda

**Obrigatório:** cada direção deve possuir animações próprias, respeitando a anatomia aracnídea, a profundidade isométrica e a distribuição correta das oito patas.

Não espelhar automaticamente os sprites quando isso comprometer a posição dos olhos, presas, detalhes do abdômen, iluminação ou articulações.

## 2. CONCEITO DE COMBATE

**Tipo:** inimigo predatório híbrido, com ataques corpo a corpo e controle de área.

**Função:** perseguir jogadores, aplicar veneno, reduzir mobilidade com teias e pressionar alvos próximos.

**Comportamento:** furtivo, territorial, agressivo e paciente.

**Ataque básico:** mordida com presas venenosas.

**Skill 01:** Cuspe Venenoso — projétil que causa dano e pode aplicar envenenamento.

**Skill 02:** Lançamento de Teia — projétil que reduz temporariamente a velocidade do jogador.

**Diferencial:** movimentação aracnídea com oito patas independentes e abdômen que reage aos ataques.

## 3. ANIMAÇÕES OBRIGATÓRIAS

### 01 — IDLE (16 frames × 8 direções = 128 frames)

A Aranha Gigante permanece parada, mas demonstra constante atividade corporal, transmitindo a sensação de uma criatura viva, vigilante e pronta para atacar.

Durante o Idle:

- O abdômen expande e contrai discretamente, simulando respiração.
- As patas dianteiras realizam pequenos ajustes de posição.
- Algumas patas intermediárias flexionam suavemente suas articulações.
- O corpo apresenta oscilações verticais mínimas e naturais.
- As quelíceras e presas realizam movimentos sutis.
- Os olhos mantêm brilho discreto e ameaçador.
- Pequenos movimentos do pedipalpo reforçam a sensação de vigilância.

As oito patas devem apresentar movimentos secundários independentes, evitando movimentação perfeitamente sincronizada ou artificial.

**Loop:** contínuo e perfeitamente conectado. A pose final deve retornar naturalmente à inicial, mantendo o mesmo posicionamento de contato das patas com o chão.

### 02 — WALK (16 frames × 8 direções = 128 frames)

Criar uma caminhada aracnídea fluida, coordenada e ameaçadora.

A movimentação deve utilizar um **padrão de marcha em trípode alternado adaptado à anatomia de oito patas**, com grupos alternados de quatro patas sustentando e impulsionando o corpo.

Durante o Walk:

- As oito patas movimentam-se com coordenação e alternância.
- Cada pata apresenta levantamento, avanço, contato e impulsão.
- O corpo realiza pequenas oscilações verticais sincronizadas com a marcha.
- O abdômen acompanha o movimento com leve atraso.
- As patas dianteiras procuram o terreno antes de apoiar.
- As patas traseiras realizam a propulsão.
- O corpo mantém orientação estável na direção do deslocamento.
- As presas e pedipalpos acompanham sutilmente o movimento.

A caminhada deve parecer rápida e predatória, sem movimentos robóticos.

**Regra fundamental:** evitar deslizamento das patas durante a fase de apoio. A engine deve controlar o deslocamento global, enquanto os sprites representam exclusivamente o ciclo locomotor.

**Loop:** perfeito, com retorno natural à configuração inicial das patas.

### 03 — ATTACK: MORDIDA VENENOSA (14 frames × 8 direções = 112 frames)

Criar um ataque corpo a corpo rápido, agressivo e claramente identificável.

Estrutura da animação:

- **Frames 1–3 — Antecipação:** a aranha recua levemente o cefalotórax, flexiona as patas dianteiras e abre as presas.
- **Frames 4–6 — Preparação:** ergue discretamente a parte frontal do corpo e direciona as presas ao alvo.
- **Frames 7–9 — Ataque:** avança rapidamente com uma mordida agressiva.
- **Frames 10–11 — Impacto:** as presas se fecham, acompanhadas de um pequeno efeito venenoso.
- **Frames 12–14 — Recuperação:** recua naturalmente e retorna à postura predatória.

A mordida deve ser acompanhada por movimentos coordenados das patas dianteiras e pequena contração do abdômen.

**Função visual:** ataque físico principal, com possibilidade de aplicar dano venenoso.

**Transição:** Idle/Walk → Attack → Idle/Walk, mantendo continuidade corporal e ponto de ancoragem.

### 04 — HURT (10 frames × 8 direções = 80 frames)

Criar uma reação clara e expressiva ao receber dano.

Durante o Hurt:

- O corpo recua levemente.
- Algumas patas se contraem em reação ao impacto.
- O cefalotórax inclina para trás ou lateralmente.
- As presas se abrem momentaneamente.
- O abdômen apresenta uma oscilação curta.
- As patas recuperam gradualmente a sustentação corporal.

Estrutura:

- Frames 1–2: impacto inicial.
- Frames 3–5: contração corporal e desequilíbrio.
- Frames 6–8: recuperação da postura.
- Frames 9–10: retorno à posição de combate.

**Função visual:** feedback de dano.

A reação deve ser perceptível, mas não excessivamente longa.

### 05 — DIED (20 frames × 8 direções = 160 frames)

Criar uma morte aracnídea completa, com colapso gradual do corpo.

Estrutura:

- **Frames 1–4:** impacto fatal e contração das patas.
- **Frames 5–8:** perda de sustentação e inclinação do corpo.
- **Frames 9–12:** abdômen aproxima-se do chão enquanto as patas começam a recolher.
- **Frames 13–16:** queda completa e contração das oito patas para próximo do corpo.
- **Frames 17–19:** pequenos movimentos residuais das patas.
- **Frame 20:** cadáver completamente imóvel.

A morte deve representar de maneira convincente a perda de sustentação de um aracnídeo.

As patas devem dobrar naturalmente em suas articulações, sem atravessar o corpo ou desaparecer.

**Sem loop.** O último frame permanece visível até a remoção do cadáver pelo sistema do jogo.

### 06 — SKILL 01: CUSPE VENENOSO (18 frames × 8 direções = 144 frames)

A Aranha Gigante prepara e dispara um projétil de veneno em direção ao jogador.

Estrutura:

- **Frames 1–4 — Preparação:** interrompe seus movimentos, ergue ligeiramente a região frontal e contrai as patas.
- **Frames 5–8 — Acúmulo:** as presas se abrem e uma pequena concentração de veneno verde-luminoso surge entre elas.
- **Frames 9–11 — Disparo:** projeta a cabeça para frente e libera uma esfera de veneno.
- **Frames 12–15 — Recuperação:** a cabeça retorna, as presas se fecham e pequenas gotas residuais desaparecem.
- **Frames 16–18 — Retorno:** recupera completamente a postura de combate.

O projétil deve ser gerado separadamente no frame de disparo, por evento configurado no JSON.

**Função visual:** ataque à distância com dano venenoso.

### 07 — SKILL 02: LANÇAMENTO DE TEIA (20 frames × 8 direções = 160 frames)

A Aranha Gigante utiliza suas glândulas produtoras de seda para disparar uma teia pegajosa contra o jogador.

Para manter coerência anatômica, a teia deve ser lançada a partir das fiandeiras na extremidade posterior do abdômen.

Estrutura:

- **Frames 1–4 — Preparação:** a aranha interrompe seus movimentos e flexiona as patas.
- **Frames 5–8 — Posicionamento:** ergue parcialmente o abdômen e o orienta para a direção do alvo, com ajuste das patas de sustentação.
- **Frames 9–12 — Disparo:** libera rapidamente uma massa compacta de seda das fiandeiras.
- **Frames 13–16 — Recuperação:** o abdômen retorna à posição natural e pequenos fios residuais se desprendem.
- **Frames 17–20 — Retorno:** a aranha estabiliza as patas e reassume sua postura ofensiva.

O projétil de teia deve expandir-se ao atingir o alvo ou o chão, formando uma pequena rede pegajosa.

**Função visual:** controle de movimento, aplicando lentidão temporária.

**Importante:** nenhuma teia deve surgir da boca ou das presas. Preservar rigorosamente a origem anatômica nas fiandeiras.

## 4. PROJÉTEIS OBRIGATÓRIOS

### PROJÉTIL 01 — ESFERA VENENOSA

Criar uma spritesheet específica para uma esfera de veneno.

**Animação de voo:** 8 frames em loop.

Características:

- núcleo verde-luminoso
- superfície irregular e viscosa
- pequenas bolhas de veneno
- gotas secundárias acompanhando o deslocamento
- pulsação orgânica discreta

**Impacto:** 8 frames sem loop.

Ao atingir o alvo ou o cenário, a esfera se rompe, espalhando pequenas gotas e uma nuvem venenosa de curta duração.

Criar variantes direcionais quando a trajetória e a perspectiva exigirem. A engine controla deslocamento e colisão.

### PROJÉTIL 02 — MASSA DE TEIA

Criar uma spritesheet específica para uma pequena massa de seda compactada.

**Animação de voo:** 8 frames em loop.

Características:

- aparência de seda branca ou acinzentada
- fios finos visíveis
- leve deformação durante o voo
- pequenas fibras acompanhando a trajetória
- silhueta compacta e legível

**Impacto:** 10 frames sem loop.

A teia atinge o alvo ou o solo e se expande rapidamente, formando uma rede pegajosa.

**Estado persistente:** criar também um sprite estático ou animação sutil de teia aderida ao chão, caso a habilidade produza uma área de lentidão.

A remoção da teia deve acontecer por desaparecimento gradual controlado pela engine.

## 5. VFX OBRIGATÓRIOS

Produzir spritesheets independentes para os efeitos visuais.

**VFX 01 — Mordida / Impacto físico (6 frames)**

Pequeno impacto orgânico associado ao fechamento das presas.

**VFX 02 — Venom Charge (8 frames)**

Acúmulo progressivo de energia venenosa entre as presas antes do disparo.

**VFX 03 — Venom Impact (8 frames)**

Explosão viscosa com pequenas gotas de veneno, sincronizada com a colisão do projétil.

**VFX 04 — Poison Status (12 frames em loop)**

Pequenas partículas verdes e bolhas discretas ao redor de um alvo envenenado.

**VFX 05 — Web Launch (6 frames)**

Fios de seda esticando rapidamente a partir das fiandeiras no momento do disparo.

**VFX 06 — Web Impact (10 frames)**

Expansão da massa de teia e formação da rede.

**VFX 07 — Step Dust (6 frames, opcional)**

Pequena poeira produzida pelo contato das patas com o solo.

**VFX 08 — Death Dust (8 frames, opcional)**

Poeira discreta durante o colapso corporal.

Todos os VFX devem preservar a estética Pixel Art Chibi e ser entregues separadamente do personagem.

Efeitos direcionais devem possuir oito orientações quando necessário, evitando rotações que distorçam pixels.

## 6. ESPECIFICAÇÕES TÉCNICAS

| Animação | Frames/direção | Direções | Total |
|---|---:|---:|---:|
| Idle | 16 | 8 | 128 |
| Walk | 16 | 8 | 128 |
| Attack — Mordida | 14 | 8 | 112 |
| Hurt | 10 | 8 | 80 |
| Died | 20 | 8 | 160 |
| Skill 01 — Veneno | 18 | 8 | 144 |
| Skill 02 — Teia | 20 | 8 | 160 |
| **Total personagem** | | | **912 frames** |

### Projéteis

| Projétil | Voo | Impacto |
|---|---:|---:|
| Esfera venenosa | 8 | 8 |
| Massa de teia | 8 | 10 |
| **Total base** | **16** | **18** |

**Total:** 912 frames corporais + 34 frames-base de projéteis, além dos VFX e das variantes direcionais necessárias.

## 7. FPS RECOMENDADOS

- **Idle:** 10–12 FPS
- **Walk:** 14–18 FPS
- **Attack:** 16–20 FPS
- **Hurt:** 16–20 FPS
- **Died:** 12–16 FPS
- **Skill Veneno:** 16–20 FPS
- **Skill Teia:** 16–20 FPS
- **Projéteis:** 16–24 FPS
- **VFX:** 16–24 FPS

A engine poderá ajustar a velocidade de reprodução conforme o comportamento do inimigo.

## 8. REGRAS OBRIGATÓRIAS DE FLUIDEZ

- Produzir sprites reais para as oito direções.
- Preservar exatamente oito patas em todos os frames.
- Manter todas as articulações consistentes, evitando patas extras, ausentes ou fundidas.
- Respeitar a anatomia aracnídea durante movimentos e ataques.
- Garantir que as patas tenham fases claras de apoio e avanço.
- Evitar deslizamento das patas sobre o chão.
- Manter o ponto de ancoragem estável e centralizado no contato corporal com o solo.
- Não alterar involuntariamente escala, volume do abdômen ou proporções do cefalotórax.
- Animar o abdômen com movimento secundário suave e coerente.
- Preservar a identidade visual das presas, olhos e marcas corporais em todas as direções.
- Garantir transições naturais entre Idle, Walk, Attack, Hurt e Skills.
- As animações Idle e Walk devem possuir loops perfeitamente contínuos.
- Attack, Hurt e Skills devem possuir poses de entrada e recuperação compatíveis com Idle.
- Died deve terminar em um cadáver estável e sem movimento.
- Evitar tremores, deformações, teleportes, mudanças abruptas de iluminação e cortes visuais.
- Não utilizar interpolação borrada ou suavização que prejudique a pixel art.
- Não criar efeitos que ocultem excessivamente a silhueta da aranha.
- Preservar a profundidade isométrica e a sobreposição correta das patas.
- Manter o mesmo padrão de contorno e iluminação em todas as animações.
- Usar fundo transparente verdadeiro.
- Não permitir bordas, halos, pixels soltos ou vazamento entre células.
- Não cortar patas, fiandeiras, abdômen ou VFX nos limites dos frames.
- Manter consistência entre sprites corporais, projéteis e efeitos visuais.

## 9. ORGANIZAÇÃO DOS ARQUIVOS

Entregar arquivos independentes:

- `giant_spider_idle.png`
- `giant_spider_walk.png`
- `giant_spider_attack.png`
- `giant_spider_hurt.png`
- `giant_spider_died.png`
- `giant_spider_skill_poison.png`
- `giant_spider_skill_web.png`
- `giant_spider_projectile_poison.png`
- `giant_spider_projectile_web.png`
- `giant_spider_vfx_bite.png`
- `giant_spider_vfx_poison.png`
- `giant_spider_vfx_web.png`
- `giant_spider_animations.json`

Cada spritesheet principal deve conter **8 linhas**, na ordem:

N, NE, E, SE, S, SW, W, NW.

Cada linha deve possuir os frames em sequência cronológica.

Os frames devem utilizar dimensões uniformes, suficientes para acomodar toda a extensão das patas.

O arquivo JSON deve conter:

- nomes das animações e direções
- quantidade exata de frames
- FPS de cada animação
- dimensões e coordenadas de recorte
- pontos de ancoragem
- hitbox e hurtbox
- eventos de dano
- eventos de spawn dos projéteis
- posição das presas e fiandeiras por frame e direção
- eventos de início e término dos VFX
- regras de repetição e interrupção das animações
- estado final de morte
- tempos recomendados para transições

## 10. VALIDAÇÃO OBRIGATÓRIA

Antes de considerar o conjunto concluído:

1. Reproduzir Idle e Walk por pelo menos cinco ciclos em cada uma das oito direções.
2. Verificar a fluidez individual de cada uma das oito patas, garantindo ausência de saltos, desaparecimentos ou deformações.
3. Testar Idle → Attack → Idle e Walk → Attack → Walk.
4. Testar interrupções por Hurt e retorno à postura de combate.
5. Reproduzir integralmente as duas Skills e verificar a sincronização dos projéteis.
6. Confirmar que o veneno sai das presas e a teia sai das fiandeiras.
7. Validar os efeitos de impacto e estados persistentes.
8. Verificar as oito animações de morte e seus respectivos cadáveres finais.
9. Conferir o alinhamento dos recortes, transparência e pontos de ancoragem.
10. Corrigir quaisquer tremores, artefatos, mudanças involuntárias de escala ou inconsistências anatômicas.

## RESULTADO ESPERADO

Entregar um conjunto completo de spritesheets de uma **Aranha Gigante em Pixel Art Chibi**, com:

- **Idle:** 128 frames
- **Walk:** 128 frames
- **Attack:** 112 frames
- **Hurt:** 80 frames
- **Died:** 160 frames
- **Skill 01 — Cuspe Venenoso:** 144 frames
- **Skill 02 — Lançamento de Teia:** 160 frames
- **Projétil venenoso com animação de voo e impacto**
- **Projétil de teia com animação de voo e impacto**
- **VFX próprios para mordida, veneno, teia, impactos e estados negativos**

**Total: 912 frames corporais em oito direções**, além de projéteis, efeitos visuais e metadados de animação.

O resultado final deve representar uma criatura ameaçadora, ágil e predatória, com locomoção aracnídea convincente, ataques fluidos, habilidades distintas e excelente integração com um MMORPG 2D isométrico inspirado em Diablo II.

**Prioridade absoluta:** consistência anatômica das oito patas, fluidez de animação, leitura visual, continuidade entre movimentos e sprites utilizáveis diretamente no jogo, sem necessidade de reconstrução artística.