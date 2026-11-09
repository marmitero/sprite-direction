# INIMIGO STONE GOLEM — SPRITESHEET COMPLETA EM 8 DIREÇÕES

Crie um conjunto completo de spritesheets para um **Stone Golem (Golem de Pedra) de RPG 2D isométrico, inspirado em Diablo II, com estética Pixel Art Chibi e fantasia medieval sombria**.

O Stone Golem deve ser um inimigo de elite de grande porte, extremamente resistente, especializado em ataques físicos devastadores, impactos sísmicos, controle de área e habilidades defensivas.

Sua aparência deve transmitir a sensação de um antigo guardião construído a partir de rochas ancestrais e animado por magia rúnica. Seu corpo é formado por blocos de pedra maciços, unidos por energia sobrenatural, capaz de manter a estrutura em movimento mesmo sem articulações orgânicas.

Diferentemente do Minotauro, que transmite força muscular e agressividade animal, o Stone Golem deve demonstrar **peso monumental, resistência extrema, movimentos mecânicos e poder elemental terrestre**.

Apesar da estética chibi, o personagem deve parecer imponente, ameaçador e praticamente indestrutível.

O objetivo é produzir animações extremamente fluidas, expressivas e prontas para gameplay real, com oito direções completas, movimentação pesada, habilidades sísmicas, efeitos visuais independentes e comportamento visual de uma criatura composta inteiramente por pedra.

---

# 1. IDENTIDADE VISUAL

O Stone Golem deve possuir:

- Corpo humanoide monumental, formado por grandes blocos de pedra.
- Cabeça proporcionalmente grande e angular, adaptada à estética chibi.
- Torso extremamente largo, com placas rochosas sobrepostas.
- Ombros enormes compostos por blocos maciços.
- Braços longos e pesados, terminando em punhos de pedra gigantes.
- Pernas curtas e robustas, capazes de sustentar seu peso.
- Pés largos, semelhantes a bases rochosas.
- Rachaduras distribuídas pelo corpo.
- Runas mágicas antigas gravadas no peito, braços e cabeça.
- Núcleo elemental luminoso localizado no centro do peito.
- Olhos formados por pequenas cavidades iluminadas por energia âmbar ou azul-ciano.
- Pequenas pedras flutuantes próximas às articulações.
- Fragmentos rochosos presos por energia mágica.
- Musgo, raízes pequenas ou sinais discretos de desgaste natural.
- Placas rochosas assimétricas, reforçando sua aparência ancestral.
- Superfícies irregulares, com textura de pedra envelhecida.
- Pequenos cristais mágicos incrustados em determinadas partes do corpo.

**Armas principais:** os próprios punhos de pedra.

**Elemento principal:** terra e rocha.

**Elemento mágico secundário:** energia rúnica âmbar ou azul-ciano.

**Personalidade visual:** silencioso, implacável, resistente, ancestral e territorial.

**Direção de animação:** movimentos lentos e pesados, com antecipações claras, aceleração convincente dos braços maciços, impactos poderosos e recuperação gradual.

O Stone Golem não deve apresentar respiração orgânica, expressões humanas exageradas ou movimentos musculares incompatíveis com sua constituição rochosa.

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
- Manter a mesma estrutura corporal em todas as orientações.
- Preservar assimetrias naturais das placas rochosas.
- Garantir que rachaduras, runas e cristais mantenham posições anatômicas consistentes.
- Não espelhar automaticamente sprites quando isso inverter detalhes assimétricos.
- Respeitar a profundidade entre braços, torso, cabeça e pernas.
- Manter proporções, escala e silhueta coerentes.
- Preservar o núcleo elemental na mesma região do peito.
- Manter ponto de ancoragem estável no chão, centralizado entre os pés.
- Reservar espaço suficiente para movimentos amplos dos braços e efeitos sísmicos.

---

# 3. CONCEITO DE COMBATE

**Tipo:** inimigo de elite elemental, especializado em combate corpo a corpo e controle de área.

**Função:** bloquear passagens, absorver dano, pressionar jogadores próximos e executar ataques de grande impacto.

**Comportamento:** lento, persistente, territorial e implacável.

**Ataque básico:** Punho Rochoso — golpe pesado com um dos braços.

