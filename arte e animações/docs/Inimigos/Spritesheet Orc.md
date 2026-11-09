# INIMIGO ORC — SPRITESHEET COMPLETA EM 8 DIREÇÕES

Crie um conjunto completo de spritesheets para um **Orc Guerreiro de RPG 2D isométrico, inspirado em Diablo II, com estética Pixel Art Chibi e fantasia medieval sombria**.

O Orc deve ser um inimigo de porte médio a grande, musculoso, resistente e agressivo, especializado em combate corpo a corpo, ataques brutais e habilidades de intimidação.

Sua aparência deve transmitir a sensação de um guerreiro tribal feroz, experiente em batalhas, que utiliza força física, resistência e agressividade para derrotar seus adversários.

Diferentemente do Minotauro, que se destaca pelo enorme peso e força devastadora, o Orc deve apresentar **movimentação mais dinâmica, ataques sucessivos e comportamento de combate agressivo**, combinando força bruta com uma experiência guerreira primitiva.

Apesar das proporções chibi, o personagem deve parecer poderoso, ameaçador e perigoso.

O objetivo é produzir animações extremamente fluidas, expressivas e prontas para gameplay real, com movimentos corporais convincentes, ataques físicos variados, habilidades especiais, efeitos visuais próprios e oito direções completas.

---

## 1. IDENTIDADE VISUAL

O Orc deve possuir:

- Corpo robusto, largo e musculoso.
- Cabeça proporcionalmente grande, característica da estética chibi.
- Pele verde-oliva ou verde-escura, com variações naturais de tonalidade.
- Mandíbula larga e proeminente.
- Dois grandes dentes inferiores projetados para fora da boca.
- Nariz achatado e largo.
- Orelhas pontudas e grossas.
- Sobrancelhas marcadas e expressão agressiva.
- Olhos pequenos, de coloração âmbar ou avermelhada.
- Braços musculosos e mãos grandes.
- Pernas fortes, com postura de guerreiro.
- Pequenas cicatrizes distribuídas pelo rosto, braços e torso.
- Cabelo escuro preso em uma pequena trança ou moicano tribal.
- Armadura improvisada com couro, metal enferrujado e peles.
- Ombreira metálica assimétrica.
- Braceletes grossos de couro.
- Cinto com fivela grande e pequenos troféus de batalha.
- Botas resistentes ou sandálias de combate reforçadas.
- Machado de guerra de uma mão, com lâmina pesada e desgastada.
- Escudo tribal de madeira reforçada com metal na outra mão.

**Arma principal:** machado de guerra de uma mão, segurado na mão direita anatômica.

**Equipamento secundário:** escudo tribal, segurado na mão esquerda anatômica.

**Personalidade visual:** guerreiro agressivo, orgulhoso, territorial, brutal e experiente.

**Direção de animação:** movimentos poderosos, rápidos para seu tamanho, com antecipações claras, ataques explosivos e recuperação dinâmica.

---

## 2. SISTEMA OBRIGATÓRIO DE 8 DIREÇÕES

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
- Manter o machado sempre na mão direita anatômica.
- Manter o escudo sempre na mão esquerda anatômica.
- Preservar assimetrias da armadura e acessórios.
- Respeitar a profundidade correta entre braços, pernas, escudo e machado.
- Não utilizar espelhamento automático quando isso inverter equipamentos ou alterar detalhes visuais.
- Preservar proporções corporais constantes.
- Manter o mesmo ponto de ancoragem no chão, centralizado entre os pés.
- Reservar espaço suficiente para golpes amplos e movimentos do machado.
- Garantir que as oito direções representem o mesmo personagem.

---

# 3. CONCEITO DE COMBATE

**Tipo:** inimigo guerreiro corpo a corpo, resistente e ofensivo.

**Função:** pressionar jogadores, realizar ataques físicos consecutivos, bloquear golpes ocasionais e utilizar habilidades de combate agressivas.

**Comportamento:** territorial, impulsivo, agressivo e persistente.

