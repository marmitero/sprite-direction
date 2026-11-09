# Personagem humanoide — visual congelado, ID SD-HUM-V3

**Status:** APROVADO: imagem frontal e Idle. **Data:** 2026-11-09.  
**Estilo:** conforme `docs/art-direction/P1_APPROVAL.md`.  
**Esta ficha prevalece sobre qualquer imagem conceitual/atlas P3 v2 anterior.**

## Identidade visual aprovada

Jovem aventureiro masculino chibi pixel art, de frente, proporções de fantasia medieval sombria e olhar vermelho-castanho. Cabelo preto/charcoal muito volumoso e desgrenhado, mechas espetadas e assimétricas, topo ligeiramente pontudo, franja irregular; expressão confiante e suave. Lenço vermelho escuro enrolado no pescoço, parte prolongada como faixa/capa curta para o lado; túnica/jaqueta marrom de couro com camada de tecido bege claro no peito e mangas arregaçadas; correia transversal com argola ou fivela metálica; ombreira **única** de aço prateado no lado visível à direita da imagem frontal; cinto de couro, fivela quadrada, pochete no quadril, luvas de couro escuro com detalhes metálicos, calças escuras largas e botas marrons de cano médio com detalhes prateados. Pequena lâmina ou punhal na cintura (não transformar em espada grande equipada nas mãos). Tons terrosos, highlights metalizados e contorno pixel art limpo.

**Não trocar a posição da ombreira**, não redesenhar o rosto ou a roupa, não aumentar armor tier; evitar transferir roupas/armaduras de imagens P3 v2 anteriores. O personagem não segura espada nem escudo na imagem frontal aprovada.

## Fonts congeladas (originais preservados nesta sessão)

| ID | Nome original | Dimensões | SHA256 original | Aprovação |
|---|---|---:|---|---|
| SD-HUM-V3-FRONT | `herói_chibi_aventureiro_em_pixel_art.png` | 1254×1254 RGB | `f528766d28a2ba7a0b22120db413dcc5ec022cb5529b09f452a2ffb2ef709113` | aprovado |
| SD-HUM-V3-IDLE | `sprite_de_aventure_em_pixel_art.png` | 1448×1086 RGB, grid visual 4×2 | `0f29e33d2500dbfe51b14e7662ae0a7064d74dbf1e5cd967e5468b90287613ef` | aprovado |

**Nota de proveniência:** hashes calculados dos PNGs originais gerados na conversa. Esta ficha registra os dados e a aprovação, **mas não representa prova de que esses dois arquivos originais estejam commitados no repositório Git**. O pacote bruto disponível na sessão deve ser arquivado e importado posteriormente sem renomear/alterar os bytes. Não confundir arte original com versões reduzidas, prévias ou folhas geradas anteriormente.

## Prompt canônico congelado

```text
CRIAR UM ÚNICO PERSONAGEM, VISTA FRONTAL COMPLETA. Pixel art chibi RPG
medieval dark fantasy, acabamento artesanal detalhado, alta legibilidade e
volume real de pixel art, contorno limpo e sombreamento em clusters coerentes.
Usar EXATAMENTE a imagem SD-HUM-V3-FRONT aprovada como identidade visual.
Mesmo jovem aventureiro de cabelo preto muito desgrenhado, franja assimétrica
e olhos rubro-castanhos; lenço vermelho escuro ao redor do pescoço, cauda do
lenço no lado original; casaco/túnica marrom e bege de aventureiro, correia
diagonal, cinto quadrado e bolsa lateral; UMA única ombreira prateada na
posição aprovada; luvas escuras, calças escuras amplas e botas marrons de
detalhes metálicos. Pequena lâmina embainhada na cintura. Sem arma nas mãos.
Proporções, tons, costuras, acessórios, volume e silhueta idênticos à imagem
aprovada. Personagem inteiro, sem cortes, centrado, pés visíveis e pivô de
chão estável. FUNDO EXCLUSIVAMENTE MAGENTA #FF00FF homogêneo, sem chão,
sombra no fundo, gradiente, cenário ou qualquer outro elemento.
SEM TEXTO, UI, PAINÉIS, QUADROS, TÍTULO, LOGOTIPO, PALETA, RETRATOS,
PERSONAGENS ALTERNATIVOS OU VARIAÇÕES DE TRAJE.
```

**Nota de fidelidade:** o texto acima é um **prompt canônico reconstituído a partir da arte aprovada e das exigências do usuário**. O texto interno original usado pela ferramenta de geração anterior não foi exposto integralmente; não apresentá-lo falsamente como transcrição literal.

## Bloqueios de consistência (negative prompt permanente)

```text
Do not change outfit, hair, face, eye color, body proportions, red scarf,
one-sided silver shoulder plate, belt, waist pouch, gloves, trousers, boots
or waist dagger. No new plate armor, helmet, full cape, sword in hands,
shield, hood, class redesign, costume variants, mirror-only eight views,
blurry rendering, vector silhouettes, geometric placeholders, UI or labels.
```

## Uso obrigatório

Cada prompt de movimento deve referenciar esta ficha, o hash do PNG frontal,
o prompt canônico acima e o Idle aprovado, preservando **literalmente a
identidade**. O Chroma Key deve ocorrer em cópias de runtime, nunca na
referência-mestre magenta.
