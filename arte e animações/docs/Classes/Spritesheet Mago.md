# CLASSE JOGÁVEL — MAGO
## SPRITESHEETS MODULARES COMPLETAS EM 8 DIREÇÕES

**Gênero:** MMORPG 2D isométrico  
**Referência de gameplay:** Diablo II  
**Direção artística:** Pixel Art Chibi de fantasia medieval sombria  
**Tipo:** Personagem jogável  
**Arquitetura:** Sprites modulares com equipamentos visíveis  
**Direções:** 8  
**Especialização:** Magia elemental, ataques à distância, controle de área, teleporte e habilidades arcanas  
**Elementos principais:** Fogo, Gelo e Arcano  
**Equipamentos principais:** Cajados, varinhas, grimórios e orbes mágicos

---

# 1. OBJETIVO PRINCIPAL

Criar um conjunto completo e profissional de spritesheets para a classe jogável **Mago**, com animações extremamente fluidas, conjurações expressivas, habilidades mágicas exclusivas, projéteis elementais, efeitos visuais próprios e sistema de equipamentos modulares.

O personagem deve possuir uma aparência-base simples, utilizando apenas roupas íntimas medievais discretas, permitindo que sua aparência evolua completamente conforme os equipamentos utilizados pelo jogador.

Diferentemente do Espadachim, o Mago utiliza energia sobrenatural, gestos arcanos, canalizações, ataques elementais e movimentação evasiva para controlar o combate.

Sua animação deve transmitir **inteligência, concentração, domínio mágico, precisão e poder crescente**.

## REGRA FUNDAMENTAL

O corpo-base não deve possuir cajado, túnica, chapéu, luvas, botas, grimório, armadura ou qualquer outro equipamento permanentemente incorporado.

Todos os equipamentos devem ser elementos visuais independentes que acompanham perfeitamente as animações.

Ao equipar um cajado, ele aparece nas mãos do personagem. Ao substituir o cajado por uma varinha, o modelo e a empunhadura devem ser atualizados. Ao equipar uma túnica, o tecido deve acompanhar os movimentos corporais. Ao remover qualquer equipamento, o corpo-base deve continuar visível.

**A geração de novos equipamentos não deve exigir reconstruir as animações corporais da classe.**

---

# 2. DIREÇÃO DE ARTE DO MAGO

## 2.1 Aparência corporal básica

Criar um personagem humanoide com proporções chibi, compartilhando o padrão anatômico e a escala do Espadachim.

Características:

- Cabeça proporcionalmente grande.
- Corpo compacto e levemente esguio.
- Ombros de largura moderada.
- Braços e pernas curtos, mas bem articulados.
- Mãos expressivas para gestos de conjuração.
- Dedos suficientemente legíveis para manipular cajados, varinhas e grimórios.
- Rosto expressivo.
- Cabelo curto ou médio.
- Expressão inteligente, concentrada e determinada.
- Anatomia adequada a movimentos de combate e magia.
- Silhueta clara mesmo em escala reduzida.

O personagem deve parecer um aventureiro iniciante com aptidão mágica, mas sem vestimentas ou equipamentos que identifiquem permanentemente sua classe.

## 2.2 Roupa-base obrigatória

O Mago deve utilizar exclusivamente:

- Roupa íntima inferior medieval simples e opaca.
- Peça íntima superior discreta, conforme a variante corporal.
- Acabamentos simples de tecido, sem aparência de armadura.
- Pés descalços.
- Braços descobertos.
- Cabeça sem chapéu ou capacete.
- Mãos sem luvas.

**Não incluir na aparência-base:**

- Túnicas.
- Mantos.
- Chapéus de mago.
- Capuzes.
- Cajados.
- Varinhas.
- Grimórios.
- Orbes mágicos.
- Botas.
- Luvas.
- Joias.
- Armaduras.
- Auras permanentes.

O corpo-base deve permanecer visualmente completo quando todos os equipamentos forem removidos.

## 2.3 Compatibilidade com outras classes

O Mago deve compartilhar o mesmo padrão corporal universal das demais classes humanoides compatíveis.

Quando possível, reutilizar:

- Idle neutro.
- Walk básico.
- Run básico.
- Dodge.
- Jump.
- Hurt.
- Stagger.
- Knockdown.
- Get Up.
- Died.

Criar animações específicas do Mago para:

- Posturas de combate mágico.
- Movimentos com cajado.
- Conjurações.
- Canalizações.
- Magias elementais.
- Teleporte.
- Habilidades especiais.

**Importante:** compartilhar a estrutura e os movimentos universais não significa tornar as classes visualmente idênticas. O Mago deve possuir gestos, posturas e movimentos próprios durante o combate.

---

# 3. SISTEMA OBRIGATÓRIO DE 8 DIREÇÕES

Produzir todas as animações nas seguintes orientações:

1. **N — Norte:** costas.
2. **NE — Nordeste:** diagonal superior direita.
3. **E — Leste:** lateral direita.
4. **SE — Sudeste:** diagonal inferior direita.
5. **S — Sul:** frente.
6. **SW — Sudoeste:** diagonal inferior esquerda.
7. **W — Oeste:** lateral esquerda.
8. **NW — Noroeste:** diagonal superior esquerda.

### Regras direcionais

- Produzir sprites próprios para as oito direções.
- Preservar rigorosamente a perspectiva isométrica.
- Manter proporções corporais constantes.
- Respeitar a posição anatômica dos braços e mãos.
- Garantir continuidade dos gestos mágicos.
- Preservar escala e iluminação.
- Não utilizar espelhamentos que invertam equipamentos assimétricos.
- Manter o mesmo ponto de ancoragem no chão.
- Garantir transições naturais entre orientações.
- Respeitar sobreposição de cajados, grimórios, túnicas e braços.

Os VFX direcionais devem acompanhar a orientação real do personagem.

---

# 4. SISTEMA DE EQUIPAMENTOS MODULARES

O Mago deverá utilizar a mesma arquitetura modular das demais classes jogáveis.

## 4.1 Camadas visuais

**BODY:** corpo-base com roupas íntimas.

**HAIR:** cabelo e variações cosméticas.

**HEAD:** chapéus, capuzes, tiaras, coroas e capacetes mágicos.

**CHEST:** túnicas, vestes arcanas, peitorais e roupas superiores.

**SHOULDERS:** ombreiras, proteções e adornos mágicos.

**ARMS:** mangas e proteções dos braços.

**HANDS:** luvas, braceletes e manoplas.

**LEGS:** calças, saias, proteções inferiores e partes inferiores das túnicas.

