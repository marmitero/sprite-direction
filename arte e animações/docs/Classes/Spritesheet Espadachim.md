# CLASSE JOGÁVEL — ESPADACHIM
## SPRITESHEETS MODULARES COMPLETAS EM 8 DIREÇÕES

**Gênero:** MMORPG 2D isométrico  
**Referência de gameplay:** Diablo II  
**Direção artística:** Pixel Art Chibi de fantasia medieval sombria  
**Tipo:** Personagem jogável  
**Arquitetura:** Sprites modulares com equipamentos visíveis  
**Direções:** 8  
**Especialização:** Combate corpo a corpo, combos, defesa, mobilidade e habilidades de espada

---

# 1. OBJETIVO PRINCIPAL

Criar um conjunto completo e profissional de spritesheets para a classe jogável **Espadachim**, com animações extremamente fluidas, combate responsivo, combos encadeados, habilidades exclusivas, efeitos visuais próprios e sistema de equipamentos visuais modulares.

O personagem deve possuir uma aparência-base simples, utilizando apenas roupas íntimas medievais discretas, permitindo que sua aparência evolua completamente conforme os equipamentos utilizados pelo jogador.

**REGRA FUNDAMENTAL:**

O personagem não deve possuir armadura, espada, escudo, capacete, botas ou qualquer outro equipamento fixo incorporado ao sprite corporal.

Todos os equipamentos devem ser elementos visuais independentes que acompanham perfeitamente as animações.

Ao equipar uma armadura, ela deve aparecer no corpo. Ao trocar a espada, o modelo exibido na mão deve mudar. Ao remover qualquer equipamento, o corpo-base e suas roupas íntimas devem continuar visíveis.

A arquitetura precisa permitir centenas de combinações de equipamentos sem exigir a criação de uma spritesheet corporal completa para cada combinação.

---

# 2. DIREÇÃO DE ARTE DO ESPADACHIM

## 2.1 Aparência corporal básica

Criar um personagem humanoide com proporções chibi, preservando a anatomia necessária para animações complexas de combate.

Características:

- Cabeça proporcionalmente grande.
- Corpo compacto e atlético.
- Ombros moderadamente largos.
- Braços e pernas curtos, mas claramente articulados.
- Mãos suficientemente legíveis para segurar armas.
- Pés definidos para sustentar contato com o chão.
- Rosto expressivo.
- Cabelo curto ou médio, com aparência medieval.
- Expressão confiante, determinada e heroica.
- Musculatura estilizada, sem exageros.
- Silhueta clara mesmo em resolução reduzida.

O personagem deve parecer um aventureiro iniciante, ainda sem equipamentos, mas com postura e movimentos de um combatente treinado.

## 2.2 Roupa-base obrigatória

O Espadachim deve utilizar exclusivamente:

- Roupa íntima inferior medieval simples e opaca.
- Peça íntima superior discreta, conforme a variante corporal.
- Faixa ou acabamento simples de tecido, sem aparência de armadura.
- Pés descalços.
- Braços descobertos.
- Cabeça sem capacete.
- Mãos sem luvas.

**Não incluir na aparência-base:**

- Armaduras.
- Peitorais metálicos.
- Ombreiras.
- Capacetes.
- Botas.
- Luvas.
- Escudos.
- Espadas permanentes.
- Capas.
- Ornamentos mágicos.
- Acessórios de classe fixos.

O personagem deve continuar visualmente completo quando todos os slots de equipamentos estiverem vazios.

## 2.3 Estilo artístico

Utilizar Pixel Art Chibi de fantasia medieval sombria, com:

- Contornos limpos e consistentes.
- Sombras definidas.
- Iluminação coerente com a direção de arte.
- Paleta controlada.
- Volumes bem construídos.
- Silhuetas reconhecíveis.
- Detalhamento suficiente para equipamentos.
- Perspectiva isométrica consistente.
- Animações com movimentos naturais e expressivos.

A aparência deve transmitir qualidade de um RPG comercial, evitando estética de ícones genéricos ou personagens montados com formas geométricas.

---

# 3. SISTEMA OBRIGATÓRIO DE 8 DIREÇÕES

Produzir todas as animações nas seguintes direções:

1. **N — Norte:** costas.
2. **NE — Nordeste:** diagonal superior direita.
3. **E — Leste:** lateral direita.
4. **SE — Sudeste:** diagonal inferior direita.
5. **S — Sul:** frente.
6. **SW — Sudoeste:** diagonal inferior esquerda.
7. **W — Oeste:** lateral esquerda.
8. **NW — Noroeste:** diagonal superior esquerda.

Cada direção deve possuir sprites próprios.

### Regras direcionais

- Preservar proporções corporais.
- Manter anatomia consistente.
- Garantir movimentação correta dos braços e pernas.
- Preservar a posição anatômica das mãos.
- Manter a escala constante.
- Respeitar profundidade e sobreposição.
- Evitar espelhamentos incorretos.
- Garantir transições naturais entre direções.
- Utilizar um sistema único de ancoragem.

As oito direções também devem ser respeitadas por armas, armaduras e demais equipamentos animados.

---

# 4. SISTEMA DE EQUIPAMENTOS MODULARES

O Espadachim deverá ser composto por múltiplas camadas visuais sincronizadas.

## 4.1 Camadas principais