**Skill 01:** Impacto Terrestre — golpe duplo no chão que provoca uma onda de choque circular.

**Skill 02:** Arremesso de Rocha — arranca ou materializa uma pedra e a lança contra o jogador.

**Skill 03:** Armadura de Pedra — reforça temporariamente sua estrutura corporal, reduzindo o dano recebido.

**Skill 04:** Erupção Rochosa — faz pilares de pedra emergirem do chão em uma região selecionada.

**Diferencial:** grande resistência, golpes lentos e poderosos, habilidades sísmicas e ataques capazes de controlar regiões do mapa.

O Stone Golem deve compensar sua baixa velocidade com alcance físico, resistência e ataques de área.

---

# 4. ANIMAÇÕES OBRIGATÓRIAS

## 01 — IDLE: VIGÍLIA DO GUARDIÃO (20 frames × 8 direções = 160 frames)

O Stone Golem permanece imóvel em sua posição de vigilância, mas apresenta pequenas movimentações que revelam sua natureza mágica.

Durante o Idle:

- O torso realiza oscilações extremamente discretas.
- Os ombros apresentam pequenos ajustes de posição.
- A cabeça rochosa inclina lentamente para observar o ambiente.
- Os braços pesados movimentam-se poucos pixels.
- As mãos de pedra abrem e fecham discretamente, quando sua estrutura permitir.
- O núcleo elemental do peito pulsa suavemente.
- As runas mágicas apresentam alterações sutis de luminosidade.
- Pequenos fragmentos de pedra próximos às articulações oscilam lentamente.
- Poeira fina pode se desprender ocasionalmente das placas rochosas.
- As rachaduras permanecem estruturalmente consistentes.
- O corpo mantém postura imponente e rígida.

O Golem não deve respirar como um ser orgânico.

**Loop:** perfeitamente contínuo.

O último frame deve retornar naturalmente à posição inicial, sem deslocamentos involuntários de partes rochosas.

---

## 02 — WALK: MARCHA MONUMENTAL (20 frames × 8 direções = 160 frames)

Criar uma caminhada extremamente pesada, lenta e poderosa.

Cada passada deve transmitir a sensação de várias toneladas de pedra sendo movimentadas por força mágica.

Durante o Walk:

- Uma perna se ergue lentamente.
- O corpo transfere seu peso para a perna de apoio.
- O pé elevado avança com movimento controlado.
- O pé atinge o chão com sensação de impacto.
- Pequenas partículas de poeira surgem no contato.
- O torso realiza oscilações verticais discretas.
- Os ombros acompanham o deslocamento com atraso natural.
- Os braços pesados balançam suavemente.
- A cabeça mantém relativa estabilidade.
- Pequenos fragmentos próximos às articulações acompanham o movimento.
- O núcleo elemental permanece estável no peito, pulsando discretamente.

### Estrutura do ciclo

- Frames 1–5: levantamento e avanço do pé esquerdo.
- Frames 6–10: contato e transferência de peso.
- Frames 11–15: levantamento e avanço do pé direito.
- Frames 16–20: contato e retorno à configuração inicial.

**Regra fundamental:** os pés não podem deslizar durante a fase de apoio.

O deslocamento global deve ser realizado pela engine.

**Loop:** perfeitamente contínuo, com transições naturais entre passadas.

---

## 03 — ATTACK: PUNHO ROCHOSO (20 frames × 8 direções = 160 frames)

O Stone Golem realiza um golpe pesado com um de seus enormes punhos.

### Estrutura

**Frames 1–4 — Antecipação**

O Golem gira discretamente o torso e recua o braço direito, preparando o ataque.

**Frames 5–8 — Acúmulo de força**

Flexiona parcialmente a articulação do ombro e posiciona o peso corporal sobre a perna de apoio.

**Frames 9–12 — Execução**

Projeta violentamente o punho rochoso em direção ao alvo.

**Frames 13–15 — Impacto**

O punho atinge sua extensão máxima, produzindo um efeito de colisão pesado.

**Frames 16–18 — Recuperação**

Recolhe lentamente o braço, enquanto pequenos fragmentos de pedra acompanham o movimento.

**Frames 19–20 — Retorno**

Assume novamente a postura de combate.

