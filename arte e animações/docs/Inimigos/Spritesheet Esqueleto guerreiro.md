# INIMIGO ESQUELETO GUERREIRO — SPRITESHEET COMPLETA EM 8 DIREÇÕES

Crie um conjunto completo de spritesheets para um **Esqueleto Guerreiro de RPG 2D isométrico, inspirado em Diablo II, com estética Pixel Art Chibi e fantasia medieval sombria**.

O Esqueleto Guerreiro deve ser um inimigo morto-vivo de porte médio, com aparência ameaçadora, movimentos rígidos porém fluidos e comportamento agressivo. Sua animação deve transmitir a sensação de uma criatura reanimada por magia necromântica, que continua lutando mesmo após a morte.

Apesar da estética chibi, o personagem deve apresentar anatomia esquelética bem definida, movimentos convincentes e uma silhueta facilmente reconhecível durante o combate.

Seu visual deve incluir:

- Crânio proporcionalmente grande, característico da estética chibi.
- Órbitas oculares profundas com pequenos brilhos de energia necromântica azulada ou verde-espectral.
- Mandíbula articulada, com movimentos ocasionais.
- Caixa torácica e coluna vertebral visíveis.
- Braços e pernas compostos por ossos articulados.
- Armadura medieval antiga, enferrujada e parcialmente destruída.
- Ombreiras assimétricas e pequenos pedaços de tecido rasgado.
- Espada curta ou espada medieval enferrujada na mão direita.
- Escudo de madeira deteriorado, reforçado com metal, na mão esquerda.
- Pequenas rachaduras e marcas de desgaste nos ossos.
- Fragmentos de energia necromântica discretamente visíveis nas articulações.

**O objetivo é produzir animações extremamente fluidas, expressivas e prontas para gameplay real**, mantendo a personalidade de um guerreiro morto-vivo: movimentos deliberados, ataques agressivos, postura defensiva e reações físicas coerentes com um corpo esquelético.

---

## 1. SISTEMA DE 8 DIREÇÕES

Produzir todas as animações corporais individualmente nas seguintes direções:

1. Norte (N) — Costas.
2. Nordeste (NE) — Diagonal superior direita.
3. Leste (E) — Lateral direita.
4. Sudeste (SE) — Diagonal inferior direita.
5. Sul (S) — Frente.
6. Sudoeste (SW) — Diagonal inferior esquerda.
7. Oeste (W) — Lateral esquerda.
8. Noroeste (NW) — Diagonal superior esquerda.

**Obrigatório:** cada direção deve possuir sprites próprios, respeitando perspectiva, anatomia esquelética, profundidade isométrica e posicionamento consistente da espada e do escudo.

A espada deve permanecer sempre na mão direita anatômica, e o escudo na mão esquerda anatômica, independentemente da direção.

Não utilizar espelhamento automático quando isso inverter os equipamentos, alterar detalhes assimétricos da armadura ou comprometer a iluminação.

---

## 2. CONCEITO DE COMBATE

**Tipo:** inimigo morto-vivo corpo a corpo, com capacidades ofensivas e defensivas.

**Função:** pressionar jogadores em curta distância, bloquear ataques e realizar golpes com espada.

**Comportamento:** persistente, agressivo, implacável e pouco inteligente.

**Ataque básico:** golpe horizontal ou diagonal com espada enferrujada.

**Skill 01:** Golpe Espectral — ataque pesado de espada potencializado por energia necromântica.

**Skill 02:** Defesa Óssea — postura defensiva com escudo, reduzindo temporariamente o dano frontal recebido.

**Diferencial:** movimentos de articulações esqueléticas, armadura desgastada, escudo funcional e energia necromântica sutil.

**Projéteis:** não utiliza projéteis convencionais. Suas habilidades são corpo a corpo e defensivas.

---

## 3. ANIMAÇÕES OBRIGATÓRIAS

### 01 — IDLE (16 frames × 8 direções = 128 frames)

O Esqueleto Guerreiro permanece em posição de combate, segurando a espada na mão direita e o escudo na esquerda.

Sua postura deve parecer artificialmente sustentada por magia necromântica, mas sem apresentar tremores visuais ou movimentos robóticos.

Durante o Idle:

- O tronco realiza oscilações muito discretas, simulando a instabilidade de um corpo reanimado.
- O crânio inclina levemente para os lados, como se procurasse inimigos.
- A mandíbula abre e fecha ocasionalmente.
- Os ombros apresentam pequenos movimentos de ajuste.
- A espada oscila discretamente acompanhando o braço.
- O escudo permanece próximo ao torso, realizando pequenos ajustes defensivos.
- Os tecidos rasgados e acessórios acompanham suavemente o movimento.
- Os olhos espectrais apresentam uma pulsação luminosa muito sutil.
- As articulações mantêm conexão anatômica correta.

