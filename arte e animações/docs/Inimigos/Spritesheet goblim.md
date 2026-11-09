# INIMIGO GOBLIN — PADRÃO DEFINITIVO DE SPRITESHEET 8 DIREÇÕES

Crie uma spritesheet completa para um **Goblin de RPG 2D isométrico, inspirado em Diablo II, com estética Pixel Art Chibi e fantasia medieval sombria**.

O Goblin é pequeno, ágil, agressivo e oportunista, com pele esverdeada, orelhas pontudas, dentes aparentes, postura curvada, roupas desgastadas e adaga enferrujada.

O objetivo é produzir animações extremamente fluidas, expressivas e consistentes, com movimentos naturais de corpo inteiro, sem tremores, cortes ou alterações involuntárias na aparência.

## 1. SISTEMA DE 8 DIREÇÕES

Todas as animações do personagem devem ser produzidas individualmente nas seguintes direções:

1. Norte (N) — Costas
2. Nordeste (NE) — Diagonal superior direita
3. Leste (E) — Lateral direita
4. Sudeste (SE) — Diagonal inferior direita
5. Sul (S) — Frente
6. Sudoeste (SW) — Diagonal inferior esquerda
7. Oeste (W) — Lateral esquerda
8. Noroeste (NW) — Diagonal superior esquerda

**Obrigatório:** produzir as oito direções com sprites próprios, respeitando perspectiva, anatomia, iluminação e posição da arma. Não espelhar automaticamente sprites quando isso causar inversão incorreta de equipamentos ou detalhes assimétricos.

## 2. ANIMAÇÕES OBRIGATÓRIAS

### 01 — IDLE (12 frames × 8 direções = 96 frames)

O Goblin permanece em postura agressiva, respirando, movimentando discretamente os ombros, observando os arredores e ajustando a posição da adaga.

- Respiração corporal visível, mas sutil.
- Pequenos movimentos de cabeça e orelhas.
- Balanço natural dos braços e da arma.
- Alternância suave do peso corporal, sem deslocar os pés.
- Primeiro e último estados devem se conectar perfeitamente.

**Loop:** contínuo e perfeito.

### 02 — WALK (12 frames × 8 direções = 96 frames)

Caminhada rápida, furtiva e nervosa, característica de um Goblin.

- Ciclo completo de passos alternados.
- Inclinação leve do tronco para frente.
- Balanço coordenado de braços e pernas.
- Movimento secundário de roupas, orelhas e acessórios.
- Pés devem apoiar corretamente no chão, sem deslizar.
- Manter velocidade visual consistente nas oito direções.

**Loop:** contínuo, com transição natural entre os passos.

### 03 — ATTACK (12 frames × 8 direções = 96 frames)

Ataque corpo a corpo com adaga enferrujada.

- Frames 1–3: antecipação, recuando o braço armado.
- Frames 4–6: avanço e execução rápida do golpe.
- Frames 7–8: conclusão do movimento e impacto.
- Frames 9–12: recuperação e retorno à postura de combate.

O ataque deve transmitir agressividade, velocidade e peso coerente.

**Transição:** Idle → Attack → Idle, sem saltos visuais.

### 04 — HURT (8 frames × 8 direções = 64 frames)

Reação ao receber dano.

- Frames 1–2: impacto inicial.
- Frames 3–4: recuo do tronco e expressão de dor.
- Frames 5–6: desequilíbrio e recuperação.
- Frames 7–8: retorno à postura de combate.

A reação deve ser expressiva, mas curta o suficiente para não prejudicar o ritmo do combate.

**Transição:** Idle/Walk → Hurt → Idle, com possibilidade de interrupção das animações de combate quando a mecânica permitir.

### 05 — DIED (16 frames × 8 direções = 128 frames)

Morte completa com queda e colapso corporal.

- Frames 1–4: impacto fatal e perda de equilíbrio.
- Frames 5–8: queda progressiva.
- Frames 9–12: contato com o chão e acomodação do corpo.
- Frames 13–16: estabilização na posição final de cadáver.

A arma e os acessórios devem acompanhar a queda de maneira coerente.

**Sem loop:** o último frame permanece visível até o desaparecimento ou remoção do inimigo.

### 06 — SKILL: INVESTIDA SELVAGEM (16 frames × 8 direções = 128 frames)

Habilidade especial de aproximação e ataque.

- Frames 1–4: agachamento e preparação.
- Frames 5–7: impulso inicial.
- Frames 8–11: investida agressiva com golpe de adaga.
- Frames 12–14: aterrissagem e recuperação.
- Frames 15–16: retorno à postura de combate.