**BODY:** corpo-base com roupas íntimas.

**HAIR:** cabelo e variações visuais.

**HEAD:** capacetes, elmos, capuzes e acessórios de cabeça.

**CHEST:** peitorais, túnicas e armaduras de torso.

**SHOULDERS:** ombreiras e proteções superiores.

**ARMS:** mangas, braçadeiras e proteções dos braços.

**HANDS:** luvas e manoplas.

**LEGS:** calças, saias de armadura e proteções das pernas.

**FEET:** botas, grevas e calçados.

**BACK:** capas, mantos e acessórios traseiros.

**MAIN_HAND:** espada ou arma principal.

**OFF_HAND:** escudo ou equipamento secundário.

**ACCESSORIES:** elementos visuais opcionais, como cintos e amuletos.

**WEAPON_VFX:** efeitos específicos da arma equipada.

## 4.2 Funcionamento visual

Cada equipamento deve possuir sprites compatíveis com as animações corporais.

Exemplo:

Se o jogador equipar uma armadura de ferro:

- O peitoral de ferro aparece sobre o torso.
- As proteções acompanham os movimentos.
- As ombreiras permanecem alinhadas.
- O equipamento mantém a aparência nas oito direções.
- Durante ataques, a armadura acompanha as rotações corporais.
- Durante Hurt, acompanha o recuo.
- Durante Died, acompanha a queda.

Se o jogador substituir a armadura por uma armadura dourada, apenas as camadas de equipamento correspondentes devem ser trocadas.

**O corpo-base e suas animações não devem precisar ser reconstruídos.**

## 4.3 Regras de sobreposição

A ordem de renderização não pode ser fixa para todas as direções.

Dependendo da orientação e da pose:

- A espada pode aparecer à frente ou atrás do torso.
- O escudo pode ocultar parcialmente um braço.
- Uma capa deve aparecer atrás do corpo, mas pode ter partes visíveis lateralmente.
- O cabelo pode ficar parcialmente oculto pelo capacete.
- As ombreiras devem acompanhar a posição dos braços.
- Botas devem seguir exatamente a posição dos pés.

O sistema deve permitir subdivisão de camadas, máscaras de ocultação e ordenação por direção e frame quando necessário.

Equipamentos devem possuir pontos de encaixe e metadados próprios.

---

# 5. CONCEITO DE COMBATE

**Arquétipo:** guerreiro especialista em espadas.

**Função:** dano físico corpo a corpo, combos rápidos, contra-ataques, esquivas e resistência moderada.

**Arma principal sugerida:** espada de uma mão.

**Arma secundária:** escudo opcional.

**Combate:** fluido, responsivo e baseado em encadeamento de golpes.

**Estilo de movimento:** guerreiro técnico, ágil e disciplinado.

**Identidade:** diferente do Orc e do Minotauro, o Espadachim utiliza técnica, precisão, movimentação coordenada e golpes controlados.

O jogador deve conseguir combinar ataques básicos, defesa, esquiva e habilidades especiais sem perceber interrupções artificiais entre as animações.

---

# 6. ANIMAÇÕES DE MOVIMENTAÇÃO

## 01 — IDLE: POSTURA NEUTRA (16 frames × 8 direções = 128 frames)

O personagem permanece parado, sem arma equipada, apresentando respiração e movimentos corporais sutis.

Durante o Idle:

- Respiração natural.
- Pequena expansão do peito.
- Oscilação discreta dos ombros.
- Movimento suave dos braços.
- Pequenos ajustes de postura.
- Movimentos ocasionais da cabeça.
- Cabelo acompanhando discretamente os gestos.
- Peso corporal distribuído naturalmente.

**Loop:** perfeitamente contínuo.

O último frame deve conectar-se ao primeiro sem qualquer salto visual.

## 02 — COMBAT IDLE: POSTURA DE COMBATE (16 × 8 = 128 frames)

O Espadachim assume uma postura ofensiva.

Durante a animação:

- Joelhos levemente flexionados.
- Tronco inclinado discretamente.
- Braço principal posicionado para segurar a espada.
- Braço secundário em posição defensiva.
- Respiração controlada.
- Pequenos movimentos de equilíbrio.
- Olhar concentrado na direção do alvo.

O corpo-base deve apresentar posições de mãos compatíveis com os equipamentos.

**Loop:** perfeitamente contínuo.

## 03 — WALK: CAMINHADA (16 × 8 = 128 frames)

Criar uma caminhada natural e fluida.

- Passos completos e alternados.
- Balanço coordenado dos braços.
- Movimento secundário do cabelo.
- Pequena rotação de tronco.
- Contato correto dos pés com o solo.
- Transferência natural de peso.
- Velocidade visual consistente.

**Loop:** perfeito.

O ciclo deve funcionar tanto sem equipamentos quanto com armaduras completas.

## 04 — RUN: CORRIDA (20 × 8 = 160 frames)

Criar uma corrida dinâmica e responsiva.

- Passos mais longos.
- Tronco inclinado para frente.
- Maior amplitude de braços.
- Movimento expressivo do cabelo.
- Oscilação natural dos ombros.
- Impulso evidente das pernas.
- Recuperação rápida entre passadas.
- Movimento secundário das roupas e equipamentos.

**Loop:** perfeito.

