# CLASSE JOGÁVEL — ARQUEIRO
## SPRITESHEETS MODULARES COMPLETAS EM 8 DIREÇÕES

**Gênero:** MMORPG 2D isométrico  
**Referência de gameplay:** Diablo II  
**Direção artística:** Pixel Art Chibi de fantasia medieval sombria  
**Tipo:** Personagem jogável  
**Arquitetura:** Sprites modulares com equipamentos visíveis  
**Direções:** 8  
**Especialização:** Combate à distância, precisão, mobilidade, disparos múltiplos, armadilhas e habilidades elementais  
**Armas principais:** Arcos curtos, arcos longos, arcos compostos e bestas  
**Equipamentos secundários:** Aljavas e munições  
**Identidade:** Precisão, agilidade, reflexos, sobrevivência e domínio do arco

---

# 1. OBJETIVO PRINCIPAL

Criar um conjunto completo e profissional de spritesheets para a classe jogável **Arqueiro**, contendo movimentações fluidas, animações completas de arco e flecha, combos de disparos, habilidades exclusivas, projéteis próprios, efeitos visuais independentes e sistema completo de equipamentos modulares.

O Arqueiro deve ser um personagem ágil, especializado em combate à distância, capaz de atacar enquanto controla seu posicionamento, utilizar diferentes tipos de flechas e executar habilidades que exigem precisão e coordenação corporal.

Sua principal característica deve ser a fluidez das animações de disparo.

O personagem não pode simplesmente levantar um arco estático e fazer uma flecha aparecer.

Cada disparo deve possuir uma sequência visual convincente:

1. Preparação corporal.
2. Retirada da flecha da aljava, quando aplicável.
3. Posicionamento da flecha no arco.
4. Tensionamento da corda.
5. Alinhamento da mira.
6. Liberação da corda.
7. Saída da flecha.
8. Recuo e recuperação.

Para manter o combate responsivo, certas fases podem ser abreviadas ou conectadas durante combos e ataques rápidos, desde que os movimentos permaneçam anatomicamente coerentes.

## REGRA FUNDAMENTAL

O corpo-base deve utilizar exclusivamente roupas íntimas medievais simples e opacas.

Não incorporar permanentemente:

- Arcos.
- Bestas.
- Flechas.
- Aljavas.
- Armaduras.
- Capuzes.
- Máscaras.
- Luvas.
- Botas.
- Calças.
- Capas.
- Facas.
- Acessórios.
- Efeitos mágicos.

Todos os equipamentos devem funcionar através de camadas modulares.

**Ao equipar um arco, ele deve aparecer nas mãos. Ao trocar o arco, seu modelo visual muda. Ao equipar uma aljava, ela deve aparecer nas costas ou no quadril, conforme o item. Ao trocar o tipo de flecha, o projétil disparado deve mudar visualmente.**

A criação de novos equipamentos não deve exigir reconstruir o corpo-base ou todas as animações.

---

# 2. DIREÇÃO DE ARTE DO ARQUEIRO

## 2.1 Aparência corporal básica

Criar personagem humanoide com proporções Pixel Art Chibi, preservando a estrutura corporal universal das demais classes jogáveis.

Características:

- Cabeça proporcionalmente grande.
- Corpo compacto e atlético.
- Ombros de largura moderada.
- Braços flexíveis e bem articulados.
- Mãos claramente definidas.
- Dedos legíveis para manipular arco e flecha.
- Pernas ágeis e fortes.
- Joelhos e tornozelos articulados.
- Pés bem definidos.
- Rosto expressivo.
- Olhar atento e concentrado.
- Cabelo curto ou médio.
- Musculatura estilizada.
- Silhueta clara em escala reduzida.

O personagem deve parecer um aventureiro fisicamente preparado, com movimentos leves e controlados.

## 2.2 Roupa-base obrigatória

Utilizar:

- Roupa íntima inferior medieval simples e opaca.
- Peça íntima superior discreta, conforme a variante corporal.
- Acabamentos simples de tecido.
- Pés descalços.
- Braços descobertos.
- Mãos descobertas.
- Cabeça sem equipamentos.

A roupa-base não deve possuir elementos fixos que identifiquem a classe.

## 2.3 Identidade visual

A identidade do Arqueiro deve ser construída principalmente através de:

- Postura de mira.
- Manipulação precisa das flechas.
- Movimentos rápidos e controlados.
- Esquivas.
- Disparos consecutivos.
- Mobilidade elevada.
- Uso de armadilhas.
- Habilidades de precisão.
- Coordenação entre mãos, braços, ombros e tronco.

O Arqueiro deve parecer mais leve e técnico que o Espadachim, menos ritualístico que o Mago e menos focado em combate físico direto que o Pugilista.

---

# 3. SISTEMA OBRIGATÓRIO DE 8 DIREÇÕES

Produzir todas as animações corporais nas seguintes orientações:

1. **N — Norte:** costas.
2. **NE — Nordeste:** diagonal superior direita.
3. **E — Leste:** lateral direita.
4. **SE — Sudeste:** diagonal inferior direita.
5. **S — Sul:** frente.
6. **SW — Sudoeste:** diagonal inferior esquerda.
7. **W — Oeste:** lateral esquerda.
8. **NW — Noroeste:** diagonal superior esquerda.

## Regras direcionais

- Criar sprites próprios para as oito direções.
- Preservar a perspectiva isométrica.
- Manter proporções anatômicas constantes.
- Respeitar a posição dos ombros, mãos e braços.
- Garantir alinhamento correto do arco.
- Manter a corda conectada ao arco.
- Preservar a posição da flecha durante a mira.
- Respeitar a profundidade entre personagem, arco e flecha.
- Não utilizar espelhamento automático que inverta detalhes assimétricos.
- Manter o ponto de ancoragem estável no chão.
- Garantir transições naturais entre orientações.

**Regra importante:** o lado anatômico de cada mão deve permanecer consistente entre todas as direções.

Para a configuração padrão, considerar:

- Mão esquerda anatômica segurando o arco.
- Mão direita anatômica puxando a corda.
- Mão direita retirando flechas da aljava.

Perfis alternativos para personagens canhotos podem ser implementados futuramente como uma configuração independente.

---

# 4. SISTEMA DE EQUIPAMENTOS MODULARES

O Arqueiro deve utilizar a mesma arquitetura modular universal das demais classes.

## 4.1 Camadas visuais

**BODY:** corpo-base com roupas íntimas.

**HAIR:** cabelo e variações cosméticas.

**HEAD:** capuzes, máscaras, chapéus e capacetes.

**CHEST:** armaduras leves, túnicas e coletes.

**SHOULDERS:** ombreiras e proteções.

**ARMS:** mangas, braçadeiras e proteções dos braços.

**HANDS:** luvas e acessórios.

**LEGS:** calças e proteções inferiores.

**FEET:** botas, sandálias e grevas.

**BACK:** capas, mantos e acessórios traseiros.

**MAIN_HAND:** arco ou besta equipada.

**OFF_HAND:** suporte visual para uso secundário, conforme perfil da arma.

**QUIVER:** aljava equipada.

**AMMO:** flecha ou virote atualmente utilizado.

**ACCESSORIES:** cintos, amuletos e ornamentos.

**WEAPON_VFX:** efeitos específicos da arma.

**PROJECTILE_VFX:** efeitos específicos da munição.

## 4.2 Armas compatíveis

### Arcos curtos

- Arco de madeira simples.
- Arco de caça.
- Arco reforçado.
- Arco élfico curto.
- Arco mágico.

