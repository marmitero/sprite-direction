# INIMIGO MINOTAURO — SPRITESHEET COMPLETA EM 8 DIREÇÕES

Crie um conjunto completo de spritesheets para um **Minotauro de RPG 2D isométrico, inspirado em Diablo II, com estética Pixel Art Chibi e fantasia medieval sombria**.

O Minotauro deve ser um inimigo de elite, de porte grande, extremamente forte e resistente, especializado em ataques físicos devastadores, investidas violentas e golpes que atingem múltiplos jogadores.

Sua aparência deve transmitir a sensação de uma criatura brutal, territorial e intimidadora, com corpo musculoso, cabeça bovina, grandes chifres e armamento pesado.

Apesar da estética chibi, o personagem deve parecer poderoso e ameaçador. Sua cabeça proporcionalmente grande deve reforçar a identidade visual sem comprometer sua imponência.

O objetivo é produzir animações extremamente fluidas, expressivas e prontas para gameplay real, com movimentos pesados e convincentes, ataques de grande impacto, habilidades especiais, efeitos visuais próprios e oito direções completas.

---

## 1. IDENTIDADE VISUAL

O Minotauro deve possuir:

- Corpo grande, largo e extremamente musculoso.
- Cabeça bovina proporcionalmente grande, característica da estética chibi.
- Dois chifres grandes, curvados e simétricos.
- Focinho largo com narinas expressivas.
- Olhos avermelhados ou âmbar, transmitindo agressividade.
- Pelagem marrom-escura, com variações em tons de castanho e preto.
- Crina espessa ao redor do pescoço e parte superior das costas.
- Ombros largos e braços musculosos.
- Pernas fortes, terminando em cascos bovinos.
- Cauda longa com tufo de pelos na extremidade.
- Armadura de placas metálicas envelhecidas nos ombros e antebraços.
- Peitoral parcial de couro reforçado.
- Cinto largo com fivelas metálicas e pequenos troféus de batalha.
- Machado de guerra de duas mãos, grande e pesado.
- Pequenas cicatrizes visíveis na pelagem.
- Braceletes e acessórios de inspiração tribal e medieval.

**Arma principal:** machado de guerra de duas mãos, com lâmina larga e metal desgastado.

**Personalidade visual:** criatura feroz, orgulhosa, territorial e brutal, que utiliza sua força física para dominar o campo de batalha.

**Direção de animação:** movimentos pesados, aceleração gradual, golpes explosivos, recuperação com sensação de peso e movimentos secundários de cauda, crina e armadura.

---

## 2. SISTEMA OBRIGATÓRIO DE 8 DIREÇÕES

Produzir todas as animações corporais individualmente nas seguintes orientações:

1. Norte (N) — Costas.
2. Nordeste (NE) — Diagonal superior direita.
3. Leste (E) — Lateral direita.
4. Sudeste (SE) — Diagonal inferior direita.
5. Sul (S) — Frente.
6. Sudoeste (SW) — Diagonal inferior esquerda.
7. Oeste (W) — Lateral esquerda.
8. Noroeste (NW) — Diagonal superior esquerda.

**Regras direcionais obrigatórias:**

- Criar sprites próprios para todas as oito direções.
- Preservar a perspectiva isométrica.
- Manter o machado segurado com ambas as mãos durante as animações de combate, salvo gestos específicos intencionais.
- Respeitar a posição anatômica dos braços, cascos, chifres e cauda.
- Preservar a mesma silhueta e proporções em todas as orientações.
- Não utilizar espelhamento automático quando comprometer acessórios, iluminação ou assimetrias.
- Manter o mesmo ponto de ancoragem no chão, centralizado entre os cascos.
- Garantir que o machado e os chifres nunca sejam cortados pelos limites dos frames.

---

## 3. CONCEITO DE COMBATE

**Tipo:** inimigo de elite corpo a corpo, com alta resistência e dano elevado.

**Função:** pressionar jogadores próximos, executar golpes em área e romper posições defensivas.

**Comportamento:** agressivo, territorial, impulsivo e intimidador.

**Ataque básico:** Corte Brutal — golpe horizontal ou diagonal com machado de duas mãos.

**Skill 01:** Investida dos Chifres — corrida curta e violenta em direção ao jogador.

**Skill 02:** Impacto Sísmico — golpe vertical com machado que provoca uma onda de choque no chão.