A corrida não deve apresentar deslizamento dos pés ou mudanças involuntárias de escala.

## 05 — DASH / DODGE: ESQUIVA (16 × 8 = 128 frames)

Criar uma esquiva rápida, com deslocamento controlado pela engine.

### Estrutura

- Frames 1–3: preparação.
- Frames 4–7: impulso.
- Frames 8–11: deslocamento evasivo.
- Frames 12–14: aterrissagem e estabilização.
- Frames 15–16: recuperação.

A esquiva deve ser curta, dinâmica e legível.

Pode utilizar um passo lateral rápido ou rolamento curto, desde que o comportamento seja consistente nas oito direções.

**Sem loop.**

## 06 — JUMP: SALTO (18 × 8 = 144 frames)

Criar uma animação de salto com:

- Preparação.
- Impulso.
- Subida.
- Ápice.
- Descida.
- Aterrissagem.
- Recuperação.

Para permitir alturas variáveis, dividir os estados em Jump Start, Airborne Hold e Landing.

O deslocamento vertical deve ser controlado pela engine.

A sombra de contato deve permanecer em uma camada separada, ancorada no chão.

## 07 — TURN: MUDANÇA DE DIREÇÃO (8 frames por transição adjacente)

Criar transições corporais suaves entre direções vizinhas.

O Espadachim deve ajustar:

- Cabeça.
- Ombros.
- Tronco.
- Quadris.
- Posição dos braços.
- Orientação dos equipamentos.

**Objetivo:** reduzir mudanças bruscas de silhueta durante rotações.

Prever 16 transições adjacentes dirigidas para cobrir os dois sentidos de rotação entre oito direções, totalizando até 128 frames de transição.

Mudanças rápidas de direção devem continuar responsivas, sem obrigar o jogador a assistir a todos os frames de Turn.

---

# 7. SISTEMA DE COMBOS BÁSICOS

O Espadachim deve possuir um **combo principal de quatro ataques consecutivos**, com animações distintas e encadeamento natural.

Cada ataque deve possuir antecipação, execução, impacto e recuperação.

Os finais dos ataques devem permitir transição suave para o ataque seguinte ou para Combat Idle.

## 08 — COMBO 01: CORTE HORIZONTAL (16 × 8 = 128 frames)

Primeiro golpe do combo.

### Estrutura

- Frames 1–3: preparação.
- Frames 4–7: corte horizontal rápido.
- Frames 8–10: extensão e contato.
- Frames 11–13: recuperação parcial.
- Frames 14–16: retorno ou preparação para Combo 02.

O movimento deve transmitir velocidade e precisão.

**Evento de dano:** aproximadamente no frame 7, ajustável no JSON.

## 09 — COMBO 02: CORTE DIAGONAL ASCENDENTE (18 × 8 = 144 frames)

Segundo golpe, conectando-se diretamente ao primeiro.

### Estrutura

- Frames 1–3: aproveitamento da postura anterior.
- Frames 4–8: corte ascendente.
- Frames 9–11: extensão máxima.
- Frames 12–15: recuperação parcial.
- Frames 16–18: preparação para Combo 03.

A espada deve percorrer uma trajetória contínua em relação ao golpe anterior.

**Evento de dano:** aproximadamente no frame 9.

## 10 — COMBO 03: CORTE GIRATÓRIO (20 × 8 = 160 frames)

Terceiro golpe, com rotação parcial do corpo.

### Estrutura

- Frames 1–4: preparação do giro.
- Frames 5–9: rotação corporal.
- Frames 10–13: golpe amplo.
- Frames 14–17: conclusão do movimento.
- Frames 18–20: preparação para Combo 04.

O Espadachim deve executar um giro controlado, mantendo equilíbrio e leitura clara da espada.

Não criar rotação artificial da spritesheet inteira. Animar a rotação corporal com poses adequadas.

**Evento de dano:** aproximadamente no frame 11.

## 11 — COMBO 04: GOLPE FINALIZADOR (24 × 8 = 192 frames)

Último golpe do combo básico.

O Espadachim concentra força e executa um corte descendente poderoso.

### Estrutura

- Frames 1–5: antecipação.
- Frames 6–10: elevação da espada.
- Frames 11–15: golpe descendente.
- Frames 16–18: impacto.
- Frames 19–22: recuperação.
- Frames 23–24: retorno à postura de combate.

O ataque deve possuir impacto mais expressivo que os anteriores.

**Evento de dano:** aproximadamente no frame 15.

### Regras do sistema de combos

- Combo 01 → Combo 02 → Combo 03 → Combo 04.
- As transições devem preservar posição corporal e trajetória da espada.
- O sistema deve aceitar entrada antecipada do próximo ataque.
- A engine controla as janelas de combo.
- Não repetir golpes com simples alteração de velocidade.
- Cada combo deve possuir poses e trajetórias próprias.
- Os equipamentos devem acompanhar todos os golpes.
- Se o combo for interrompido, permitir recuperação natural para Combat Idle.
- Sincronizar VFX e hitboxes com cada movimento.
- Criar pontos de cancelamento apropriados para esquiva, bloqueio e habilidades.

**Importante:** os combos são animações individuais que se conectam naturalmente, e não um único vídeo ou uma spritesheet impossível de interromper.

---

# 8. ANIMAÇÕES DEFENSIVAS