### Características

- Movimento extremamente pesado.
- Aceleração gradual seguida de impacto explosivo.
- Rotação convincente dos blocos do ombro.
- Pequenas vibrações secundárias nas placas rochosas.
- Movimento coerente das articulações mágicas.
- Sensação de massa elevada.
- Recuperação mais lenta que inimigos orgânicos.

**Função visual:** ataque físico principal.

**Transição:** Idle/Walk → Attack → Idle/Walk.

---

## 04 — HURT: ABALO ESTRUTURAL (12 frames × 8 direções = 96 frames)

Criar uma reação de dano compatível com uma criatura extremamente resistente.

O Stone Golem deve apresentar uma reação curta, baseada em vibrações e deslocamentos de suas placas rochosas.

### Estrutura

- **Frames 1–3:** impacto inicial.
- **Frames 4–6:** pequena oscilação do torso e deslocamento das placas.
- **Frames 7–9:** fragmentos e poeira se desprendem discretamente.
- **Frames 10–12:** recuperação da postura.

### Durante o Hurt

- O torso recua poucos pixels.
- A cabeça inclina levemente.
- O núcleo elemental pulsa brevemente.
- Algumas rachaduras podem emitir brilho momentâneo.
- Pequenos fragmentos de pedra se desprendem.
- Os braços reagem ao impacto.
- Os pés permanecem firmemente apoiados no chão.

**Função visual:** feedback de dano.

O Golem não deve demonstrar dor orgânica ou expressões faciais humanas.

---

## 05 — DIED: COLAPSO DO COLOSSO DE PEDRA (32 frames × 8 direções = 256 frames)

Criar uma animação de morte elaborada, representando a perda da energia mágica que mantém o Golem unido.

### Estrutura

**Frames 1–4 — Impacto fatal**

O Golem recebe o golpe final, provocando uma forte oscilação estrutural.

**Frames 5–8 — Instabilidade elemental**

O núcleo mágico começa a piscar irregularmente e as runas perdem intensidade.

**Frames 9–12 — Ruptura das articulações**

Pequenos fragmentos se desprendem, enquanto os braços começam a perder sustentação.

**Frames 13–16 — Falha estrutural**

As pernas cedem parcialmente e o torso começa a inclinar.

**Frames 17–20 — Desmoronamento**

Grandes blocos rochosos começam a se separar e cair.

**Frames 21–24 — Impacto no solo**

O torso e a cabeça atingem o chão, produzindo poeira e fragmentos.

**Frames 25–28 — Dissipação mágica**

O núcleo elemental perde completamente seu brilho, enquanto a energia que unia os blocos desaparece.

**Frames 29–31 — Estabilização**

Os fragmentos rochosos concluem seus movimentos residuais.

**Frame 32 — Ruínas finais**

O Golem transforma-se em uma pilha de blocos de pedra, com o núcleo apagado entre os destroços.

### Regras da morte

- Preservar a identidade visual dos blocos durante o colapso.
- Não criar ou remover pedras arbitrariamente.
- Manter continuidade espacial dos fragmentos.
- Respeitar gravidade e perspectiva.
- Separar poeira e energia elemental em VFX independentes.
- Finalizar com composição estática de destroços.

**Sem loop.** O último frame permanece visível até a remoção dos destroços.

---

# 5. HABILIDADES ESPECIAIS

## 06 — SKILL 01: IMPACTO TERRESTRE (28 frames × 8 direções = 224 frames)

O Stone Golem ergue ambos os punhos e golpeia violentamente o solo, provocando uma onda de choque circular.

### Estrutura

**Frames 1–4 — Preparação**

O Golem firma os pés e inclina o torso para trás.

**Frames 5–9 — Elevação**

Ergue lentamente os dois braços acima da cabeça.

**Frames 10–13 — Acúmulo**

O núcleo elemental brilha intensamente enquanto energia percorre as rachaduras dos braços.

**Frames 14–18 — Golpe**

Os dois punhos descem violentamente em direção ao solo.

**Frames 19–21 — Impacto**

Os punhos atingem o chão, desencadeando uma explosão de poeira e uma onda sísmica.

**Frames 22–25 — Recuperação**

O Golem começa a erguer o torso e recolher os braços.