O Esqueleto não deve apresentar respiração pulmonar, pois é uma criatura sem órgãos vivos.

**Loop:** perfeitamente contínuo. O último frame deve retornar naturalmente à posição inicial, mantendo a mesma postura de combate.

### 02 — WALK (16 frames × 8 direções = 128 frames)

Criar uma caminhada característica de um guerreiro morto-vivo, com passos firmes, levemente rígidos e ameaçadores.

Durante o Walk:

- As pernas executam um ciclo completo de passos alternados.
- Os joelhos flexionam de maneira coerente com a anatomia óssea.
- O tronco apresenta pequenas oscilações verticais.
- A espada acompanha discretamente o balanço do braço.
- O escudo permanece à frente ou ao lado do torso, indicando prontidão defensiva.
- A cabeça mantém o olhar direcionado ao avanço.
- As articulações dos tornozelos e quadris realizam movimentos completos.
- Pequenos fragmentos de tecido acompanham o deslocamento.
- A armadura pode apresentar movimentos secundários discretos.

A caminhada deve transmitir a sensação de um soldado morto-vivo que continua avançando de maneira obstinada.

Não utilizar movimentos excessivamente lentos ou travados. A rigidez deve ser uma característica da atuação, não uma falha na animação.

**Regra fundamental:** os pés devem manter contato convincente com o chão durante a fase de apoio, sem deslizar.

**Loop:** perfeito, com continuidade natural entre as passadas.

### 03 — ATTACK: CORTE DE ESPADA (16 frames × 8 direções = 128 frames)

Criar um ataque básico corpo a corpo com espada enferrujada.

O golpe deve apresentar antecipação, aceleração, contato e recuperação.

**Estrutura da animação:**

- **Frames 1–4 — Antecipação:** o Esqueleto gira levemente o tronco e recua o braço armado, posicionando a espada para o golpe.
- **Frames 5–7 — Preparação:** amplia a rotação do ombro, posiciona o escudo defensivamente e concentra o peso corporal.
- **Frames 8–10 — Execução:** realiza um corte diagonal agressivo em direção ao alvo.
- **Frames 11–12 — Finalização:** a espada completa seu arco e o tronco acompanha a força do movimento.
- **Frames 13–16 — Recuperação:** retorna gradualmente à postura de combate, com escudo e espada nas posições iniciais.

O movimento deve transmitir a força de um guerreiro treinado, mesmo que sua execução seja ligeiramente imperfeita devido à condição de morto-vivo.

**Função visual:** ataque básico principal.

**Transição:** Idle/Walk → Attack → Idle/Walk, sem saltos bruscos na posição da espada, escudo ou articulações.

### 04 — HURT (10 frames × 8 direções = 80 frames)

Criar uma reação clara ao receber dano.

Como o personagem é um esqueleto, a reação deve ser baseada no impacto físico sobre ossos e armadura, sem movimentos musculares exagerados.

Durante o Hurt:

- O tronco recua em resposta ao golpe.
- O crânio inclina abruptamente para trás ou para o lado.
- A mandíbula abre momentaneamente.
- O escudo perde discretamente sua posição defensiva.
- A espada oscila acompanhando o impacto.
- As articulações apresentam pequena desestabilização.
- Partículas ósseas podem se desprender durante impactos mais fortes.

**Estrutura:**

- Frames 1–2: impacto inicial.
- Frames 3–5: recuo corporal e perda momentânea de equilíbrio.
- Frames 6–8: recuperação das articulações e da postura.
- Frames 9–10: retorno à posição de combate.

**Função visual:** feedback de dano recebido.

A reação deve ser expressiva, mas suficientemente curta para preservar o ritmo do combate.

### 05 — DIED: COLAPSO ÓSSEO (24 frames × 8 direções = 192 frames)

Criar uma animação de morte em que a energia necromântica responsável pela reanimação desaparece, provocando o colapso do esqueleto.

**Estrutura:**

- **Frames 1–4 — Impacto fatal:** o Esqueleto recebe o golpe final e perde parcialmente o equilíbrio.
- **Frames 5–8 — Dissipação mágica:** o brilho dos olhos começa a desaparecer e pequenos fragmentos de energia espectral se desprendem do corpo.
- **Frames 9–12 — Falha estrutural:** a coluna, joelhos e braços começam a ceder, enquanto a espada e o escudo perdem sustentação.
- **Frames 13–16 — Desmoronamento:** o corpo colapsa progressivamente, com ossos e peças de armadura caindo em sequência.
- **Frames 17–20 — Queda final:** o crânio, a caixa torácica e os membros se acomodam no chão, formando uma pilha de ossos.
- **Frames 21–23 — Estabilização:** pequenos ossos e fragmentos concluem seus movimentos residuais.
- **Frame 24 — Cadáver final:** pilha de ossos completamente imóvel, com espada e escudo caídos próximos ao corpo.

