# INIMIGO MINI-DRAGÃO VERMELHO — PADRÃO DEFINITIVO DE SPRITESHEET 8 DIREÇÕES

Crie uma spritesheet completa para um **Mini-Dragão Vermelho** de RPG 2D isométrico, inspirado em Diablo II, com estética **Pixel Art Chibi** e fantasia medieval sombria.

O Mini-Dragão Vermelho deve ser um inimigo de porte pequeno para médio, compacto, veloz e perigoso, com aparência dracônica bem legível mesmo em escala reduzida. Ele deve transmitir a sensação de uma criatura agressiva, territorial e instável, capaz de atacar com garras, mordida e pequenas rajadas de fogo.

Seu visual deve incluir:

- corpo dracônico compacto
- cabeça grande e expressiva
- chifres curtos ou crista óssea
- asas pequenas, porém funcionais visualmente
- cauda ativa e articulada
- escamas vermelhas com variações em tons quentes
- ventre em cor secundária, como bege, laranja ou vermelho mais claro
- garras e dentes visíveis
- olhos intensos e hostis
- possível fumaça sutil nas narinas em estados agressivos

O objetivo é produzir animações fluidas, expressivas e prontas para gameplay, preservando legibilidade em combate e forte identidade visual.

---

## 1. SISTEMA DE 8 DIREÇÕES

Todas as animações do personagem devem ser produzidas individualmente nas seguintes direções:

1. Norte (N)
2. Nordeste (NE)
3. Leste (E)
4. Sudeste (SE)
5. Sul (S)
6. Sudoeste (SW)
7. Oeste (W)
8. Noroeste (NW)

**Obrigatório:** criar sprites próprios para as oito direções, respeitando anatomia, profundidade isométrica, posição das asas, cauda, cabeça, patas e boca. Não depender apenas de espelhamento quando isso comprometer leitura, iluminação ou sobreposição de partes do corpo.

---

## 2. CONCEITO DE COMBATE

**Tipo:** inimigo agressivo híbrido, com ataque corpo a corpo e ataque de fogo à distância curta ou média  
**Função:** pressão ofensiva, perseguição e controle de espaço com fogo  
**Comportamento:** inquieto, territorial, feroz e impulsivo  
**Ataque básico:** mordida ou golpe de garras  
**Ataque secundário:** sopro de fogo / bola de fogo curta  
**Leitura visual:** inimigo mais perigoso que monstros iniciais comuns, com mobilidade e ameaça elemental

---

## 3. ANIMAÇÕES OBRIGATÓRIAS

## 01 — IDLE (12 frames × 8 direções = 96 frames)

O Mini-Dragão Vermelho deve parecer vivo, tenso e ameaçador mesmo parado.

Durante o idle:

- respiração visível no peito e tronco
- pequeno movimento da cabeça, como se farejasse ou vigiasse
- asas com microajustes sutis, sem abrir completamente
- cauda balançando levemente com ritmo orgânico
- pequenas contrações nos ombros e patas
- narinas podendo emitir fumaça sutil ocasional
- olhos atentos e expressão agressiva

A pose deve transmitir prontidão para atacar.  
O loop precisa ser contínuo e natural.

**Função visual:** estado de espera / combate.

---

## 02 — WALK (12 frames × 8 direções = 96 frames)

Criar uma locomoção dracônica ágil e animal, com sensação de criatura leve, predatória e inquieta.

Durante o walk:

- ciclo completo de passada em quatro patas
- deslocamento corporal coordenado entre frente e traseira
- cabeça acompanhando o movimento com leve oscilação
- asas recolhidas, mas reagindo com pequenos balanços secundários
- cauda usada como contrapeso, com movimento fluido
- contato correto dos pés com o chão, sem deslizamento
- sensação de avanço rápido e confiante

O Mini-Dragão não deve andar como um cão comum nem como um lagarto duro demais.  
O movimento deve parecer dracônico, compacto e ágil.

**Função visual:** perseguição, patrulha e reposicionamento.

---

## 03 — ATTACK (14 frames × 8 direções = 112 frames)

Ataque básico corpo a corpo.

O ataque principal pode combinar **mordida agressiva** ou **golpe de garras**, desde que a leitura seja muito clara. Preferencialmente, usar uma mordida frontal/lateral como ataque base.

Estrutura recomendada:

- Frames 1–3: antecipação, recuando cabeça e parte dianteira do corpo
- Frames 4–7: avanço rápido com mordida ou ataque de garra
- Frames 8–10: impacto / extensão máxima do golpe
- Frames 11–14: recuperação e retorno à postura de combate

Elementos obrigatórios:

- pescoço e cabeça com arco de movimento convincente
- boca abrindo de forma expressiva
- patas dianteiras ajudando na impulsão
- asas e cauda reagindo ao movimento
- sensação de velocidade e ferocidade

**Função visual:** ataque básico principal.

---

## 04 — HURT (8 frames × 8 direções = 64 frames)

Reação ao receber dano.

O Mini-Dragão deve reagir de maneira clara e expressiva:

- recuo do tronco
- cabeça indo para trás ou para o lado
- boca abrindo em reação de dor ou irritação
- asas contraindo momentaneamente
- cauda se retraindo com tensão
- leve desequilíbrio e recuperação

A animação deve ser curta e eficaz, sem comprometer o ritmo de combate.

**Função visual:** feedback de dano recebido.

---

## 05 — DIED (18 frames × 8 direções = 144 frames)

Morte completa com colapso corporal.

Estrutura recomendada:

- Frames 1–4: impacto fatal e perda de força
- Frames 5–8: quebra de sustentação das patas
- Frames 9–12: queda do corpo e acomodação da cabeça, asas e cauda
- Frames 13–16: corpo terminando de colapsar no chão
- Frames 17–18: frame final estabilizado de cadáver

A morte deve:

- parecer dracônica e pesada, mesmo com proporções chibi
- manter leitura clara da silhueta caída
- terminar em uma pose final usável
- incluir acomodação orgânica de asas e cauda

**Sem loop.**  
O último frame permanece visível até remoção do inimigo.

---

## 06 — SKILL 01: SOPRO DE FOGO (16 frames × 8 direções = 128 frames)

Skill principal elemental.

O Mini-Dragão recua a cabeça, expande o peito e libera uma rajada curta de fogo em linha ou cone curto.

Estrutura recomendada:

- Frames 1–4: preparação, inflando o peito e abrindo a boca
- Frames 5–7: acúmulo de energia ígnea na garganta ou boca
- Frames 8–11: emissão do sopro de fogo
- Frames 12–14: redução da chama e exaustão curta
- Frames 15–16: retorno à postura de combate

Elementos importantes:

- luz quente refletindo sutilmente na boca / focinho
- pescoço estendido durante a emissão
- asas e cauda reagindo à força do ataque
- boca bem aberta para leitura clara
- possível fumaça residual ao final

**Função visual:** habilidade de fogo em linha curta ou cone frontal.

---

## 07 — SKILL 02: SALTO DRACÔNICO (opcional, 14 frames × 8 direções = 112 frames)

Se desejar uma segunda habilidade, o Mini-Dragão pode realizar um salto curto e agressivo.

Estrutura recomendada:

- Frames 1–3: agachamento e compressão corporal
- Frames 4–6: impulso
- Frames 7–9: fase aérea curta, com asas abrindo parcialmente
- Frames 10–12: aterrissagem
- Frames 13–14: recuperação

Essa skill pode ser usada como investida curta ou reposicionamento ofensivo.

**Função visual:** aproximação explosiva / variação de combate.  
**Opcional:** incluir apenas se o design de gameplay utilizar duas skills.

---

## 4. PROJÉTIL

## PROJÉTIL — BOLA DE FOGO MENOR (8 frames de loop + 4 frames de impacto)

Como o Mini-Dragão Vermelho utiliza fogo, criar projétil próprio.

### Bola de fogo em voo
- 8 frames de loop
- esfera de fogo pequena ou média
- núcleo brilhante
- bordas instáveis
- pequena cauda de chama
- deve funcionar em qualquer direção pela engine, mas pode ter variantes direcionais se necessário

### Impacto da bola de fogo
- 4 a 6 frames
- pequena explosão ígnea
- dispersão curta de chamas
- desaparecer rapidamente

**Função visual:** projétil de skill ou ataque especial à distância.

---

## 5. VFX OBRIGATÓRIOS

Criar os VFX separados do personagem, com a mesma linguagem visual do jogo.

### A. Hit Slash / Impacto físico (5–6 frames)
Para mordida ou golpe de garras.  
Pequeno efeito de corte / impacto físico.

### B. Fire Charge (6 frames)
Acúmulo de energia ígnea na boca antes do sopro.

### C. Fire Breath (8–10 frames)
Trecho visual do sopro de fogo, podendo ser modular para extensão pela engine.

### D. Fireball Cast Burst (5–6 frames)
Explosão pequena na saída da bola de fogo.

### E. Fireball Impact (4–6 frames)
Impacto do projétil no alvo ou no cenário.

### F. Step Dust / Ground Contact (4 frames, opcional)
Pequena poeira para reforçar passada ou aterrissagem.

