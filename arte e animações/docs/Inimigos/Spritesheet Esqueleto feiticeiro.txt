# INIMIGO ESQUELETO FEITICEIRO — SPRITESHEET COMPLETA EM 8 DIREÇÕES

Crie um conjunto completo de spritesheets para um **Esqueleto Feiticeiro de RPG 2D isométrico, inspirado em Diablo II, com estética Pixel Art Chibi e fantasia medieval sombria**.

O Esqueleto Feiticeiro deve ser um inimigo morto-vivo de porte médio, especializado em magia necromântica, ataques à distância e controle de área.

Diferentemente do Esqueleto Guerreiro, sua força não está no combate físico, mas na capacidade de canalizar energia sobrenatural, lançar projéteis mágicos, amaldiçoar inimigos e manipular forças obscuras.

Sua aparência deve transmitir a sensação de um antigo mago que foi reanimado por forças proibidas, conservando parte de seus conhecimentos e poderes mágicos.

Apesar da estética chibi, o personagem deve parecer sombrio, inteligente, ameaçador e misterioso.

## 1. IDENTIDADE VISUAL

O Esqueleto Feiticeiro deve possuir:

- Crânio grande, característico da estética chibi, com estrutura óssea bem definida.
- Órbitas oculares profundas, iluminadas por chamas espectrais violetas.
- Mandíbula articulada, realizando movimentos sutis durante conjurações.
- Caixa torácica, coluna e braços esqueléticos parcialmente visíveis.
- Manto antigo, rasgado e desgastado, em tons de roxo-escuro, preto e cinza.
- Capuz parcialmente cobrindo o crânio, sem ocultar completamente os olhos.
- Cinto com pequenos amuletos, ossos, pergaminhos e frascos alquímicos.
- Cajado de madeira retorcida na mão direita anatômica.
- Cristal violeta ou verde-espectral na extremidade superior do cajado.
- Mão esquerda livre para gestos mágicos.
- Pequenas runas necromânticas discretamente gravadas no cajado e nas vestimentas.
- Energia sobrenatural visível apenas durante determinadas ações.

**Personalidade visual:** um conjurador morto-vivo calculista, sinistro e experiente, com movimentos deliberados, gestos precisos e magia poderosa.

**Objetivo:** produzir animações extremamente fluidas, expressivas e consistentes, com oito direções completas, habilidades mágicas exclusivas, projéteis animados e efeitos visuais independentes.

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

**Regras direcionais:**

- Cada direção deve possuir sprites próprios.
- Respeitar a perspectiva isométrica em todas as orientações.
- Manter o cajado sempre na mão direita anatômica.
- Manter a mão esquerda livre para conjurações.
- Preservar a assimetria do manto, acessórios e equipamentos.
- Não utilizar espelhamento automático quando isso inverter detalhes anatômicos ou acessórios.
- Garantir que o capuz, manto, crânio e cajado apresentem sobreposição correta.
- Manter o personagem na mesma escala em todas as direções.
- Preservar o ponto de ancoragem no chão entre os pés.

---

## 3. CONCEITO DE COMBATE

**Tipo:** inimigo morto-vivo conjurador, especializado em ataques mágicos à distância.

**Função:** causar dano mágico, manter distância dos jogadores e controlar regiões do campo de batalha.

**Comportamento:** calculista, persistente, sombrio e estrategicamente defensivo.

**Ataque básico:** Projétil Espectral — disparo mágico de energia necromântica.

**Skill 01:** Explosão Necromântica — ataque mágico em área ao redor de um ponto selecionado.

**Skill 02:** Maldição Sombria — aplica temporariamente um efeito negativo ao jogador.

**Skill 03 opcional:** Teleporte Espectral — deslocamento mágico curto para escapar de ameaças próximas.

**Diferencial:** magia necromântica, cajado encantado, projéteis espectrais e efeitos de conjuração próprios.

O inimigo deve priorizar distância média, evitando permanecer próximo de combatentes corpo a corpo.

---

# 4. ANIMAÇÕES OBRIGATÓRIAS

## 01 — IDLE (16 frames × 8 direções = 128 frames)