## 12 — BLOCK START (10 × 8 = 80 frames)

O Espadachim ergue o escudo ou posiciona a espada defensivamente.

- Identificação da ameaça.
- Ajuste de postura.
- Elevação do equipamento.
- Flexão dos joelhos.
- Preparação para impacto.

**Sem loop.**

## 13 — BLOCK HOLD (12 × 8 = 96 frames)

Manutenção da postura defensiva.

- Respiração controlada.
- Pequenas oscilações.
- Ajustes de equilíbrio.
- Equipamento mantendo proteção frontal.

**Loop:** perfeito.

## 14 — BLOCK IMPACT (10 × 8 = 80 frames)

Reação a um ataque bloqueado.

- Impacto inicial.
- Recuo dos braços.
- Compressão corporal.
- Recuperação defensiva.

O efeito deve variar visualmente conforme espada ou escudo equipado.

## 15 — PARRY: APARO PERFEITO (14 × 8 = 112 frames)

Criar uma animação de defesa técnica, utilizada quando o jogador realiza um bloqueio no momento correto.

- Frames 1–3: preparação rápida.
- Frames 4–7: interceptação do golpe.
- Frames 8–10: desvio da força adversária.
- Frames 11–14: recuperação ou preparação para contra-ataque.

**Função:** defesa precisa, podendo abrir oportunidade ofensiva.

## 16 — COUNTER ATTACK (18 × 8 = 144 frames)

Contra-ataque realizado após Parry.

- Movimento rápido de recuperação.
- Avanço controlado da espada.
- Golpe de precisão.
- Retorno à postura de combate.

O contra-ataque deve conectar-se diretamente à pose final do Parry.

---

# 9. HABILIDADES ESPECIAIS DO ESPADACHIM

## 17 — SKILL 01: CORTE CRESCENTE (24 × 8 = 192 frames)

O Espadachim concentra energia na espada e executa um corte ascendente poderoso.

### Estrutura

- Frames 1–4: preparação.
- Frames 5–9: concentração de energia.
- Frames 10–14: corte ascendente.
- Frames 15–18: liberação de arco energético.
- Frames 19–22: dissipação.
- Frames 23–24: recuperação.

**Função:** causar dano em uma área frontal curta.

**VFX:** arco luminoso ascendente, independente do personagem.

## 18 — SKILL 02: INVESTIDA PERFURANTE (22 × 8 = 176 frames)

O Espadachim avança rapidamente com a espada apontada para frente.

### Estrutura

- Frames 1–4: preparação.
- Frames 5–8: postura de estocada.
- Frames 9–14: investida.
- Frames 15–17: impacto.
- Frames 18–22: recuperação.

**Função:** aproximação ofensiva, podendo atingir inimigos em linha.

A engine controla distância, velocidade e colisão.

Os frames centrais devem permitir um subloop durante a investida, caso sua duração seja variável.

## 19 — SKILL 03: REDEMOINHO DE LÂMINAS (32 × 8 = 256 frames)

O Espadachim executa uma sequência de giros com a espada estendida, atingindo inimigos próximos.

### Estrutura

- Frames 1–5: preparação.
- Frames 6–9: início da rotação.
- Frames 10–25: giros ofensivos.
- Frames 26–29: desaceleração.
- Frames 30–32: recuperação.

Criar adicionalmente um ciclo central de rotação que possa ser repetido enquanto a habilidade estiver ativa.

**Função:** dano em área ao redor do personagem.

**VFX:** rastros circulares de espada, posicionados em camada independente.

## 20 — SKILL 04: GOLPE DEMOLIDOR (28 × 8 = 224 frames)

Ataque pesado com grande concentração de força.

### Estrutura

- Frames 1–5: preparação.
- Frames 6–11: elevação da espada.
- Frames 12–16: concentração.
- Frames 17–21: golpe descendente.
- Frames 22–24: impacto no solo.
- Frames 25–28: recuperação.

**Função:** dano elevado e possível atordoamento.

**VFX:** impacto de solo, poeira e pequena onda de choque.

## 21 — SKILL 05: LÂMINA DE ENERGIA (26 × 8 = 208 frames)

O Espadachim canaliza energia na espada e libera uma lâmina cortante que viaja em linha reta.

### Estrutura

- Frames 1–5: preparação.
- Frames 6–11: canalização energética.
- Frames 12–16: movimento de corte.
- Frames 17–19: liberação do projétil.
- Frames 20–23: dissipação.
- Frames 24–26: recuperação.

**Função:** ataque físico-energético à distância.

O projétil deve possuir spritesheet própria.

**Evento de spawn sugerido:** frame 18.

## 22 — SKILL 06: GRITO DE BATALHA (24 × 8 = 192 frames)

O Espadachim ergue sua arma e realiza um grito que fortalece temporariamente seu poder de combate.

### Estrutura

- Frames 1–4: preparação.
- Frames 5–9: elevação da arma.
- Frames 10–14: grito.
- Frames 15–18: ativação da aura.
- Frames 19–22: estabilização.
- Frames 23–24: retorno ao combate.

**Função:** fortalecimento temporário.

**VFX:** pulso energético e aura de fortalecimento.

Criar uma camada de aura em loop, independente das animações corporais, permitindo que o Espadachim continue caminhando e atacando enquanto o efeito estiver ativo.