### G. Death Dust / Ember Fade (6 frames, opcional)
Pequena dissipação de poeira e brasas ao morrer.

**Importante:** os VFX devem ser utilizáveis separadamente, sem depender do corpo do personagem.

---

## 6. ESPECIFICAÇÕES TÉCNICAS

| Animação | Frames/direção | Direções | Total |
|---|---:|---:|---:|
| Idle | 12 | 8 | 96 |
| Walk | 12 | 8 | 96 |
| Attack | 14 | 8 | 112 |
| Hurt | 8 | 8 | 64 |
| Died | 18 | 8 | 144 |
| Skill 01 — Sopro de Fogo | 16 | 8 | 128 |
| **Total personagem** |  |  | **640** |

### Opcional
| Animação opcional | Frames/direção | Direções | Total |
|---|---:|---:|---:|
| Skill 02 — Salto Dracônico | 14 | 8 | 112 |

### Projéteis e VFX separados
- Bola de fogo: 8 frames
- Impacto da bola de fogo: 4–6 frames
- Fire Charge: 6 frames
- Fire Breath: 8–10 frames
- Hit Slash / Impacto físico: 5–6 frames
- Poeira / brasas / impacto extra conforme necessidade

---

## 7. FPS RECOMENDADOS

- **Idle:** 10–12 FPS
- **Walk:** 12–16 FPS
- **Attack:** 16–20 FPS
- **Hurt:** 16–20 FPS
- **Died:** 12–16 FPS
- **Skill Sopro de Fogo:** 16–20 FPS
- **Skill opcional de salto:** 16–20 FPS
- **Projéteis e VFX:** 16–20 FPS

A engine poderá ajustar playback speed sem alterar os sprites base.

---

## 8. REGRAS OBRIGATÓRIAS DE CONSISTÊNCIA

- manter **Pixel Art Chibi** consistente em todos os frames
- preservar proporções, cores, anatomia e silhueta do Mini-Dragão
- manter escala estável nas 8 direções
- manter ponto de ancoragem consistente no chão
- evitar tremidos, desalinhamentos e oscilações involuntárias
- respeitar volume corporal, sobreposição de patas, asas, pescoço e cauda
- não deformar cabeça, mandíbula, asas ou tronco entre frames
- garantir boa leitura visual da criatura em tamanho reduzido
- usar fundo transparente verdadeiro
- não gerar bordas, halos, pixels soltos ou vazamento entre células
- organizar os frames em ordem cronológica e separação clara por direção
- garantir transições naturais entre Idle, Walk, Attack, Hurt e Skill
- validar contato correto das patas com o chão
- garantir que asas e cauda tenham animação secundária coerente
- garantir que os efeitos de fogo mantenham a mesma identidade visual do inimigo
- morte deve terminar em um frame final limpo e utilizável
- projéteis e VFX devem ser independentes do personagem
- se houver iluminação do fogo, ela deve ser sutil e coerente, sem descaracterizar a pixel art

---

## 9. ORGANIZAÇÃO DOS ARQUIVOS

Separar em arquivos independentes para facilitar implementação:

- `mini_red_dragon_idle.png`
- `mini_red_dragon_walk.png`
- `mini_red_dragon_attack.png`
- `mini_red_dragon_hurt.png`
- `mini_red_dragon_died.png`
- `mini_red_dragon_skill_fire_breath.png`
- `mini_red_dragon_skill_leap.png` *(opcional)*
- `mini_red_dragon_projectile_fireball.png`
- `mini_red_dragon_vfx.png`
- `mini_red_dragon_animations.json`

Cada spritesheet principal deve usar **8 linhas direcionais**, na ordem:

**N, NE, E, SE, S, SW, W, NW**

com os frames de cada direção organizados horizontalmente.

O arquivo JSON deve conter:

- nomes das animações
- quantidade de frames
- FPS sugerido
- pontos de ancoragem
- área de hit / hurtbox sugerida
- eventos de impacto
- eventos de spawn de projétil
- eventos de início/fim de VFX

---

## 10. RESULTADO ESPERADO

Entregar um conjunto completo de spritesheets de um **Mini-Dragão Vermelho**, pronto para uso em um RPG 2D isométrico com estética Chibi, contendo:

- **Idle**
- **Walk**
- **Attack**
- **Hurt**
- **Died**
- **Skill de Sopro de Fogo**
- **Skill opcional de Salto**
- **Projétil de Bola de Fogo**
- **VFX de fogo e impacto**

O resultado deve transmitir uma criatura dracônica pequena, feroz, rápida e elemental, com animações fluidas, boa leitura visual e excelente integração com gameplay real.