O Esqueleto Feiticeiro permanece em postura de vigilância, apoiando o cajado próximo ao corpo e observando os arredores.

Sua movimentação deve transmitir a sensação de que uma força sobrenatural mantém seus ossos e vestimentas em movimento.

Durante o Idle:

- O tronco apresenta pequenas oscilações sobrenaturais.
- O crânio inclina discretamente para observar os arredores.
- A mandíbula realiza pequenos movimentos ocasionais.
- A mão esquerda abre e fecha lentamente os dedos esqueléticos.
- O cajado oscila suavemente, acompanhando os movimentos do braço.
- O cristal do cajado pulsa com brilho discreto.
- O manto apresenta ondulações leves, como se estivesse sob influência mágica.
- Pequenos amuletos e acessórios acompanham o movimento.
- As chamas espectrais dos olhos apresentam uma pulsação suave.

O personagem não deve respirar como um ser vivo.

**Loop:** perfeitamente contínuo, com retorno natural à mesma pose inicial.

## 02 — WALK (16 frames × 8 direções = 128 frames)

Criar uma caminhada de conjurador morto-vivo, com passos controlados, postura levemente curvada e movimentos sobrenaturais.

Durante o Walk:

- As pernas realizam ciclos completos de passos alternados.
- Os joelhos e tornozelos articulam naturalmente.
- O manto acompanha a caminhada, apresentando movimentos secundários fluidos.
- O cajado permanece firmemente segurado pela mão direita.
- A mão esquerda acompanha discretamente o deslocamento.
- O crânio mantém o olhar direcionado ao movimento.
- Os acessórios pendurados oscilam suavemente.
- O tronco realiza pequenas oscilações verticais.
- A parte inferior do manto deve reagir à movimentação sem atravessar as pernas.

A caminhada deve parecer sobrenatural e controlada, mas não rígida ou artificial.

**Loop:** perfeito, com contato convincente dos pés no chão e ausência de deslizamento.

## 03 — ATTACK: PROJÉTIL ESPECTRAL (18 frames × 8 direções = 144 frames)

O Esqueleto Feiticeiro utiliza seu cajado para lançar um projétil de energia necromântica.

**Estrutura:**

- **Frames 1–4 — Preparação:** o feiticeiro interrompe seus movimentos, aproxima o cajado do corpo e direciona o olhar ao alvo.
- **Frames 5–8 — Canalização:** ergue o cajado e concentra energia espectral em seu cristal.
- **Frames 9–11 — Acúmulo:** o cristal emite brilho violeta intenso e pequenas partículas mágicas convergem para sua extremidade.
- **Frames 12–13 — Disparo:** realiza um gesto rápido com o cajado e libera uma esfera de energia.
- **Frames 14–16 — Dissipação:** a energia residual desaparece gradualmente enquanto o braço retorna.
- **Frames 17–18 — Recuperação:** volta à postura inicial de combate.

O disparo deve acontecer por evento de gameplay sincronizado com o frame 12, sem manter o projétil preso à spritesheet corporal.

**Função visual:** ataque mágico básico à distância.

**Transição:** Idle/Walk → Attack → Idle/Walk.

## 04 — HURT (10 frames × 8 direções = 80 frames)

Criar uma reação clara ao receber dano.

Como o personagem é um esqueleto, a reação deve enfatizar o impacto sobre ossos, roupas e equipamentos.

Durante o Hurt:

- O tronco recua em resposta ao golpe.
- O crânio inclina rapidamente para trás.
- A mandíbula abre em reação.
- O cajado oscila, mas permanece seguro.
- A mão esquerda realiza um gesto involuntário.
- O manto acompanha o recuo corporal.
- Pequenas partículas de energia espectral podem escapar das articulações.
- O personagem recupera gradualmente o equilíbrio.

**Estrutura:**

- Frames 1–2: impacto inicial.
- Frames 3–5: recuo e desequilíbrio.
- Frames 6–8: recuperação corporal.
- Frames 9–10: retorno à postura de combate.

**Função visual:** feedback de dano e possibilidade de interrupção de conjurações conforme as regras de combate.

## 05 — DIED: DISSOLUÇÃO NECROMÂNTICA (24 frames × 8 direções = 192 frames)