### Arcos longos

- Arco longo de madeira.
- Arco longo reforçado.
- Arco de guerra.
- Arco ancestral.
- Arco lendário.

### Arcos compostos

- Arco composto simples.
- Arco composto reforçado.
- Arco de precisão.
- Arco encantado.
- Arco composto lendário.

### Bestas

- Besta leve.
- Besta de caça.
- Besta reforçada.
- Besta de repetição.
- Besta lendária.

## 4.3 Perfis de arma

Criar perfis específicos de animação:

**SHORT_BOW:** arco curto com tensão e recuperação rápidas.

**LONG_BOW:** arco longo com amplitude maior dos braços.

**COMPOSITE_BOW:** arco composto com postura compacta e tensão controlada.

**CROSSBOW:** besta com sistema próprio de carregamento e disparo.

**UNARMED:** personagem sem arma equipada.

A besta não deve utilizar automaticamente a mesma animação de tensionamento de um arco convencional.

Ela exige poses e eventos específicos de carregamento.

## 4.4 Aljavas

Criar suporte para:

- Aljava simples de couro.
- Aljava reforçada.
- Aljava de caça.
- Aljava ornamentada.
- Aljava elemental.
- Aljava lendária.

A aljava deve possuir:

- Ponto de ancoragem.
- Orientação própria.
- Profundidade adequada.
- Compatibilidade com capas.
- Animação de movimento secundário.
- Posição acessível para retirada de flechas.

A aljava deve permanecer visível durante movimentação, disparos, habilidades, quedas e morte.

## 4.5 Munições

Criar suporte para:

- Flecha comum.
- Flecha reforçada.
- Flecha perfurante.
- Flecha de fogo.
- Flecha de gelo.
- Flecha explosiva.
- Flecha venenosa.
- Flecha mágica.
- Virotes de besta.

A aparência do projétil disparado deve corresponder ao tipo de munição utilizado.

Quando uma habilidade possuir munição própria, o projétil especial deve ser claramente diferenciado da flecha comum.

---

# 5. SISTEMA ANATÔMICO DE ARCO E FLECHA

Esta é uma das partes mais importantes da classe.

O arco deve funcionar visualmente como um equipamento real.

## 5.1 Mão de sustentação

A mão esquerda deve:

- Segurar corretamente o arco.
- Manter o ponto de empunhadura.
- Acompanhar a orientação da mira.
- Estabilizar o arco durante o disparo.
- Reagir discretamente à liberação da corda.

## 5.2 Mão de tração

A mão direita deve:

- Alcançar a aljava.
- Retirar uma flecha.
- Posicionar a flecha no arco.
- Segurar a corda.
- Puxar a corda até a posição de mira.
- Liberar a corda.
- Retornar naturalmente.

## 5.3 Corda do arco

A corda deve possuir estados visuais próprios:

**Rest:** posição relaxada.

**Draw Start:** início da tensão.

**Half Draw:** tensão intermediária.

**Full Draw:** tensão máxima.

**Release:** liberação rápida.

**Return:** retorno à posição relaxada.

A corda não pode atravessar o corpo ou aparecer desconectada das extremidades do arco.

## 5.4 Flecha encaixada

A flecha deve permanecer corretamente posicionada entre a mão de tração e o arco.

Durante a mira:

- A ponta aponta na direção do alvo.
- A haste permanece alinhada ao disparo.
- A mão de tração acompanha a corda.
- O corpo mantém postura estável.
- O projétil não muda de tamanho entre frames.

Quando a corda for liberada, a flecha deve sair do arco e passar a ser controlada pela engine como entidade independente.

**Não duplicar a flecha no frame de disparo.**

## 5.5 Compatibilidade com diferentes arcos

Cada arco deve possuir:

- Pontos de empunhadura.
- Pontos de fixação da corda.
- Comprimento da corda.
- Posição da flecha.
- Ponto de origem do projétil.
- Perfil de tensão.
- Profundidade de renderização.

Arcos longos, curtos e compostos podem utilizar perfis de pose diferentes.

**Nunca deformar arbitrariamente um arco para fazê-lo caber em uma animação incompatível.**

---

# 6. CONCEITO DE COMBATE

**Arquétipo:** combatente de precisão à distância.

**Função:** dano físico e elemental, mobilidade, ataques múltiplos, controle de área e suporte tático.

**Ataque básico:** disparos de flechas.

**Combo principal:** quatro disparos encadeados.

**Skill 01:** Flecha Perfurante.

**Skill 02:** Disparo Múltiplo.

**Skill 03:** Chuva de Flechas.

**Skill 04:** Flecha Explosiva.

**Skill 05:** Flecha Congelante.

**Skill 06:** Armadilha do Caçador.

**Skill 07:** Chamado do Falcão.

**Skill 08:** Rajada Implacável.

**Skill 09:** Camuflagem.

**Skill 10:** Disparo Devastador.

**Diferencial:** precisão, alcance, versatilidade de munições, reposicionamento rápido e ataques com trajetória independente.

O Arqueiro deve ser capaz de realizar ataques rápidos, mas também possuir habilidades de preparação prolongada que recompensem uma mira bem executada.

---

# 7. ANIMAÇÕES DE MOVIMENTAÇÃO

## 01 — IDLE: POSTURA NEUTRA (16 frames × 8 direções = 128 frames)

O Arqueiro permanece parado, apresentando movimentos corporais sutis.

Durante o Idle:

- Respiração natural.
- Pequena expansão do peito.
- Oscilação discreta dos ombros.
- Movimento suave da cabeça.
- Braços relaxados.
- Alternância natural do peso corporal.
- Movimento secundário do cabelo.
- Pequenos ajustes de postura.

Quando houver arco equipado, ele deve permanecer em posição relaxada, sem manter a corda tensionada.

**Loop:** perfeitamente contínuo.

## 02 — ARCHERY COMBAT IDLE (20 × 8 = 160 frames)

O Arqueiro assume uma postura de combate.

Durante a animação:

- Joelhos ligeiramente flexionados.
- Tronco orientado ao alvo.
- Arco preparado na mão esquerda.
- Mão direita próxima à aljava ou ao arco.
- Olhar atento.
- Pequenas oscilações de equilíbrio.
- Respiração controlada.
- Ombros preparados para o movimento de disparo.

**Loop:** perfeito.

O arco não deve permanecer com a corda completamente tensionada neste estado.

## 03 — WALK (16 × 8 = 128 frames)

Criar caminhada natural e fluida.

- Passos alternados.
- Movimento coordenado dos braços.
- Arco acompanhando o deslocamento.
- Aljava reagindo suavemente.
- Contato correto dos pés.
- Movimento secundário das roupas.
- Transferência natural de peso.

**Loop:** perfeito.

## 04 — RUN (20 × 8 = 160 frames)

Criar corrida rápida e ágil.

- Passadas amplas.
- Tronco inclinado.
- Braços coordenados.
- Arco mantido firmemente seguro.
- Aljava acompanhando o movimento.
- Capa reagindo à velocidade.
- Recuperação rápida entre passos.

O Arqueiro deve apresentar excelente mobilidade.

**Loop:** perfeito.

## 05 — DODGE: ROLAMENTO EVASIVO (16 × 8 = 128 frames)

Criar uma esquiva rápida, utilizando rolamento curto ou deslocamento evasivo.

### Estrutura

- Frames 1–3: preparação.
- Frames 4–7: impulso.
- Frames 8–11: rolamento ou movimento evasivo.
- Frames 12–14: aterrissagem.
- Frames 15–16: recuperação.

