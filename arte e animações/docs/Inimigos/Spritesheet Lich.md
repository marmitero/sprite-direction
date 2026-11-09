# INIMIGO LICH — SPRITESHEET COMPLETA EM 8 DIREÇÕES

Crie um conjunto completo de spritesheets para um **Lich de RPG 2D isométrico, inspirado em Diablo II, com estética Pixel Art Chibi e fantasia medieval sombria**.

O Lich deve ser um inimigo de elite, classificado como um poderoso conjurador morto-vivo, especializado em necromancia avançada, magia destrutiva, invocação de mortos-vivos, controle de área e habilidades sobrenaturais.

Sua aparência deve transmitir a sensação de um antigo arquimago que transcendeu a morte através de rituais proibidos, preservando sua inteligência, conhecimento arcano e imenso poder mágico.

Diferentemente do Esqueleto Feiticeiro, que representa um conjurador morto-vivo comum, o Lich deve transmitir **superioridade mágica, autoridade, frieza e poder ancestral**, possuindo animações mais elaboradas, efeitos sobrenaturais mais intensos e habilidades visualmente marcantes.

Apesar da estética chibi, o personagem deve parecer imponente, misterioso, ameaçador e digno de um inimigo de elite ou miniboss.

O objetivo é produzir animações extremamente fluidas, expressivas e prontas para gameplay real, com oito direções completas, movimentos sobrenaturais, habilidades necromânticas exclusivas, projéteis, invocações e efeitos visuais independentes.

---

# 1. IDENTIDADE VISUAL

O Lich deve possuir:

- Corpo esquelético humanoide, de porte médio a grande.
- Crânio proporcionalmente grande, característico da estética chibi.
- Estrutura óssea antiga, desgastada e parcialmente escurecida.
- Órbitas profundas com chamas espectrais azul-ciano ou violeta.
- Mandíbula articulada, com movimentos sutis durante conjurações.
- Coroa necromântica antiga, de metal escurecido, com pontas irregulares.
- Pequenos cristais mágicos incrustados na coroa.
- Manto longo, deteriorado e imponente, em tons de preto, roxo profundo e azul-escuro.
- Capuz ou gola elevada envolvendo parcialmente o crânio.
- Ombreiras ornamentadas com detalhes ósseos e runas arcanas.
- Peitoral ritualístico antigo, parcialmente visível sob o manto.
- Braços esqueléticos com braceletes mágicos.
- Mãos ósseas com dedos longos e expressivos.
- Cinto com pequenos pergaminhos, amuletos e fragmentos de cristal.
- Cajado necromântico longo, segurado na mão direita anatômica.
- Cristal flutuante ou gema espectral na extremidade superior do cajado.
- Mão esquerda livre para gestos mágicos.
- Pequenas correntes ou adornos rúnicos presos à vestimenta.
- Aura sobrenatural discreta envolvendo a parte inferior do corpo.

**Arma principal:** Cajado do Sepulcro — cajado necromântico ornamentado, com cristal espectral pulsante.

**Elemento mágico principal:** energia necromântica azul-ciano e violeta.

**Elemento secundário:** sombras, runas ancestrais e chamas espectrais.

**Personalidade visual:** inteligente, calculista, arrogante, frio, poderoso e praticamente imperturbável.

**Direção de animação:** movimentos deliberados e precisos, gestos de conjuração amplos, flutuação sobrenatural, movimentação fluida do manto e efeitos mágicos que reforçam a superioridade do personagem.

---

# 2. SISTEMA OBRIGATÓRIO DE 8 DIREÇÕES

Produzir todas as animações corporais individualmente nas seguintes orientações:

1. **Norte (N)** — Costas.
2. **Nordeste (NE)** — Diagonal superior direita.
3. **Leste (E)** — Lateral direita.
4. **Sudeste (SE)** — Diagonal inferior direita.
5. **Sul (S)** — Frente.
6. **Sudoeste (SW)** — Diagonal inferior esquerda.
7. **Oeste (W)** — Lateral esquerda.
8. **Noroeste (NW)** — Diagonal superior esquerda.

### Regras direcionais

- Criar sprites próprios para todas as oito direções.
- Preservar rigorosamente a perspectiva isométrica.
- Manter o cajado sempre na mão direita anatômica.
- Manter a mão esquerda livre para conjurações.
- Preservar a posição e o formato da coroa em todas as orientações.
- Manter consistência na distribuição dos detalhes do manto.
- Respeitar a profundidade entre corpo, braços, cajado e vestimentas.
- Não utilizar espelhamento automático quando comprometer detalhes assimétricos.
- Preservar proporções, escala e silhueta.
- Manter ponto de ancoragem constante no solo, mesmo durante flutuação.
- Garantir que efeitos mágicos não ocultem excessivamente o personagem.