A morte deve transmitir claramente a perda da força sobrenatural que mantinha o guerreiro de pé.

O crânio deve permanecer reconhecível, e os ossos não podem desaparecer ou se multiplicar arbitrariamente.

**Sem loop.** O último frame permanece visível até a remoção do cadáver.

### 06 — SKILL 01: GOLPE ESPECTRAL (20 frames × 8 direções = 160 frames)

O Esqueleto Guerreiro concentra energia necromântica em sua espada e executa um golpe pesado com alcance ligeiramente superior ao ataque básico.

**Estrutura:**

- **Frames 1–4 — Preparação:** posiciona os pés firmemente no chão, recua a espada e inclina o tronco.
- **Frames 5–8 — Canalização:** energia espectral azul-esverdeada começa a envolver a lâmina e as articulações do braço armado.
- **Frames 9–12 — Acúmulo:** a energia se intensifica, enquanto o Esqueleto ergue a espada acima do ombro.
- **Frames 13–15 — Golpe:** executa um corte poderoso, liberando um arco curto de energia necromântica.
- **Frames 16–18 — Dissipação:** a energia desaparece progressivamente e o movimento da espada perde velocidade.
- **Frames 19–20 — Recuperação:** retorna à postura de combate.

O golpe deve possuir uma sensação de impacto superior ao ataque básico, com antecipação bem definida.

**Função visual:** ataque especial corpo a corpo com dano ampliado.

O arco espectral é um VFX de curto alcance, não um projétil viajante independente.

### 07 — SKILL 02: DEFESA ÓSSEA (18 frames × 8 direções = 144 frames)

O Esqueleto Guerreiro assume uma postura defensiva reforçada por energia necromântica.

**Estrutura:**

- **Frames 1–4 — Preparação:** flexiona os joelhos e aproxima o escudo do centro do corpo.
- **Frames 5–8 — Elevação:** ergue o escudo à frente do torso, protegendo a cabeça e o peito.
- **Frames 9–12 — Ativação:** pequenas runas espectrais aparecem no escudo e uma aura discreta envolve suas bordas.
- **Frames 13–15 — Estabilização:** assume postura defensiva firme.
- **Frames 16–18 — Recuperação:** quando a defesa termina, abaixa suavemente o escudo e retorna à posição de combate.

**Função visual:** habilidade defensiva que reduz temporariamente dano frontal.

Para permitir bloqueios com duração variável, criar adicionalmente:

**DEFENSE HOLD — 8 frames × 8 direções = 64 frames**

Um loop curto de sustentação defensiva, com o escudo erguido e pequenas pulsações espectrais.

A habilidade deve funcionar em três etapas: ativação → sustentação defensiva → encerramento.

O sistema de gameplay controla a duração da defesa.

---

## 4. PROJÉTEIS

**Não aplicável ao Esqueleto Guerreiro base.**

Este inimigo utiliza espada, escudo e habilidades de curta distância.

Não criar projéteis artificiais apenas para preencher a spritesheet.

O arco produzido pelo Golpe Espectral deve ser tratado como VFX associado ao ataque.

Variantes futuras, como Esqueleto Arqueiro ou Esqueleto Mago, poderão possuir projéteis específicos.

---

## 5. VFX OBRIGATÓRIOS

Produzir spritesheets independentes para cada efeito visual, mantendo a estética Pixel Art Chibi.

### VFX 01 — SWORD SLASH (8 frames)

Arco de corte físico associado ao ataque básico.

- Movimento rápido e direcional.
- Pequeno rastro metálico.
- Desaparecimento gradual.
- Sincronização com os frames de impacto da espada.

### VFX 02 — BONE HIT IMPACT (6 frames)

Efeito de impacto físico contra ossos e armadura.

- Pequenos fragmentos ósseos.
- Poeira discreta.
- Estalo visual de curta duração.
- Sem sangue ou efeitos orgânicos incompatíveis com um esqueleto.

### VFX 03 — NECROMANTIC CHARGE (10 frames)

Energia espectral envolvendo a espada durante a preparação do Golpe Espectral.