O arco deve permanecer seguro durante o movimento.

A aljava deve acompanhar o corpo sem atravessar o chão incorretamente.

**Sem loop.**

## 06 — DASH: PASSO DO CAÇADOR (18 × 8 = 144 frames)

Criar um avanço evasivo extremamente rápido.

### Estrutura

- Frames 1–3: preparação.
- Frames 4–7: impulso.
- Frames 8–12: deslocamento veloz.
- Frames 13–16: desaceleração.
- Frames 17–18: recuperação.

**Função:** reposicionamento rápido.

O deslocamento global deve ser controlado pela engine.

## 07 — JUMP (18 × 8 = 144 frames)

Criar salto completo:

- Preparação.
- Impulso.
- Subida.
- Ápice.
- Descida.
- Aterrissagem.
- Recuperação.

O arco e a aljava devem acompanhar o movimento.

Separar Jump Start, Airborne Hold e Landing quando necessário para permitir altura variável.

## 08 — TURN (8 frames × 16 transições = 128 frames)

Criar transições suaves entre direções adjacentes.

O personagem deve ajustar:

- Cabeça.
- Ombros.
- Tronco.
- Quadris.
- Braços.
- Arco.
- Aljava.

A mudança de direção deve preservar a responsividade.

---

# 8. SISTEMA COMPLETO DE MIRA

O Arqueiro deve possuir animações específicas para preparar, manter, disparar e cancelar a mira.

## 09 — AIM START (12 × 8 = 96 frames)

O personagem retira uma flecha da aljava, posiciona-a no arco e inicia o tensionamento.

### Estrutura

- Frames 1–3: mão direita alcança a aljava.
- Frames 4–5: retirada da flecha.
- Frames 6–8: posicionamento no arco.
- Frames 9–10: início da tensão.
- Frames 11–12: alinhamento da mira.

O movimento deve preservar anatomia e posição dos equipamentos.

## 10 — AIM HOLD (16 × 8 = 128 frames)

O Arqueiro mantém o arco tensionado enquanto mira.

Durante o Hold:

- Braço esquerdo estendido.
- Mão direita mantendo a corda puxada.
- Flecha alinhada.
- Olhar concentrado.
- Pequenas oscilações corporais.
- Respiração controlada.
- Movimento discreto de roupas e cabelo.
- Corda permanecendo tensionada.

**Loop:** perfeitamente contínuo.

A flecha não deve deslizar ou mudar de comprimento.

## 11 — AIM RELEASE (10 × 8 = 80 frames)

O personagem libera a corda e dispara.

### Estrutura

- Frames 1–2: preparação final.
- Frames 3–4: liberação da corda.
- Frames 5–6: saída da flecha.
- Frames 7–8: recuo do arco.
- Frames 9–10: recuperação.

**Spawn do projétil:** frame 4.

A flecha deve deixar de ser renderizada como elemento encaixado quando o projétil independente for criado.

## 12 — AIM CANCEL (8 × 8 = 64 frames)

O jogador interrompe a mira sem disparar.

- Redução gradual da tensão.
- Retorno da mão direita.
- Reposicionamento da flecha.
- Retorno à postura de combate.

**Sem loop.**

A flecha deve permanecer disponível conforme as regras de munição, sem ser consumida indevidamente.

---

# 9. SISTEMA DE COMBO PRINCIPAL

Criar um **combo de quatro ataques com arco**, encadeados naturalmente.

O combo deve ser rápido e responsivo, utilizando movimentos abreviados de carregamento quando necessário.

## 13 — COMBO 01: DISPARO RÁPIDO (16 × 8 = 128 frames)

Primeiro ataque.

O Arqueiro retira uma flecha e executa um disparo rápido.

### Estrutura

- Frames 1–3: preparação.
- Frames 4–6: encaixe da flecha.
- Frames 7–9: tensionamento.
- Frames 10–11: disparo.
- Frames 12–14: recuperação parcial.
- Frames 15–16: preparação para Combo 02.

**Spawn:** frame 10.

## 14 — COMBO 02: DISPARO DUPLO (18 × 8 = 144 frames)

Segundo ataque.

O Arqueiro realiza dois disparos rápidos consecutivos.

### Estrutura

- Frames 1–3: preparação.
- Frames 4–6: primeiro disparo.
- Frames 7–10: recarga rápida.
- Frames 11–13: segundo disparo.
- Frames 14–16: recuperação.
- Frames 17–18: preparação para Combo 03.

**Spawns:** frames 6 e 12.

O movimento das mãos deve ser extremamente fluido.

## 15 — COMBO 03: FLECHA PRECISA (22 × 8 = 176 frames)

Terceiro ataque.

O Arqueiro realiza um disparo concentrado, com maior precisão e força.

### Estrutura

- Frames 1–4: preparação.
- Frames 5–9: posicionamento da flecha.
- Frames 10–14: tensão máxima.
- Frames 15–17: disparo.
- Frames 18–20: recuperação.
- Frames 21–22: preparação para Combo 04.

**Spawn:** frame 16.

A postura deve transmitir concentração e estabilidade.

## 16 — COMBO 04: DISPARO FINALIZADOR (24 × 8 = 192 frames)

Último ataque do combo.

O Arqueiro concentra força e executa um disparo poderoso.

### Estrutura

- Frames 1–5: preparação.
- Frames 6–11: tensionamento.
- Frames 12–16: concentração.
- Frames 17–19: disparo.
- Frames 20–22: recuperação.
- Frames 23–24: retorno à postura de combate.

**Spawn:** frame 18.

O disparo deve possuir impacto visual superior aos anteriores.

### Regras dos combos

- Combo 01 → Combo 02 → Combo 03 → Combo 04.
- Manter continuidade da posição do arco.
- Não reiniciar a postura entre golpes.
- Permitir entrada antecipada.
- A engine controla janelas de combo.
- Sincronizar retirada de flechas e disparos.
- Não duplicar flechas visualmente.
- Preservar a posição da aljava.
- Permitir cancelamentos quando autorizados.
- Manter todos os equipamentos visíveis.
- Garantir transições suaves para Combat Idle.

---

# 10. HABILIDADES ESPECIAIS DO ARQUEIRO

## 17 — SKILL 01: FLECHA PERFURANTE (26 × 8 = 208 frames)

O Arqueiro utiliza um tensionamento poderoso para disparar uma flecha capaz de atravessar múltiplos inimigos.

### Estrutura

- Frames 1–5: preparação.
- Frames 6–11: posicionamento da flecha.
- Frames 12–16: tensão máxima.
- Frames 17–20: disparo.
- Frames 21–24: recuperação.
- Frames 25–26: retorno ao combate.

### Características

- Postura firme.
- Corda altamente tensionada.
- Flecha especial de ponta alongada.
- Rastro de velocidade.
- Recuo convincente do arco.

**Função:** dano elevado em linha, com capacidade de perfuração.

**Spawn:** frame 18.

**Projétil próprio:** Piercing Arrow.

---

## 18 — SKILL 02: DISPARO MÚLTIPLO (28 × 8 = 224 frames)

O Arqueiro prepara várias flechas e as dispara em formato de leque.

### Estrutura

- Frames 1–5: preparação.
- Frames 6–11: retirada e posicionamento das flechas.
- Frames 12–16: tensionamento.
- Frames 17–20: disparo múltiplo.
- Frames 21–25: recuperação.
- Frames 26–28: retorno ao combate.