**Skill 03:** Fúria Bestial — estado temporário de fortalecimento, aumentando velocidade e agressividade.

**Diferencial:** sensação de grande massa corporal, ataques com antecipação perceptível, movimentos explosivos e forte presença visual no campo de batalha.

**Projéteis:** não utiliza projéteis convencionais. A onda sísmica é um efeito de solo independente que pode se propagar em curta distância.

---

# 4. ANIMAÇÕES OBRIGATÓRIAS

## 01 — IDLE (16 frames × 8 direções = 128 frames)

O Minotauro permanece em postura ameaçadora, segurando seu machado de duas mãos à frente ou ao lado do corpo.

Durante o Idle:

- O peito expande e contrai lentamente, simulando respiração pesada.
- Os ombros sobem e descem discretamente.
- A cabeça realiza pequenos movimentos, observando os arredores.
- As narinas se dilatam ocasionalmente.
- A cauda balança suavemente de um lado para o outro.
- A crina acompanha pequenos movimentos do pescoço.
- Os braços realizam ajustes discretos na empunhadura do machado.
- O peso corporal alterna levemente entre os cascos, sem deslocá-los.
- A armadura acompanha naturalmente a movimentação.
- A expressão permanece agressiva e intimidadora.

O Minotauro deve parecer constantemente preparado para atacar.

**Loop:** perfeitamente contínuo, com retorno natural à pose inicial.

## 02 — WALK (18 frames × 8 direções = 144 frames)

Criar uma caminhada pesada, ameaçadora e convincente.

O Minotauro deve se deslocar como uma criatura de grande massa corporal.

Durante o Walk:

- Os cascos executam passos largos e firmes.
- O corpo apresenta pequenas oscilações verticais, sincronizadas com a passada.
- Os ombros acompanham o movimento com sensação de peso.
- O machado oscila discretamente, mantendo a empunhadura coerente.
- A cabeça realiza pequenas compensações para manter o equilíbrio.
- A cauda funciona como movimento secundário.
- A crina e os acessórios acompanham o deslocamento.
- Cada passo deve possuir levantamento, avanço, contato e impulsão.
- O tronco permanece levemente inclinado para frente.
- A recuperação de cada passada deve demonstrar a massa da criatura.

**Regra fundamental:** os cascos não podem deslizar durante a fase de apoio.

A animação deve transmitir poder e ameaça, sem parecer excessivamente lenta.

**Loop:** contínuo, com transição natural entre as passadas.

## 03 — ATTACK: CORTE BRUTAL (18 frames × 8 direções = 144 frames)

Criar um ataque básico pesado com machado de duas mãos.

**Estrutura:**

- **Frames 1–4 — Antecipação:** o Minotauro gira parcialmente o tronco e leva o machado para trás do ombro.
- **Frames 5–7 — Preparação:** flexiona os joelhos e concentra o peso corporal sobre a perna de apoio.
- **Frames 8–11 — Execução:** realiza um golpe diagonal poderoso em direção ao alvo.
- **Frames 12–14 — Finalização:** o machado completa seu arco, enquanto o tronco acompanha a força do movimento.
- **Frames 15–18 — Recuperação:** retorna gradualmente à postura de combate.

O ataque deve apresentar:

- Sensação de peso elevado.
- Movimento coordenado das duas mãos.
- Rotação convincente do tronco.
- Participação dos ombros e quadris.
- Pequeno movimento secundário da cauda.
- Recuperação relativamente lenta.
- Impacto visual claramente identificável.

**Função visual:** ataque físico principal de alto dano.

**Transição:** Idle/Walk → Attack → Idle/Walk.

## 04 — HURT (10 frames × 8 direções = 80 frames)

Criar uma reação de dano compatível com uma criatura extremamente resistente.

O Minotauro não deve recuar exageradamente diante de ataques comuns.

Durante o Hurt:

- O tronco sofre um pequeno recuo.
- A cabeça inclina rapidamente.
- Os ombros contraem em reação ao impacto.
- O machado oscila discretamente.
- A cauda reage ao movimento.
- O Minotauro demonstra irritação através da expressão facial.
- Os cascos permanecem firmes no chão.
- O corpo recupera rapidamente sua postura.

**Estrutura:**