**Ataque básico:** Corte Selvagem — golpe diagonal com machado.

**Skill 01:** Golpe Esmagador — ataque pesado com machado, capaz de provocar forte impacto e possível atordoamento.

**Skill 02:** Investida Brutal — avanço rápido com escudo, utilizado para aproximar-se do jogador e empurrá-lo.

**Skill 03:** Grito de Guerra — rugido que fortalece temporariamente o Orc e pode beneficiar outros Orcs próximos.

**Diferencial:** combina ataques de força bruta, defesa com escudo e agressividade tribal.

**Projéteis:** não utiliza projéteis convencionais. Todos os ataques são físicos ou habilidades de curto alcance.

---

# 4. ANIMAÇÕES OBRIGATÓRIAS

## 01 — IDLE (16 frames × 8 direções = 128 frames)

O Orc permanece em posição de combate, segurando o machado na mão direita e o escudo na esquerda.

Sua postura deve transmitir agressividade, impaciência e prontidão para atacar.

Durante o Idle:

- O peito expande e contrai lentamente, simulando respiração forte.
- Os ombros apresentam pequenas oscilações.
- A cabeça inclina discretamente, observando os arredores.
- A mandíbula movimenta-se ocasionalmente, exibindo os dentes.
- O Orc aperta e ajusta a empunhadura do machado.
- O escudo realiza pequenos ajustes defensivos.
- O tronco inclina-se levemente para frente.
- O peso corporal alterna discretamente entre as pernas.
- As roupas e acessórios acompanham suavemente os movimentos.
- A expressão permanece ameaçadora.
- Pequenos movimentos das sobrancelhas reforçam sua personalidade agressiva.

O Orc deve parecer constantemente pronto para iniciar um confronto.

**Loop:** perfeitamente contínuo, com retorno natural à postura inicial.

---

## 02 — WALK (16 frames × 8 direções = 128 frames)

Criar uma caminhada firme, agressiva e dinâmica.

O Orc deve se movimentar como um guerreiro robusto, mas relativamente ágil.

Durante o Walk:

- As pernas executam um ciclo completo de passos alternados.
- Os pés apresentam levantamento, avanço, contato e impulsão.
- O tronco mantém leve inclinação para frente.
- Os ombros acompanham o deslocamento com movimentos coordenados.
- O machado oscila naturalmente com a caminhada.
- O escudo permanece próximo ao corpo, protegendo parcialmente o torso.
- A cabeça mantém o olhar direcionado à movimentação.
- A armadura e os acessórios apresentam movimentos secundários.
- O peso corporal desloca-se naturalmente entre as pernas.
- Os joelhos flexionam de maneira convincente.
- A passada deve transmitir confiança e agressividade.

O Orc não deve caminhar tão lentamente quanto um Minotauro, nem tão rapidamente quanto um Goblin.

**Regra fundamental:** os pés devem permanecer estáveis durante a fase de apoio, sem deslizar sobre o chão.

**Loop:** perfeito, com continuidade natural entre passos.

---

## 03 — ATTACK: CORTE SELVAGEM (16 frames × 8 direções = 128 frames)

Criar um ataque básico com machado de uma mão.

O movimento deve ser rápido, poderoso e agressivo.

### Estrutura

**Frames 1–4 — Antecipação**

O Orc recua o braço armado, gira parcialmente o tronco e prepara o golpe.

**Frames 5–7 — Preparação**

Flexiona discretamente os joelhos, posiciona o escudo à frente e concentra o peso corporal.

**Frames 8–10 — Execução**

Realiza um corte diagonal rápido e brutal, direcionando o machado contra o alvo.

**Frames 11–12 — Finalização**

O machado completa seu arco, enquanto o torso acompanha a força do golpe.

**Frames 13–16 — Recuperação**

O Orc recolhe o machado e retorna à postura ofensiva.

### Características obrigatórias