Criar uma morte completa em que a magia responsável pela reanimação do feiticeiro deixa de sustentar seus ossos.

**Estrutura:**

- **Frames 1–4 — Impacto fatal:** o feiticeiro recebe o golpe final e perde o equilíbrio.
- **Frames 5–8 — Instabilidade mágica:** o cristal do cajado começa a perder brilho, enquanto as chamas espectrais dos olhos oscilam.
- **Frames 9–12 — Dissipação:** pequenas partículas de energia escapam do corpo e o cajado começa a escapar de sua mão.
- **Frames 13–16 — Colapso:** as pernas cedem, o torso se inclina e os ossos começam a se desarticular.
- **Frames 17–20 — Queda final:** o corpo desmorona no chão, acompanhado pelo manto e pelo cajado.
- **Frames 21–23 — Estabilização:** os ossos e acessórios concluem seus movimentos residuais.
- **Frame 24 — Cadáver:** pilha de ossos parcialmente coberta pelo manto, com o cajado caído próximo ao corpo.

As chamas espectrais dos olhos devem desaparecer completamente antes do último frame.

**Sem loop.** Manter o frame final até a remoção do cadáver.

## 06 — SKILL 01: EXPLOSÃO NECROMÂNTICA (24 frames × 8 direções = 192 frames)

O Esqueleto Feiticeiro concentra energia sombria e provoca uma explosão mágica em uma área selecionada próxima ao jogador.

**Estrutura:**

- **Frames 1–4 — Preparação:** firma os pés no chão e posiciona o cajado verticalmente.
- **Frames 5–8 — Canalização:** ergue a mão esquerda enquanto o cristal começa a emitir luz violeta.
- **Frames 9–12 — Acúmulo:** runas espectrais surgem ao redor do cajado e a energia aumenta.
- **Frames 13–16 — Conjuração:** aponta o cajado na direção do alvo e conclui o encantamento.
- **Frames 17–18 — Ativação:** realiza um gesto brusco, provocando a explosão no ponto marcado.
- **Frames 19–22 — Dissipação:** as partículas ao redor do feiticeiro desaparecem.
- **Frames 23–24 — Recuperação:** retorna à postura de combate.

**Função visual:** ataque mágico em área.

A explosão deve ser representada por VFX independente, posicionado pela engine no solo.

O evento de detonação deve ocorrer no frame 17, sincronizado com a animação.

## 07 — SKILL 02: MALDIÇÃO SOMBRIA (22 frames × 8 direções = 176 frames)

O Esqueleto Feiticeiro lança uma maldição sobre o jogador, reduzindo temporariamente sua resistência ou capacidade ofensiva.

**Estrutura:**

- **Frames 1–4 — Preparação:** abaixa discretamente o cajado e abre a mão esquerda.
- **Frames 5–8 — Canalização:** pequenos símbolos necromânticos surgem ao redor dos dedos.
- **Frames 9–12 — Concentração:** o crânio se inclina e os olhos espectrais brilham intensamente.
- **Frames 13–15 — Conjuração:** estende a mão esquerda em direção ao alvo, liberando um símbolo mágico.
- **Frames 16–19 — Dissipação:** as runas desaparecem gradualmente enquanto o braço retorna.
- **Frames 20–22 — Recuperação:** volta à posição inicial.

**Função visual:** aplicação de efeito negativo temporário.

A maldição deve possuir um VFX separado, exibido sobre ou ao redor do alvo atingido.

O evento de aplicação deve ser sincronizado com o frame 14.

## 08 — SKILL 03: TELEPORTE ESPECTRAL (opcional — 20 frames × 8 direções = 160 frames)

Habilidade opcional de reposicionamento defensivo.

O feiticeiro desaparece temporariamente em uma nuvem de energia necromântica e reaparece em outra posição.

**Estrutura:**

- Frames 1–4: preparação e concentração.
- Frames 5–8: energia envolvendo o corpo.
- Frames 9–11: dissolução visual do personagem.
- Frames 12–14: reaparecimento no destino definido pela engine.
- Frames 15–18: reconstrução da silhueta e dissipação energética.
- Frames 19–20: recuperação da postura de combate.