- Frames 1–2: impacto.
- Frames 3–5: contração e recuo corporal.
- Frames 6–8: recuperação.
- Frames 9–10: retorno à postura de combate.

**Função visual:** feedback de dano.

Para impactos mais fortes, a engine poderá aplicar um pequeno deslocamento de knockback sem modificar a animação-base.

## 05 — DIED: QUEDA DO COLOSSO (28 frames × 8 direções = 224 frames)

Criar uma animação de morte longa e impactante, enfatizando o enorme peso corporal do Minotauro.

**Estrutura:**

- **Frames 1–4 — Impacto fatal:** o Minotauro recebe o golpe final, recua e perde parcialmente o equilíbrio.
- **Frames 5–8 — Resistência:** tenta permanecer de pé, apoiando o machado no chão ou utilizando a própria força para evitar a queda.
- **Frames 9–12 — Falha corporal:** os joelhos começam a ceder e o tronco inclina progressivamente.
- **Frames 13–17 — Queda:** o machado escapa das mãos, enquanto o corpo inicia um colapso pesado.
- **Frames 18–22 — Impacto no solo:** o Minotauro atinge o chão com força, levantando poeira e movimentando a armadura.
- **Frames 23–26 — Estabilização:** o corpo, a cauda e os acessórios concluem seus movimentos residuais.
- **Frames 27–28 — Cadáver final:** o Minotauro permanece completamente imóvel.

O corpo deve cair de maneira coerente com a orientação atual, respeitando a perspectiva isométrica.

O machado deve permanecer próximo ao corpo após a queda.

**Sem loop.** Manter o frame final até a remoção do cadáver.

---

# 5. HABILIDADES ESPECIAIS

## 06 — SKILL 01: INVESTIDA DOS CHIFRES (24 frames × 8 direções = 192 frames)

O Minotauro abaixa a cabeça e realiza uma investida violenta contra o jogador.

**Estrutura:**

- **Frames 1–4 — Preparação:** inclina o tronco, abaixa a cabeça e posiciona os chifres à frente.
- **Frames 5–8 — Acúmulo:** raspa um casco no chão, tensionando os músculos.
- **Frames 9–12 — Impulso:** inicia uma corrida explosiva.
- **Frames 13–17 — Investida:** avança rapidamente com os chifres direcionados ao alvo.
- **Frames 18–20 — Impacto:** realiza um movimento de cabeçada, acompanhado de uma pequena reação dos ombros.
- **Frames 21–24 — Recuperação:** estabiliza o corpo e retorna à postura de combate.

Durante a investida:

- O machado deve permanecer firmemente seguro ou em posição recolhida.
- A cabeça permanece abaixada.
- Os chifres ficam claramente visíveis.
- A cauda acompanha o deslocamento.
- Pequenas partículas de poeira surgem nos cascos.
- O corpo apresenta forte inclinação para frente.

**Função visual:** habilidade de aproximação com alto dano e possibilidade de empurrar o jogador.

**Importante:** o deslocamento real deve ser controlado pela engine. A spritesheet representa o movimento corporal, sem aplicar translação global.

Para distâncias variáveis, permitir repetição dos frames centrais da corrida durante o deslocamento, com transições suaves para o impacto e a recuperação.

## 07 — SKILL 02: IMPACTO SÍSMICO (26 frames × 8 direções = 208 frames)

O Minotauro ergue seu machado acima da cabeça e golpeia violentamente o chão, provocando uma onda de choque.

**Estrutura:**

- **Frames 1–4 — Preparação:** firma os cascos no chão e ajusta a empunhadura.
- **Frames 5–9 — Elevação:** ergue o machado acima da cabeça utilizando os dois braços.
- **Frames 10–13 — Acúmulo:** tensiona os músculos e mantém a arma erguida.
- **Frames 14–17 — Golpe:** desce o machado com força extrema.
- **Frames 18–20 — Impacto:** a lâmina atinge o chão, desencadeando uma onda sísmica.
- **Frames 21–24 — Recuperação:** retira o machado do chão e endireita o corpo.
- **Frames 25–26 — Retorno:** assume novamente a postura de combate.

O golpe deve transmitir força extrema.

**Função visual:** ataque em área com dano físico e possibilidade de atordoamento.

A onda sísmica deve ser um VFX independente, sincronizado com o impacto no frame 18.