---

# 3. CONCEITO DE COMBATE

**Tipo:** inimigo de elite mágico, especializado em necromancia e controle de área.

**Função:** atacar jogadores à distância, invocar aliados mortos-vivos, aplicar efeitos negativos e controlar o campo de batalha.

**Comportamento:** estratégico, calculista, defensivo e extremamente perigoso.

**Ataque básico:** Orbe Necromântico — projétil de energia espectral.

**Skill 01:** Nova da Morte — explosão circular de energia necromântica ao redor do Lich.

**Skill 02:** Invocação dos Mortos — ritual que invoca esqueletos para auxiliá-lo.

**Skill 03:** Prisão de Ossos — estruturas ósseas emergem do chão, aprisionando ou restringindo o movimento do jogador.

**Skill 04:** Teleporte Sombrio — deslocamento mágico instantâneo para reposicionamento.

**Skill 05:** Drenagem de Vida — canaliza energia vital de um alvo, causando dano contínuo e recuperando parte de sua própria vida.

**Diferencial:** domínio da necromancia, flutuação, múltiplas habilidades mágicas, invocações e controle territorial.

O Lich deve funcionar como um inimigo de elite ou miniboss, exigindo movimentação constante e atenção às áreas de perigo.

---

# 4. ANIMAÇÕES OBRIGATÓRIAS

## 01 — IDLE: VIGÍLIA NECROMÂNTICA (20 frames × 8 direções = 160 frames)

O Lich permanece flutuando discretamente acima do solo, sustentado por energia sobrenatural.

Seu corpo deve apresentar movimentos lentos, controlados e imponentes.

Durante o Idle:

- O corpo oscila verticalmente alguns pixels, simulando levitação.
- O manto acompanha o movimento com atraso natural.
- As extremidades inferiores da roupa ondulam suavemente.
- O crânio inclina discretamente, observando os arredores.
- As chamas espectrais dos olhos pulsam lentamente.
- A mandíbula realiza pequenos movimentos ocasionais.
- O cajado permanece vertical ou ligeiramente inclinado.
- O cristal do cajado emite uma pulsação luminosa discreta.
- A mão esquerda abre e fecha lentamente os dedos esqueléticos.
- Pequenas partículas espectrais surgem ocasionalmente ao redor do corpo.
- A coroa permanece rigidamente posicionada sobre o crânio.
- Os acessórios acompanham os movimentos de flutuação.

O Lich não deve respirar como uma criatura viva.

**Loop:** perfeitamente contínuo, sem saltos na posição vertical.

O ponto de ancoragem no chão deve permanecer imóvel, enquanto a flutuação acontece apenas dentro da animação.

---

## 02 — WALK: DESLOCAMENTO ESPECTRAL (20 frames × 8 direções = 160 frames)

O Lich não caminha convencionalmente. Sua movimentação principal consiste em deslizar ou flutuar sobre o terreno.

Criar uma animação de deslocamento sobrenatural, fluida e imponente.

Durante o Walk:

- O corpo permanece suspenso acima do chão.
- A postura mantém-se ereta e controlada.
- O manto ondula em direção oposta ao deslocamento.
- As extremidades inferiores da vestimenta apresentam movimento secundário.
- O cajado acompanha discretamente o deslocamento.
- A mão esquerda permanece parcialmente erguida ou próxima ao torso.
- O crânio mantém o olhar direcionado ao movimento.
- A coroa e os acessórios preservam estabilidade.
- Pequenas partículas espectrais podem surgir sob o manto.
- A flutuação vertical apresenta ritmo suave e contínuo.
- O corpo não deve simular passos humanos.

**Função visual:** perseguição, recuo e reposicionamento.

**Loop:** perfeito.

**Importante:** o deslocamento global é controlado pela engine. O sprite deve representar apenas a animação local de flutuação e movimento do manto.

---

## 03 — ATTACK: ORBE NECROMÂNTICO (20 frames × 8 direções = 160 frames)

O Lich lança um projétil de energia necromântica através de seu cajado.

### Estrutura

**Frames 1–4 — Preparação**

O Lich inclina discretamente o cajado em direção ao alvo e ergue a mão esquerda.

**Frames 5–8 — Canalização**

Pequenas partículas espectrais começam a convergir para o cristal do cajado.