**FEET:** botas e calçados.

**BACK:** mantos, capas e acessórios traseiros.

**MAIN_HAND:** cajado, varinha ou arma mágica principal.

**OFF_HAND:** grimório, orbe, foco mágico ou mão livre.

**ACCESSORIES:** cintos, amuletos, bolsas e ornamentos visuais.

**MAGIC_VFX:** efeitos mágicos independentes.

## 4.2 Equipamentos mágicos

Preparar o sistema para suportar:

**Cajados**
- Cajado de madeira simples.
- Cajado elemental.
- Cajado de cristal.
- Cajado arcano.
- Cajado lendário.

**Varinhas**
- Varinha de aprendiz.
- Varinha de fogo.
- Varinha de gelo.
- Varinha arcana.
- Varinha encantada.

**Focos secundários**
- Grimório.
- Orbe mágico.
- Cristal flutuante.
- Tomo arcano.
- Mão secundária vazia.

**Vestuário**
- Túnicas simples.
- Vestes elementais.
- Mantos encantados.
- Chapéus de mago.
- Capuzes.
- Botas mágicas.
- Luvas e braceletes.

## 4.3 Perfis de empunhadura

Criar perfis específicos:

**Staff Two-Handed:** cajado longo segurado com duas mãos durante determinados movimentos.

**Staff One-Handed:** cajado utilizado com uma mão, permitindo gestos com a outra.

**Wand + Focus:** varinha em uma mão e grimório ou orbe na outra.

**Wand Only:** varinha com mão secundária livre.

**Unarmed Magic:** conjurações realizadas diretamente com as mãos.

Cada perfil deve utilizar as mesmas bases anatômicas, mas possuir ajustes de pose quando necessário.

Não forçar uma varinha curta a utilizar exatamente a mesma empunhadura de um cajado longo.

## 4.4 Regras de renderização

- Cajados devem permanecer alinhados às mãos.
- Varinhas devem acompanhar o movimento do pulso.
- Grimórios devem abrir, fechar e acompanhar os gestos quando utilizados.
- Orbes podem flutuar próximos à mão, utilizando pontos de ancoragem.
- Túnicas devem acompanhar pernas, quadris e tronco.
- Capas devem apresentar movimentos secundários.
- Chapéus devem permanecer alinhados à cabeça.
- Capuzes devem ocultar corretamente as partes apropriadas do cabelo.
- Luvas devem acompanhar cada posição dos dedos e mãos.
- Botas devem acompanhar os pés.
- Equipamentos não podem desaparecer durante habilidades.

A ordem de renderização deve variar conforme direção, animação e frame.

---

# 5. CONCEITO DE COMBATE

**Arquétipo:** conjurador elemental.

**Função:** causar dano mágico à distância, controlar multidões, proteger-se com barreiras e reposicionar-se rapidamente.

**Atributos visuais:** concentração, precisão, poder elemental e fragilidade física relativa.

**Ataque básico:** Projétil Arcano.

**Combo mágico:** sequência de três conjurações ofensivas.

**Skill 01:** Bola de Fogo.

**Skill 02:** Lança de Gelo.

**Skill 03:** Nova Glacial.

**Skill 04:** Chuva de Meteoros.

**Skill 05:** Teleporte Arcano.

**Skill 06:** Barreira Arcana.

**Skill 07:** Raio Canalizado.

**Skill 08:** Explosão Arcana.

O Mago deve possuir grande variedade de ataques, mas todos precisam compartilhar uma linguagem corporal coerente.

As habilidades devem ser claramente diferenciadas por cores, gestos, partículas, ritmo e trajetória.

---

# 6. ANIMAÇÕES DE MOVIMENTAÇÃO

## 01 — IDLE: POSTURA NEUTRA (16 frames × 8 direções = 128 frames)

O Mago permanece parado, sem equipamento obrigatório nas mãos.

Durante o Idle:

- Respiração natural.
- Pequena expansão do peito.
- Oscilação suave dos ombros.
- Movimento discreto da cabeça.
- Ajustes naturais das mãos.
- Alternância sutil de peso corporal.
- Movimento secundário do cabelo.
- Expressão tranquila e concentrada.

**Loop:** perfeitamente contínuo.

## 02 — MAGIC COMBAT IDLE (20 × 8 = 160 frames)

Criar postura específica de combate mágico.

Durante a animação:

- Joelhos ligeiramente flexionados.
- Tronco ereto, com leve inclinação ofensiva.
- Mão principal posicionada para segurar o foco mágico.
- Mão secundária parcialmente erguida.
- Dedos preparados para conjuração.
- Pequenos movimentos de concentração.
- Olhar fixo na direção do alvo.
- Respiração controlada.

Quando houver cajado, o equipamento deve acompanhar a pose.

Quando não houver equipamento, o personagem deve manter uma postura de conjuração desarmada.

**Loop:** perfeitamente contínuo.

## 03 — WALK (16 × 8 = 128 frames)

Criar caminhada natural, fluida e controlada.

- Passos alternados.
- Movimentos coordenados dos braços.
- Oscilação moderada do tronco.
- Contato correto dos pés com o solo.
- Movimento secundário de cabelo e equipamentos.
- Velocidade visual consistente.
- Postura levemente mais ereta que a do Espadachim em combate.

**Loop:** perfeito.

## 04 — RUN (20 × 8 = 160 frames)

Criar corrida ágil, utilizada para escapar de ameaças.

- Inclinação moderada do tronco.
- Passos rápidos.
- Braços coordenados.
- Movimento natural de cabelo e vestimentas.
- Equipamentos acompanhando o deslocamento.
- Recuperação rápida entre passadas.

O Mago deve parecer ágil, mas menos orientado ao combate físico que o Espadachim.

**Loop:** perfeitamente contínuo.

## 05 — DODGE: PASSO EVASIVO (16 × 8 = 128 frames)

O Mago realiza um deslocamento evasivo rápido.

### Estrutura

- Frames 1–3: preparação.
- Frames 4–7: impulso lateral ou diagonal.
- Frames 8–11: deslocamento.
- Frames 12–14: estabilização.
- Frames 15–16: recuperação.

O deslocamento global deve ser controlado pela engine.

**Sem loop.**

## 06 — JUMP (18 × 8 = 144 frames)

Criar salto completo, com preparação, impulso, subida, ápice, descida e aterrissagem.

Dividir em estados quando necessário para permitir duração variável:

- Jump Start.
- Airborne Hold.
- Landing.

A sombra do personagem deve permanecer em camada independente, ancorada ao chão.

