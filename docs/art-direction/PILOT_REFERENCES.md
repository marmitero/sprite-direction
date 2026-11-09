# P1 — Lote de referência (brief para amostras)

**Status: direção visual dos conceitos aprovada; amostras funcionais ainda não produzidas.** Não são spritesheets de runtime, e nenhum PNG técnico de referência foi versionado no GitHub nesta etapa. O brief passa a ser contrato para P2/P3, sem reabrir o estilo salvo necessidade expressa.

## Pacote piloto

| ID | Entidade | Visões | Itens de comparação |
|---|---|---|---|
| P1-HUM-01 | Corpo-base humanoide/espadachim | 8 direções da mesma identidade | silhueta, cabeça, mãos, pés, postura neutra |
| P1-MOB-01 | Goblin | 8 direções | orelhas, adaga, postura, escala |
| P1-NPC-01 | Ferreiro | 1 vista isométrica de trabalho | bigorna, martelo, ênfase mãos/props |
| P1-ENV-01 | Piso pedra/terra | 2 tiles 64×32 + 1 transição | encaixe, textura, perspectiva |
| P1-ENV-02 | Props | árvore, parede, bigorna | escala vs personagem, oclusão |

## Regras para as amostras

- Pixel art real e limpa, sem fundo magenta nos arquivos runtime; boards de apresentação podem ter fundo.
- Todas as vistas são do mesmo personagem, não personagens similares com roupas/anatomia variáveis.
- Corpo humanoide-base sem arma/armadura permanente; armadura apenas overlay independente demonstrativo.
- Resolução de canvas não deve recortar capuz, arma, ataque ou corpo deslocado.
- As 8 direções usam IDs canônicos N,NE,E,SE,S,SW,W,NW.
- Evitar textos técnicos gerados sobre a imagem como fonte de verdade: os números são registrados em JSON/Markdown.

## Processo de validação técnica futura (P2/P3)

1. Mostrar conceito com comparativo de escala humanoide / goblin / ferreiro / objeto / tile.
2. Comparar versões 1× e 3× por nearest-neighbor.
3. Revisar silhuetas nas oito direções e posição do contato ao chão.
4. Ajustar proporção, paleta e volume após feedback.
5. Congelar a direção aprovada em documentação; somente então criar templates definitivos na P2.

**Não considerar a P1 aprovada automaticamente por um moodboard ou pelo texto do próprio conceito.**