**Frames 26–28 — Retorno**

Reassume sua postura de combate.

### Características

- Grande antecipação visual.
- Movimento sincronizado dos braços.
- Forte impacto no solo.
- Poeira e fragmentos.
- Energia elemental percorrendo as rachaduras.
- Onda circular em perspectiva isométrica.

**Função visual:** ataque físico em área, com possibilidade de atordoamento.

O evento de impacto deve ocorrer no frame 19.

---

## 07 — SKILL 02: ARREMESSO DE ROCHA (26 frames × 8 direções = 208 frames)

O Stone Golem materializa uma grande rocha em uma de suas mãos e a arremessa contra o jogador.

### Estrutura

**Frames 1–4 — Preparação**

O Golem interrompe seus movimentos e direciona o olhar ao alvo.

**Frames 5–9 — Conjuração terrestre**

Ergue uma das mãos enquanto pequenas pedras começam a se reunir.

**Frames 10–13 — Formação**

Os fragmentos se unem, formando uma rocha compacta.

**Frames 14–17 — Preparação do arremesso**

O Golem recua o braço e gira parcialmente o torso.

**Frames 18–20 — Arremesso**

Projeta o braço para frente e libera a rocha.

**Frames 21–24 — Recuperação**

O braço retorna gradualmente enquanto pequenas partículas residuais desaparecem.

**Frames 25–26 — Retorno**

Assume novamente a postura de combate.

### Características

- Formação progressiva da rocha.
- Fragmentos flutuando antes de se unirem.
- Movimento pesado do braço.
- Arremesso com sensação de força.
- Poeira e pequenas partículas.
- Continuidade visual entre a rocha formada e o projétil.

**Função visual:** ataque físico à distância.

O projétil deve ser criado pela engine no frame 19.

---

## 08 — SKILL 03: ARMADURA DE PEDRA (26 frames × 8 direções = 208 frames)

O Stone Golem utiliza energia elemental para reforçar temporariamente sua estrutura corporal.

### Estrutura

**Frames 1–4 — Preparação**

O Golem recolhe os braços e adota uma postura defensiva.

**Frames 5–8 — Canalização**

O núcleo elemental começa a brilhar intensamente.

**Frames 9–13 — Formação**

Pequenos fragmentos de pedra surgem ao redor do corpo e começam a se fixar sobre sua estrutura.

**Frames 14–18 — Reforço**

Novas placas rochosas se formam sobre ombros, torso e braços.

**Frames 19–22 — Estabilização**

As placas se consolidam e as runas emitem um pulso luminoso.

**Frames 23–26 — Retorno**

O Golem reassume a postura de combate, agora protegido por uma camada adicional de pedra.

### Características

- Formação progressiva das placas.
- Energia elemental concentrada no núcleo.
- Pequenas partículas minerais.
- Brilho rúnico discreto.
- Sensação de reforço estrutural.

**Função visual:** redução temporária de dano.

### STONE ARMOR HOLD — 12 frames × 8 direções = 96 frames

Criar uma animação complementar para o estado defensivo.

Durante o Hold:

- O núcleo permanece mais luminoso.
- As placas adicionais continuam visíveis.
- Pequenas partículas minerais surgem ocasionalmente.
- O corpo apresenta movimentos discretos.
- As runas pulsam suavemente.

**Loop:** perfeitamente contínuo.

**Importante:** as placas adicionais devem ser entregues preferencialmente como camadas visuais independentes, permitindo que o Golem caminhe, ataque e utilize outras habilidades com a armadura ativa.

O Hold não deve substituir as animações de combate.

---

## 09 — SKILL 04: ERUPÇÃO ROCHOSA (30 frames × 8 direções = 240 frames)

O Stone Golem manipula a energia terrestre para fazer pilares rochosos emergirem do chão sob os jogadores.

### Estrutura

**Frames 1–4 — Preparação**

O Golem firma os pés e ergue lentamente os braços.

**Frames 5–9 — Canalização**

O núcleo elemental brilha intensamente, enquanto pequenas pedras flutuam próximas ao corpo.

**Frames 10–14 — Acúmulo**

As runas do torso e dos braços se iluminam, indicando concentração de energia terrestre.