## 07 — TURN: MUDANÇA DE DIREÇÃO (8 frames × 16 transições = 128 frames)

Criar transições suaves entre direções adjacentes, nos dois sentidos.

O movimento deve envolver:

- Cabeça.
- Ombros.
- Tronco.
- Quadris.
- Braços.
- Cajado ou varinha.
- Grimório e equipamentos secundários.

**Importante:** movimentos instantâneos de mira não devem ficar bloqueados por uma animação longa de rotação.

---

# 7. ANIMAÇÕES UNIVERSAIS DE CONJURAÇÃO

Além das habilidades específicas, criar animações reutilizáveis de magia.

## 08 — CAST QUICK (12 × 8 = 96 frames)

Conjuração rápida, ideal para ataques básicos.

### Estrutura

- Frames 1–3: preparação.
- Frames 4–6: concentração.
- Frames 7–8: liberação.
- Frames 9–12: recuperação.

O Mago ergue rapidamente o foco mágico ou a mão principal, executando um gesto curto e preciso.

**Função:** ataques rápidos de baixo tempo de conjuração.

## 09 — CAST STANDARD (20 × 8 = 160 frames)

Conjuração intermediária.

### Estrutura

- Frames 1–4: preparação.
- Frames 5–9: canalização.
- Frames 10–13: acúmulo.
- Frames 14–16: liberação.
- Frames 17–20: recuperação.

**Função:** magias ofensivas e utilitárias de duração média.

## 10 — CAST HEAVY (28 × 8 = 224 frames)

Conjuração poderosa.

### Estrutura

- Frames 1–5: preparação.
- Frames 6–12: canalização.
- Frames 13–18: intensificação.
- Frames 19–22: liberação.
- Frames 23–28: recuperação.

O corpo deve demonstrar concentração e esforço mágico.

**Função:** magias de grande impacto.

## 11 — CHANNEL START (12 × 8 = 96 frames)

Animação de início de canalização contínua.

O Mago posiciona os braços, concentra energia e estabelece o fluxo mágico.

## 12 — CHANNEL HOLD (16 × 8 = 128 frames)

Animação de sustentação.

- Braços em posição estável.
- Pequenas oscilações.
- Energia fluindo continuamente.
- Movimento secundário de vestimentas.
- Concentração expressiva.

**Loop:** perfeitamente contínuo.

## 13 — CHANNEL END (12 × 8 = 96 frames)

Encerramento da canalização.

- Redução gradual da energia.
- Relaxamento dos braços.
- Desaparecimento dos efeitos.
- Retorno à postura de combate.

A transição Channel Start → Channel Hold → Channel End deve ser perfeitamente fluida.

---

# 8. SISTEMA DE COMBO MÁGICO

Criar um combo principal de três conjurações rápidas.

O objetivo é proporcionar um ataque básico responsivo, com golpes visualmente distintos e transições naturais.

## 14 — COMBO 01: DISPARO ARCANO (14 × 8 = 112 frames)

Primeiro ataque.

O Mago ergue rapidamente uma mão ou o cajado e dispara um pequeno projétil arcano.

### Estrutura

- Frames 1–3: preparação.
- Frames 4–6: concentração.
- Frames 7–8: disparo.
- Frames 9–11: dissipação.
- Frames 12–14: recuperação parcial.

**Spawn do projétil:** frame 7.

O movimento deve ser rápido e preciso.

## 15 — COMBO 02: DUPLO PULSO ARCANO (16 × 8 = 128 frames)

Segundo ataque.

O Mago realiza um gesto lateral e libera dois pequenos pulsos de energia em sequência.

### Estrutura

- Frames 1–3: transição do movimento anterior.
- Frames 4–7: primeiro disparo.
- Frames 8–11: segundo disparo.
- Frames 12–14: dissipação.
- Frames 15–16: preparação para o terceiro ataque.

**Spawns:** frames 6 e 10.

Os projéteis devem possuir sprites próprios e trajetórias independentes.

## 16 — COMBO 03: RAJADA ARCANA (20 × 8 = 160 frames)

Terceiro e último ataque básico do combo.

O Mago concentra energia e lança um projétil maior, com impacto mais expressivo.

### Estrutura

- Frames 1–4: preparação.
- Frames 5–9: concentração.
- Frames 10–13: liberação.
- Frames 14–16: dissipação.
- Frames 17–20: recuperação.

**Spawn do projétil:** frame 11.

O ataque deve possuir maior impacto visual e sonoro que os dois anteriores.

### Regras do combo

- Combo 01 → Combo 02 → Combo 03.
- Os gestos devem conectar-se naturalmente.
- O personagem não pode reiniciar a postura entre cada conjuração.
- Permitir entrada antecipada do próximo ataque.
- A engine controla a janela de combo.
- Permitir cancelamento apropriado por esquiva.
- Manter cajado, varinha ou foco mágico sincronizados.
- Criar VFX próprios para cada etapa.
- O dano deve ser controlado pelo sistema de combate.
- Cada projétil deve possuir colisão independente.

---

# 9. HABILIDADES ESPECIAIS DO MAGO

## 17 — SKILL 01: BOLA DE FOGO (26 × 8 = 208 frames)

O Mago concentra energia ígnea e lança uma grande esfera de fogo contra o alvo.

### Estrutura

**Frames 1–5 — Preparação**

O Mago posiciona o cajado ou a mão principal em direção ao alvo.

**Frames 6–11 — Canalização**

Pequenas chamas começam a surgir próximas à extremidade do foco mágico.

**Frames 12–16 — Formação**

Uma bola de fogo cresce progressivamente.

**Frames 17–19 — Disparo**

O Mago realiza um gesto ofensivo e libera o projétil.

**Frames 20–23 — Dissipação**

A energia residual desaparece gradualmente.

**Frames 24–26 — Recuperação**

Retorna à postura de combate.

**Função:** dano elemental de fogo com explosão em pequena área.

**Spawn:** frame 18.

**Projétil próprio:** Fireball.

**VFX:** Fire Charge, Fire Trail e Fire Explosion.

---

## 18 — SKILL 02: LANÇA DE GELO (24 × 8 = 192 frames)

O Mago materializa uma lança cristalina de gelo e a dispara em alta velocidade.

### Estrutura

- Frames 1–4: preparação.
- Frames 5–9: concentração de energia gélida.
- Frames 10–14: formação da lança.
- Frames 15–17: disparo.
- Frames 18–21: dissipação.
- Frames 22–24: recuperação.

Durante a conjuração:

- Cristais de gelo surgem gradualmente.
- Pequenas partículas azul-claras flutuam.
- A lança apresenta núcleo cristalino.
- O Mago realiza um gesto preciso de lançamento.
- O projétil mantém orientação coerente com a trajetória.

**Função:** dano de gelo em linha, podendo reduzir a velocidade do alvo.

**Spawn:** frame 16.

**Projétil próprio:** Ice Spear.

---

## 19 — SKILL 03: NOVA GLACIAL (28 × 8 = 224 frames)

O Mago libera uma explosão circular de energia congelante ao redor do próprio corpo.

### Estrutura

- Frames 1–4: preparação.
- Frames 5–10: canalização.
- Frames 11–16: concentração de energia.
- Frames 17–20: explosão.
- Frames 21–25: dissipação.
- Frames 26–28: recuperação.

Durante a animação:

- O Mago posiciona os braços próximos ao torso.
- Pequenos cristais surgem ao seu redor.
- Uma aura azul-clara aumenta de intensidade.
- Os braços se abrem no momento da liberação.
- Uma onda circular de gelo se expande pelo chão.
- Pequenos cristais e partículas desaparecem progressivamente.

**Função:** dano em área e possível congelamento ou lentidão.

**Evento de ativação:** frame 18.

**VFX:** Frost Nova, Ice Shards e Frozen Ground.

---

## 20 — SKILL 04: CHUVA DE METEOROS (36 × 8 = 288 frames)

O Mago realiza uma conjuração avançada, invocando meteoros flamejantes sobre uma região selecionada.

### Estrutura

**Frames 1–5 — Preparação**

O Mago firma os pés e posiciona o cajado verticalmente.

**Frames 6–12 — Canalização**

Ergue a mão secundária e começa a concentrar energia de fogo.

**Frames 13–19 — Intensificação**

Um círculo mágico surge sobre a região selecionada enquanto partículas incandescentes se acumulam.

**Frames 20–24 — Conjuração**

O Mago ergue os braços e conclui o ritual.

**Frames 25–29 — Ativação**

Os meteoros começam a cair na área determinada.

**Frames 30–33 — Dissipação**

A energia ao redor do personagem diminui.

**Frames 34–36 — Recuperação**

Retorna à postura de combate.

**Função:** dano elevado em área durante múltiplos impactos.

**Ativação:** frame 25.

Os meteoros devem possuir spritesheets independentes, permitindo que vários sejam instanciados simultaneamente.

O círculo de aviso no chão deve aparecer antes dos impactos.

---

## 21 — SKILL 05: TELEPORTE ARCANO (24 × 8 = 192 frames)

O Mago desaparece em energia arcana e reaparece em uma posição próxima.

### Estrutura

- Frames 1–4: preparação.
- Frames 5–8: concentração de energia.
- Frames 9–12: dissolução corporal.
- Frames 13–15: desaparecimento.
- Frames 16–19: reaparecimento.
- Frames 20–22: reconstrução visual.
- Frames 23–24: recuperação.

### Características

- Partículas arcanas violetas.
- Pequenos símbolos luminosos.
- Dissolução progressiva.
- Ausência de movimento global dentro do sprite.
- Reconstrução coerente do corpo e equipamentos.
- Retorno à postura de combate.

**Função:** reposicionamento rápido e evasão.

**Importante:** todos os equipamentos devem desaparecer e reaparecer sincronizados com o corpo.

O destino e a colisão são controlados pela engine.

---

## 22 — SKILL 06: BARREIRA ARCANA (28 × 8 = 224 frames)

O Mago conjura um escudo mágico que absorve temporariamente parte do dano recebido.

### Estrutura

- Frames 1–4: preparação.
- Frames 5–9: canalização.
- Frames 10–14: formação da barreira.
- Frames 15–19: estabilização.
- Frames 20–24: ativação.
- Frames 25–28: retorno ao combate.

Durante a conjuração:

- O Mago aproxima as mãos.
- Pequenas runas surgem ao redor do corpo.
- Uma película translúcida de energia se forma.
- A barreira assume formato esférico ou oval.
- Runas circulam discretamente pela superfície.
- O personagem retorna à postura ofensiva.

**Função:** absorção temporária de dano.

### BARRIER HOLD

Criar VFX independente de 16 frames em loop.

A barreira deve continuar visível enquanto o Mago caminha, ataca ou utiliza outras habilidades.

Não substituir as animações corporais por uma pose fixa durante o efeito.

Criar também animações de impacto e destruição da barreira.

---

## 23 — SKILL 07: RAIO CANALIZADO (30 × 8 = 240 frames)

O Mago libera um feixe contínuo de energia arcana contra um alvo.

### Estrutura

- Frames 1–4: preparação.
- Frames 5–9: concentração.
- Frames 10–13: formação do feixe.
- Frames 14–21: canalização.
- Frames 22–25: redução da energia.
- Frames 26–30: recuperação.

### Características

- Feixe mágico contínuo.
- Núcleo luminoso.
- Partículas direcionais.
- Pequenos pulsos de energia.
- Movimento secundário do manto.
- Cajado ou mãos firmemente direcionados ao alvo.

**Função:** dano mágico contínuo enquanto a habilidade estiver ativa.

### BEAM HOLD — 16 frames × 8 direções

Criar um loop próprio para duração variável.

O personagem deve manter a pose de canalização enquanto o feixe permanece ativo.

A engine deve controlar a duração, o alvo e o dano periódico.

**Transição obrigatória:** Beam Start → Beam Hold → Beam End.

O feixe deve ser independente do personagem e ajustar-se dinamicamente à distância do alvo.

---

## 24 — SKILL 08: EXPLOSÃO ARCANA (30 × 8 = 240 frames)

Habilidade de alto impacto que libera uma explosão concentrada de energia arcana em uma área selecionada.

### Estrutura

**Frames 1–5 — Preparação**

O Mago ergue o foco mágico e concentra sua atenção na área de destino.

**Frames 6–11 — Canalização**

Pequenas runas violetas surgem ao redor das mãos.

**Frames 12–17 — Acúmulo**

A energia arcana se intensifica e começa a convergir para um núcleo luminoso.

**Frames 18–22 — Ativação**

O Mago realiza um gesto amplo, direcionando a energia à região selecionada.

**Frames 23–26 — Explosão**

O núcleo mágico detona, criando uma expansão de energia.

**Frames 27–30 — Recuperação**

O personagem abaixa os braços e retorna à postura de combate.

**Função:** dano arcano em área, com possível interrupção de inimigos.