- Brilho azul-esverdeado.
- Pequenas partículas sobrenaturais.
- Concentração progressiva na lâmina.
- Pulsação energética discreta.

### VFX 04 — SPECTRAL SLASH (12 frames)

Arco espectral produzido pelo Golpe Espectral.

- Corte de energia de curto alcance.
- Formato curvo acompanhando a trajetória da espada.
- Núcleo luminoso e bordas translúcidas.
- Dissipação rápida após o impacto.

### VFX 05 — BONE SHIELD AURA (8 frames em loop)

Aura defensiva associada à Defesa Óssea.

- Pequenas runas flutuantes.
- Energia necromântica ao redor do escudo.
- Pulsação luminosa.
- Movimento contínuo e discreto.

### VFX 06 — BLOCK IMPACT (6 frames)

Efeito exibido quando um ataque é bloqueado pelo escudo.

- Faíscas pequenas.
- Impacto metálico.
- Breve pulso espectral.
- Desaparecimento rápido.

### VFX 07 — NECROMANTIC DEATH (12 frames)

Dissipação da energia necromântica durante a morte.

- Brilho dos olhos desaparecendo.
- Pequenas partículas espectrais.
- Energia escapando das articulações.
- Dissipação gradual ao redor da pilha de ossos.

### VFX 08 — BONE DUST (8 frames)

Poeira e pequenos fragmentos durante o colapso final.

Os VFX direcionais devem possuir oito orientações quando necessário. Efeitos simétricos podem compartilhar frames quando isso não comprometer a perspectiva.

---

## 6. ESPECIFICAÇÕES TÉCNICAS

| Animação | Frames/direção | Direções | Total |
|---|---:|---:|---:|
| Idle | 16 | 8 | 128 |
| Walk | 16 | 8 | 128 |
| Attack — Espada | 16 | 8 | 128 |
| Hurt | 10 | 8 | 80 |
| Died | 24 | 8 | 192 |
| Skill 01 — Golpe Espectral | 20 | 8 | 160 |
| Skill 02 — Defesa Óssea | 18 | 8 | 144 |
| Defense Hold | 8 | 8 | 64 |
| **TOTAL** | | | **1.024 frames** |

Os VFX devem ser produzidos em arquivos separados, com 70 frames-base antes de considerar variantes direcionais.

**Total do personagem: 1.024 frames em oito direções.**

---

## 7. FPS RECOMENDADOS

- **Idle:** 10–12 FPS.
- **Walk:** 12–16 FPS.
- **Attack:** 16–20 FPS.
- **Hurt:** 16–20 FPS.
- **Died:** 12–16 FPS.
- **Golpe Espectral:** 16–20 FPS.
- **Defesa Óssea:** 16–20 FPS.
- **Defense Hold:** 8–12 FPS.
- **VFX:** 16–24 FPS.

A engine poderá ajustar a velocidade de reprodução, respeitando a duração dos ataques e os eventos de gameplay.

---

## 8. REGRAS OBRIGATÓRIAS DE FLUIDEZ

- Produzir sprites próprios para as oito direções.
- Preservar rigorosamente a anatomia esquelética.
- Manter crânio, caixa torácica, coluna, braços e pernas com proporções constantes.
- Não criar, remover ou duplicar ossos entre frames, exceto durante o colapso intencional da morte.
- Manter a espada na mão direita e o escudo na mão esquerda.
- Preservar os detalhes assimétricos da armadura em todas as direções.
- Garantir continuidade dos movimentos da espada e do escudo.
- Utilizar movimentos rígidos de maneira intencional, sem comprometer a fluidez.
- Manter contato correto dos pés com o chão.
- Evitar deslizamento dos pés durante a caminhada.
- Manter ponto de ancoragem consistente no chão.
- Evitar tremores, deformações, teleportes e alterações repentinas de escala.
- Preservar a perspectiva isométrica em todos os movimentos.
- Garantir transições naturais entre Idle, Walk, Attack, Hurt e Skills.
- Idle, Walk e Defense Hold devem possuir loops perfeitamente contínuos.
- Attack e Skills devem terminar em poses compatíveis com a postura de combate.
- Hurt deve permitir retorno natural ao Idle ou Walk.
- A morte deve terminar em um estado estático de cadáver.
- Nenhum osso, arma ou acessório pode atravessar visualmente outros elementos de maneira incorreta.
- Manter consistência na iluminação, paleta e contornos.
- Não utilizar interpolação borrada que descaracterize a pixel art.
- Usar fundo transparente verdadeiro.
- Não permitir bordas, halos, pixels residuais ou vazamentos entre células.
- Reservar espaço suficiente para os movimentos completos da espada, escudo e efeitos visuais.
- Preservar dimensões uniformes e coordenadas de recorte consistentes.
- Garantir legibilidade durante combates com múltiplos inimigos simultâneos.