**Frames 9–12 — Acúmulo**

Uma esfera de energia azul-ciano e violeta surge na extremidade do cajado, aumentando progressivamente de intensidade.

**Frames 13–14 — Disparo**

O Lich realiza um gesto rápido e preciso, liberando o Orbe Necromântico.

**Frames 15–18 — Dissipação**

A energia residual desaparece enquanto o cajado retorna à posição original.

**Frames 19–20 — Recuperação**

O Lich reassume sua postura imponente de combate.

### Características

- Gestos de conjuração precisos.
- Cristal do cajado com brilho progressivo.
- Partículas convergindo naturalmente.
- Energia necromântica claramente identificável.
- Manto acompanhando discretamente os movimentos.
- Disparo sincronizado com o frame 13.

**Função visual:** ataque mágico básico à distância.

**Transição:** Idle/Walk → Attack → Idle/Walk.

---

## 04 — HURT: INSTABILIDADE ESPECTRAL (12 frames × 8 direções = 96 frames)

Criar uma reação de dano compatível com um poderoso morto-vivo.

O Lich não deve demonstrar dor humana exagerada, mas uma breve instabilidade em sua sustentação mágica.

### Estrutura

- **Frames 1–3:** impacto inicial e oscilação corporal.
- **Frames 4–6:** recuo do crânio, braços e cajado.
- **Frames 7–9:** aura espectral oscila enquanto o Lich recupera estabilidade.
- **Frames 10–12:** retorno à postura de combate.

### Durante a animação

- O corpo recua discretamente.
- As chamas dos olhos oscilam.
- O cajado inclina momentaneamente.
- O manto reage ao impacto.
- Pequenas partículas de energia escapam do corpo.
- A mão esquerda realiza um gesto involuntário.
- O Lich recupera rapidamente sua postura.

**Função visual:** feedback de dano recebido.

A reação deve ser expressiva sem descaracterizar sua imponência.

---

## 05 — DIED: DISSOLUÇÃO DO ARQUILICH (32 frames × 8 direções = 256 frames)

Criar uma morte elaborada e marcante, representando a destruição da magia que sustenta o Lich.

### Estrutura

**Frames 1–4 — Impacto fatal**

O Lich recebe o golpe final e perde parcialmente sua estabilidade sobrenatural.

**Frames 5–8 — Colapso mágico**

O cristal do cajado começa a apresentar rachaduras luminosas e as chamas espectrais dos olhos oscilam violentamente.

**Frames 9–12 — Ruptura necromântica**

Pequenas ondas de energia escapam do corpo, enquanto as runas de suas vestimentas perdem intensidade.

**Frames 13–16 — Perda da levitação**

O corpo desce progressivamente, com o manto acompanhando a queda.

**Frames 17–20 — Desintegração**

O cajado escapa da mão direita, enquanto o corpo esquelético começa a perder sua sustentação.

**Frames 21–24 — Colapso corporal**

Os ossos se desarticulam e caem dentro do manto, acompanhados pela coroa e pelos acessórios.

**Frames 25–28 — Dissipação final**

A energia necromântica abandona completamente os restos mortais.

**Frames 29–31 — Estabilização**

Os ossos, a coroa e o cajado concluem seus movimentos residuais.

**Frame 32 — Cadáver final**

Restos ósseos parcialmente cobertos pelo manto, com coroa e cajado caídos próximos ao corpo.

### Regras da morte

- Preservar continuidade da anatomia durante o colapso.
- Não fazer ossos, coroa ou cajado desaparecerem abruptamente.
- Respeitar a gravidade e a perspectiva isométrica.
- Manter identidade visual até o final.
- Terminar com uma composição estável.
- Separar a dissipação mágica dos sprites corporais quando necessário.

**Sem loop.** O último frame permanece visível até a remoção do cadáver.

---

# 5. HABILIDADES ESPECIAIS

## 06 — SKILL 01: NOVA DA MORTE (28 frames × 8 direções = 224 frames)

O Lich concentra uma grande quantidade de energia necromântica e libera uma explosão circular ao redor de seu corpo.

### Estrutura

**Frames 1–4 — Preparação**

O Lich interrompe seus movimentos e posiciona o cajado verticalmente diante do corpo.

**Frames 5–9 — Canalização**

Ergue lentamente a mão esquerda, enquanto pequenas runas surgem ao redor do cajado.

**Frames 10–14 — Acúmulo**

Uma aura espectral intensa envolve o Lich, concentrando energia em seu torso e no cristal.