### Características

- Múltiplas flechas visíveis.
- Distribuição coerente sobre a corda.
- Mão de tração segurando o conjunto.
- Disparo simultâneo.
- Pequenos rastros individuais.
- Trajetórias divergentes.

**Função:** atingir múltiplos inimigos à frente.

**Spawn:** frame 19.

Cada flecha deve ser uma entidade independente, com trajetória própria definida pela engine.

---

## 19 — SKILL 03: CHUVA DE FLECHAS (34 × 8 = 272 frames)

O Arqueiro dispara uma sequência de flechas em direção ao alto, provocando uma chuva de projéteis sobre uma área selecionada.

### Estrutura

**Frames 1–5 — Preparação**

O Arqueiro firma os pés e direciona o arco para cima.

**Frames 6–11 — Carregamento**

Retira várias flechas e prepara a sequência.

**Frames 12–17 — Tensionamento**

Eleva o arco e concentra o ataque.

**Frames 18–22 — Disparo**

Realiza uma sequência rápida de lançamentos ascendentes.

**Frames 23–28 — Chuva**

As flechas começam a atingir a região selecionada.

**Frames 29–32 — Recuperação**

O Arqueiro abaixa o arco e recupera a postura.

**Frames 33–34 — Retorno**

Assume novamente a posição de combate.

### Características

- Disparos ascendentes.
- Flechas viajando acima do campo.
- Área de aviso no chão.
- Múltiplas quedas.
- Pequenos impactos individuais.
- Poeira e partículas.

**Função:** dano em área ao longo de um período.

A engine deve controlar a quantidade de flechas, posições de impacto e duração da habilidade.

---

## 20 — SKILL 04: FLECHA EXPLOSIVA (28 × 8 = 224 frames)

O Arqueiro prepara uma flecha elemental capaz de explodir ao atingir o alvo.

### Estrutura

- Frames 1–5: preparação.
- Frames 6–11: canalização de energia ígnea.
- Frames 12–16: formação da flecha elemental.
- Frames 17–20: disparo.
- Frames 21–25: dissipação.
- Frames 26–28: recuperação.

### Características

- Ponta da flecha envolvida em fogo.
- Pequenas partículas incandescentes.
- Brilho alaranjado.
- Rastro flamejante.
- Explosão no impacto.

**Função:** dano de fogo em área.

**Spawn:** frame 19.

**Projétil próprio:** Explosive Arrow.

---

## 21 — SKILL 05: FLECHA CONGELANTE (26 × 8 = 208 frames)

O Arqueiro prepara uma flecha envolvida por energia gélida.

### Estrutura

- Frames 1–4: preparação.
- Frames 5–10: canalização de gelo.
- Frames 11–15: formação cristalina.
- Frames 16–19: disparo.
- Frames 20–23: dissipação.
- Frames 24–26: recuperação.

### Características

- Ponta cristalina.
- Pequenas partículas de gelo.
- Brilho azul-claro.
- Rastro congelante.
- Fragmentação no impacto.

**Função:** dano de gelo e aplicação de lentidão ou congelamento.

**Spawn:** frame 18.

**Projétil próprio:** Frost Arrow.

---

## 22 — SKILL 06: ARMADILHA DO CAÇADOR (30 × 8 = 240 frames)

O Arqueiro posiciona uma armadilha no chão para imobilizar ou causar dano ao inimigo.

### Estrutura

- Frames 1–5: preparação.
- Frames 6–11: retirada da armadilha do equipamento.
- Frames 12–17: agachamento.
- Frames 18–22: posicionamento.
- Frames 23–26: ativação.
- Frames 27–30: recuperação.

### Características

- Movimento corporal de agachamento.
- Braços posicionando o mecanismo.
- Interação convincente com o solo.
- Pequenas partículas.
- Retorno rápido à postura de combate.

**Função:** controle territorial.

**Evento de posicionamento:** frame 21.

Criar spritesheets independentes da armadilha:

- Colocação.
- Estado armado.
- Ativação.
- Impacto.
- Destruição ou desaparecimento.

A armadilha deve possuir colisão e duração controladas pela engine.

---

## 23 — SKILL 07: CHAMADO DO FALCÃO (32 × 8 = 256 frames)

O Arqueiro invoca ou chama um falcão de caça treinado para auxiliá-lo.

### Estrutura

- Frames 1–5: preparação.
- Frames 6–11: gesto de comando.
- Frames 12–17: assobio ou sinalização.
- Frames 18–23: aproximação do falcão.
- Frames 24–28: comando de ataque.
- Frames 29–32: recuperação.

### Características

- Braço erguido.
- Gesto de comando.
- Expressão concentrada.
- Pequeno movimento do corpo acompanhando o falcão.
- Animação de aproximação da criatura.
- Movimento natural das roupas.

**Função:** invocar um aliado temporário para atacar ou marcar inimigos.

O falcão deve possuir spritesheets próprias de voo, Idle aéreo, ataque, Hurt, Died e habilidades quando necessárias.

A criatura deve existir como entidade independente com IA própria.

---

## 24 — SKILL 08: RAJADA IMPLACÁVEL (28 × 8 = 224 frames)

O Arqueiro executa uma sequência extremamente rápida de disparos.

### Estrutura

- Frames 1–4: preparação.
- Frames 5–8: primeiro disparo.
- Frames 9–20: sequência rápida.
- Frames 21–24: disparo final.
- Frames 25–28: recuperação.

### Características

- Movimentos rápidos de retirada e encaixe de flechas.
- Cordas tensionadas e liberadas repetidamente.
- Braços coordenados.
- Recuos curtos.
- Rastros de velocidade.
- Pequenos efeitos de disparo.

### RAPID FIRE HOLD — 12 × 8 = 96 frames

Criar subloop capaz de sustentar disparos consecutivos durante duração variável.

O loop deve retornar naturalmente ao primeiro frame.

Cada flecha deve ser gerada por evento individual.

**Função:** alto dano contínuo contra alvos à distância.

---

## 25 — SKILL 09: CAMUFLAGEM (26 × 8 = 208 frames)

O Arqueiro utiliza técnicas de ocultação para reduzir sua visibilidade e dificultar sua detecção.

### Estrutura

- Frames 1–4: preparação.
- Frames 5–9: agachamento e controle da postura.
- Frames 10–15: ativação da camuflagem.
- Frames 16–20: estabilização.
- Frames 21–24: conclusão.
- Frames 25–26: retorno ao movimento.

### Características

- Postura baixa.
- Movimento corporal discreto.
- Pequenas partículas naturais.
- Redução gradual da opacidade.
- Efeito visual sutil de ocultação.
- Preservação da silhueta.

**Função:** furtividade temporária.

O efeito deve ser aplicado a todas as camadas do personagem.

**Não substituir o personagem equipado por uma silhueta genérica.**

A engine controla duração, visibilidade e regras de cancelamento.

---

## 26 — SKILL 10: DISPARO DEVASTADOR (34 × 8 = 272 frames)

O Arqueiro concentra toda sua precisão e força em um único disparo extremamente poderoso.

### Estrutura

**Frames 1–5 — Preparação**

O Arqueiro assume postura firme e retira uma flecha especial.

**Frames 6–12 — Tensionamento**

Puxa lentamente a corda até sua extensão máxima.

**Frames 13–19 — Concentração**

Mantém a mira enquanto energia se acumula ao redor da flecha.

**Frames 20–24 — Intensificação**

A energia atinge seu ápice e o corpo demonstra esforço controlado.