**VFX:** Arcane Charge, Arcane Circle e Arcane Explosion.

A explosão deve ser uma entidade visual independente posicionada pela engine.

---

# 10. ANIMAÇÕES DE DANO E MORTE

## 25 — HURT (10 × 8 = 80 frames)

Criar uma reação rápida ao receber dano.

- Recuo do torso.
- Movimento involuntário dos braços.
- Oscilação do cajado.
- Expressão de dor.
- Recuperação natural.

O equipamento permanece visível durante todos os frames.

## 26 — STAGGER (16 × 8 = 128 frames)

Reação de atordoamento.

- Perda temporária de concentração.
- Desequilíbrio corporal.
- Braços afastando-se da postura de conjuração.
- Recuperação gradual.

Quando ocorrer durante uma canalização, o sistema deve interromper corretamente os efeitos mágicos associados.

## 27 — KNOCKDOWN (20 × 8 = 160 frames)

Queda completa do personagem.

- Impacto.
- Perda de equilíbrio.
- Queda.
- Contato com o solo.
- Estabilização.

## 28 — GET UP (20 × 8 = 160 frames)

Recuperação após queda.

- Apoio no chão.
- Elevação do torso.
- Recuperação das pernas.
- Retorno à postura de combate.

A pose inicial deve conectar-se ao estado final de Knockdown.

## 29 — DIED (28 × 8 = 224 frames)

Criar uma morte completa.

### Estrutura

- Frames 1–4: impacto fatal.
- Frames 5–8: perda de equilíbrio.
- Frames 9–14: queda.
- Frames 15–20: contato com o solo.
- Frames 21–26: estabilização.
- Frames 27–28: estado final imóvel.

O cajado, as vestimentas e os acessórios devem acompanhar naturalmente a queda.

**Sem loop.**

O corpo deve permanecer equipado após a morte.

---

# 11. PROJÉTEIS OBRIGATÓRIOS

Todos os projéteis devem ser entregues como spritesheets independentes.

## 01 — ARCANE BOLT

**Voo:** 12 frames em loop.  
**Impacto:** 8 frames.

Pequeno projétil violeta de energia arcana.

Utilizado nos ataques básicos.

## 02 — ARCANE DOUBLE PULSE

**Voo:** 12 frames em loop.  
**Impacto:** 8 frames.

Pulso arcano ligeiramente mais rápido e estreito.

Utilizado no segundo ataque do combo.

## 03 — ARCANE BURST

**Voo:** 14 frames em loop.  
**Impacto:** 12 frames.

Projétil arcano maior, utilizado como finalizador do combo.

## 04 — FIREBALL

**Voo:** 12 frames em loop.  
**Impacto:** 16 frames.

Bola de fogo com núcleo incandescente, bordas instáveis e rastro flamejante.

## 05 — ICE SPEAR

**Voo:** 12 frames em loop.  
**Impacto:** 12 frames.

Lança cristalina de gelo, com fragmentos e partículas gélidas.

## 06 — METEOR

**Queda:** 16 frames.  
**Impacto:** 20 frames.

Rocha flamejante envolvida por fogo e partículas incandescentes.

A engine controla a trajetória de queda e o posicionamento.

## 07 — ARCANE BEAM

**Loop:** 16 frames.

Feixe contínuo de energia arcana, preparado para ajuste dinâmico de comprimento.

## 08 — ARCANE EXPLOSION CORE

**Formação:** 12 frames.  
**Detonação:** 18 frames.

Núcleo mágico utilizado durante a Explosão Arcana.

### Regras dos projéteis

- Transparência verdadeira.
- Origem e ponto de ancoragem definidos.
- Trajetória independente do personagem.
- Colisão controlada pela engine.
- Variações direcionais quando necessárias.
- Não utilizar rotação com interpolação borrada.
- Manter aparência coerente em oito direções.
- Criar impactos específicos.
- Evitar vazamentos entre células.
- Permitir múltiplas instâncias simultâneas.

---

# 12. VFX OBRIGATÓRIOS

Produzir efeitos visuais separados do corpo e dos equipamentos.

### VFX 01 — ARCANE CAST (12 frames)

Energia arcana concentrando-se nas mãos ou no foco mágico.

### VFX 02 — ARCANE BOLT IMPACT (8 frames)

Impacto do projétil básico.

### VFX 03 — ARCANE COMBO FINISHER (12 frames)

Impacto energético do terceiro ataque.

### VFX 04 — FIRE CHARGE (12 frames)

Formação progressiva de energia ígnea.

### VFX 05 — FIREBALL TRAIL (12 frames em loop)

Rastro flamejante da Bola de Fogo.

### VFX 06 — FIRE EXPLOSION (16 frames)

Explosão ígnea ao atingir o alvo.

### VFX 07 — ICE CHARGE (12 frames)

Cristais e partículas de gelo surgindo durante a conjuração.

### VFX 08 — ICE SPEAR IMPACT (12 frames)

Fragmentação da lança de gelo.

### VFX 09 — FROST NOVA (18 frames)

Onda circular congelante.

### VFX 10 — FROZEN GROUND (12 frames em loop)

Área congelada temporária.

### VFX 11 — METEOR TELEGRAPH (16 frames)

Círculo de aviso no chão, indicando a área que será atingida.

### VFX 12 — METEOR TRAIL (16 frames)

Rastro flamejante durante a queda.

### VFX 13 — METEOR EXPLOSION (20 frames)

Grande impacto de fogo e fragmentos.

### VFX 14 — TELEPORT DISAPPEAR (14 frames)

Dissolução corporal em partículas arcanas.

### VFX 15 — TELEPORT APPEAR (14 frames)

Reconstrução visual no destino.

### VFX 16 — ARCANE BARRIER ACTIVATION (16 frames)

Formação da barreira.

### VFX 17 — ARCANE BARRIER HOLD (16 frames em loop)

Barreira translúcida com runas em movimento.

### VFX 18 — ARCANE BARRIER IMPACT (10 frames)

Reação visual ao absorver dano.

### VFX 19 — ARCANE BARRIER BREAK (14 frames)

Destruição da barreira em partículas mágicas.

### VFX 20 — ARCANE BEAM CHARGE (12 frames)

Preparação do raio canalizado.

### VFX 21 — ARCANE BEAM LOOP (16 frames em loop)

Feixe mágico contínuo.

### VFX 22 — ARCANE BEAM IMPACT (12 frames em loop)

Energia concentrada no ponto de contato com o alvo.

### VFX 23 — ARCANE EXPLOSION CHARGE (16 frames)