**Frames 15–18 — Direcionamento**

O Golem aponta os braços para a região selecionada.

**Frames 19–22 — Ativação**

Fecha os punhos e realiza um gesto brusco, provocando a erupção dos pilares.

**Frames 23–26 — Dissipação**

A energia residual desaparece gradualmente.

**Frames 27–30 — Recuperação**

O Golem retorna à postura de combate.

### Características

- Gestos elementais pesados.
- Energia percorrendo rachaduras.
- Pequenas pedras flutuantes.
- Impacto visual forte.
- Pilares emergindo progressivamente.
- Poeira e fragmentos.
- Perspectiva isométrica consistente.

**Função visual:** controle de área e dano físico elemental.

Os pilares devem possuir spritesheets independentes de surgimento, sustentação e destruição.

---

# 6. PROJÉTEIS OBRIGATÓRIOS

## PROJÉTIL 01 — ROCHA ARREMESSADA

Criar uma spritesheet própria para a rocha utilizada pelo Stone Golem.

**Animação de voo:** 12 frames em loop.

Características:

- Rocha irregular de tamanho médio.
- Textura consistente com o corpo do Golem.
- Pequenas rachaduras.
- Rotação controlada durante o voo.
- Fragmentos de poeira acompanhando o deslocamento.
- Silhueta clara em tamanho reduzido.

**Impacto:** 12 frames sem loop.

Ao atingir o alvo ou o cenário, a rocha se fragmenta em pedaços menores, acompanhados por uma pequena explosão de poeira.

**Sincronização:** spawn no frame 19 da Skill Arremesso de Rocha.

---

# 7. EFEITOS DE SOLO E ESTRUTURAS

## ELEMENTO 01 — ONDA SÍSMICA

**Animação:** 16 frames.

Uma onda circular de força percorre o terreno a partir do ponto de impacto.

Características:

- Expansão radial em perspectiva isométrica.
- Poeira e pequenos fragmentos.
- Rachaduras temporárias.
- Energia elemental discreta.
- Desaparecimento gradual.

A área de colisão deve ser controlada pela engine.

## ELEMENTO 02 — PILAR ROCHOSO

Criar três estados independentes.

### Surgimento — 18 frames

- Pequenas rachaduras aparecem no chão.
- Poeira começa a emergir.
- A ponta do pilar rompe a superfície.
- O pilar sobe progressivamente.
- Fragmentos menores se desprendem.
- A estrutura atinge sua altura final.

### Sustentação — 8 frames em loop

- Pilar permanece firme.
- Pequenas partículas de poeira se desprendem.
- Rachaduras podem apresentar brilho elemental discreto.

### Destruição — 16 frames

- O pilar apresenta novas rachaduras.
- Fragmentos começam a se desprender.
- A estrutura colapsa progressivamente.
- Poeira e pedras se espalham.
- O efeito desaparece.

**Função visual:** obstáculo temporário ou ataque em área, conforme o gameplay.

---

# 8. VFX OBRIGATÓRIOS

Produzir spritesheets independentes.

### VFX 01 — STONE FIST IMPACT (10 frames)

Impacto físico de punho rochoso.

- Poeira.
- Pequenos fragmentos.
- Explosão curta.
- Rachaduras discretas.

### VFX 02 — GROUND SLAM CHARGE (12 frames)

Energia elemental percorrendo os braços durante o Impacto Terrestre.

### VFX 03 — GROUND SLAM EXPLOSION (16 frames)

Explosão de poeira e fragmentos no ponto de impacto.

### VFX 04 — SEISMIC WAVE (16 frames)

Onda de choque circular sobre o terreno.

### VFX 05 — ROCK FORMATION (12 frames)

Fragmentos de pedra reunindo-se para formar o projétil.

### VFX 06 — ROCK PROJECTILE IMPACT (12 frames)

Fragmentação da rocha arremessada.

### VFX 07 — STONE ARMOR ACTIVATION (16 frames)

Formação das placas de reforço.

### VFX 08 — STONE ARMOR AURA (12 frames em loop)

Brilho rúnico discreto durante o estado defensivo.

### VFX 09 — ROCK ERUPTION CHARGE (12 frames)

Concentração de energia antes da Erupção Rochosa.