- Movimento coordenado de ombros, tronco e braços.
- Sensação convincente de peso do machado.
- Arco de ataque claramente legível.
- Escudo permanecendo em posição defensiva.
- Expressão facial agressiva.
- Recuperação relativamente rápida.
- Movimento secundário dos acessórios.

**Função visual:** ataque físico principal.

**Transição:** Idle/Walk → Attack → Idle/Walk.

---

## 04 — HURT (10 frames × 8 direções = 80 frames)

Criar uma reação ao receber dano compatível com um guerreiro forte e resistente.

O Orc deve demonstrar dor e irritação, mas não parecer excessivamente frágil.

### Estrutura

- **Frames 1–2:** impacto inicial.
- **Frames 3–5:** recuo do tronco, contração dos ombros e expressão de dor.
- **Frames 6–8:** recuperação do equilíbrio.
- **Frames 9–10:** retorno à postura de combate.

### Durante a animação

- A cabeça recua rapidamente.
- A mandíbula abre em expressão de dor ou raiva.
- O machado oscila acompanhando o impacto.
- O escudo perde discretamente sua posição defensiva.
- Os ombros se contraem.
- O corpo apresenta pequeno desequilíbrio.
- As pernas permanecem firmes.
- O Orc recupera sua postura com agressividade.

**Função visual:** feedback de dano recebido.

A reação deve ser rápida e clara, preservando a fluidez do combate.

---

## 05 — DIED: QUEDA DO GUERREIRO (24 frames × 8 direções = 192 frames)

Criar uma morte completa e convincente, enfatizando o peso corporal e a brutalidade do Orc.

### Estrutura

**Frames 1–4 — Impacto fatal**

O Orc recebe o golpe final, recua e perde parcialmente o equilíbrio.

**Frames 5–8 — Resistência**

Tenta permanecer em pé, apoiando-se momentaneamente no escudo ou firmando as pernas.

**Frames 9–12 — Perda de força**

Os joelhos começam a ceder, enquanto o machado escapa parcialmente de sua mão.

**Frames 13–16 — Colapso**

O Orc cai progressivamente, acompanhado pelo movimento da armadura e dos acessórios.

**Frames 17–20 — Impacto no solo**

O corpo atinge o chão, provocando pequena nuvem de poeira. Machado e escudo caem próximos ao corpo.

**Frames 21–23 — Estabilização**

Os membros e acessórios concluem os movimentos residuais.

**Frame 24 — Cadáver final**

O Orc permanece completamente imóvel, em uma pose de morte clara e legível.

### Regras da morte

- Preservar a anatomia durante a queda.
- Não permitir desaparecimento repentino dos equipamentos.
- Manter machado e escudo próximos ao corpo.
- Respeitar a direção em que o Orc estava orientado.
- Representar o peso corporal de maneira convincente.
- Terminar em uma pose estável.

**Sem loop.** Manter o último frame até a remoção do cadáver.

---

# 5. HABILIDADES ESPECIAIS

## 06 — SKILL 01: GOLPE ESMAGADOR (20 frames × 8 direções = 160 frames)

O Orc ergue seu machado e executa um golpe vertical devastador.

### Estrutura

**Frames 1–4 — Preparação**

O Orc firma os pés no chão e posiciona o machado próximo ao ombro.

**Frames 5–8 — Elevação**

Ergue o machado acima da cabeça, utilizando grande parte de sua força corporal.

**Frames 9–11 — Acúmulo**

Contrai os músculos e prepara o golpe, mantendo o machado erguido por um breve instante.

**Frames 12–15 — Execução**

Desce o machado violentamente em direção ao alvo.

**Frames 16–17 — Impacto**

A lâmina atinge o alvo ou o chão, produzindo um efeito de impacto pesado.

**Frames 18–20 — Recuperação**

O Orc recolhe o machado e retorna à postura de combate.

### Características

- Forte antecipação visual.
- Movimento amplo e pesado.
- Rotação natural do tronco.
- Sensação de grande impacto.
- Pequena poeira ou faísca no ponto de contato.
- Recuperação mais lenta que o ataque básico.