Acúmulo de energia antes da explosão.

### VFX 24 — ARCANE EXPLOSION (20 frames)

Detonação de energia arcana.

### VFX 25 — DODGE DUST (8 frames)

Poeira discreta durante esquiva.

### VFX 26 — LANDING IMPACT (8 frames)

Efeito de aterrissagem.

### VFX 27 — MAGIC INTERRUPT (10 frames)

Dissipação de uma conjuração interrompida.

### VFX 28 — DEATH DUST (10 frames)

Poeira discreta durante a queda final.

### Regras dos VFX

- Utilizar paletas distintas para fogo, gelo e arcano.
- Preservar a estética Pixel Art Chibi.
- Garantir transparência verdadeira.
- Respeitar perspectiva isométrica.
- Permitir posicionamento independente.
- Sincronizar efeitos com eventos de gameplay.
- Não ocultar excessivamente o personagem.
- Criar variantes direcionais quando necessárias.
- Utilizar sprites próprios para efeitos persistentes.
- Evitar interpolação borrada.
- Não permitir halos ou pixels residuais.

---

# 13. ESPECIFICAÇÃO TÉCNICA — FRAMES CORPORAIS

| Animação | Frames/direção | Direções | Total |
|---|---:|---:|---:|
| Idle | 16 | 8 | 128 |
| Magic Combat Idle | 20 | 8 | 160 |
| Walk | 16 | 8 | 128 |
| Run | 20 | 8 | 160 |
| Dodge | 16 | 8 | 128 |
| Jump | 18 | 8 | 144 |
| Turn | 8 | 16 transições | 128 |
| Cast Quick | 12 | 8 | 96 |
| Cast Standard | 20 | 8 | 160 |
| Cast Heavy | 28 | 8 | 224 |
| Channel Start | 12 | 8 | 96 |
| Channel Hold | 16 | 8 | 128 |
| Channel End | 12 | 8 | 96 |
| Combo 01 — Disparo Arcano | 14 | 8 | 112 |
| Combo 02 — Duplo Pulso | 16 | 8 | 128 |
| Combo 03 — Rajada Arcana | 20 | 8 | 160 |
| Skill 01 — Bola de Fogo | 26 | 8 | 208 |
| Skill 02 — Lança de Gelo | 24 | 8 | 192 |
| Skill 03 — Nova Glacial | 28 | 8 | 224 |
| Skill 04 — Chuva de Meteoros | 36 | 8 | 288 |
| Skill 05 — Teleporte Arcano | 24 | 8 | 192 |
| Skill 06 — Barreira Arcana | 28 | 8 | 224 |
| Skill 07 — Raio Canalizado | 30 | 8 | 240 |
| Skill 08 — Explosão Arcana | 30 | 8 | 240 |
| Beam Hold | 16 | 8 | 128 |
| Hurt | 10 | 8 | 80 |
| Stagger | 16 | 8 | 128 |
| Knockdown | 20 | 8 | 160 |
| Get Up | 20 | 8 | 160 |
| Died | 28 | 8 | 224 |
| **TOTAL PLANEJADO** | | | **5.104 frames** |

Os 5.104 frames representam as animações corporais planejadas, incluindo as transições Turn e o Beam Hold.

Animações de sustentação adicionais, transições específicas de equipamentos e variantes de empunhadura devem ser contabilizadas separadamente quando exigirem frames exclusivos.

Os VFX e projéteis não estão incluídos nesse total.

---

# 14. FPS RECOMENDADOS

- **Idle:** 10–12 FPS.
- **Magic Combat Idle:** 10–12 FPS.
- **Walk:** 12–16 FPS.
- **Run:** 16–20 FPS.
- **Dodge:** 18–24 FPS.
- **Jump:** 14–20 FPS.
- **Cast Quick:** 18–24 FPS.
- **Cast Standard:** 16–20 FPS.
- **Cast Heavy:** 16–20 FPS.
- **Channel Start:** 16–20 FPS.
- **Channel Hold:** 10–12 FPS.
- **Channel End:** 16–20 FPS.
- **Combos mágicos:** 18–24 FPS.
- **Skills:** 16–24 FPS.
- **Hurt:** 18–24 FPS.
- **Stagger:** 16–20 FPS.
- **Died:** 12–16 FPS.
- **Projéteis:** 18–24 FPS.
- **VFX:** 18–24 FPS.

A engine deve controlar a duração efetiva de cada animação conforme o gameplay.

**Regra:** mais frames devem proporcionar maior fluidez, não necessariamente animações mais lentas.

---

# 15. REGRAS OBRIGATÓRIAS DO SISTEMA MODULAR

## 15.1 Sincronização corporal

Todas as camadas visuais devem utilizar:

- Mesmo identificador de animação.
- Mesma direção.
- Mesmo índice de frame.
- Mesma referência temporal.
- Mesmo sistema de ancoragem.
- Mesma pose corporal.

Os equipamentos devem acompanhar exatamente os movimentos do corpo-base.

## 15.2 Sincronização dos focos mágicos

Cada foco deve possuir:

- Ponto de empunhadura.
- Ponto de emissão de magia.
- Ponto de conexão com a mão.
- Orientação por frame.
- Profundidade de renderização.
- Compatibilidade com o perfil de arma.

**Exemplo:** ao equipar um cajado longo, a Bola de Fogo deve surgir na extremidade de seu cristal. Ao equipar uma varinha, a Bola de Fogo deve surgir na ponta da varinha.

Se o jogador estiver desarmado, a magia poderá surgir na palma da mão.

## 15.3 Túnicas e mantos

Vestimentas longas precisam acompanhar:

- Movimentos das pernas.
- Caminhada e corrida.
- Esquiva.
- Saltos.
- Conjurações.
- Quedas.
- Morte.

As partes inferiores das túnicas não devem atravessar as pernas ou permanecer imóveis durante a movimentação.

Utilizar subdivisão das camadas quando necessário.

## 15.4 Capuzes e chapéus

- Devem acompanhar a cabeça.
- Não podem flutuar ou deslocar-se entre frames.
- Devem ocultar corretamente partes do cabelo.
- Devem preservar volume e perspectiva.
- Não podem alterar involuntariamente o tamanho da cabeça.

## 15.5 Equipamentos durante habilidades

Durante qualquer habilidade:

- Cajados permanecem equipados.
- Varinhas acompanham a mão.
- Grimórios acompanham a postura.
- Túnicas mantêm sua aparência.
- Capas continuam visíveis.
- Auras são aplicadas como camadas independentes.
- Nenhum equipamento desaparece.
- Nenhum equipamento é substituído por um modelo genérico.