### VFX 10 — ROCK PILLAR EMERGENCE (18 frames)

Poeira, rachaduras e fragmentos durante o surgimento dos pilares.

### VFX 11 — ROCK PILLAR DESTRUCTION (16 frames)

Fragmentos e poeira durante o colapso das estruturas.

### VFX 12 — HEAVY FOOTSTEP (8 frames)

Poeira e pequenas vibrações no contato dos pés com o chão.

### VFX 13 — STONE HIT (8 frames)

Pequenos fragmentos desprendendo-se ao receber dano.

### VFX 14 — GOLEM DEATH COLLAPSE (20 frames)

Grande nuvem de poeira e fragmentos durante a morte.

### VFX 15 — ELEMENTAL CORE FADE (12 frames)

Dissipação gradual da energia do núcleo após a morte.

Todos os VFX devem preservar a estética Pixel Art Chibi, a perspectiva isométrica e a identidade elemental terrestre.

---

# 9. ESPECIFICAÇÕES TÉCNICAS

| Animação | Frames/direção | Direções | Total |
|---|---:|---:|---:|
| Idle | 20 | 8 | 160 |
| Walk | 20 | 8 | 160 |
| Attack — Punho Rochoso | 20 | 8 | 160 |
| Hurt | 12 | 8 | 96 |
| Died — Colapso Rochoso | 32 | 8 | 256 |
| Skill 01 — Impacto Terrestre | 28 | 8 | 224 |
| Skill 02 — Arremesso de Rocha | 26 | 8 | 208 |
| Skill 03 — Armadura de Pedra | 26 | 8 | 208 |
| Stone Armor Hold | 12 | 8 | 96 |
| Skill 04 — Erupção Rochosa | 30 | 8 | 240 |
| **TOTAL** | | | **1.808 frames** |

**Total corporal: 1.808 frames distribuídos em oito direções.**

Projéteis, pilares, ondas sísmicas e VFX devem ser entregues separadamente.

---

# 10. FPS RECOMENDADOS

- **Idle:** 10–12 FPS.
- **Walk:** 12–16 FPS.
- **Attack:** 16–20 FPS.
- **Hurt:** 16–20 FPS.
- **Died:** 12–16 FPS.
- **Impacto Terrestre:** 16–20 FPS.
- **Arremesso de Rocha:** 16–20 FPS.
- **Armadura de Pedra:** 16–20 FPS.
- **Stone Armor Hold:** 8–12 FPS.
- **Erupção Rochosa:** 16–20 FPS.
- **Projéteis:** 16–24 FPS.
- **VFX:** 18–24 FPS.

A engine poderá ajustar a velocidade de reprodução conforme as necessidades de gameplay.

---

# 11. REGRAS OBRIGATÓRIAS DE FLUIDEZ

- Produzir sprites próprios para todas as oito direções.
- Preservar rigorosamente a estrutura rochosa do personagem.
- Manter cada placa, rachadura e cristal com aparência consistente.
- Não alterar involuntariamente a quantidade de blocos corporais.
- Preservar proporções, escala e silhueta.
- Respeitar a anatomia humanoide construída em pedra.
- Garantir que as articulações funcionem de maneira convincente.
- Manter continuidade espacial dos fragmentos rochosos.
- Evitar pedras surgindo ou desaparecendo sem justificativa visual.
- Animar movimentos pesados com antecipação, aceleração e recuperação.
- Preservar sensação de massa corporal elevada.
- Garantir contato correto dos pés com o chão.
- Evitar deslizamento durante a caminhada.
- Manter ponto de ancoragem estável.
- Preservar a perspectiva isométrica.
- Garantir transições suaves entre Idle, Walk, Attack, Hurt e Skills.
- Idle, Walk e Stone Armor Hold devem possuir loops perfeitamente contínuos.
- Attack e Skills devem começar e terminar em poses compatíveis com a postura de combate.
- Hurt deve permitir retorno natural ao Idle ou Walk.
- Died deve terminar em uma composição estática de destroços.
- Não deformar o corpo como se fosse composto por músculos orgânicos.
- Preservar rigidez individual dos blocos, utilizando articulações coerentes.
- Evitar tremores, teleportes involuntários e mudanças bruscas de escala.
- Manter iluminação, paleta e contornos consistentes.
- Não utilizar interpolação borrada.
- Usar fundo transparente verdadeiro.
- Não permitir bordas, halos, pixels soltos ou vazamentos entre células.
- Reservar espaço suficiente para os braços erguidos e golpes amplos.
- Manter dimensões uniformes e recortes consistentes.
- Separar VFX, projéteis e estruturas do corpo principal.
- Sincronizar todos os efeitos com os eventos de gameplay.
- Garantir boa leitura visual em escala reduzida.
- Validar todas as oito direções individualmente.