**Função visual:** evasão e reposicionamento.

O teleporte deve ser controlado pela engine. Não simular deslocamento global dentro da spritesheet.

---

# 5. PROJÉTEIS OBRIGATÓRIOS

## PROJÉTIL 01 — ESFERA ESPECTRAL

Criar um projétil de energia necromântica violeta.

**Animação de voo:** 12 frames em loop.

Características:

- núcleo violeta luminoso
- bordas energéticas irregulares
- pequenas partículas espectrais
- pulsação contínua
- rastro curto de energia
- silhueta legível mesmo em movimento rápido

**Impacto:** 10 frames sem loop.

Ao atingir o alvo, a esfera explode em pequenos fragmentos luminosos e energia espectral.

Criar orientações próprias quando a perspectiva exigir; o deslocamento e a colisão são controlados pela engine.

**Sincronização:** gerado no frame 12 da animação Attack.

## PROJÉTIL 02 — SÍMBOLO DA MALDIÇÃO

Criar um símbolo mágico utilizado para aplicar a Maldição Sombria.

**Animação de conjuração/deslocamento:** 12 frames.

Características:

- runa circular violeta-escura
- pequenos símbolos necromânticos
- bordas translúcidas
- brilho pulsante
- partículas convergindo para o centro

O símbolo pode viajar até o alvo ou ser aplicado diretamente sobre ele, conforme o sistema de gameplay.

**Impacto/aplicação:** 8 frames.

O símbolo se contrai e se transforma em um pequeno selo de maldição.

**Estado persistente:** criar um loop adicional de 12 frames para representar o alvo amaldiçoado, caso o efeito permaneça visível durante a duração do debuff.

---

# 6. VFX OBRIGATÓRIOS

Produzir spritesheets independentes para todos os efeitos visuais.

### VFX 01 — NECROMANTIC CAST (12 frames)

Energia espectral concentrando-se no cristal do cajado.

- partículas violetas
- pequenas runas flutuantes
- brilho progressivo
- dissipação após o disparo

### VFX 02 — SPECTRAL PROJECTILE IMPACT (10 frames)

Explosão de energia ao atingir o alvo.

- expansão rápida
- fragmentos luminosos
- partículas espectrais
- desaparecimento gradual

### VFX 03 — NECROMANTIC EXPLOSION (16 frames)

Explosão mágica em área.

- círculo rúnico surgindo no chão
- energia concentrando-se no centro
- expansão de chamas espectrais
- pequenas partículas sobrenaturais
- dissipação gradual

Criar também uma animação opcional de telegraph de 12 frames, indicando a área que será atingida antes da explosão.

### VFX 04 — DARK CURSE CAST (10 frames)

Runas surgindo ao redor da mão esquerda durante a conjuração.

### VFX 05 — CURSE APPLICATION (8 frames)

Símbolo mágico se fixando no alvo.

### VFX 06 — CURSE STATUS (12 frames em loop)

Pequenas runas escuras e partículas espectrais representando o efeito negativo ativo.

### VFX 07 — TELEPORT DISAPPEAR (12 frames, opcional)

Dissolução do corpo em partículas necromânticas.

### VFX 08 — TELEPORT APPEAR (12 frames, opcional)

Reconstrução visual do personagem na posição de destino.

### VFX 09 — NECROMANTIC DEATH (14 frames)

Dissipação da magia que mantém o Esqueleto Feiticeiro reanimado.

### VFX 10 — BONE DUST (8 frames)

Pequena nuvem de poeira e fragmentos ósseos durante a morte.

Todos os VFX devem preservar a estética Pixel Art Chibi e ser entregues separadamente do personagem.

---

# 7. ESPECIFICAÇÕES TÉCNICAS

| Animação | Frames/direção | Direções | Total |
|---|---:|---:|---:|
| Idle | 16 | 8 | 128 |
| Walk | 16 | 8 | 128 |
| Attack — Projétil Espectral | 18 | 8 | 144 |
| Hurt | 10 | 8 | 80 |
| Died | 24 | 8 | 192 |
| Skill 01 — Explosão Necromântica | 24 | 8 | 192 |
| Skill 02 — Maldição Sombria | 22 | 8 | 176 |
| **TOTAL OBRIGATÓRIO** | | | **1.040 frames** |
| Skill 03 — Teleporte (opcional) | 20 | 8 | 160 |
| **TOTAL COM TELEPORTE** | | | **1.200 frames** |