## 15.6 Compatibilidade com futuras classes

A arquitetura deve permitir reutilização dos equipamentos entre classes compatíveis.

Por exemplo:

- Um chapéu simples pode ser utilizado por Mago e Espadachim.
- Uma túnica pode ser utilizada por diferentes classes.
- Botas e luvas podem compartilhar o mesmo sistema.
- Cajados podem ser utilizados por outras classes mágicas.

As diferenças devem ser controladas por compatibilidade de equipamentos, perfis de empunhadura e animações específicas.

---

# 16. MÁQUINA DE ESTADOS DE ANIMAÇÃO

Criar estados preparados para integração com gameplay real.

## Movimentação

Idle ↔ Walk ↔ Run

## Combate mágico

Magic Combat Idle → Combo 01 → Combo 02 → Combo 03 → Magic Combat Idle

## Conjuração

Magic Combat Idle → Cast Start → Cast Release → Cast Recovery → Magic Combat Idle

## Canalização

Channel Start → Channel Hold → Channel End

## Habilidades

Magic Combat Idle / Walk → Skill → Recovery → Magic Combat Idle / Walk

## Teleporte

Teleport Start → Disappear → Reposition → Appear → Recovery

## Dano

Qualquer estado interrompível → Hurt / Stagger → Recovery

## Queda

Knockdown → Grounded → Get Up → Magic Combat Idle

## Morte

Died → Cadáver

### Regras de interrupção

- Conjurações rápidas podem permitir cancelamento após liberação.
- Conjurações pesadas podem possuir recuperação maior.
- Canalizações devem permitir interrupção por dano ou comando do jogador, conforme o gameplay.
- Teleporte deve respeitar eventos de desaparecimento e reaparecimento.
- Dodge deve utilizar janelas de invulnerabilidade definidas pela engine.
- Combos devem aceitar entrada antecipada.
- Projéteis já disparados não devem desaparecer automaticamente quando a animação do personagem terminar.
- Equipamentos devem permanecer sincronizados durante qualquer transição.

---

# 17. ORGANIZAÇÃO DOS ARQUIVOS

Entregar estrutura modular:

```text
characters/
└── mage/
    ├── body/
    │   ├── idle.png
    │   ├── combat_idle.png
    │   ├── walk.png
    │   ├── run.png
    │   ├── dodge.png
    │   ├── jump.png
    │   ├── turn.png
    │   ├── cast_quick.png
    │   ├── cast_standard.png
    │   ├── cast_heavy.png
    │   ├── channel_start.png
    │   ├── channel_hold.png
    │   ├── channel_end.png
    │   ├── combo_01.png
    │   ├── combo_02.png
    │   ├── combo_03.png
    │   ├── skill_fireball.png
    │   ├── skill_ice_spear.png
    │   ├── skill_frost_nova.png
    │   ├── skill_meteor.png
    │   ├── skill_teleport.png
    │   ├── skill_barrier.png
    │   ├── skill_arcane_beam.png
    │   ├── skill_arcane_explosion.png
    │   ├── beam_hold.png
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
    │   │   ├── staves/
    │   │   └── wands/
    │   ├── off_hand/
    │   │   ├── grimoires/
    │   │   └── orbs/
    │   └── accessories/
    │
    ├── projectiles/
    │   ├── arcane/
    │   ├── fire/
    │   └── ice/
    │
    ├── vfx/
    │   ├── casting/
    │   ├── arcane/
    │   ├── fire/
    │   ├── ice/
    │   ├── teleport/
    │   ├── barrier/
    │   └── impacts/
    │
    ├── metadata/
    │   ├── animations.json
    │   ├── equipment_slots.json
    │   ├── attachment_points.json
    │   ├── weapon_profiles.json
    │   ├── hitboxes.json
    │   ├── projectiles.json
    │   ├── skills.json
    │   └── state_machine.json
    │
    └── previews/
        ├── idle.gif
        ├── walk.gif
        ├── run.gif
        ├── casting.gif
        ├── combos.gif
        ├── skills.gif
        └── equipment_test.gif
```

Cada spritesheet corporal deve utilizar oito linhas direcionais na ordem:

**N, NE, E, SE, S, SW, W, NW.**

Para animações de Turn, utilizar estrutura própria com direção de origem e destino.

Se o arquivo exceder limites práticos de textura, dividir a spritesheet em arquivos menores sem alterar os metadados.

---

# 18. METADADOS OBRIGATÓRIOS

Criar arquivos JSON contendo:

- Identificador da classe.
- Identificador do corpo-base.
- Direções disponíveis.
- Nomes das animações.
- Quantidade exata de frames.
- FPS.
- Coordenadas de recorte.
- Dimensões das células.
- Origem e ponto de ancoragem.
- Pontos de encaixe dos equipamentos.
- Posição das mãos.
- Posição da ponta do cajado.
- Posição da ponta da varinha.
- Posição e orientação do grimório.
- Pontos de emissão de magia.
- Ordem de renderização por frame.
- Máscaras de ocultação.
- Hitboxes e hurtboxes.
- Eventos de conjuração.
- Eventos de spawn dos projéteis.
- Eventos de impacto.
- Eventos de ativação das habilidades.
- Eventos de aplicação de efeitos negativos.
- Janelas de combo.
- Janelas de cancelamento.
- Janelas de invulnerabilidade.
- Estados de canalização.
- Eventos de início e término de feixes.
- Eventos de teleporte.
- Estados de barreira.
- Estados de morte.
- Compatibilidade de armas e equipamentos.
- Referências aos VFX.
- Transições permitidas.

Os eventos devem ser sincronizados com os frames efetivamente entregues.

---

# 19. REGRAS OBRIGATÓRIAS DE FLUIDEZ

- Produzir oito direções completas.
- Preservar proporções chibi.
- Manter anatomia constante.
- Não deformar mãos, braços, pernas ou rosto.
- Garantir que os gestos mágicos sejam naturais.
- Manter movimentos coordenados de ombros e tronco.
- Preservar escala em todas as orientações.
- Evitar tremores e deslocamentos involuntários.
- Não utilizar interpolação borrada.
- Manter contato correto dos pés com o chão.
- Garantir loops perfeitos de Idle, Walk, Run e Channel Hold.
- Criar transições suaves entre conjurações.
- Garantir que o último frame de uma conjuração seja compatível com a recuperação.
- Preservar equipamentos durante todas as animações.
- Animar mantos e túnicas com movimentos secundários coerentes.
- Garantir que cajados e varinhas não atravessem incorretamente o corpo.
- Manter VFX separados do corpo.
- Sincronizar os projéteis com os frames de lançamento.
- Permitir múltiplos projéteis simultâneos.
- Manter efeitos persistentes independentes das animações corporais.
- Garantir que a barreira continue visível durante movimentação.
- Preservar todos os equipamentos durante teleporte.
- Utilizar fundo transparente verdadeiro.
- Não permitir bordas, halos, pixels soltos ou vazamentos entre células.
- Reservar espaço suficiente para gestos amplos.
- Manter recortes consistentes.
- Garantir leitura visual clara em escala de gameplay.
- Validar todas as oito direções individualmente.