## 08 — SKILL 03: FÚRIA BESTIAL (24 frames × 8 direções = 192 frames)

O Minotauro entra em um estado temporário de agressividade extrema.

**Estrutura:**

- **Frames 1–4 — Irritação:** contrai os ombros, abaixa a cabeça e aperta o machado.
- **Frames 5–8 — Preparação:** expande o peito e abre a boca, preparando um rugido.
- **Frames 9–13 — Rugido:** ergue a cabeça e solta um rugido poderoso.
- **Frames 14–17 — Ativação:** os olhos brilham intensamente e uma aura avermelhada surge ao redor do corpo.
- **Frames 18–21 — Intensificação:** a aura pulsa enquanto o Minotauro assume uma postura agressiva.
- **Frames 22–24 — Estabilização:** retorna à posição de combate, mantendo os sinais visuais de fúria.

**Função visual:** fortalecimento temporário de velocidade de ataque, agressividade e dano.

### FURY HOLD — 12 frames × 8 direções = 96 frames

Criar uma animação complementar para o estado de fúria ativo.

Durante o Fury Hold:

- Os olhos permanecem avermelhados.
- A respiração torna-se mais intensa.
- Os ombros apresentam movimentos mais agressivos.
- Pequenas partículas avermelhadas surgem discretamente.
- A cauda se movimenta com maior intensidade.
- O corpo demonstra tensão muscular constante.

**Loop:** perfeitamente contínuo.

A engine deve poder aplicar a aura de fúria sobre as demais animações, permitindo que o Minotauro caminhe, ataque e utilize habilidades enquanto o fortalecimento estiver ativo.

O Fury Hold funciona como animação de sustentação visual, mas não deve substituir as demais animações de gameplay durante o combate.

---

# 6. PROJÉTEIS E EFEITOS DE SOLO

O Minotauro não utiliza projéteis tradicionais.

Entretanto, a habilidade Impacto Sísmico exige um efeito de onda de choque independente.

## ONDA SÍSMICA — SHOCKWAVE

Criar uma spritesheet de onda de choque terrestre.

**Animação:** 12 frames.

Características:

- Energia cinética propagando-se pelo solo.
- Pequenos fragmentos de pedra.
- Poeira e rachaduras temporárias.
- Expansão visual progressiva.
- Perspectiva isométrica coerente.
- Desaparecimento gradual.

A onda deve ter sua área e duração controladas pela engine, permitindo colisão independente do personagem.

Caso a habilidade utilize propagação direcional, criar as oito variantes correspondentes.

---

# 7. VFX OBRIGATÓRIOS

Produzir spritesheets independentes para os efeitos visuais.

### VFX 01 — HEAVY AXE SLASH (10 frames)

Arco de corte pesado produzido pelo machado.

- Rastro metálico largo.
- Movimento rápido e agressivo.
- Pequenas partículas de impacto.
- Dissipação curta.

### VFX 02 — HEAVY HIT IMPACT (8 frames)

Impacto físico de grande intensidade.

- Faíscas.
- Poeira.
- Pequenos fragmentos.
- Expansão rápida.

### VFX 03 — CHARGE DUST (10 frames)

Poeira levantada durante a Investida dos Chifres.

- Pequenas nuvens junto aos cascos.
- Partículas seguindo o deslocamento.
- Dissipação gradual.

### VFX 04 — HORN IMPACT (8 frames)

Impacto produzido pela cabeçada.

- Explosão curta de força.
- Poeira e partículas.
- Pequena onda de impacto.

### VFX 05 — SEISMIC CHARGE (10 frames)

Efeito de preparação do Impacto Sísmico.

- Pequenas vibrações visuais no solo.
- Poeira próxima aos cascos.
- Energia cinética concentrada.

### VFX 06 — SEISMIC EXPLOSION (16 frames)

Explosão de impacto ao atingir o chão com o machado.

- Rachaduras no terreno.
- Fragmentos de rocha.
- Nuvem de poeira.
- Expansão circular em perspectiva isométrica.

### VFX 07 — FURY ACTIVATION (14 frames)

Ativação da Fúria Bestial.

- Aura avermelhada.
- Pequenas partículas energéticas.
- Pulso de energia ao redor do corpo.
- Brilho intenso momentâneo nos olhos.

### VFX 08 — FURY AURA (12 frames em loop)