**Função visual:** ataque físico de alto dano, com possibilidade de atordoamento.

O VFX de impacto deve ser independente e sincronizado com o frame 16.

---

## 07 — SKILL 02: INVESTIDA BRUTAL (22 frames × 8 direções = 176 frames)

O Orc posiciona o escudo à frente do corpo e realiza uma investida agressiva contra o jogador.

### Estrutura

**Frames 1–4 — Preparação**

Flexiona os joelhos, inclina o tronco e aproxima o escudo do centro do corpo.

**Frames 5–8 — Posicionamento**

Ergue o escudo à frente, preparando-se para avançar.

**Frames 9–12 — Impulso**

Inicia uma corrida curta e explosiva, mantendo o escudo à frente.

**Frames 13–16 — Investida**

Avança rapidamente, utilizando o peso corporal para atingir o alvo.

**Frames 17–19 — Impacto**

Realiza uma colisão com o escudo, acompanhada por um pequeno recuo dos ombros.

**Frames 20–22 — Recuperação**

Retorna à posição de combate.

### Características

- Escudo claramente posicionado à frente.
- Tronco inclinado durante o avanço.
- Passos rápidos e agressivos.
- Movimento coordenado dos braços.
- Machado mantido recolhido ao lado do corpo.
- Poeira nos pés durante o avanço.
- Impacto visual forte ao atingir o alvo.

**Função visual:** aproximação ofensiva, dano físico e possível empurrão.

**Importante:** o deslocamento global deve ser realizado pela engine.

Para permitir distâncias variáveis, os frames centrais da corrida devem formar um subloop fluido, separado da preparação e da recuperação.

---

## 08 — SKILL 03: GRITO DE GUERRA (24 frames × 8 direções = 192 frames)

O Orc solta um rugido poderoso que aumenta temporariamente sua agressividade e pode fortalecer aliados próximos.

### Estrutura

**Frames 1–4 — Preparação**

O Orc interrompe seus movimentos, firma os pés e contrai os ombros.

**Frames 5–8 — Acúmulo**

Expande o peito, ergue discretamente a cabeça e abre a mandíbula.

**Frames 9–13 — Rugido**

Solta um rugido intenso, levantando parcialmente o machado.

**Frames 14–17 — Ativação**

Uma aura avermelhada ou alaranjada surge ao redor do corpo.

**Frames 18–21 — Intensificação**

A aura pulsa enquanto o Orc mantém postura agressiva.

**Frames 22–24 — Recuperação**

Abaixa o machado e retorna à posição de combate, mantendo os efeitos do fortalecimento ativo.

### Características

- Expressão extremamente agressiva.
- Boca bem aberta durante o rugido.
- Contração convincente do torso.
- Movimento secundário dos acessórios.
- Pequeno pulso energético expandindo ao redor do personagem.
- Brilho temporário nos olhos.

**Função visual:** fortalecimento temporário de dano, velocidade de ataque ou agressividade.

### WAR CRY BUFF HOLD — 12 frames × 8 direções = 96 frames

Criar uma animação complementar para o estado fortalecido.

Durante o Buff Hold:

- O Orc apresenta respiração mais intensa.
- Os ombros mantêm maior tensão.
- Os olhos podem permanecer levemente avermelhados.
- Pequenas partículas energéticas surgem ocasionalmente.
- A postura apresenta agressividade ampliada.
- O corpo realiza movimentos discretos e contínuos.

**Loop:** perfeitamente contínuo.

A aura deve ser produzida como VFX independente, permitindo sua sobreposição às animações Idle, Walk, Attack e Skills enquanto o fortalecimento estiver ativo.

---

# 6. ANIMAÇÃO COMPLEMENTAR DE DEFESA

## 09 — BLOCK: DEFESA COM ESCUDO (12 frames × 8 direções = 96 frames)

Criar uma animação específica de bloqueio para reforçar a identidade de guerreiro do Orc.

### Estrutura