**Frames 15–18 — Intensificação**

O manto se expande discretamente, os olhos brilham intensamente e a energia atinge seu ápice.

**Frames 19–21 — Explosão**

O Lich abre os braços e libera uma onda circular de energia necromântica.

**Frames 22–25 — Dissipação**

A energia se afasta do corpo e desaparece gradualmente.

**Frames 26–28 — Recuperação**

O Lich retorna à postura de combate.

### Características

- Explosão radial em perspectiva isométrica.
- Energia azul-ciano e violeta.
- Runas necromânticas.
- Pequenas partículas espectrais.
- Forte antecipação visual.
- Ataque sincronizado com o frame 19.

**Função visual:** dano mágico em área ao redor do Lich.

A onda de energia deve ser um VFX independente, com raio e colisão controlados pela engine.

---

## 07 — SKILL 02: INVOCAÇÃO DOS MORTOS (32 frames × 8 direções = 256 frames)

O Lich realiza um ritual necromântico para invocar esqueletos guerreiros.

### Estrutura

**Frames 1–5 — Preparação**

O Lich firma o cajado verticalmente e direciona o olhar ao solo.

**Frames 6–10 — Início do ritual**

Ergue a mão esquerda e começa a desenhar símbolos arcanos no ar.

**Frames 11–15 — Canalização**

Um círculo rúnico surge no solo e pequenas partículas de energia convergem para ele.

**Frames 16–20 — Intensificação**

O Lich ergue o cajado, enquanto o círculo mágico aumenta de intensidade.

**Frames 21–24 — Invocação**

Realiza um gesto poderoso, ativando o ritual e desencadeando a manifestação dos esqueletos.

**Frames 25–28 — Estabilização**

O Lich mantém a mão erguida enquanto a energia começa a desaparecer.

**Frames 29–32 — Recuperação**

Abaixa o cajado e retorna à postura de combate.

### Características

- Gestos ritualísticos elaborados.
- Runas necromânticas flutuantes.
- Círculo mágico no chão.
- Energia ascendendo do solo.
- Pequenas partículas ósseas e espectrais.
- Forte leitura visual do momento da invocação.

**Função visual:** invocar aliados mortos-vivos.

Os esqueletos invocados devem utilizar suas próprias spritesheets de Idle, Walk, Attack, Hurt e Died.

O evento de invocação deve ocorrer no frame 21.

---

## 08 — SKILL 03: PRISÃO DE OSSOS (28 frames × 8 direções = 224 frames)

O Lich conjura estruturas ósseas que emergem do chão e aprisionam temporariamente o jogador.

### Estrutura

**Frames 1–4 — Preparação**

O Lich inclina o cajado em direção ao alvo.

**Frames 5–9 — Canalização**

Pequenos símbolos necromânticos aparecem ao redor da mão esquerda.

**Frames 10–14 — Acúmulo**

O cristal do cajado começa a emitir energia intensa, enquanto o Lich concentra o poder.

**Frames 15–18 — Conjuração**

O Lich aponta o cajado para o solo próximo ao alvo.

**Frames 19–21 — Erupção óssea**

Grandes estruturas de ossos emergem rapidamente do chão, formando uma prisão.

**Frames 22–25 — Estabilização**

O Lich mantém o gesto enquanto a energia residual desaparece.

**Frames 26–28 — Recuperação**

Retorna à postura de combate.

### Características

- Magia de controle territorial.
- Ossos emergindo do solo.
- Poeira e fragmentos.
- Pequenas runas necromânticas.
- Animação de formação progressiva.
- Estruturas com profundidade isométrica correta.

**Função visual:** aprisionar ou restringir temporariamente a movimentação do jogador.

A prisão deve possuir sprites próprios de surgimento, sustentação e destruição.

---

## 09 — SKILL 04: TELEPORTE SOMBRIO (24 frames × 8 direções = 192 frames)

O Lich utiliza magia sombria para desaparecer e reaparecer em outra posição do campo de batalha.

### Estrutura

**Frames 1–4 — Preparação**

O Lich aproxima o cajado do torso e concentra energia espectral.

**Frames 5–8 — Canalização**

Uma aura de sombras envolve progressivamente o corpo.

**Frames 9–12 — Dissolução**

O personagem começa a se desfazer em partículas necromânticas, preservando sua silhueta durante a transição.

**Frames 13–15 — Desaparecimento**

A silhueta desaparece completamente, deixando apenas partículas residuais.

**Frames 16–19 — Reaparecimento**