---

## 9. ORGANIZAÇÃO DOS ARQUIVOS

Entregar arquivos independentes:

- `skeleton_warrior_idle.png`
- `skeleton_warrior_walk.png`
- `skeleton_warrior_attack.png`
- `skeleton_warrior_hurt.png`
- `skeleton_warrior_died.png`
- `skeleton_warrior_skill_spectral_slash.png`
- `skeleton_warrior_skill_bone_defense.png`
- `skeleton_warrior_defense_hold.png`
- `skeleton_warrior_vfx_slash.png`
- `skeleton_warrior_vfx_bone_hit.png`
- `skeleton_warrior_vfx_necromancy.png`
- `skeleton_warrior_vfx_shield.png`
- `skeleton_warrior_vfx_death.png`
- `skeleton_warrior_animations.json`

Cada spritesheet principal deve possuir **8 linhas direcionais**, nesta ordem:

N, NE, E, SE, S, SW, W, NW.

Os frames devem estar organizados horizontalmente em sequência cronológica.

Todas as spritesheets devem preservar escala, identidade visual, dimensões de célula e sistema de ancoragem compatíveis.

### O arquivo JSON deve conter:

- Identificador do inimigo.
- Nomes das animações e direções.
- Quantidade exata de frames.
- Coordenadas de recorte e dimensões das células.
- FPS de reprodução.
- Configurações de loop.
- Ponto de ancoragem dos pés.
- Hitbox e hurtbox.
- Posição da espada e do escudo por direção.
- Eventos de início e término de ataques.
- Frames de aplicação de dano.
- Eventos de ativação e encerramento da defesa.
- Pontos de sincronização dos VFX.
- Regras de interrupção por dano.
- Estados e transições de animação.
- Estado final de morte.
- Referências aos arquivos de efeitos visuais.

---

## 10. VALIDAÇÃO OBRIGATÓRIA

Antes de considerar o conjunto concluído:

1. Reproduzir Idle, Walk e Defense Hold por cinco ciclos completos em cada direção.
2. Verificar continuidade dos ossos e articulações entre todos os frames.
3. Confirmar que espada e escudo permanecem nas mãos corretas.
4. Testar Idle → Attack → Idle e Walk → Attack → Walk.
5. Testar Idle → Golpe Espectral → Idle.
6. Testar Defesa Óssea → Defense Hold → recuperação.
7. Validar a interrupção por Hurt e retorno à postura de combate.
8. Testar a morte completa em todas as oito direções.
9. Verificar se a espada, o escudo e os ossos caídos permanecem coerentes no frame final.
10. Sincronizar efeitos de corte, impacto, necromancia e bloqueio.
11. Inspecionar todos os recortes e identificar possíveis pixels residuais.
12. Corrigir tremores, mudanças involuntárias de escala, deformações e saltos visuais.
13. Validar transições de direção durante a caminhada.
14. Confirmar que os efeitos espectrais não ocultam a leitura corporal.
15. Verificar o comportamento das animações na escala real de gameplay.

---

## 11. RESULTADO ESPERADO

Entregar um conjunto completo de spritesheets do **Esqueleto Guerreiro em Pixel Art Chibi**, contendo:

- **Idle:** 128 frames.
- **Walk:** 128 frames.
- **Attack — Corte de Espada:** 128 frames.
- **Hurt:** 80 frames.
- **Died — Colapso Ósseo:** 192 frames.
- **Skill 01 — Golpe Espectral:** 160 frames.
- **Skill 02 — Defesa Óssea:** 144 frames.
- **Defense Hold:** 64 frames.
- **VFX próprios:** golpes, impactos, necromancia, escudo e morte.
- **Metadados completos:** JSON com animações, direções, recortes, sincronização e eventos.

**TOTAL: 1.024 frames corporais distribuídos em oito direções, além dos efeitos visuais independentes.**

O Esqueleto Guerreiro deve funcionar como um inimigo morto-vivo completo, com movimentação convincente, ataques de espada, defesa com escudo, habilidades necromânticas e morte por desmoronamento ósseo.

**PRIORIDADE ABSOLUTA:** fluidez, consistência anatômica, continuidade entre movimentos, perspectiva isométrica, integridade dos equipamentos e sprites prontos para integração direta ao jogo.

Não substituir animações completas por poses estáticas, espelhamentos inadequados, efeitos genéricos ou frames duplicados artificialmente. Todas as animações devem ser produzidas e validadas individualmente nas oito direções.