---

# 10. ANIMAÇÕES DE DANO E MORTE

## 23 — HURT (10 × 8 = 80 frames)

Criar reação rápida e expressiva ao receber dano.

- Frames 1–2: impacto.
- Frames 3–5: recuo corporal.
- Frames 6–8: recuperação.
- Frames 9–10: retorno ao estado apropriado.

O personagem deve reagir com o equipamento atualmente equipado.

Não remover ou substituir visualmente a armadura durante Hurt.

## 24 — STAGGER: ATORDOAMENTO (16 × 8 = 128 frames)

Animação de desequilíbrio mais intenso.

- Perda momentânea da postura.
- Movimento involuntário dos braços.
- Recuo do torso.
- Recuperação gradual.

Permitir um estado intermediário de sustentação para atordoamentos de duração variável.

## 25 — KNOCKDOWN: QUEDA (20 × 8 = 160 frames)

O Espadachim perde o equilíbrio e cai no chão.

- Impacto inicial.
- Perda de sustentação.
- Queda.
- Contato com o solo.
- Estabilização.

A direção da queda deve respeitar a orientação e o vetor de impacto definidos pelo gameplay.

## 26 — GET UP: LEVANTAR (20 × 8 = 160 frames)

O personagem se levanta após uma queda.

- Apoio com braços ou joelhos.
- Recuperação da sustentação.
- Elevação do torso.
- Retorno à postura de combate.

A pose inicial deve corresponder ao estado final de Knockdown.

## 27 — DIED (28 × 8 = 224 frames)

Criar uma morte completa.

### Estrutura

- Frames 1–4: impacto fatal.
- Frames 5–8: perda de equilíbrio.
- Frames 9–14: queda.
- Frames 15–20: contato com o solo.
- Frames 21–26: estabilização.
- Frames 27–28: estado final imóvel.

Armadura, arma, cabelo e acessórios devem acompanhar naturalmente a queda.

**Sem loop.**

O corpo deve permanecer completamente equipado durante a morte.

---

# 11. PROJÉTEIS DA CLASSE

## PROJÉTIL 01 — LÂMINA DE ENERGIA

**Voo:** 12 frames em loop.

Características:

- Arco cortante de energia.
- Núcleo luminoso.
- Bordas afiadas.
- Rastro curto.
- Movimento direcional.
- Silhueta legível.

**Impacto:** 10 frames.

Ao atingir um alvo:

- O arco se fragmenta.
- Pequenas partículas energéticas se espalham.
- O brilho diminui.
- O efeito desaparece.

Criar variantes direcionais apropriadas para as oito orientações.

## PROJÉTIL / EFEITO 02 — ONDA DO GOLPE DEMOLIDOR

**Expansão:** 12 frames.

Criar uma onda de choque baixa e curta, propagando-se pelo solo.

A colisão e o alcance devem ser controlados pela engine.

---

# 12. VFX OBRIGATÓRIOS

Todos os VFX devem ser independentes do personagem, mantendo compatibilidade com as armas e equipamentos utilizados.

### VFX 01 — BASIC SLASH 01 (8 frames)

Rastro de corte horizontal.

### VFX 02 — BASIC SLASH 02 (8 frames)

Rastro de corte ascendente.

### VFX 03 — BASIC SLASH 03 (10 frames)

Rastro de corte giratório.

### VFX 04 — COMBO FINISHER (12 frames)

Efeito de impacto do golpe final.

### VFX 05 — PHYSICAL HIT (8 frames)

Impacto físico genérico.

### VFX 06 — BLOCK IMPACT (8 frames)

Faíscas ou energia de bloqueio.

### VFX 07 — PERFECT PARRY (10 frames)

Efeito de defesa perfeita.

### VFX 08 — DODGE DUST (8 frames)

Poeira ou rastro durante esquiva.

### VFX 09 — CRESCENT SLASH (14 frames)

Arco energético ascendente.

### VFX 10 — PIERCING CHARGE (12 frames)

Rastro de velocidade da investida.

### VFX 11 — BLADE WHIRLWIND (16 frames em loop)

Rastros circulares de espada.

### VFX 12 — DEMOLISHING STRIKE (16 frames)

Impacto pesado no chão.

### VFX 13 — ENERGY BLADE CHARGE (12 frames)

Energia concentrando-se na espada.

### VFX 14 — ENERGY BLADE PROJECTILE (12 frames em loop)

Projétil da habilidade.

### VFX 15 — ENERGY BLADE IMPACT (10 frames)

Impacto do projétil.

### VFX 16 — BATTLE CRY ACTIVATION (14 frames)

Pulso energético de fortalecimento.

### VFX 17 — BATTLE CRY AURA (12 frames em loop)

Aura durante o estado fortalecido.

### VFX 18 — FOOTSTEP DUST (6 frames)

Poeira discreta de movimentação.

### VFX 19 — LANDING IMPACT (8 frames)

Efeito de aterrissagem.

### VFX 20 — DEATH DUST (10 frames)

Poeira discreta durante a queda final.

**Regra obrigatória:** o efeito de corte deve acompanhar a trajetória e a extremidade da espada equipada, não a posição de uma espada fixa imaginária.

---

# 13. ESPECIFICAÇÃO TÉCNICA — FRAMES

