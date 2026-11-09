# P3 — Revisão artística v2 (arte ilustrada, não geométrica)

Data: 2026-11-09. **Status: EM PRODUÇÃO / AINDA NÃO APROVADA.** Esta revisão substitui visualmente a P3 procedimental rejeitada. A P4 continua BLOQUEADA.

## Motivo da revisão

O usuário reprovou expressamente a P3 original: os 896 frames gerados programaticamente por retângulos/polígonos produziram boneco geométrico, incompatível com o material P1 aprovado. O workflow legado foi desativado para geração automática e os 18 arquivos da antiga produção movidos para `tests/fixtures/legacy_p3_geometric/`. **Nunca usar esses arquivos como assets do jogo.**

## Arte v2 produzida e publicamente verificável

**Fonte ilustrada original de IA**, baseada na linguagem do style guide P1, com corte e transparência tratados e importados pelo mesmo pipeline técnico P2:

1. [Oito vistas de Idle](../../assets/characters/classes/shared_humanoid_art_v2/idle_8_directions.png) — uma ilustração-base por direção.
2. [Oito poses de referência de caminhada](../../assets/characters/classes/shared_humanoid_art_v2/walk_8_directions_reference.png) — uma pose por direção; **não equivale a animação Walk completa**.
3. [Oito quadros de Walk SE equipada](../../assets/characters/classes/shared_humanoid_art_v2/walk_SE_8_frame_art_reference.png) — sequência ilustrada real, separada do corpo-base.
4. [GIF do Walk SE equipado](../../assets/characters/classes/shared_humanoid_art_v2/runtime/equipped_walk_se/humanoid_equipped_walk_se_reference_walk_SE.gif) — gerado pelos oito frames processados e exportados.
5. [Atlas PNG e JSON por direção](../../assets/characters/classes/shared_humanoid_art_v2/runtime/) — saída do pipeline P2.
6. [Visualizador de direção ilustrada](../../demo/p3.html) — o antigo boneco geométrico não é mais o preview padrão.

**Total ativo ilustrado nesta revisão:** 16 poses estáticas (8 Idle e 8 Walk reference) + 8 quadros de Walk SE equipada = **24 desenhos exportados**, de naturezas diferentes. Não apresentar como 24 frames homogêneos de corpo-base modular; Walk equipada possui armadura/cabelo/arma embutidos na imagem de referência.

O ciclo Walk SE foi criado em ferramenta de ilustração/geração de imagem, **não** por deformação de formas programáticas. Os recortes PNG de GIF foram normalizados com transparência e pixelização para inspeção na escala do projeto. Isso ainda não constitui garantia de que todos os pixels, bordas e pontos de contato estejam artisticamente perfeitos.

## Pipeline e testes

- `tools/import_p3_art.py`: importa e confere folhas autorais de 8 direções e sequência Walk SE, convertendo em P2 PNG/JSON e GIF de QA.
- `tests/test_p3_art.py`: valida RGBA, oito ângulos, atlas e GIF de oito frames.
- [GitHub Actions aprovado](https://github.com/marmitero/sprite-direction/actions/runs/42685488085) — 3 testes novos aprovados e runtime binário publicado em `main`.
- Workflow antigo de geometria foi alterado para execução manual e não publica sprites de produção.

## QA / critérios de aceite

| Requisito P3 | Status |
|---|---|
| Abandonar boneco geométrico como arte final | CONCLUÍDO |
| Estilo ilustrado chibi dark fantasy baseado em P1 | CONCEITO PRODUZIDO, aprovação visual pendente |
| Oito direções de referência Idle | ENTREGUE (1 frame/direção) |
| Oito direções de referência Walk | ENTREGUE (1 pose/direção) |
| Walk SE com 8 frames desenhados | ENTREGUE (equipado, não modular) |
| Idle completo 8 direções × frames definidos por animação | PENDENTE |
| Walk completo 8 direções × quadros únicos | PENDENTE |
| Corpo-base com roupa simples e sem equipamento embutido em todas as animações | PENDENTE |
| Cabelo, peitoral, mãos, botas, espada e escudo como camadas reais com arte P1 | PENDENTE |
| Âncoras de pulso, máscaras, oclusões dinâmicas por frame/direção | PENDENTE |
| Testes de fluidez e ausência de tremor com todo equipamento | PENDENTE |
| Aceite visual final da P3 | PENDENTE |
| Permissão de início de P4 | NÃO CONCEDIDA |

## Orientação inegociável para continuação

- Arte de personagem deve ser ilustrada, com leitura de volume, silhueta e textura de pixel art chibi.
- Não reimplementar o corpo como combinações de primitivas geométricas PIL/SVG/CSS.
- Não usar um frame duplicado, deformado ou espelhado para alegar que há oito frames desenhados.
- Não recortar a armadura embutida da sequência equipada e chamar de overlay funcional sem separação artística e sincronização reais.
- Usar atlas e JSON só depois de separar corretamente corpo, cabelo, torso, luvas, botas, armas e escudo por orientação e frame.
- Recalcular contagem de frames quando melhorar fluidez e registrá-la; nunca preencher contagens por obrigação aritmética.

**Checkpoint:** P3 v2 avançou com PNG/atlas/JSON e GIF artístico reais; continua em revisão e **não deve ser declarada concluída nem liberar P4**.