**Frames 25–28 — Disparo**

Libera a corda, disparando uma flecha de grande velocidade.

**Frames 29–32 — Recuperação**

O braço de tração retorna enquanto o arco oscila discretamente.

**Frames 33–34 — Retorno**

Assume a postura de combate.

### Características

- Grande antecipação.
- Cordas altamente tensionadas.
- Flecha especial.
- Energia concentrada.
- Rastro de alta velocidade.
- Forte impacto.
- Recuperação expressiva.

**Função:** dano extremamente elevado, com possível perfuração e impacto em área reduzida.

**Spawn:** frame 27.

**Projétil próprio:** Devastating Arrow.

---

# 11. ANIMAÇÕES DE DANO E MORTE

## 27 — HURT (10 × 8 = 80 frames)

Criar reação rápida ao receber dano.

- Recuo corporal.
- Movimento involuntário dos braços.
- Oscilação do arco.
- Expressão de dor.
- Recuperação natural.

O arco e a aljava devem permanecer equipados.

## 28 — STAGGER (16 × 8 = 128 frames)

Reação de atordoamento.

- Perda de equilíbrio.
- Interrupção da postura de mira.
- Recuo dos ombros.
- Recuperação gradual.

Se o personagem estiver mirando, a tensão da corda deverá ser interrompida de maneira coerente.

## 29 — KNOCKDOWN (20 × 8 = 160 frames)

Queda completa.

- Impacto inicial.
- Perda de equilíbrio.
- Queda.
- Contato com o solo.
- Estabilização.

O arco deve acompanhar o corpo.

A aljava não pode atravessar o chão.

## 30 — GET UP (20 × 8 = 160 frames)

Recuperação após queda.

- Apoio no chão.
- Elevação do torso.
- Recuperação das pernas.
- Reposicionamento do arco.
- Retorno à postura de combate.

A pose inicial deve conectar-se ao estado final de Knockdown.

## 31 — DIED (28 × 8 = 224 frames)

Criar morte completa.

### Estrutura

- Frames 1–4: impacto fatal.
- Frames 5–8: perda de equilíbrio.
- Frames 9–14: queda.
- Frames 15–20: contato com o solo.
- Frames 21–26: estabilização.
- Frames 27–28: cadáver imóvel.

**Sem loop.**

Arco, aljava, roupas e equipamentos devem acompanhar a queda.

---

# 12. SISTEMA DE PROJÉTEIS

Todos os projéteis devem ser independentes do personagem.

## PROJÉTIL 01 — FLECHA COMUM

**Voo:** 8 frames ou estado visual equivalente, conforme a trajetória.

**Impacto:** 6 frames.

Características:

- Haste de madeira.
- Ponta metálica.
- Penas traseiras.
- Silhueta clara.
- Orientação coerente.
- Movimento rápido.

A animação de voo deve evitar rotação artificial que prejudique o pixel art.

## PROJÉTIL 02 — FLECHA PERFURANTE

**Voo:** 12 frames.

**Impacto:** 10 frames.

- Ponta alongada.
- Rastro de velocidade.
- Pequenas partículas metálicas.
- Movimento direto.

## PROJÉTIL 03 — FLECHAS MÚLTIPLAS

**Voo:** 8 frames por flecha.

**Impacto:** 6 frames.

Cada flecha deve possuir trajetória independente.

## PROJÉTIL 04 — FLECHA EXPLOSIVA

**Voo:** 12 frames.

**Impacto:** 18 frames.

- Ponta flamejante.
- Rastro incandescente.
- Explosão no impacto.
- Partículas de fogo.

## PROJÉTIL 05 — FLECHA CONGELANTE

**Voo:** 12 frames.

**Impacto:** 14 frames.

- Ponta cristalina.
- Partículas gélidas.
- Rastro de gelo.
- Fragmentação no impacto.

## PROJÉTIL 06 — FLECHA DEVASTADORA

**Voo:** 14 frames.

**Impacto:** 16 frames.

- Rastro energético intenso.
- Ponta reforçada.
- Movimento de alta velocidade.
- Impacto expressivo.

## PROJÉTIL 07 — FLECHAS DA CHUVA

**Queda:** 10 frames.

**Impacto:** 8 frames.

As flechas devem cair em posições controladas pela engine.

### Regras gerais

- Utilizar transparência verdadeira.
- Manter orientação correta.
- Criar variantes direcionais quando necessário.
- Preservar silhueta.
- Controlar trajetória pela engine.
- Controlar colisão independentemente.
- Sincronizar spawn com os frames de disparo.
- Não duplicar flechas.
- Não permitir vazamentos entre células.
- Permitir múltiplos projéteis simultâneos.
- Aplicar a aparência da munição realmente equipada.

---

# 13. ARMADILHAS E CRIATURAS AUXILIARES

## 13.1 ARMADILHA DO CAÇADOR

Criar spritesheets independentes para:

**Trap Place:** 12 frames.

**Trap Armed:** 12 frames em loop.

**Trap Trigger:** 10 frames.

**Trap Impact:** 12 frames.

**Trap Destroy:** 10 frames.

A armadilha deve possuir:

- Perspectiva isométrica correta.
- Ponto de ancoragem no chão.
- Colisão independente.
- Estados próprios.
- Duração controlada pela engine.

## 13.2 FALCÃO DE CAÇA

Criar uma criatura auxiliar em Pixel Art Chibi, compatível com a direção artística do jogo.

Características:

- Corpo compacto.
- Cabeça expressiva.
- Bico curvado.
- Olhos atentos.
- Asas bem definidas.
- Garras visíveis.
- Plumagem marrom, bege ou acinzentada.
- Silhueta clara em tamanho reduzido.

### Animações do falcão

- Idle aéreo: 16 frames.
- Fly: 16 frames.
- Dive Attack: 18 frames.
- Claw Attack: 14 frames.
- Hurt: 8 frames.
- Died: 18 frames.
- Summon / Arrive: 20 frames.
- Despawn / Leave: 16 frames.

Criar orientações compatíveis com as oito direções do jogo.

O falcão deve funcionar como entidade independente.

Não utilizar uma imagem estática deslizando pelo cenário.

---

# 14. VFX OBRIGATÓRIOS

Produzir efeitos independentes do corpo e dos equipamentos.

### VFX 01 — BOW STRING RELEASE (6 frames)

Vibração visual da corda durante o disparo.

### VFX 02 — ARROW SHOT (6 frames)

Pequeno efeito de saída da flecha.

### VFX 03 — ARROW IMPACT (8 frames)

Impacto de flecha comum.

### VFX 04 — PIERCING ARROW TRAIL (12 frames)

Rastro de flecha perfurante.

### VFX 05 — PIERCING IMPACT (10 frames)

Impacto de perfuração.

### VFX 06 — MULTISHOT RELEASE (10 frames)

Liberação simultânea de múltiplas flechas.

### VFX 07 — ARROW RAIN TELEGRAPH (14 frames)

Área de aviso da Chuva de Flechas.

### VFX 08 — ARROW RAIN IMPACT (12 frames)

Impactos individuais no solo.

### VFX 09 — FIRE ARROW CHARGE (12 frames)

Energia ígnea envolvendo a flecha.

### VFX 10 — FIRE ARROW TRAIL (12 frames)

Rastro flamejante.

### VFX 11 — FIRE EXPLOSION (18 frames)

Explosão da flecha de fogo.

### VFX 12 — FROST ARROW CHARGE (12 frames)

Formação de energia gélida.