O corpo começa a se reconstruir na posição de destino.

**Frames 20–22 — Materialização**

O Lich recupera sua forma completa.

**Frames 23–24 — Recuperação**

Retorna à postura de combate.

### Características

- Dissolução progressiva.
- Partículas sombrias.
- Pequenas runas.
- Reconstrução visual coerente.
- Transição suave entre desaparecimento e reaparecimento.

**Função visual:** evasão e reposicionamento.

O deslocamento deve ser controlado pela engine. A spritesheet não deve conter movimento global entre a origem e o destino.

---

## 10 — SKILL 05: DRENAGEM DE VIDA (30 frames × 8 direções = 240 frames)

O Lich canaliza energia necromântica para drenar a força vital de um alvo.

### Estrutura

**Frames 1–4 — Preparação**

O Lich ergue a mão esquerda e direciona o cajado ao alvo.

**Frames 5–9 — Canalização**

Pequenas partículas espectrais aparecem ao redor da mão e do cristal.

**Frames 10–13 — Conexão**

Um feixe de energia sombria se conecta ao alvo.

**Frames 14–21 — Drenagem**

O Lich mantém uma postura de concentração enquanto pequenas partículas fluem do alvo em sua direção.

**Frames 22–25 — Encerramento**

O fluxo de energia diminui gradualmente.

**Frames 26–28 — Dissipação**

O feixe desaparece e a energia residual retorna ao cajado.

**Frames 29–30 — Recuperação**

O Lich retorna à postura de combate.

### Características

- Feixe de energia necromântica.
- Partículas fluindo do alvo para o Lich.
- Pulsações sincronizadas.
- Pequenas alterações na intensidade do cristal.
- Movimento sutil do manto durante a canalização.

**Função visual:** dano mágico contínuo e recuperação de vida.

### LIFE DRAIN HOLD — 12 frames × 8 direções = 96 frames

Criar uma animação complementar para sustentar a drenagem por duração variável.

Durante o Hold:

- O Lich mantém a mão esquerda estendida.
- O cajado permanece direcionado ao alvo.
- O corpo apresenta pequenas oscilações.
- O cristal pulsa continuamente.
- O manto reage à energia.
- O feixe permanece conectado ao alvo.

**Loop:** perfeitamente contínuo.

O estado de drenagem deve funcionar em três partes: preparação → canalização em loop → encerramento.

A duração e o dano periódico devem ser controlados pela engine.

---

# 6. PROJÉTEIS OBRIGATÓRIOS

## PROJÉTIL 01 — ORBE NECROMÂNTICO

Criar um projétil mágico próprio.

**Voo:** 12 frames em loop.

Características:

- Núcleo azul-ciano luminoso.
- Bordas violetas instáveis.
- Pequenas chamas espectrais.
- Rastro curto de energia.
- Partículas flutuantes.
- Pulsação constante.

**Impacto:** 10 frames sem loop.

O orbe explode em pequenas partículas e energia necromântica.

**Sincronização:** spawn no frame 13 do ataque básico.

## PROJÉTIL 02 — FRAGMENTO DE ALMA

Criar pequenos fragmentos de energia espiritual utilizados em habilidades e efeitos secundários.

**Voo:** 10 frames em loop.

Características:

- Pequena chama espectral.
- Formato irregular e translúcido.
- Núcleo luminoso.
- Movimento pulsante.
- Rastro discreto.

**Impacto:** 8 frames.

Os fragmentos se dissipam ao atingir o alvo ou alcançar o destino.

Esse elemento pode ser utilizado como efeito secundário ou como projétil de uma futura variante de ataque.

## PROJÉTIL 03 — ONDA DA MORTE

Criar uma onda expansiva de energia necromântica.

**Expansão:** 16 frames.

Características:

- Anel de energia espectral.
- Expansão circular no plano do chão.
- Runas e partículas.
- Bordas irregulares.
- Dissipação progressiva.

A onda deve ser implementada como efeito de área, com colisão independente.

Não tratá-la como uma esfera convencional.

---

# 7. VFX OBRIGATÓRIOS

Produzir spritesheets independentes para cada efeito.

### VFX 01 — NECROMANTIC CAST (12 frames)

Energia acumulando-se no cajado durante conjurações.

### VFX 02 — NECROMANTIC PROJECTILE IMPACT (10 frames)

Explosão de energia espectral ao atingir o alvo.

### VFX 03 — DEATH NOVA CHARGE (12 frames)

Acúmulo de energia ao redor do Lich antes da Nova da Morte.