- **Frames 1–3:** identificação da ameaça e preparação.
- **Frames 4–6:** elevação do escudo para proteger o corpo.
- **Frames 7–9:** sustentação da postura defensiva.
- **Frames 10–12:** retorno à posição de combate.

Durante o bloqueio:

- O escudo deve ficar claramente posicionado entre o corpo e o ataque.
- O braço esquerdo suporta o impacto.
- Os joelhos flexionam discretamente.
- O tronco recua levemente quando ocorre colisão.
- O machado permanece pronto para contra-atacar.

**Função visual:** bloqueio ocasional de ataques frontais.

Para bloqueios de duração variável, criar adicionalmente um loop de sustentação:

**BLOCK HOLD — 8 frames × 8 direções = 64 frames.**

O escudo permanece erguido, com pequenas oscilações de postura.

A engine deve controlar a duração do bloqueio e a transição de retorno ao combate.

---

# 7. PROJÉTEIS

**Não aplicável ao Orc Guerreiro base.**

O Orc utiliza machado, escudo e habilidades de combate físico.

Não criar projéteis artificiais apenas para preencher o conjunto.

Variantes futuras, como Orc Arremessador, Orc Caçador ou Orc Xamã, poderão possuir projéteis próprios.

---

# 8. VFX OBRIGATÓRIOS

Produzir spritesheets independentes para os efeitos visuais.

### VFX 01 — AXE SLASH (8 frames)

Arco de corte associado ao ataque básico.

- Rastro metálico.
- Movimento rápido.
- Pequenas partículas de impacto.
- Dissipação curta.

### VFX 02 — PHYSICAL HIT IMPACT (6 frames)

Efeito físico ao atingir o alvo.

- Faíscas pequenas.
- Fragmentos discretos.
- Estalo visual.
- Expansão rápida.

### VFX 03 — CRUSHING BLOW (12 frames)

Impacto pesado do Golpe Esmagador.

- Explosão curta de força.
- Pequenos fragmentos de pedra.
- Poeira.
- Ondulação discreta de impacto.

### VFX 04 — CHARGE DUST (8 frames)

Poeira produzida durante a Investida Brutal.

- Pequenas nuvens junto aos pés.
- Partículas acompanhando o deslocamento.
- Dissipação gradual.

### VFX 05 — SHIELD IMPACT (8 frames)

Colisão do escudo durante a investida.

- Impacto físico concentrado.
- Pequenas faíscas.
- Poeira e partículas.
- Expansão rápida.

### VFX 06 — WAR CRY ACTIVATION (14 frames)

Ativação do Grito de Guerra.

- Pulso avermelhado.
- Pequenas partículas energéticas.
- Expansão circular curta.
- Dissipação progressiva.

### VFX 07 — WAR CRY AURA (12 frames em loop)

Aura de fortalecimento.

- Brilho alaranjado ou avermelhado discreto.
- Pequenas partículas ascendentes.
- Pulsação suave.
- Compatível com todas as animações corporais.

### VFX 08 — BLOCK IMPACT (6 frames)

Impacto de golpe bloqueado.

- Faíscas no escudo.
- Pequeno efeito de colisão.
- Dissipação rápida.

### VFX 09 — DEATH DUST (10 frames)

Poeira produzida durante a queda do Orc.

### VFX 10 — FOOTSTEP DUST (6 frames)

Pequenas partículas levantadas durante passos mais fortes.

Todos os VFX devem respeitar a mesma identidade visual do inimigo, com orientação adequada à perspectiva isométrica.

---

# 9. ESPECIFICAÇÕES TÉCNICAS

| Animação | Frames/direção | Direções | Total |
|---|---:|---:|---:|
| Idle | 16 | 8 | 128 |
| Walk | 16 | 8 | 128 |
| Attack — Corte Selvagem | 16 | 8 | 128 |
| Hurt | 10 | 8 | 80 |
| Died | 24 | 8 | 192 |
| Skill 01 — Golpe Esmagador | 20 | 8 | 160 |
| Skill 02 — Investida Brutal | 22 | 8 | 176 |
| Skill 03 — Grito de Guerra | 24 | 8 | 192 |
| Buff Hold | 12 | 8 | 96 |
| Block | 12 | 8 | 96 |
| Block Hold | 8 | 8 | 64 |
| **TOTAL** | | | **1.440 frames** |

