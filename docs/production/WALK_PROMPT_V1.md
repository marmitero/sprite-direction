# Próxima geração — Walk do personagem SD-HUM-V3

**Status:** prompt preparado; **NENHUMA folha Walk aprovada**.  
**Fonte prioritária:** `docs/production/APPROVED_HUMANOID_LOCK.md` e `IDLE_APPROVAL_AND_PROMPT.md`.  
**Especificação:** `arte e animações/docs/Classes/Spritesheet Espadachim.md`, seção 6 / Walk: **16 frames × 8 direções = 128 frames**, sujeito a correção justificada para fluidez.

## Prompt obrigatório para a próxima geração — APENAS WALK

```text
A TAREFA É SOMENTE UMA FOLHA DE SPRITES PARA A ANIMAÇÃO WALK.
PERSONAGEM CONGELADO: referência original SD-HUM-V3-FRONT + oito quadros
SD-HUM-V3-IDLE + prompt canônico (versão APPROVED_HUMANOID_LOCK.md).
O MESMO jovem aventureiro chibi, cabelo preto volumoso/desgrenhado, olhos
rubro-castanhos, lenço vermelho escuro, túnica/casaco marrom com camisa
bege, correia diagonal, ombreira prateada em um só ombro, luvas escuras,
cinto, bolsa lateral, calças largas e botas marrons. Punhal na cintura.
SEM mudança de roupa ou item. NÃO criar armadura nova, elmo, espada
desembainhada, escudo, novos adornos, variações de cor ou personagem novo.

Animação WALK: ciclo de caminhada REAL, com alternância de apoio,
contato/impulso/passing/contato do pé oposto, transferência de peso,
balanço inverso dos braços, pequena rotação de tronco e movimento secundário
sutil do cabelo e da ponta do lenço. Cada frame deve ter pose distinta,
coerente e conectada ao anterior; último conecta perfeitamente ao primeiro.
Conservar escala, olhos, cabelo, roupa, quantidade/posição de objetos,
comprimento de membros e ponto estável no chão. Real pixel art de fantasia
medieval sombria, sem blur, sem geometria de placeholder.
Ordenar as oito direções no padrão:
N, NE, E, SE, S, SW, W, NW (telas: cima, diagonais, direita, baixo...).
Preferir 16 quadros desenhados por direção conforme fonte; caso não caiba
com clareza em uma única folha, NÃO comprimir nem simular 128 quadros:
entregar a maior parte coerente e registrar complementos necessários,
mantendo UMA geração temática Walk por lote de trabalho.
FUNDO #FF00FF MAGENTA uniforme; quadro a quadro com células bem definidas
sem molduras e sem artefatos ao redor da silhueta.
SEM TEXTO, TÍTULOS, NUMERAÇÃO, LOGOTIPO, PORTFÓLIO, DASHBOARD, UI,
RETRATOS, PALETA, ICONOGRAFIA OU OUTRAS ANIMAÇÕES.
```

## Critérios de reprovação

- Mudança para guerreiro de armadura completa, capa nova, cabelo alterado ou
  cores incompatíveis com a referência.
- Entregar um painel explicativo com várias animações em vez de Walk puro.
- Pés escorregando, salto acidental, membro que some, escala mudando;
  cenas ou sombra incorporada ao fundo magenta.
- Rotular poses repetidas como 16 frames ou espelhar ângulos assimétricos.
- Exportar como asset funcional antes de validar por preview/GIF e teste P2.

## Tentativas nesta sessão

Foram geradas folhas conceituais contendo **painéis, títulos e múltiplas
animações, com armadura diferente da imagem aprovada**. Todas foram
**REPROVADAS como Walk** e não devem ser usadas em atlas de produção.
Esta distinção impede contabilizar imagens como avanço funcional.

## Ordem após Walk

A sequência universal sugerida é Run, Dodge, Jump, Turn, Combat Idle,
Hurt, Stagger, Knockdown, Get Up, Died; ataques, combos, bloqueios, parry
e skills seguem os requisitos específicos da classe. Executar somente
com checkpoints, uma animação por etapa.