### VFX 04 — DEATH NOVA EXPLOSION (16 frames)

Onda circular de energia necromântica.

### VFX 05 — SUMMONING CIRCLE (20 frames)

Círculo rúnico de invocação, com surgimento, intensificação e desaparecimento.

### VFX 06 — SKELETON EMERGENCE (24 frames)

Animação de surgimento dos esqueletos a partir do solo.

### VFX 07 — BONE PRISON EMERGENCE (18 frames)

Estruturas ósseas emergindo progressivamente do chão.

### VFX 08 — BONE PRISON HOLD (12 frames em loop)

Prisão óssea estabilizada, com pequenas pulsações mágicas.

### VFX 09 — BONE PRISON BREAK (14 frames)

Destruição ou dissipação da prisão, com fragmentos ósseos.

### VFX 10 — TELEPORT DISAPPEAR (14 frames)

Dissolução do Lich em partículas sombrias.

### VFX 11 — TELEPORT APPEAR (14 frames)

Reconstrução da silhueta no destino.

### VFX 12 — LIFE DRAIN BEAM (12 frames em loop)

Feixe necromântico conectado entre Lich e alvo.

### VFX 13 — LIFE DRAIN IMPACT (10 frames)

Energia concentrada no ponto de contato com o alvo.

### VFX 14 — LIFE ABSORPTION (12 frames)

Partículas vitais sendo absorvidas pelo Lich.

### VFX 15 — NECROMANTIC DEATH (20 frames)

Dissipação da energia que mantém o Lich reanimado.

### VFX 16 — BONE COLLAPSE DUST (10 frames)

Poeira e pequenos fragmentos durante a morte.

Todos os VFX devem:

- Utilizar a mesma paleta necromântica.
- Preservar estética Pixel Art Chibi.
- Respeitar a perspectiva isométrica.
- Possuir transparência verdadeira.
- Funcionar independentemente do personagem.
- Ser sincronizados por eventos da engine.
- Não ocultar excessivamente a silhueta do Lich.
- Possuir variantes direcionais quando necessário.

---

# 8. ESPECIFICAÇÕES TÉCNICAS

| Animação | Frames/direção | Direções | Total |
|---|---:|---:|---:|
| Idle | 20 | 8 | 160 |
| Walk — Flutuação | 20 | 8 | 160 |
| Attack — Orbe Necromântico | 20 | 8 | 160 |
| Hurt | 12 | 8 | 96 |
| Died | 32 | 8 | 256 |
| Skill 01 — Nova da Morte | 28 | 8 | 224 |
| Skill 02 — Invocação dos Mortos | 32 | 8 | 256 |
| Skill 03 — Prisão de Ossos | 28 | 8 | 224 |
| Skill 04 — Teleporte Sombrio | 24 | 8 | 192 |
| Skill 05 — Drenagem de Vida | 30 | 8 | 240 |
| Life Drain Hold | 12 | 8 | 96 |
| **TOTAL** | | | **2.064 frames** |

**Total corporal: 2.064 frames distribuídos em oito direções.**

Projéteis, efeitos visuais, esqueletos invocados e estruturas ósseas devem ser entregues separadamente.

---

# 9. FPS RECOMENDADOS

- **Idle:** 10–12 FPS.
- **Walk / Flutuação:** 12–16 FPS.
- **Attack:** 16–20 FPS.
- **Hurt:** 16–20 FPS.
- **Died:** 12–16 FPS.
- **Nova da Morte:** 16–20 FPS.
- **Invocação dos Mortos:** 16–20 FPS.
- **Prisão de Ossos:** 16–20 FPS.
- **Teleporte Sombrio:** 18–24 FPS.
- **Drenagem de Vida:** 16–20 FPS.
- **Life Drain Hold:** 10–12 FPS.
- **Projéteis:** 16–24 FPS.
- **VFX:** 18–24 FPS.

A engine poderá ajustar as velocidades de reprodução conforme a dificuldade e o ritmo do combate.

---

# 10. REGRAS OBRIGATÓRIAS DE FLUIDEZ

