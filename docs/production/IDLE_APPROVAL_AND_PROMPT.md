# Idle — etapa aprovada e congelada

**Personagem:** `SD-HUM-V3`  
**Etapa:** `ANIM-IDLE-V1` — aprovada visualmente pelo usuário em 2026-11-09.  
**Fonte:** `sprite_de_aventure_em_pixel_art.png` (SHA256 `0f29e33d2500dbfe51b14e7662ae0a7064d74dbf1e5cd967e5468b90287613ef`), folha magenta com grid ilustrado 4×2.  
**Aprovação:** visual da arte/Idle; **não** certifica oito orientações, 16 frames/direção nem atlas completo.

## Prompt congelado de continuidade (reconstituição editorial)

```text
Basear-se na referência principal SD-HUM-V3-FRONT aprovada e no seu prompt
canônico. GERAR APENAS A ANIMAÇÃO IDLE do MESMO personagem em visão frontal:
folha 4 colunas × 2 linhas com oito poses desenhadas de respiração leve e
postura natural; pés apoiados na mesma linha de chão, pequeno movimento
torácico/ombros e cauda do lenço discretamente variável, início e fim
compatíveis em loop. Manter a MESMA roupa marrom, lenço vermelho, ombreira
única de prata, cabelos, rosto, cinto, bolsa, luvas, calças e botas,
sem alternâncias nem novos equipamentos. Todas as oito poses devem
representar o MESMO indivíduo. Pixel art chibi medieval dark fantasy.
Fundo magenta #FF00FF uniforme, margem segura para recorte por chroma.
SEM UI, LOGOS, TÍTULOS, LEGENDAS, MOLDURAS, PALETAS OU OUTRAS ANIMAÇÕES.
```

Este texto é prompt *canônico para reprodução*, reconstruído das regras de
estilo e do resultado aprovado, porque o prompt interno bruto do gerador
anterior não está disponível. Não alegar transcrição exata.

## Restrições de escopo

A folha aprovada documenta **oito poses de Idle frontal**, não oito ângulos.
A matriz final exige **oito direções** (N, NE, E, SE, S, SW, W, NW)
e meta de **16 frames/direção** em `Spritesheet Espadachim.md`;
isso será completado em iterações sem invalidar a aprovação visual desta
referência. Não duplicar a folha frontal e atribuir nomes de outras direções.

## Checklist

- [x] Aparência frontal aprovada.
- [x] Folha visual de Idle aprovada pelo usuário.
- [x] Hash e prompt de continuidade documentados.
- [ ] Arquivos originais **raw** congelados/upload confirmados no GitHub.
- [ ] Chroma key e recorte verificados em bordas e lenço.
- [ ] GIF e atlas runtime derivados dos frames reais aprovados e testados.
- [ ] Outras sete direções Idle com frames e loop aprovados.