### Projéteis e efeitos adicionais

| Elemento | Frames-base |
|---|---:|
| Esfera espectral — Voo | 12 |
| Esfera espectral — Impacto | 10 |
| Símbolo da maldição — Deslocamento | 12 |
| Símbolo da maldição — Aplicação | 8 |
| Maldição — Estado persistente | 12 |
| **Total de projéteis/estados** | **54** |

Os VFX adicionais devem ser contabilizados separadamente, considerando suas variantes direcionais.

**Total obrigatório:** 1.040 frames corporais em oito direções, além dos projéteis e efeitos visuais.

---

# 8. FPS RECOMENDADOS

- **Idle:** 10–12 FPS.
- **Walk:** 12–16 FPS.
- **Attack:** 16–20 FPS.
- **Hurt:** 16–20 FPS.
- **Died:** 12–16 FPS.
- **Explosão Necromântica:** 16–20 FPS.
- **Maldição Sombria:** 16–20 FPS.
- **Teleporte:** 18–24 FPS.
- **Projéteis:** 16–24 FPS.
- **VFX:** 16–24 FPS.

A engine poderá ajustar as velocidades de reprodução sem modificar os sprites originais.

---

# 9. REGRAS OBRIGATÓRIAS DE FLUIDEZ

- Produzir sprites próprios para as oito direções.
- Preservar rigorosamente a anatomia esquelética.
- Manter crânio, caixa torácica, coluna, braços e pernas com proporções constantes.
- Não criar, remover ou duplicar ossos entre frames, exceto durante a morte.
- Manter o cajado na mão direita anatômica e a mão esquerda livre.
- Preservar os detalhes assimétricos do manto e dos acessórios.
- Garantir continuidade dos movimentos do cajado e dos gestos mágicos.
- Animar o manto de maneira fluida, respeitando movimento e profundidade.
- Manter contato correto dos pés com o chão.
- Evitar deslizamento durante a caminhada.
- Preservar o ponto de ancoragem no chão em todos os frames.
- Evitar tremores, deformações, teleportes involuntários e alterações de escala.
- Garantir transições naturais entre Idle, Walk, Attack, Hurt e Skills.
- Idle e Walk devem possuir loops perfeitamente contínuos.
- Attack e Skills devem começar e terminar em poses compatíveis com a postura de combate.
- Hurt deve permitir retorno natural ao Idle ou Walk.
- Died deve terminar em um cadáver estático.
- Nenhum osso, cajado ou acessório pode atravessar outros elementos incorretamente.
- Manter identidade visual, iluminação, paleta e contornos consistentes.
- Não utilizar interpolação borrada que prejudique a pixel art.
- Usar transparência verdadeira.
- Não permitir bordas, halos, pixels soltos ou vazamentos entre células.
- Garantir espaço suficiente para o cajado erguido e gestos amplos de conjuração.
- Manter dimensões uniformes e coordenadas de recorte consistentes.
- Projéteis devem ser independentes do personagem e sincronizados por eventos.
- VFX devem respeitar perspectiva, posição das mãos e extremidade do cajado.
- Efeitos mágicos não devem ocultar excessivamente a silhueta.
- Validar todas as transições e orientações antes da entrega.

---

# 10. ORGANIZAÇÃO DOS ARQUIVOS

Entregar arquivos independentes:

- `skeleton_mage_idle.png`
- `skeleton_mage_walk.png`
- `skeleton_mage_attack.png`
- `skeleton_mage_hurt.png`
- `skeleton_mage_died.png`
- `skeleton_mage_skill_necromantic_explosion.png`
- `skeleton_mage_skill_dark_curse.png`
- `skeleton_mage_skill_teleport.png` (opcional)
- `skeleton_mage_projectile_spectral.png`
- `skeleton_mage_projectile_curse.png`
- `skeleton_mage_vfx_cast.png`
- `skeleton_mage_vfx_explosion.png`
- `skeleton_mage_vfx_curse.png`
- `skeleton_mage_vfx_teleport.png` (opcional)
- `skeleton_mage_vfx_death.png`
- `skeleton_mage_animations.json`