- Produzir sprites próprios para as oito direções.
- Preservar rigorosamente a anatomia esquelética.
- Manter proporções constantes de crânio, braços, torso e vestimentas.
- Preservar coroa, cajado, cristais, runas e acessórios em todos os frames.
- Manter o cajado na mão direita anatômica.
- Garantir continuidade dos gestos mágicos da mão esquerda.
- Preservar a mesma escala em todas as direções.
- Garantir que o manto tenha movimento secundário fluido.
- Manter a flutuação vertical suave, sem tremores.
- Preservar o ponto de ancoragem no solo.
- Não deslocar o personagem dentro da spritesheet durante a flutuação.
- Respeitar a perspectiva isométrica.
- Garantir transições naturais entre Idle, Walk, Attack, Hurt e Skills.
- Idle, Walk e Life Drain Hold devem possuir loops perfeitamente contínuos.
- Attack e Skills devem começar e terminar em poses compatíveis com a postura de combate.
- Hurt deve permitir interrupções conforme as regras do jogo.
- Died deve terminar em um cadáver estático.
- Evitar deformações, mudanças de escala, teleportes involuntários e saltos visuais.
- Não permitir que cajado, braços ou coroa atravessem incorretamente o corpo.
- Preservar paleta, iluminação e contornos.
- Não utilizar interpolação borrada.
- Utilizar transparência verdadeira.
- Evitar bordas, halos, pixels soltos e vazamentos entre células.
- Garantir enquadramento suficiente para o cajado erguido e gestos amplos.
- Manter dimensões uniformes e coordenadas de recorte consistentes.
- Separar VFX, projéteis e estruturas invocadas do personagem.
- Sincronizar efeitos mágicos com os frames corretos.
- Garantir que círculos mágicos e efeitos de solo respeitem a perspectiva isométrica.
- Preservar legibilidade durante combates com múltiplos inimigos.
- Não utilizar efeitos exagerados que ocultem o personagem.
- Validar todas as direções individualmente.

---

# 11. ORGANIZAÇÃO DOS ARQUIVOS

Entregar arquivos independentes:

### Spritesheets corporais

- `lich_idle.png`
- `lich_walk.png`
- `lich_attack.png`
- `lich_hurt.png`
- `lich_died.png`
- `lich_skill_death_nova.png`
- `lich_skill_summon.png`
- `lich_skill_bone_prison.png`
- `lich_skill_teleport.png`
- `lich_skill_life_drain.png`
- `lich_life_drain_hold.png`

### Projéteis

- `lich_projectile_necromantic_orb.png`
- `lich_projectile_soul_fragment.png`
- `lich_projectile_death_wave.png`

### VFX

- `lich_vfx_cast.png`
- `lich_vfx_projectile_impact.png`
- `lich_vfx_death_nova.png`
- `lich_vfx_summoning_circle.png`
- `lich_vfx_skeleton_emergence.png`
- `lich_vfx_bone_prison.png`
- `lich_vfx_bone_prison_break.png`
- `lich_vfx_teleport.png`
- `lich_vfx_life_drain.png`
- `lich_vfx_death.png`

### Metadados

- `lich_animations.json`

Cada spritesheet corporal deve utilizar **8 linhas direcionais**, nesta ordem:

**N, NE, E, SE, S, SW, W, NW.**

Os frames devem estar organizados horizontalmente em sequência cronológica.

### O arquivo JSON deve conter:

- Identificador do inimigo.
- Nomes das animações.
- Direções e quantidade exata de frames.
- Coordenadas de recorte.
- Dimensões das células.
- FPS de reprodução.
- Configurações de loop.
- Ponto de ancoragem no solo.
- Hitbox e hurtbox.
- Coordenadas do cristal do cajado por frame e direção.
- Coordenadas da mão esquerda.
- Eventos de conjuração.
- Eventos de geração dos projéteis.
- Eventos de aplicação de dano.
- Eventos de detonação da Nova da Morte.
- Eventos de invocação dos esqueletos.
- Eventos de surgimento e destruição da Prisão de Ossos.
- Eventos de desaparecimento e reaparecimento do teleporte.
- Eventos de início, sustentação e término da Drenagem de Vida.
- Referências aos VFX.
- Regras de interrupção por Hurt.
- Estados e transições.
- Estado final de morte.

---

# 12. REGRAS DE GAMEPLAY E SINCRONIZAÇÃO

A spritesheet deve ser construída para permitir integração direta com uma máquina de estados de animação.

**Estados principais:**

Idle → Walk → Attack → Skills → Hurt → Died.

Cada habilidade deve possuir eventos próprios, sincronizados com o gameplay.

### Orbe Necromântico

- Spawn do projétil: frame 13.
- Posição: cristal do cajado.
- Direção: orientação atual do personagem.
- Dano e colisão: controlados pela engine.

### Nova da Morte

- Ativação: frame 19.
- Origem: centro do Lich.
- Área: círculo no chão em perspectiva isométrica.
- Colisão: controlada pela engine.