### VFX 13 — FROST ARROW TRAIL (12 frames)

Rastro congelante.

### VFX 14 — ICE IMPACT (14 frames)

Fragmentação de gelo.

### VFX 15 — TRAP ACTIVATION (12 frames)

Ativação da armadilha.

### VFX 16 — TRAP IMPACT (12 frames)

Impacto da armadilha.

### VFX 17 — FALCON SUMMON (16 frames)

Surgimento ou aproximação do falcão.

### VFX 18 — FALCON ATTACK (10 frames)

Impacto das garras.

### VFX 19 — RAPID FIRE TRAIL (12 frames em loop)

Rastros de disparos consecutivos.

### VFX 20 — CAMOUFLAGE ACTIVATION (14 frames)

Ativação da camuflagem.

### VFX 21 — CAMOUFLAGE HOLD (12 frames em loop)

Efeito de ocultação persistente.

### VFX 22 — DEVASTATING SHOT CHARGE (16 frames)

Concentração de energia no arco.

### VFX 23 — DEVASTATING SHOT TRAIL (14 frames)

Rastro de alta velocidade.

### VFX 24 — DEVASTATING IMPACT (16 frames)

Impacto do disparo final.

### VFX 25 — DODGE DUST (8 frames)

Poeira durante esquivas.

### VFX 26 — DASH TRAIL (10 frames)

Rastro de velocidade.

### VFX 27 — FOOTSTEP DUST (6 frames)

Poeira de movimentação.

### VFX 28 — LANDING IMPACT (8 frames)

Efeito de aterrissagem.

### VFX 29 — DEATH DUST (10 frames)

Poeira durante a queda final.

### Regras dos VFX

- Preservar a estética Pixel Art Chibi.
- Utilizar transparência verdadeira.
- Respeitar perspectiva isométrica.
- Sincronizar efeitos com os eventos de gameplay.
- Posicionar efeitos na ponta da flecha, arco ou alvo.
- Evitar ocultar excessivamente o personagem.
- Criar variantes direcionais quando necessário.
- Não utilizar interpolação borrada.
- Não permitir bordas ou halos.
- Manter identidade artística consistente.

---

# 15. ESPECIFICAÇÃO TÉCNICA — FRAMES CORPORAIS

| Animação | Frames/direção | Direções | Total |
|---|---:|---:|---:|
| Idle | 16 | 8 | 128 |
| Archery Combat Idle | 20 | 8 | 160 |
| Walk | 16 | 8 | 128 |
| Run | 20 | 8 | 160 |
| Dodge | 16 | 8 | 128 |
| Dash | 18 | 8 | 144 |
| Jump | 18 | 8 | 144 |
| Turn | 8 | 16 transições | 128 |
| Aim Start | 12 | 8 | 96 |
| Aim Hold | 16 | 8 | 128 |
| Aim Release | 10 | 8 | 80 |
| Aim Cancel | 8 | 8 | 64 |
| Combo 01 — Disparo Rápido | 16 | 8 | 128 |
| Combo 02 — Disparo Duplo | 18 | 8 | 144 |
| Combo 03 — Flecha Precisa | 22 | 8 | 176 |
| Combo 04 — Finalizador | 24 | 8 | 192 |
| Skill 01 — Flecha Perfurante | 26 | 8 | 208 |
| Skill 02 — Disparo Múltiplo | 28 | 8 | 224 |
| Skill 03 — Chuva de Flechas | 34 | 8 | 272 |
| Skill 04 — Flecha Explosiva | 28 | 8 | 224 |
| Skill 05 — Flecha Congelante | 26 | 8 | 208 |
| Skill 06 — Armadilha | 30 | 8 | 240 |
| Skill 07 — Chamado do Falcão | 32 | 8 | 256 |
| Skill 08 — Rajada Implacável | 28 | 8 | 224 |
| Rapid Fire Hold | 12 | 8 | 96 |
| Skill 09 — Camuflagem | 26 | 8 | 208 |
| Skill 10 — Disparo Devastador | 34 | 8 | 272 |
| Hurt | 10 | 8 | 80 |
| Stagger | 16 | 8 | 128 |
| Knockdown | 20 | 8 | 160 |
| Get Up | 20 | 8 | 160 |
| Died | 28 | 8 | 224 |
| **TOTAL PLANEJADO** | | | **5.312 frames** |

**Total corporal planejado: 5.312 frames**, incluindo as 16 transições direcionais de Turn.

Esse total não inclui:

- Variações de equipamentos.
- Perfis alternativos de arco e besta.
- Projéteis.
- VFX.
- Armadilhas.
- Spritesheets do falcão.
- Estados adicionais de sustentação.
- Ajustes específicos de empunhadura.

---

# 16. FPS RECOMENDADOS

- **Idle:** 10–12 FPS.
- **Combat Idle:** 12 FPS.
- **Walk:** 12–16 FPS.
- **Run:** 16–20 FPS.
- **Dodge:** 20–24 FPS.
- **Dash:** 20–24 FPS.
- **Jump:** 16–20 FPS.
- **Aim Start:** 16–20 FPS.
- **Aim Hold:** 10–12 FPS.
- **Aim Release:** 20–24 FPS.
- **Combos:** 18–24 FPS.
- **Skills rápidas:** 18–24 FPS.
- **Skills carregadas:** 16–20 FPS.
- **Hurt:** 18–24 FPS.
- **Stagger:** 16–20 FPS.
- **Died:** 12–16 FPS.
- **Projéteis:** 18–24 FPS.
- **VFX:** 18–24 FPS.

A engine deve controlar a duração efetiva de cada ação.

As animações de arco devem permanecer fluidas sem prejudicar a responsividade.

---

# 17. REGRAS DO SISTEMA MODULAR

## 17.1 Sincronização

Todas as camadas visuais devem compartilhar:

- Mesma animação.
- Mesma direção.
- Mesmo índice de frame.
- Mesma referência temporal.
- Mesmo sistema de ancoragem.
- Mesma pose corporal.

## 17.2 Arcos

Cada arco deve:

- Permanecer preso à mão de sustentação.
- Possuir corda própria.
- Acompanhar tensão e liberação.
- Manter proporções.
- Não atravessar o corpo.
- Não desaparecer durante habilidades.
- Possuir pontos de disparo consistentes.

## 17.3 Aljavas

A aljava deve:

- Permanecer presa ao ponto de equipamento.
- Acompanhar movimentos do corpo.
- Respeitar a profundidade.
- Permitir animação de retirada da flecha.
- Manter aparência durante todas as habilidades.
- Ser compatível com capas e mantos.

## 17.4 Munições

As flechas devem:

- Utilizar o visual do tipo equipado.
- Possuir pontos de origem corretos.
- Permanecer alinhadas ao arco durante a mira.
- Tornar-se projéteis independentes no disparo.
- Não aparecer duplicadas.
- Não atravessar incorretamente as mãos.
- Utilizar VFX apropriados.

## 17.5 Equipamentos durante habilidades

Todos os equipamentos devem permanecer visíveis durante:

- Combos.
- Disparos.
- Esquivas.
- Saltos.
- Armadilhas.
- Invocações.
- Camuflagem.
- Hurt.
- Stagger.
- Knockdown.
- Get Up.
- Died.

## 17.6 Compatibilidade entre classes

O Arqueiro deve compartilhar o corpo-base universal com Espadachim, Mago, Pugilista e Necromante.

Equipamentos compatíveis poderão ser reutilizados.