---

# 12. ORGANIZAÇÃO DOS ARQUIVOS

Entregar arquivos independentes.

### Spritesheets corporais

- `stone_golem_idle.png`
- `stone_golem_walk.png`
- `stone_golem_attack.png`
- `stone_golem_hurt.png`
- `stone_golem_died.png`
- `stone_golem_skill_ground_slam.png`
- `stone_golem_skill_rock_throw.png`
- `stone_golem_skill_stone_armor.png`
- `stone_golem_stone_armor_hold.png`
- `stone_golem_skill_rock_eruption.png`

### Projéteis e estruturas

- `stone_golem_projectile_rock.png`
- `stone_golem_seismic_wave.png`
- `stone_golem_rock_pillar_emerge.png`
- `stone_golem_rock_pillar_hold.png`
- `stone_golem_rock_pillar_break.png`

### VFX

- `stone_golem_vfx_fist_impact.png`
- `stone_golem_vfx_ground_slam.png`
- `stone_golem_vfx_seismic.png`
- `stone_golem_vfx_rock_formation.png`
- `stone_golem_vfx_rock_impact.png`
- `stone_golem_vfx_stone_armor.png`
- `stone_golem_vfx_eruption.png`
- `stone_golem_vfx_footstep.png`
- `stone_golem_vfx_hit.png`
- `stone_golem_vfx_death.png`
- `stone_golem_vfx_core_fade.png`

### Metadados

- `stone_golem_animations.json`

Cada spritesheet corporal deve utilizar **8 linhas direcionais**, na ordem:

N, NE, E, SE, S, SW, W, NW.

Os frames devem estar organizados horizontalmente em sequência cronológica.

### O arquivo JSON deve conter

- Identificador do inimigo.
- Nomes das animações.
- Direções e quantidade de frames.
- Coordenadas de recorte.
- Dimensões das células.
- FPS de reprodução.
- Configurações de loop.
- Ponto de ancoragem dos pés.
- Hitbox e hurtbox.
- Coordenadas dos punhos e articulações.
- Coordenadas do núcleo elemental.
- Eventos de início e término dos ataques.
- Frames de aplicação de dano.
- Eventos de impacto no solo.
- Eventos de geração de projéteis.
- Eventos de surgimento e destruição dos pilares.
- Eventos de ativação e encerramento da Armadura de Pedra.
- Referências aos VFX.
- Regras de interrupção por Hurt.
- Estados e transições.
- Estado final de morte.

---

# 13. REGRAS DE GAMEPLAY E SINCRONIZAÇÃO

As animações devem ser preparadas para integração com uma máquina de estados de gameplay.

**Estados principais:** Idle → Walk → Attack → Skills → Hurt → Died.

### Punho Rochoso

- Contato principal: frame 13.
- Origem: punho ativo.
- Alcance: curto.
- Dano e colisão: controlados pela engine.

### Impacto Terrestre

- Ativação: frame 19.
- Origem: ponto de contato dos punhos com o solo.
- Área: circular em perspectiva isométrica.
- Colisão: independente do sprite corporal.

### Arremesso de Rocha

- Spawn do projétil: frame 19.
- Origem: mão utilizada no arremesso.
- Direção: orientação atual do personagem.
- Dano e trajetória: controlados pela engine.

### Armadura de Pedra

- Ativação: frame 19.
- Duração: controlada pela engine.
- Placas adicionais: camadas visuais independentes.
- Redução de dano: determinada pelo sistema de combate.

### Erupção Rochosa

- Ativação: frame 19.
- Origem: pontos selecionados no terreno.
- Pilares: entidades visuais independentes.
- Colisão: controlada pela engine.
- Destruição: animação específica.