### Invocação dos Mortos

- Spawn dos esqueletos: frame 21.
- Posição: pontos válidos próximos ao Lich.
- Entidades: utilizam spritesheets e inteligência artificial próprias.

### Prisão de Ossos

- Surgimento: frame 19.
- Posição: área selecionada pela IA.
- Persistência: controlada pela engine.
- Destruição: animação independente.

### Teleporte Sombrio

- Desaparecimento: frames 13–15.
- Reposicionamento: controlado pela engine durante a fase invisível.
- Reaparecimento: frames 16–19.
- Colisão e invulnerabilidade: definidas pelo gameplay.

### Drenagem de Vida

- Conexão inicial: frame 10.
- Início da drenagem: frame 14.
- Sustentação: Life Drain Hold.
- Encerramento: animação de recuperação.
- Dano periódico e recuperação de vida: controlados pela engine.

---

# 13. VALIDAÇÃO OBRIGATÓRIA

Antes de considerar o conjunto concluído:

1. Reproduzir Idle e Walk por cinco ciclos completos em cada direção.
2. Confirmar consistência da anatomia, coroa, manto e cajado.
3. Validar a flutuação, sem deslocamentos involuntários.
4. Testar Idle → Attack → Idle e Walk → Attack → Walk.
5. Confirmar a geração do Orbe Necromântico na extremidade correta do cajado.
6. Testar Nova da Morte e sincronização do VFX circular.
7. Testar Invocação dos Mortos com surgimento dos esqueletos.
8. Validar a Prisão de Ossos, incluindo formação, permanência e destruição.
9. Testar Teleporte Sombrio, desaparecimento e reaparecimento.
10. Validar Drenagem de Vida, feixe e animação de sustentação.
11. Testar interrupções por Hurt conforme as regras de gameplay.
12. Reproduzir a morte completa nas oito direções.
13. Verificar continuidade do colapso esquelético.
14. Confirmar estabilidade do cadáver final.
15. Inspecionar recortes, transparência e limites de todos os frames.
16. Corrigir tremores, deformações, alterações de escala e saltos visuais.
17. Validar mudanças de direção durante o deslocamento.
18. Confirmar posicionamento correto dos VFX em todas as direções.
19. Testar a legibilidade do Lich na escala real do jogo.
20. Validar combates com múltiplos inimigos, projéteis e invocações simultâneas.

---

# 14. RESULTADO ESPERADO

Entregar um conjunto completo de spritesheets para um **Lich em Pixel Art Chibi**, contendo:

- **Idle:** 160 frames.
- **Walk / Flutuação:** 160 frames.
- **Attack — Orbe Necromântico:** 160 frames.
- **Hurt:** 96 frames.
- **Died — Dissolução do Arquilich:** 256 frames.
- **Skill 01 — Nova da Morte:** 224 frames.
- **Skill 02 — Invocação dos Mortos:** 256 frames.
- **Skill 03 — Prisão de Ossos:** 224 frames.
- **Skill 04 — Teleporte Sombrio:** 192 frames.
- **Skill 05 — Drenagem de Vida:** 240 frames.
- **Life Drain Hold:** 96 frames.
- **Projéteis próprios:** Orbe Necromântico e Fragmento de Alma.
- **Efeito de área:** Onda da Morte.
- **VFX exclusivos:** conjuração, explosão, invocação, prisão óssea, teleporte, drenagem e morte.
- **Metadados completos:** JSON com recortes, direções, âncoras, eventos e transições.

**TOTAL: 2.064 frames corporais distribuídos em oito direções, além dos projéteis, efeitos mágicos, estruturas invocadas e VFX independentes.**

O Lich deve funcionar como um inimigo mágico de elite ou miniboss completo, capaz de lançar projéteis necromânticos, invocar mortos-vivos, aprisionar jogadores, realizar teleportes, drenar energia vital e provocar explosões mágicas devastadoras.

Sua movimentação deve transmitir **poder ancestral, inteligência, frieza, domínio absoluto da necromancia e superioridade sobrenatural**.

**PRIORIDADE ABSOLUTA:** oito direções completas, fluidez excepcional, consistência anatômica, animações mágicas elaboradas, continuidade entre movimentos, sincronização precisa de habilidades e efeitos, identidade visual consistente e sprites prontos para integração direta em um MMORPG 2D isométrico.

Não substituir animações completas por poses estáticas, espelhamentos inadequados, frames artificialmente duplicados ou efeitos genéricos. Cada animação deve ser produzida e validada individualmente nas oito direções.