| Animação | Frames/direção | Direções | Total |
|---|---:|---:|---:|
| Idle | 16 | 8 | 128 |
| Combat Idle | 16 | 8 | 128 |
| Walk | 16 | 8 | 128 |
| Run | 20 | 8 | 160 |
| Dodge | 16 | 8 | 128 |
| Jump | 18 | 8 | 144 |
| Turn | 8 | 16 transições | 128 |
| Combo 01 | 16 | 8 | 128 |
| Combo 02 | 18 | 8 | 144 |
| Combo 03 | 20 | 8 | 160 |
| Combo 04 | 24 | 8 | 192 |
| Block Start | 10 | 8 | 80 |
| Block Hold | 12 | 8 | 96 |
| Block Impact | 10 | 8 | 80 |
| Parry | 14 | 8 | 112 |
| Counter Attack | 18 | 8 | 144 |
| Skill 01 — Corte Crescente | 24 | 8 | 192 |
| Skill 02 — Investida | 22 | 8 | 176 |
| Skill 03 — Redemoinho | 32 | 8 | 256 |
| Skill 04 — Golpe Demolidor | 28 | 8 | 224 |
| Skill 05 — Lâmina de Energia | 26 | 8 | 208 |
| Skill 06 — Grito de Batalha | 24 | 8 | 192 |
| Hurt | 10 | 8 | 80 |
| Stagger | 16 | 8 | 128 |
| Knockdown | 20 | 8 | 160 |
| Get Up | 20 | 8 | 160 |
| Died | 28 | 8 | 224 |
| **TOTAL BASE** | | | **4.320 frames** |

Os 4.320 frames representam o conjunto corporal-base planejado, incluindo as transições Turn. Os subloops, poses de sustentação adicionais e estados divididos para habilidades de duração variável devem ser documentados e contabilizados separadamente caso exijam frames extras.

**Importante:** esses frames não precisam ser reproduzidos integralmente a cada ação. A engine deve controlar duração, interrupções, cancelamentos e transições conforme o gameplay.

---

# 14. REGRAS DO SISTEMA MODULAR

Esta é a parte mais importante da classe jogável.

## 14.1 Corpo-base como referência universal

Todas as camadas de equipamentos devem utilizar exatamente:

- A mesma animação.
- A mesma direção.
- O mesmo índice de frame.
- O mesmo ponto de ancoragem.
- A mesma linha temporal.
- A mesma pose corporal.

Um peitoral não pode executar um movimento diferente do torso.

Uma luva não pode permanecer parada enquanto a mão se move.

Uma bota não pode deslizar independentemente do pé.

## 14.2 Equipamentos devem acompanhar 100% das animações

Todo equipamento compatível deve funcionar durante:

- Idle.
- Combat Idle.
- Walk.
- Run.
- Dodge.
- Jump.
- Combos.
- Defesa.
- Parry.
- Contra-ataque.
- Skills.
- Hurt.
- Stagger.
- Knockdown.
- Get Up.
- Died.

É proibido fazer o equipamento desaparecer ou retornar à aparência-base durante habilidades.

## 14.3 Sistema de armas

O Espadachim deve suportar inicialmente:

**Espadas de uma mão:**
- Espada curta.
- Espada longa.
- Sabre.
- Espada larga de uma mão.
- Espadas raras ou mágicas.

**Equipamentos secundários:**
- Escudo pequeno.
- Escudo médio.
- Escudo pesado.
- Mão secundária vazia.

As espadas devem manter pontos de empunhadura consistentes.

O tamanho da arma poderá variar, mas sua posição deverá acompanhar corretamente as mãos.

Para armas muito diferentes em comprimento, peso ou empunhadura, criar perfis próprios de animação ou ajustes específicos. Não deformar uma espada curta para simular uma espada longa.

## 14.4 Armas de duas mãos

Preparar a arquitetura para futuras espadas de duas mãos.

Essas armas podem exigir:

- Combat Idle próprio.
- Combo próprio.
- Bloqueios específicos.
- Ajustes de postura.
- Novos pontos de empunhadura.
- Adaptações nas habilidades.

Não forçar a utilização das animações de uma mão quando isso comprometer a anatomia ou a fluidez.

## 14.5 Ocultação de partes do corpo

Quando equipamentos cobrirem completamente determinada região, utilizar máscaras ou regras de visibilidade.

Exemplos:

- Capacete fechado pode ocultar parte do cabelo.
- Peitoral fechado pode ocultar o torso-base.
- Luvas podem ocultar as mãos-base.
- Botas podem ocultar os pés-base.
- Armadura de pernas pode ocultar a roupa íntima inferior.
- Capas podem exigir renderização atrás e à frente de diferentes partes do corpo.

O sistema deve evitar sobreposição incorreta, vazamento de pixels e partes duplicadas.

---

# 15. SISTEMA DE ANIMAÇÃO E TRANSIÇÕES

Criar um conjunto preparado para máquina de estados de animação.

### Estados de movimentação

Idle ↔ Walk ↔ Run

### Estados de combate

Combat Idle → Combo 01 → Combo 02 → Combo 03 → Combo 04 → Combat Idle

### Estados defensivos

Combat Idle → Block Start → Block Hold → Block Impact / Block End → Combat Idle

Combat Idle → Parry → Counter Attack → Combat Idle

### Estados de habilidade