Arcos, bestas e aljavas podem ser restritos a classes específicas, conforme o sistema de equipamentos.

---

# 18. MÁQUINA DE ESTADOS DE ANIMAÇÃO

Criar estados preparados para gameplay real.

### Movimentação

Idle ↔ Walk ↔ Run

Idle / Combat Idle → Dodge / Dash → Recovery

### Mira

Combat Idle → Aim Start → Aim Hold → Aim Release → Combat Idle

Combat Idle → Aim Start → Aim Hold → Aim Cancel → Combat Idle

### Combo

Combat Idle → Combo 01 → Combo 02 → Combo 03 → Combo 04 → Combat Idle

### Habilidades

Combat Idle / Walk → Skill → Recovery → Combat Idle / Walk

### Rajada Implacável

Rapid Fire Start → Rapid Fire Hold → Rapid Fire End

### Camuflagem

Camouflage Activation → Camouflage State → Camouflage End

### Dano

Qualquer estado interrompível → Hurt / Stagger → Recovery

### Queda

Knockdown → Grounded → Get Up → Combat Idle

### Morte

Died → Cadáver

### Regras de transição

- Permitir entrada antecipada de combos.
- Utilizar janelas de cancelamento.
- Preservar a continuidade corporal.
- Não reiniciar poses incorretamente.
- Manter arco, aljava e flechas sincronizados.
- Controlar hitboxes por eventos.
- Permitir interrupções conforme o gameplay.
- Garantir responsividade.
- Não cancelar projéteis já disparados indevidamente.
- Manter armadilhas e falcão independentes do corpo.
- Sincronizar todos os VFX.
- Permitir atualização visual de equipamentos.

---

# 19. ORGANIZAÇÃO DOS ARQUIVOS

Entregar estrutura modular:

```text
characters/
└── archer/
    ├── body/
    │   ├── idle.png
    │   ├── combat_idle.png
    │   ├── walk.png
    │   ├── run.png
    │   ├── dodge.png
    │   ├── dash.png
    │   ├── jump.png
    │   ├── turn.png
    │   ├── aim_start.png
    │   ├── aim_hold.png
    │   ├── aim_release.png
    │   ├── aim_cancel.png
    │   ├── combo_01.png
    │   ├── combo_02.png
    │   ├── combo_03.png
    │   ├── combo_04.png
    │   ├── skill_piercing_arrow.png
    │   ├── skill_multishot.png
    │   ├── skill_arrow_rain.png
    │   ├── skill_explosive_arrow.png
    │   ├── skill_frost_arrow.png
    │   ├── skill_hunter_trap.png
    │   ├── skill_falcon_call.png
    │   ├── skill_rapid_fire.png
    │   ├── rapid_fire_hold.png
    │   ├── skill_camouflage.png
    │   ├── skill_devastating_shot.png
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
    │   ├── bows/
    │   │   ├── shortbows/
    │   │   ├── longbows/
    │   │   └── composite_bows/
    │   ├── crossbows/
    │   ├── quivers/
    │   ├── ammunition/
    │   └── accessories/
    │
    ├── projectiles/
    │   ├── normal_arrow/
    │   ├── piercing_arrow/
    │   ├── multishot/
    │   ├── explosive_arrow/
    │   ├── frost_arrow/
    │   ├── devastating_arrow/
    │   └── arrow_rain/
    │
    ├── traps/
    │   └── hunter_trap/
    │
    ├── companions/
    │   └── falcon/
    │       ├── idle.png
    │       ├── fly.png
    │       ├── dive_attack.png
    │       ├── claw_attack.png
    │       ├── hurt.png
    │       ├── died.png
    │       ├── summon.png
    │       └── despawn.png
    │
    ├── vfx/
    │   ├── shots/
    │   ├── combos/
    │   ├── fire/
    │   ├── ice/
    │   ├── traps/
    │   ├── falcon/
    │   ├── camouflage/
    │   ├── movement/
    │   └── impacts/
    │
    ├── metadata/
    │   ├── animations.json
    │   ├── equipment_slots.json
    │   ├── attachment_points.json
    │   ├── bow_profiles.json
    │   ├── ammo_profiles.json
    │   ├── projectiles.json
    │   ├── hitboxes.json
    │   ├── skills.json
    │   ├── companions.json
    │   └── state_machine.json
    │
    └── previews/
        ├── idle.gif
        ├── walk.gif
        ├── run.gif
        ├── aiming.gif
        ├── combos.gif
        ├── skills.gif
        ├── falcon.gif
        └── equipment_test.gif
```

Cada spritesheet corporal deve possuir oito linhas direcionais na ordem:

**N, NE, E, SE, S, SW, W, NW.**

As animações Turn devem utilizar estrutura própria com direção de origem e destino.

Arquivos excessivamente grandes devem ser divididos sem alterar os metadados.

---

# 20. METADADOS OBRIGATÓRIOS

Criar JSON contendo:

- Identificador da classe.
- Identificador do corpo-base.
- Direções disponíveis.
- Animações disponíveis.
- Quantidade exata de frames.
- FPS.
- Coordenadas de recorte.
- Dimensões das células.
- Origem e ponto de ancoragem.
- Pontos de encaixe dos equipamentos.
- Posição das mãos.
- Posição do arco.
- Pontos de fixação da corda.
- Estado de tensão da corda.
- Posição da flecha encaixada.
- Ponto de origem do projétil.
- Posição da aljava.
- Pontos de retirada das flechas.
- Ordem de renderização por frame.
- Máscaras de ocultação.
- Hitboxes.
- Hurtboxes.
- Eventos de disparo.
- Eventos de recarga.
- Eventos de consumo de munição.
- Eventos de spawn de projéteis.
- Eventos de impacto.
- Janelas de combo.
- Janelas de cancelamento.
- Janelas de invulnerabilidade.
- Estados de mira.
- Estados de camuflagem.
- Eventos de armadilha.
- Eventos de invocação do falcão.
- Estados de morte.
- Perfis de arco e besta.
- Compatibilidade de equipamentos.
- Referências aos VFX.
- Transições permitidas.

Todos os eventos devem corresponder exatamente aos frames entregues.

---

# 21. REGRAS OBRIGATÓRIAS DE FLUIDEZ

- Produzir oito direções completas.
- Preservar proporções chibi.
- Manter anatomia consistente.
- Garantir continuidade dos movimentos dos braços.
- Não deformar mãos, dedos ou ombros.
- Animar retirada da flecha de maneira convincente.
- Manter o arco corretamente posicionado.
- Preservar conexão da corda.
- Garantir tensão gradual da corda.
- Não duplicar flechas.
- Sincronizar disparo e saída do projétil.
- Preservar escala entre todas as direções.
- Evitar tremores e deslocamentos involuntários.
- Não utilizar interpolação borrada.
- Manter contato correto dos pés com o chão.
- Garantir loops perfeitos de Idle, Walk, Run e Aim Hold.
- Criar transições suaves entre os quatro golpes do combo.
- Manter equipamentos sincronizados.
- Garantir que aljavas acompanhem o corpo.
- Animar capas e mantos de maneira fluida.
- Evitar armas atravessando o corpo incorretamente.
- Preservar a posição da flecha durante a mira.
- Manter VFX independentes.
- Sincronizar projéteis com os frames corretos.
- Preservar a mesma direção artística das outras classes.
- Utilizar transparência verdadeira.
- Não permitir bordas, halos ou pixels soltos.
- Não permitir vazamentos entre células.
- Reservar espaço suficiente para arcos longos.
- Manter recortes consistentes.
- Validar todas as direções individualmente.
- Garantir boa leitura visual na escala real do jogo.