Os números de frame indicam eventos visuais e devem ser interpretados com indexação iniciada em 1. O JSON deve registrar a convenção utilizada para evitar erros de sincronização.

---

# 14. VALIDAÇÃO OBRIGATÓRIA

Antes de considerar o conjunto concluído:

1. Reproduzir Idle e Walk por cinco ciclos completos em cada direção.
2. Confirmar consistência das placas, rachaduras e runas.
3. Validar contato correto dos pés com o chão.
4. Testar transições Idle → Attack → Idle e Walk → Attack → Walk.
5. Verificar a trajetória completa do Punho Rochoso.
6. Testar Impacto Terrestre e sincronização da onda sísmica.
7. Validar formação, arremesso e impacto da rocha.
8. Confirmar continuidade visual do projétil.
9. Testar Armadura de Pedra e suas camadas adicionais.
10. Validar o estado defensivo durante Walk e Attack.
11. Testar Erupção Rochosa, incluindo surgimento e destruição dos pilares.
12. Validar interrupções por Hurt.
13. Reproduzir a morte completa em todas as oito direções.
14. Confirmar estabilidade dos destroços finais.
15. Verificar consistência dos fragmentos durante o colapso.
16. Inspecionar recortes, transparências e limites dos frames.
17. Corrigir tremores, deformações e alterações involuntárias de escala.
18. Testar mudanças de direção durante o deslocamento.
19. Validar posicionamento dos VFX em todas as orientações.
20. Testar o tamanho do Golem na escala real do jogo.
21. Confirmar legibilidade durante combates com múltiplos inimigos.
22. Verificar a sincronização dos eventos de gameplay.
23. Confirmar ausência de bordas ou vazamentos entre células.
24. Validar todos os loops em reprodução contínua.

---

# 15. RESULTADO ESPERADO

Entregar um conjunto completo de spritesheets para um **Stone Golem em Pixel Art Chibi**, contendo:

- **Idle:** 160 frames.
- **Walk:** 160 frames.
- **Attack — Punho Rochoso:** 160 frames.
- **Hurt:** 96 frames.
- **Died — Colapso Rochoso:** 256 frames.
- **Skill 01 — Impacto Terrestre:** 224 frames.
- **Skill 02 — Arremesso de Rocha:** 208 frames.
- **Skill 03 — Armadura de Pedra:** 208 frames.
- **Stone Armor Hold:** 96 frames.
- **Skill 04 — Erupção Rochosa:** 240 frames.
- **Projétil próprio:** Rocha Arremessada, com voo e impacto.
- **Efeito de área:** Onda Sísmica.
- **Estruturas independentes:** Pilares Rochosos com surgimento, sustentação e destruição.
- **VFX exclusivos:** impactos, poeira, fragmentos, energia elemental, armadura, erupção e morte.
- **Metadados completos:** JSON com recortes, direções, âncoras, eventos e transições.

**TOTAL: 1.808 frames corporais distribuídos em oito direções, além dos projéteis, estruturas e VFX independentes.**

O Stone Golem deve funcionar como um inimigo elemental de elite completo, capaz de absorver grandes quantidades de dano, executar golpes físicos devastadores, provocar ondas sísmicas, arremessar pedras, reforçar sua própria defesa e criar pilares rochosos para controlar o campo de batalha.

Sua movimentação deve transmitir **peso monumental, resistência extrema, força elemental, rigidez estrutural e poder ancestral**.

**PRIORIDADE ABSOLUTA:** oito direções completas, fluidez excepcional, consistência estrutural, peso convincente, continuidade entre movimentos, sincronização precisa dos ataques, identidade visual consistente e sprites prontos para integração direta em um MMORPG 2D isométrico.

Não substituir animações completas por poses estáticas, espelhamentos inadequados, frames artificialmente duplicados ou efeitos genéricos. Cada animação deve ser produzida e validada individualmente nas oito direções.

**CRITÉRIO FINAL DE APROVAÇÃO:** o Stone Golem somente estará concluído quando todas as animações, projéteis, estruturas, VFX e metadados estiverem completos, organizados e validados, sem tremores, bordas, deformações ou inconsistências entre frames.