---

# 20. VALIDAÇÃO OBRIGATÓRIA

Antes de considerar o conjunto concluído:

1. Reproduzir Idle e Magic Combat Idle por cinco ciclos em cada direção.
2. Validar Walk e Run, verificando contato dos pés.
3. Testar mudanças rápidas entre oito direções.
4. Verificar Dodge e Jump.
5. Testar Cast Quick, Cast Standard e Cast Heavy.
6. Confirmar continuidade de Channel Start → Hold → End.
7. Reproduzir o combo mágico completo.
8. Verificar os três tipos de projéteis do combo.
9. Testar Bola de Fogo e seu impacto.
10. Validar Lança de Gelo e fragmentação.
11. Testar Nova Glacial e efeito de área.
12. Validar Chuva de Meteoros com múltiplos impactos.
13. Testar Teleporte com equipamentos completos.
14. Confirmar que todas as camadas desaparecem e reaparecem sincronizadas.
15. Testar Barreira Arcana durante Walk, Run e Attack.
16. Validar Raio Canalizado e seu loop de sustentação.
17. Testar Explosão Arcana.
18. Verificar interrupção de conjurações por Hurt.
19. Reproduzir Stagger, Knockdown e Get Up.
20. Validar Died nas oito direções.
21. Testar corpo-base sem equipamentos.
22. Testar personagem com túnica completa.
23. Equipar diferentes cajados e validar os pontos de emissão.
24. Substituir cajado por varinha.
25. Equipar grimório e validar a postura secundária.
26. Testar diferentes chapéus e capuzes.
27. Validar o movimento das capas.
28. Confirmar que botas acompanham os pés.
29. Verificar sobreposição correta de camadas.
30. Inspecionar recortes, transparência e bordas.
31. Eliminar tremores e deformações.
32. Validar desempenho com múltiplos jogadores e efeitos simultâneos.
33. Confirmar correspondência exata entre frames, JSON e eventos de gameplay.

---

# 21. CRITÉRIOS TÉCNICOS DE ENTREGA

A geração deve produzir **spritesheets funcionais**, não apenas folhas ilustrativas.

Cada frame deve:

- Possuir ordem cronológica correta.
- Respeitar a grade de recorte.
- Possuir transparência verdadeira.
- Preservar identidade visual.
- Manter anatomia consistente.
- Utilizar o mesmo sistema de ancoragem.
- Permitir reprodução individual.
- Manter sincronização com equipamentos.
- Não apresentar membros duplicados ou ausentes.
- Não apresentar vazamento de pixels de células vizinhas.

Os VFX e projéteis devem ser entregues em arquivos independentes.

Os arquivos JSON devem corresponder às animações reais.

Os GIFs de prévia devem ser gerados a partir dos mesmos frames utilizados no jogo.

Nenhuma animação deve ser considerada validada sem reprodução e inspeção efetivas.

---

# 22. RESULTADO ESPERADO

Entregar uma classe **Mago completamente modular e pronta para integração em um MMORPG 2D isométrico**, contendo:

### Personagem-base

- Corpo chibi com roupas íntimas simples.
- Oito direções completas.
- Aparência independente dos equipamentos.
- Compatibilidade com o corpo-base universal.
- Animações corporais completas.

### Movimentação

- Idle.
- Magic Combat Idle.
- Walk.
- Run.
- Dodge.
- Jump.
- Turn.

### Combate mágico

- Cast Quick.
- Cast Standard.
- Cast Heavy.
- Channel Start.
- Channel Hold.
- Channel End.
- Combo mágico de três ataques.

### Habilidades

- Bola de Fogo.
- Lança de Gelo.
- Nova Glacial.
- Chuva de Meteoros.
- Teleporte Arcano.
- Barreira Arcana.
- Raio Canalizado.
- Explosão Arcana.

### Estados

- Hurt.
- Stagger.
- Knockdown.
- Get Up.
- Died.

### Sistema visual

- Cajados substituíveis.
- Varinhas substituíveis.
- Grimórios e orbes equipáveis.
- Túnicas e mantos animados.
- Chapéus, capuzes e capacetes.
- Luvas, botas e acessórios.
- Equipamentos modulares visíveis.
- Pontos de encaixe por frame.
- Máscaras de ocultação.
- Ordenação de camadas.
- Projéteis elementais próprios.
- VFX exclusivos.
- Canalizações contínuas.
- Efeitos persistentes independentes.

**TOTAL PLANEJADO: 5.104 frames corporais-base em oito direções e transições de rotação, além das variações de equipamento, projéteis, VFX e metadados.**

O Mago deve transmitir **inteligência, concentração, fragilidade física relativa, mobilidade arcana e domínio crescente dos elementos**, evoluindo visualmente de um aventureiro sem equipamentos para um arquimago completamente equipado.

## PRIORIDADES ABSOLUTAS

1. Oito direções completas e consistentes.
2. Fluidez excepcional das animações.
3. Corpo-base universal sem equipamentos fixos.
4. Sistema modular com aparência determinada pelos itens equipados.
5. Gestos de conjuração naturais e expressivos.
6. Combos mágicos encadeados.
7. Habilidades elementais visualmente distintas.
8. Projéteis e VFX independentes.
9. Canalizações e efeitos persistentes funcionais.
10. Recortes perfeitos, sem tremores ou bordas.
11. Sincronização precisa de equipamentos e efeitos.
12. Compatibilidade com novas armas, armaduras e habilidades.

**REGRA FINAL:** o Mago deve utilizar a mesma arquitetura modular do Espadachim, permitindo que equipamentos compatíveis sejam compartilhados entre classes, enquanto suas animações de combate, conjurações e habilidades preservam uma identidade própria.

O resultado deve oferecer a fluidez, a personalização visual, a riqueza de efeitos e a consistência esperadas de uma classe jogável de um MMORPG isométrico profissional.