---

# 22. VALIDAÇÃO OBRIGATÓRIA

Antes de considerar o conjunto concluído:

1. Reproduzir Idle e Combat Idle por cinco ciclos em cada direção.
2. Validar Walk e Run.
3. Testar mudanças rápidas entre oito direções.
4. Verificar Dodge e Dash.
5. Validar Jump e aterrissagem.
6. Testar Aim Start.
7. Confirmar retirada correta da flecha.
8. Validar posicionamento da flecha no arco.
9. Testar tensionamento da corda.
10. Reproduzir Aim Hold por cinco ciclos.
11. Verificar estabilidade da flecha durante a mira.
12. Testar Aim Release e spawn do projétil.
13. Confirmar que a flecha não permanece duplicada.
14. Testar Aim Cancel.
15. Reproduzir o combo completo de quatro disparos.
16. Validar continuidade das mãos e do arco entre os golpes.
17. Testar Flecha Perfurante.
18. Testar Disparo Múltiplo.
19. Validar Chuva de Flechas.
20. Testar Flecha Explosiva.
21. Validar Flecha Congelante.
22. Testar Armadilha do Caçador.
23. Confirmar funcionamento independente da armadilha.
24. Testar Chamado do Falcão.
25. Validar animações e IA do falcão.
26. Testar Rajada Implacável e seu loop.
27. Validar Camuflagem com equipamentos completos.
28. Testar Disparo Devastador.
29. Verificar interrupções por Hurt e Stagger.
30. Reproduzir Knockdown e Get Up.
31. Validar Died nas oito direções.
32. Testar corpo-base sem equipamentos.
33. Equipar diferentes arcos curtos.
34. Equipar arco longo e validar a empunhadura.
35. Equipar arco composto.
36. Testar besta com perfil próprio de recarga.
37. Trocar aljavas e validar posicionamento.
38. Trocar tipos de flechas e validar projéteis.
39. Testar capuzes, capas e armaduras.
40. Confirmar que os equipamentos permanecem visíveis durante todas as animações.
41. Inspecionar recortes, transparências e bordas.
42. Eliminar tremores, deformações e alterações de escala.
43. Testar desempenho com múltiplos arqueiros disparando simultaneamente.
44. Confirmar correspondência exata entre frames, JSON e eventos.
45. Validar a leitura visual de todas as animações na escala real de gameplay.

---

# 23. CRITÉRIOS TÉCNICOS DE ENTREGA

A geração deve produzir **spritesheets reais, completas e funcionais**, não apenas folhas ilustrativas de apresentação.

Cada frame deve:

- Possuir ordem cronológica correta.
- Respeitar a grade de recorte.
- Utilizar transparência verdadeira.
- Preservar identidade visual.
- Manter anatomia consistente.
- Compartilhar o sistema de ancoragem.
- Permitir reprodução independente.
- Manter sincronização com equipamentos.
- Não conter membros duplicados ou ausentes.
- Não apresentar pixels de células vizinhas.

As animações do arco devem possuir continuidade real entre:

**Retirar flecha → Encaixar → Tensionar → Mirar → Disparar → Recuperar.**

As animações das habilidades devem possuir eventos sincronizados com o gameplay.

As flechas devem ser projetadas como entidades independentes, com trajetória e colisão controladas pela engine.

Os GIFs de prévia devem ser gerados a partir dos próprios frames utilizados no jogo.

Nenhuma animação deve ser considerada validada sem reprodução e inspeção efetivas.

---

# 24. RESULTADO ESPERADO

Entregar uma classe **Arqueiro completamente modular e pronta para integração em um MMORPG 2D isométrico**, contendo:

### Personagem-base

- Corpo chibi com roupas íntimas simples.
- Oito direções completas.
- Aparência independente dos equipamentos.
- Compatibilidade com o corpo-base universal.
- Animações corporais completas.

### Movimentação

- Idle.
- Archery Combat Idle.
- Walk.
- Run.
- Dodge.
- Dash.
- Jump.
- Turn.

### Sistema de arco e flecha

- Aim Start.
- Aim Hold.
- Aim Release.
- Aim Cancel.
- Retirada de flecha.
- Posicionamento no arco.
- Tensionamento da corda.
- Mira.
- Disparo.
- Recuperação.
- Combo de quatro disparos.

### Habilidades

- Flecha Perfurante.
- Disparo Múltiplo.
- Chuva de Flechas.
- Flecha Explosiva.
- Flecha Congelante.
- Armadilha do Caçador.
- Chamado do Falcão.
- Rajada Implacável.
- Camuflagem.
- Disparo Devastador.

### Estados

- Hurt.
- Stagger.
- Knockdown.
- Get Up.
- Died.

### Sistema visual

- Arcos substituíveis.
- Bestas substituíveis.
- Aljavas equipáveis.
- Flechas com aparência variável.
- Armaduras modulares.
- Capuzes, capacetes e máscaras.
- Luvas, botas e acessórios.
- Capas e mantos animados.
- Pontos de encaixe por frame.
- Perfis próprios de empunhadura.
- Corda do arco animada.
- Projéteis independentes.
- VFX exclusivos.
- Armadilhas próprias.
- Falcão auxiliar com animações completas.
- Efeitos persistentes de camuflagem.
- Metadados de animação e gameplay.

**TOTAL PLANEJADO: 5.312 frames corporais-base**, incluindo as transições Turn, além das variações de equipamentos, projéteis, VFX, armadilhas, falcão e metadados.

O Arqueiro deve transmitir **precisão, agilidade, controle, sobrevivência, domínio do arco e progressão visual**, evoluindo de um aventureiro sem equipamentos para um mestre arqueiro completamente equipado.

## PRIORIDADES ABSOLUTAS

1. Oito direções completas e consistentes.
2. Fluidez excepcional das animações.
3. Corpo-base universal sem equipamentos fixos.
4. Equipamentos verdadeiramente modulares.
5. Sistema completo e convincente de arco e flecha.
6. Cordas e flechas corretamente animadas.
7. Combos de disparos encadeados.
8. Dez habilidades próprias e visualmente distintas.
9. Projéteis com trajetórias e impactos independentes.
10. Armadilhas e companheiros funcionais.
11. Equipamentos sincronizados durante todas as animações.
12. Recortes perfeitos, sem tremores ou bordas.
13. Responsividade elevada.
14. Compatibilidade com diferentes modelos de arco e besta.
15. Integração direta com os sistemas de combate, animação e equipamentos.

**REGRA FINAL:** o Arqueiro deve utilizar a mesma arquitetura modular das demais classes jogáveis, compartilhando corpo-base e equipamentos universais quando compatíveis, mas possuindo animações exclusivas de mira, recarga, tensionamento, disparo, combos e habilidades.

A aparência do personagem deve ser determinada pelos equipamentos efetivamente equipados. A criação de novos arcos, aljavas, flechas ou armaduras não deve exigir refazer o corpo-base ou os combos existentes.

**CRITÉRIO FINAL DE APROVAÇÃO:** a classe somente estará concluída quando todas as animações, projéteis, VFX, equipamentos e metadados estiverem completos, organizados e validados, sem tremores, deformações, bordas, inconsistências de empunhadura ou falhas na continuidade dos disparos.

O resultado deve oferecer a fluidez, personalização visual, precisão e qualidade artística esperadas de uma classe jogável de um MMORPG isométrico profissional.