Cada spritesheet corporal deve possuir **8 linhas direcionais**, na seguinte ordem:

N, NE, E, SE, S, SW, W, NW.

Os frames de cada direção devem ser organizados horizontalmente em sequência cronológica.

O arquivo JSON deve conter:

- Identificador do inimigo.
- Nomes das animações.
- Direções e quantidade de frames.
- Coordenadas de recorte.
- Dimensões de cada célula.
- FPS de reprodução.
- Configurações de loop.
- Ponto de ancoragem dos pés.
- Hitbox e hurtbox.
- Coordenadas da extremidade do cajado por frame e direção.
- Coordenadas da mão esquerda para efeitos de magia.
- Eventos de início e término de conjuração.
- Frames de geração de projéteis.
- Eventos de dano e detonação.
- Eventos de aplicação e duração da maldição.
- Regras de interrupção por Hurt.
- Eventos de teleporte, quando aplicável.
- Estados e transições das animações.
- Estado final de morte.
- Referências aos VFX correspondentes.

---

# 11. VALIDAÇÃO OBRIGATÓRIA

Antes de considerar o conjunto concluído:

1. Reproduzir Idle e Walk por cinco ciclos completos em cada direção.
2. Confirmar consistência da anatomia esquelética, do manto e do cajado.
3. Testar Idle → Attack → Idle e Walk → Attack → Walk.
4. Verificar o surgimento do projétil na extremidade correta do cajado.
5. Validar a sincronização dos frames de conjuração e disparo.
6. Testar integralmente a Explosão Necromântica e seu VFX de área.
7. Confirmar aplicação da Maldição Sombria e seu estado persistente.
8. Validar o Teleporte Espectral, caso implementado.
9. Verificar interrupções por Hurt e recuperação da postura de combate.
10. Testar a morte completa nas oito direções.
11. Confirmar a continuidade visual dos efeitos mágicos.
12. Inspecionar todos os recortes e transparências.
13. Corrigir tremores, deformações, saltos visuais e mudanças involuntárias de escala.
14. Verificar transições entre direções durante a caminhada.
15. Testar todas as animações na escala real de gameplay, inclusive com múltiplos inimigos simultâneos.

---

# 12. RESULTADO ESPERADO

Entregar um conjunto completo de spritesheets para o **Esqueleto Feiticeiro em Pixel Art Chibi**, contendo:

- **Idle:** 128 frames.
- **Walk:** 128 frames.
- **Attack — Projétil Espectral:** 144 frames.
- **Hurt:** 80 frames.
- **Died — Dissolução Necromântica:** 192 frames.
- **Skill 01 — Explosão Necromântica:** 192 frames.
- **Skill 02 — Maldição Sombria:** 176 frames.
- **Skill 03 — Teleporte Espectral:** 160 frames opcionais.
- **Projétil Espectral:** voo e impacto.
- **Símbolo de Maldição:** conjuração, aplicação e estado persistente.
- **VFX próprios:** conjuração, explosão, maldição, necromancia, teleporte e morte.
- **Metadados completos:** JSON com recortes, direções, animações, âncoras e eventos.

**TOTAL: 1.040 frames corporais obrigatórios, ou 1.200 frames com a habilidade opcional de teleporte, além de projéteis e VFX independentes.**

O Esqueleto Feiticeiro deve funcionar como um inimigo mágico completo, capaz de atacar à distância, lançar maldições, controlar áreas e utilizar energia necromântica.

**PRIORIDADE ABSOLUTA:** oito direções completas, fluidez excepcional, consistência anatômica, movimentos naturais de conjuração, continuidade entre animações, projéteis sincronizados e sprites prontos para integração direta em um MMORPG 2D isométrico.

Não substituir animações completas por poses estáticas, espelhamentos inadequados, frames duplicados artificialmente ou efeitos mágicos genéricos. Cada animação deve ser produzida e validada individualmente em todas as oito direções.