**Total corporal: 1.440 frames distribuídos em oito direções.**

Os VFX devem ser entregues separadamente.

---

# 10. FPS RECOMENDADOS

- **Idle:** 10–12 FPS.
- **Walk:** 12–16 FPS.
- **Attack:** 16–20 FPS.
- **Hurt:** 16–20 FPS.
- **Died:** 12–16 FPS.
- **Golpe Esmagador:** 16–20 FPS.
- **Investida Brutal:** 18–24 FPS.
- **Grito de Guerra:** 16–20 FPS.
- **Buff Hold:** 10–12 FPS.
- **Block:** 16–20 FPS.
- **Block Hold:** 8–12 FPS.
- **VFX:** 18–24 FPS.

A engine poderá ajustar as velocidades de reprodução de acordo com o ritmo de combate.

---

# 11. REGRAS OBRIGATÓRIAS DE FLUIDEZ

- Produzir sprites próprios nas oito direções.
- Preservar a anatomia humanoide robusta do Orc.
- Manter dentes, orelhas, cicatrizes e características faciais consistentes.
- Não alterar involuntariamente a proporção de cabeça, braços, pernas ou torso.
- Manter machado e escudo sempre nas mãos anatômicas corretas.
- Preservar os detalhes assimétricos da armadura.
- Garantir continuidade dos movimentos da arma e do escudo.
- Animar roupas, acessórios e cabelo com movimentos secundários naturais.
- Manter contato correto dos pés com o chão.
- Evitar deslizamento durante a caminhada.
- Preservar ponto de ancoragem estável.
- Respeitar a perspectiva isométrica em todos os frames.
- Utilizar antecipação, aceleração, impacto e recuperação nos ataques.
- Manter sensação de peso sem comprometer a velocidade do personagem.
- Garantir transições suaves entre Idle, Walk, Attack, Hurt, Block e Skills.
- Idle, Walk, Buff Hold e Block Hold devem possuir loops perfeitos.
- Attack e Skills devem iniciar e terminar em poses compatíveis com a postura de combate.
- Hurt deve permitir interrupção das ações quando a mecânica permitir.
- Died deve terminar em um cadáver estável.
- Evitar tremores, deformações, mudanças repentinas de escala e teleportes involuntários.
- Não permitir que armas ou membros atravessem incorretamente o corpo.
- Manter iluminação, paleta e contornos consistentes.
- Não utilizar interpolação borrada.
- Usar fundo transparente verdadeiro.
- Não permitir bordas, halos, pixels soltos ou vazamentos entre células.
- Reservar espaço suficiente para o arco completo do machado.
- Manter dimensões uniformes e recortes consistentes.
- Produzir VFX independentes e sincronizados com os eventos de gameplay.
- Garantir leitura visual clara mesmo com múltiplos inimigos na tela.
- Validar todas as direções individualmente.

---

# 12. ORGANIZAÇÃO DOS ARQUIVOS

Entregar arquivos independentes:

- `orc_idle.png`
- `orc_walk.png`
- `orc_attack.png`
- `orc_hurt.png`
- `orc_died.png`
- `orc_skill_crushing_blow.png`
- `orc_skill_charge.png`
- `orc_skill_war_cry.png`
- `orc_buff_hold.png`
- `orc_block.png`
- `orc_block_hold.png`
- `orc_vfx_axe_slash.png`
- `orc_vfx_hit.png`
- `orc_vfx_crushing_blow.png`
- `orc_vfx_charge.png`
- `orc_vfx_shield.png`
- `orc_vfx_war_cry.png`
- `orc_vfx_death.png`
- `orc_animations.json`

Cada spritesheet corporal deve utilizar **8 linhas direcionais**, nesta ordem:

N, NE, E, SE, S, SW, W, NW.

Os frames de cada direção devem estar organizados horizontalmente, em sequência cronológica.

### O arquivo JSON deve conter:

- Identificador do inimigo.
- Nomes das animações.
- Direções e quantidade de frames.
- Coordenadas de recorte.
- Dimensões de cada célula.
- FPS de reprodução.
- Configurações de loop.
- Ponto de ancoragem dos pés.
- Hitbox e hurtbox.
- Alcance dos ataques.
- Coordenadas do machado e escudo por direção.
- Eventos de início e término dos ataques.
- Frames de aplicação de dano.
- Eventos de ativação e impacto das Skills.
- Eventos de ativação e encerramento do Grito de Guerra.
- Eventos de bloqueio.
- Referências aos VFX.
- Regras de interrupção por Hurt.
- Estados e transições de animação.
- Estado final de morte.

---

# 13. VALIDAÇÃO OBRIGATÓRIA

Antes de considerar o conjunto concluído:

1. Reproduzir Idle e Walk por cinco ciclos completos em cada direção.
2. Confirmar consistência anatômica, facial e dos equipamentos.
3. Validar contato correto dos pés com o chão.
4. Testar Idle → Attack → Idle e Walk → Attack → Walk.
5. Verificar o arco completo do machado durante os ataques.
6. Testar Golpe Esmagador e sincronização do impacto.
7. Testar Investida Brutal com deslocamento controlado pela engine.
8. Validar transição entre preparação, corrida, impacto e recuperação.
9. Testar Grito de Guerra e ativação da aura.
10. Confirmar que a aura funciona sobre outras animações.
11. Testar Block e Block Hold.
12. Validar interrupções por Hurt.
13. Reproduzir a morte completa nas oito direções.
14. Confirmar a estabilidade do cadáver final.
15. Inspecionar os recortes, bordas e transparências.
16. Corrigir tremores, deformações e mudanças involuntárias de escala.
17. Testar mudanças de direção durante a caminhada.
18. Validar a escala real do Orc no jogo.
19. Testar a leitura visual em combates com múltiplos inimigos.
20. Confirmar que todos os VFX são independentes e sincronizados.

---

# 14. RESULTADO ESPERADO

Entregar um conjunto completo de spritesheets para um **Orc Guerreiro em Pixel Art Chibi**, contendo:

- **Idle:** 128 frames.
- **Walk:** 128 frames.
- **Attack — Corte Selvagem:** 128 frames.
- **Hurt:** 80 frames.
- **Died — Queda do Guerreiro:** 192 frames.
- **Skill 01 — Golpe Esmagador:** 160 frames.
- **Skill 02 — Investida Brutal:** 176 frames.
- **Skill 03 — Grito de Guerra:** 192 frames.
- **Buff Hold:** 96 frames.
- **Block:** 96 frames.
- **Block Hold:** 64 frames.
- **VFX próprios:** cortes, impactos, investida, escudo, grito de guerra, aura e morte.
- **Metadados completos:** JSON com recortes, direções, animações, âncoras e eventos de combate.

**TOTAL: 1.440 frames corporais distribuídos em oito direções, além dos efeitos visuais independentes.**

O Orc deve funcionar como um inimigo guerreiro completo, com combate agressivo, ataques físicos variados, defesa com escudo, investidas e habilidades de fortalecimento.

Sua movimentação deve transmitir **força, brutalidade, experiência em combate e agressividade constante**, diferenciando-se claramente de Goblins, Esqueletos e Minotauros.

**PRIORIDADE ABSOLUTA:** oito direções completas, fluidez excepcional, consistência anatômica, peso convincente, continuidade entre movimentos, sincronização dos ataques, identidade visual consistente e sprites prontos para integração direta em um MMORPG 2D isométrico.

Não substituir animações completas por poses estáticas, espelhamentos inadequados, frames artificialmente duplicados ou efeitos genéricos. Cada animação deve ser produzida e validada individualmente nas oito direções.