Aura contínua utilizada durante o fortalecimento.

Deve funcionar como camada independente sobre Idle, Walk, Attack e Skills.

### VFX 09 — DEATH IMPACT (12 frames)

Poeira e fragmentos levantados durante a queda final.

### VFX 10 — GROUND DUST (6 frames)

Pequenas partículas produzidas pelas passadas pesadas.

Os efeitos devem manter a mesma linguagem visual do jogo e não ocultar excessivamente o Minotauro.

---

# 8. ESPECIFICAÇÕES TÉCNICAS

| Animação | Frames/direção | Direções | Total |
|---|---:|---:|---:|
| Idle | 16 | 8 | 128 |
| Walk | 18 | 8 | 144 |
| Attack — Corte Brutal | 18 | 8 | 144 |
| Hurt | 10 | 8 | 80 |
| Died — Queda do Colosso | 28 | 8 | 224 |
| Skill 01 — Investida | 24 | 8 | 192 |
| Skill 02 — Impacto Sísmico | 26 | 8 | 208 |
| Skill 03 — Fúria Bestial | 24 | 8 | 192 |
| Fury Hold | 12 | 8 | 96 |
| **TOTAL** | | | **1.408 frames** |

Os projéteis de solo e VFX devem ser produzidos separadamente.

**Total corporal: 1.408 frames em oito direções.**

---

# 9. FPS RECOMENDADOS

- **Idle:** 10–12 FPS.
- **Walk:** 12–16 FPS.
- **Attack:** 16–20 FPS.
- **Hurt:** 16–20 FPS.
- **Died:** 12–16 FPS.
- **Investida:** 18–24 FPS.
- **Impacto Sísmico:** 16–20 FPS.
- **Fúria Bestial:** 16–20 FPS.
- **Fury Hold:** 10–12 FPS.
- **VFX:** 18–24 FPS.

A engine poderá ajustar o playback conforme a velocidade de combate.

---

# 10. REGRAS OBRIGATÓRIAS DE FLUIDEZ

- Produzir sprites próprios para todas as oito direções.
- Preservar a anatomia bovina e humanoide do Minotauro.
- Manter os dois chifres com formato, comprimento e curvatura consistentes.
- Preservar a estrutura muscular e proporções chibi.
- Manter o machado com as mesmas dimensões em todos os frames.
- Garantir empunhadura coerente com ambas as mãos.
- Evitar mudanças repentinas na posição da arma.
- Animar cauda, crina e acessórios com movimentos secundários naturais.
- Preservar a perspectiva isométrica.
- Manter os cascos corretamente apoiados no chão.
- Evitar deslizamento dos pés durante a caminhada.
- Utilizar movimentos com antecipação, aceleração, impacto e recuperação.
- Garantir sensação convincente de peso corporal.
- Manter o ponto de ancoragem consistente no chão.
- Evitar tremores, deformações, teleportes involuntários e alterações de escala.
- Garantir transições suaves entre Idle, Walk, Attack, Hurt e Skills.
- Idle, Walk e Fury Hold devem possuir loops perfeitamente contínuos.
- Attack e Skills devem começar e terminar em poses compatíveis com a postura de combate.
- Hurt deve permitir retorno natural ao Idle ou Walk.
- Died deve terminar em cadáver estático.
- Nenhuma parte do corpo, chifre ou machado pode atravessar elementos incorretamente.
- Manter iluminação, paleta e contornos consistentes.
- Não utilizar interpolação borrada que prejudique a pixel art.
- Usar fundo transparente verdadeiro.
- Não permitir bordas, halos, pixels soltos ou vazamentos entre células.
- Reservar espaço suficiente para machado erguido, chifres e golpes amplos.
- Manter dimensões uniformes e coordenadas de recorte consistentes.
- Separar efeitos visuais do personagem.
- Garantir sincronização dos VFX com os frames de ataque.
- Manter boa leitura visual em tamanho reduzido.
- Validar todas as direções individualmente.

---

# 11. ORGANIZAÇÃO DOS ARQUIVOS

Entregar arquivos independentes:

- `minotaur_idle.png`
- `minotaur_walk.png`
- `minotaur_attack.png`
- `minotaur_hurt.png`
- `minotaur_died.png`
- `minotaur_skill_charge.png`
- `minotaur_skill_seismic.png`
- `minotaur_skill_fury.png`
- `minotaur_fury_hold.png`
- `minotaur_vfx_axe_slash.png`
- `minotaur_vfx_heavy_impact.png`
- `minotaur_vfx_charge.png`
- `minotaur_vfx_seismic.png`
- `minotaur_vfx_fury.png`
- `minotaur_vfx_death.png`
- `minotaur_animations.json`

Cada spritesheet corporal deve utilizar **8 linhas direcionais**, na seguinte ordem:

N, NE, E, SE, S, SW, W, NW.

Os frames devem estar organizados horizontalmente em sequência cronológica.

### O arquivo JSON deve conter:

- Identificador do inimigo.
- Nomes das animações.
- Direções e quantidade de frames.
- Coordenadas de recorte.
- Dimensões de cada célula.
- FPS de reprodução.
- Configurações de loop.
- Ponto de ancoragem dos cascos.
- Hitbox e hurtbox.
- Alcance dos ataques.
- Coordenadas do machado e dos chifres por direção.
- Eventos de início e término dos ataques.
- Frames de aplicação de dano.
- Eventos de início, deslocamento e impacto da investida.
- Eventos de ativação da onda sísmica.
- Eventos de ativação e encerramento da Fúria Bestial.
- Referências aos VFX.
- Regras de interrupção por Hurt.
- Estados e transições das animações.
- Estado final de morte.

---

# 12. VALIDAÇÃO OBRIGATÓRIA

Antes de considerar o conjunto concluído:

1. Reproduzir Idle e Walk por cinco ciclos completos em cada direção.
2. Confirmar consistência dos chifres, músculos, machado e armadura.
3. Validar contato correto dos cascos com o chão.
4. Testar Idle → Attack → Idle e Walk → Attack → Walk.
5. Verificar o arco completo do machado durante o ataque.
6. Testar a Investida dos Chifres e sua sincronização com o deslocamento da engine.
7. Verificar a transição entre preparação, corrida, impacto e recuperação.
8. Testar o Impacto Sísmico e a onda de choque independente.
9. Validar a ativação da Fúria Bestial.
10. Confirmar que a aura de fúria funciona sobre outras animações.
11. Testar interrupções por Hurt e retorno à postura de combate.
12. Reproduzir a morte completa em todas as oito direções.
13. Verificar a estabilidade do cadáver final.
14. Inspecionar os recortes e transparências.
15. Corrigir tremores, deformações, mudanças de escala e saltos visuais.
16. Testar mudanças de direção durante o movimento.
17. Validar o tamanho do Minotauro na escala real do jogo.
18. Testar as animações em combates com múltiplos inimigos simultâneos.

---

# 13. RESULTADO ESPERADO

Entregar um conjunto completo de spritesheets para um **Minotauro em Pixel Art Chibi**, contendo:

- **Idle:** 128 frames.
- **Walk:** 144 frames.
- **Attack — Corte Brutal:** 144 frames.
- **Hurt:** 80 frames.
- **Died — Queda do Colosso:** 224 frames.
- **Skill 01 — Investida dos Chifres:** 192 frames.
- **Skill 02 — Impacto Sísmico:** 208 frames.
- **Skill 03 — Fúria Bestial:** 192 frames.
- **Fury Hold:** 96 frames.
- **Onda Sísmica:** efeito independente.
- **VFX próprios:** cortes, impactos, poeira, investida, explosão sísmica, fúria e morte.
- **Metadados completos:** JSON com animações, direções, recortes, âncoras, eventos e sincronização.

**TOTAL: 1.408 frames corporais distribuídos em oito direções, além dos efeitos visuais independentes.**

O Minotauro deve funcionar como um inimigo de elite completo, capaz de executar golpes físicos devastadores, investir contra jogadores, provocar ondas sísmicas e entrar em estado de fúria.

Seu comportamento visual deve transmitir força, peso, brutalidade e ameaça constante.

**PRIORIDADE ABSOLUTA:** oito direções completas, fluidez excepcional, consistência anatômica, peso convincente, continuidade entre movimentos, sincronização dos ataques e sprites prontos para integração direta em um MMORPG 2D isométrico.

Não substituir animações completas por poses estáticas, espelhamentos inadequados, frames artificialmente duplicados ou efeitos genéricos. Cada animação deve ser produzida e validada individualmente nas oito direções.