Combat Idle / Walk → Skill → Recovery → Combat Idle / Walk

### Estados de dano

Qualquer estado interrompível → Hurt / Stagger → Recuperação

### Estados de queda

Knockdown → Grounded → Get Up → Combat Idle

### Estado final

Died → Cadáver

### Regras de transição

- Preservar continuidade de cabeça, torso, braços e pernas.
- Evitar saltos de posição.
- Não reiniciar a pose corporal incorretamente.
- Manter equipamentos sincronizados.
- Utilizar janelas de cancelamento.
- Permitir entrada antecipada de combos.
- Priorizar responsividade dos controles.
- Não bloquear movimentos desnecessariamente.
- Manter hitboxes independentes do desenho.
- Garantir que o dano ocorra nos frames corretos.
- Utilizar animações de recuperação quando necessário.

---

# 16. FPS RECOMENDADOS

- **Idle:** 10–12 FPS.
- **Combat Idle:** 12 FPS.
- **Walk:** 12–16 FPS.
- **Run:** 16–20 FPS.
- **Dodge:** 18–24 FPS.
- **Jump:** 14–20 FPS.
- **Combos:** 18–24 FPS.
- **Block:** 16–20 FPS.
- **Parry:** 20–24 FPS.
- **Counter Attack:** 20–24 FPS.
- **Skills:** 18–24 FPS.
- **Hurt:** 18–24 FPS.
- **Stagger:** 16–20 FPS.
- **Died:** 12–16 FPS.
- **VFX:** 18–24 FPS.

A duração efetiva de cada movimento deve ser calibrada conforme a velocidade de ataque e as necessidades de gameplay.

A quantidade elevada de frames existe para proporcionar fluidez, não para tornar as ações artificialmente lentas.

---

# 17. ORGANIZAÇÃO DOS ARQUIVOS

Organizar os arquivos em uma estrutura modular.

```text
characters/
└── swordsman/
    ├── body/
    │   ├── idle.png
    │   ├── combat_idle.png
    │   ├── walk.png
    │   ├── run.png
    │   ├── dodge.png
    │   ├── jump.png
    │   ├── turn.png
    │   ├── combo_01.png
    │   ├── combo_02.png
    │   ├── combo_03.png
    │   ├── combo_04.png
    │   ├── block_start.png
    │   ├── block_hold.png
    │   ├── block_impact.png
    │   ├── parry.png
    │   ├── counter_attack.png
    │   ├── skill_01.png
    │   ├── skill_02.png
    │   ├── skill_03.png
    │   ├── skill_04.png
    │   ├── skill_05.png
    │   ├── skill_06.png
    │   ├── hurt.png
    │   ├── stagger.png
    │   ├── knockdown.png
    │   ├── get_up.png
    │   └── died.png
    │
    ├── equipment/
    │   ├── head/
    │   ├── chest/
    │   ├── shoulders/
    │   ├── arms/
    │   ├── hands/
    │   ├── legs/
    │   ├── feet/
    │   ├── back/
    │   ├── main_hand/
    │   └── off_hand/
    │
    ├── vfx/
    │   ├── combos/
    │   ├── skills/
    │   ├── defense/
    │   ├── movement/
    │   └── impacts/
    │
    ├── projectiles/
    │   ├── energy_blade.png
    │   └── shockwave.png
    │
    ├── metadata/
    │   ├── animations.json
    │   ├── equipment_slots.json
    │   ├── attachment_points.json
    │   ├── hitboxes.json
    │   └── state_machine.json
    │
    └── previews/
        ├── idle.gif
        ├── walk.gif
        ├── run.gif
        ├── combat.gif
        ├── combos.gif
        └── equipment_test.gif
```

Cada spritesheet corporal deve utilizar oito linhas direcionais na ordem:

**N, NE, E, SE, S, SW, W, NW.**

As animações Turn devem utilizar uma estrutura própria identificando direção de origem e direção de destino.

Caso uma spritesheet exceda limites práticos de resolução ou tamanho, dividir em arquivos menores sem alterar a numeração, âncoras ou metadados.

---

# 18. METADADOS OBRIGATÓRIOS

Criar arquivos JSON descrevendo:

- Identificador da classe.
- Identificador do corpo-base.
- Direções disponíveis.
- Animações disponíveis.
- Quantidade de frames.
- FPS.
- Coordenadas de recorte.
- Dimensões das células.
- Origem e ponto de ancoragem.
- Pontos de encaixe dos equipamentos.
- Pontos de empunhadura das mãos.
- Posição da ponta e trajetória da espada.
- Ordem de renderização por direção e frame.
- Máscaras de ocultação.
- Hitboxes.
- Hurtboxes.
- Estados de colisão.
- Eventos de dano.
- Eventos de spawn de projéteis.
- Eventos de ativação de VFX.
- Janelas de combo.
- Janelas de cancelamento.
- Janelas de invulnerabilidade.
- Início e término das habilidades.
- Transições permitidas.
- Estados de loop.
- Estados de morte.
- Compatibilidade dos equipamentos.
- Perfis de armas.
- Referências aos arquivos de sprites.

Todas as coordenadas e temporizações devem corresponder aos frames realmente entregues.

---

# 19. VALIDAÇÃO OBRIGATÓRIA

Antes de considerar o conjunto concluído:

1. Reproduzir Idle e Combat Idle por cinco ciclos em todas as direções.
2. Validar Walk e Run, verificando contato dos pés e ausência de deslizamento.
3. Testar todas as oito direções individualmente.
4. Testar mudanças rápidas de direção.
5. Validar Dodge, Jump e aterrissagem.
6. Reproduzir Combo 01 → 02 → 03 → 04 sem interrupções visuais.
7. Testar cancelamento de combos e retorno ao Combat Idle.
8. Verificar trajetória da espada em todos os golpes.
9. Sincronizar hitboxes com os frames de impacto.
10. Validar Block, Parry e Counter Attack.
11. Testar todas as seis habilidades.
12. Validar projéteis e efeitos visuais.
13. Testar Hurt, Stagger, Knockdown e Get Up.
14. Reproduzir Died nas oito direções.
15. Confirmar que equipamentos permanecem visíveis durante todas as animações.
16. Testar corpo-base sem nenhum equipamento.
17. Testar personagem com conjunto completo de armadura.
18. Trocar armas durante Idle e verificar atualização correta.
19. Testar espada e escudo durante os quatro combos.
20. Confirmar ordenação correta das camadas em todas as direções.
21. Verificar se capacetes ocultam corretamente partes do cabelo.
22. Confirmar que botas acompanham os pés.
23. Confirmar que luvas acompanham as mãos.
24. Validar movimento das capas.
25. Inspecionar transparência, recortes e bordas.
26. Eliminar tremores, deformações, halos e pixels residuais.
27. Verificar fluidez na escala real do jogo.
28. Testar animações com equipamentos de tamanhos diferentes.
29. Validar o desempenho com múltiplos jogadores equipados.
30. Garantir correspondência exata entre sprites e metadados.

---

# 20. CRITÉRIOS TÉCNICOS DE ENTREGA

A geração deve produzir **arquivos reais de animação**, não apenas uma folha ilustrativa de apresentação.

Cada frame deve:

- Possuir posição cronológica correta.
- Respeitar a mesma grade de recorte.
- Utilizar transparência verdadeira.
- Preservar a mesma identidade visual.
- Manter proporções anatômicas.
- Compartilhar o sistema de ancoragem.
- Permitir reprodução independente.
- Manter sincronização com os equipamentos.
- Não conter membros duplicados ou ausentes.
- Não apresentar bordas ou pixels de frames vizinhos.

As imagens de apresentação podem ser produzidas adicionalmente, mas não substituem as spritesheets funcionais.

Os GIFs devem ser gerados a partir dos frames reais entregues, e não de uma animação alternativa.

**Nenhuma animação deve ser declarada validada sem sua reprodução e inspeção efetivas.**

---

# 21. RESULTADO ESPERADO

Entregar uma classe **Espadachim completamente modular e pronta para integração em um MMORPG 2D isométrico**, contendo:

**Personagem-base**
- Corpo chibi com roupas íntimas simples.
- Oito direções completas.
- Aparência independente dos equipamentos.
- Animações corporais completas.

**Movimentação**
- Idle.
- Combat Idle.
- Walk.
- Run.
- Dodge.
- Jump.
- Turn.

**Combate**
- Combo de quatro golpes.
- Bloqueio.
- Defesa sustentada.
- Reação de bloqueio.
- Parry.
- Contra-ataque.

**Habilidades**
- Corte Crescente.
- Investida Perfurante.
- Redemoinho de Lâminas.
- Golpe Demolidor.
- Lâmina de Energia.
- Grito de Batalha.

**Estados**
- Hurt.
- Stagger.
- Knockdown.
- Get Up.
- Died.

**Sistema visual**
- Equipamentos modulares.
- Armaduras visíveis.
- Espadas substituíveis.
- Escudos substituíveis.
- Capacetes, botas, luvas e capas.
- Pontos de encaixe.
- Máscaras de ocultação.
- Ordenação de camadas por frame.
- VFX sincronizados.
- Projéteis próprios.

**TOTAL PLANEJADO: 4.320 frames corporais-base**, incluindo 128 frames de transições Turn, além de variações de equipamentos, subloops adicionais, projéteis, VFX e metadados.

O Espadachim deve transmitir **técnica, precisão, força, agilidade e progressão visual**, passando de um aventureiro sem equipamentos para um guerreiro completamente armado conforme os itens conquistados.

## PRIORIDADES ABSOLUTAS

1. Oito direções completas e consistentes.
2. Fluidez excepcional e combate responsivo.
3. Sistema de equipamentos verdadeiramente modular.
4. Corpo-base sem equipamentos fixos.
5. Combos encadeados e habilidades próprias.
6. Continuidade anatômica e visual entre os frames.
7. VFX e projéteis independentes.
8. Recortes perfeitos, sem tremores ou bordas.
9. Metadados completos para integração.
10. Compatibilidade com expansão futura de equipamentos e habilidades.

**REGRA FINAL:** a aparência visual do personagem deve ser determinada pelos equipamentos efetivamente equipados, enquanto todas as animações permanecem sincronizadas. A criação de novos equipamentos não deve exigir refazer o corpo-base, os combos ou as habilidades do Espadachim.

O resultado deve oferecer a qualidade, fluidez, personalização e consistência esperadas de uma classe jogável de um MMORPG isométrico profissional.