O deslocamento efetivo deve ser controlado pelo jogo, sem duplicar a movimentação dentro dos sprites.

**Transição:** Idle/Walk → Skill → Idle/Walk.

## 3. PROJÉTEIS E EFEITOS VISUAIS

**Projétil:** não aplicável ao Goblin corpo a corpo. Não gerar projéteis artificiais para preencher a spritesheet.

Criar os seguintes VFX separados do personagem:

- **Slash de adaga:** 6 frames, arco de corte sincronizado com o ataque.
- **Hit Impact:** 6 frames, efeito de impacto ao atingir o alvo.
- **Poeira de passos:** 6 frames, pequenas partículas de poeira.
- **Investida selvagem:** 8 frames, efeito de velocidade e impacto.
- **Morte:** 8 frames, poeira discreta durante a queda.

Os efeitos direcionais devem acompanhar as oito orientações quando necessário. Efeitos visualmente simétricos podem compartilhar animações, desde que preservem a perspectiva.

## 4. ESPECIFICAÇÕES TÉCNICAS

| Animação | Frames/direção | Direções | Total |
|---|---:|---:|---:|
| Idle | 12 | 8 | 96 |
| Walk | 12 | 8 | 96 |
| Attack | 12 | 8 | 96 |
| Hurt | 8 | 8 | 64 |
| Died | 16 | 8 | 128 |
| Skill | 16 | 8 | 128 |
| **Total personagem** | | | **608** |

Os efeitos visuais devem ser entregues em spritesheets separadas, com 34 frames de animações-base, antes de considerar eventuais variantes direcionais.

**FPS recomendados:**
- Idle: 10–12 FPS.
- Walk: 12–16 FPS, sincronizados à velocidade de movimento.
- Attack: 16–20 FPS.
- Hurt: 16–20 FPS.
- Died: 12–16 FPS.
- Skill: 16–20 FPS.

A velocidade pode ser ajustada pela engine sem alterar os sprites originais.

## 5. REGRAS DE FLUIDEZ E CONSISTÊNCIA

- Produzir todos os frames com arte Pixel Art Chibi consistente.
- Manter proporções, cores, contornos e iluminação idênticos.
- Não deformar cabeça, braços, pernas, arma ou acessórios.
- Preservar a mesma escala nas oito direções.
- Manter um ponto de ancoragem consistente no chão, entre os pés.
- Garantir contato correto dos pés com o chão durante Walk.
- Usar poses intermediárias suficientes para movimentos suaves.
- Aplicar antecipação, aceleração, desaceleração e recuperação aos ataques.
- Garantir transições visuais naturais entre Idle, Walk, Attack, Hurt e Skill.
- Permitir troca de direção sem mudanças abruptas na silhueta.
- Manter o Goblin sempre reconhecível, independentemente da orientação.
- Evitar frames duplicados desnecessariamente, bordas, pixels soltos e vazamentos entre células.
- Não utilizar interpolação borrada que comprometa a nitidez da pixel art.
- Usar fundo transparente verdadeiro.
- Organizar os frames em ordem cronológica e separar claramente cada animação e direção.
- Entregar dados de recorte, pontos de ancoragem, FPS e eventos de impacto em formato JSON para integração com a engine.
- Garantir que VFX, projéteis e equipamentos sejam sincronizados com os movimentos.
- Validar cada animação em reprodução contínua e em transições de gameplay.

## 6. ORGANIZAÇÃO DOS ARQUIVOS

Para evitar spritesheets excessivamente grandes, dividir a entrega em arquivos individuais:

- `goblin_idle.png`
- `goblin_walk.png`
- `goblin_attack.png`
- `goblin_hurt.png`
- `goblin_died.png`
- `goblin_skill.png`
- `goblin_vfx.png`
- `goblin_animations.json`

Cada spritesheet do personagem deve utilizar oito linhas direcionais, na ordem N, NE, E, SE, S, SW, W e NW, com os frames de cada direção organizados horizontalmente.

Todos os arquivos devem compartilhar identidade visual, escala e sistema de ancoragem. Se necessário, dividir os VFX em arquivos menores.

**RESULTADO ESPERADO:** um conjunto completo de spritesheets contendo **608 frames de personagem**, mais os efeitos visuais, com oito direções independentes e animações fluidas para Idle, Walk, Attack, Hurt, Died e Skill.

O Goblin deve funcionar como um inimigo completo para MMORPG isométrico, com combate responsivo, movimentos naturais, excelente leitura visual e integração direta com o sistema de animação do jogo.