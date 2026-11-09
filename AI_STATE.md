# AI_STATE — Sprite Direction

Data: 2026-11-09
Branch: main
Etapa: **P3 — revisão artística v2 EM ANDAMENTO**
Estado: arte geométrica rejeitada pelo usuário; substituição por arte ilustrada iniciada, exportada e testada parcialmente.
Próxima etapa: **P4 — BLOQUEADA**
P1: direção artística aprovada e congelada
P2: pipeline testado e funcional

## Por que a P3 anterior foi rejeitada

A versão procedimental de `tools/generate_p3_pilot.py` produzia boneco construído de formas geométricas. O usuário solicitou pixel art 8-direction desenhada e visual próximo ao Style Guide P1. A produção antiga (896 quadros de geometria) foi movida para `tests/fixtures/legacy_p3_geometric/` e o workflow legado desativado para autopublicação. NÃO contar esses 896 quadros como arte válida.

## O que existe efetivamente na P3 v2

- `assets/characters/classes/shared_humanoid_art_v2/idle_8_directions.png`: 8 vistas ilustradas, 1 pose Idle por direção.
- `assets/characters/classes/shared_humanoid_art_v2/walk_8_directions_reference.png`: 8 poses ilustradas Walk, 1 por direção.
- `assets/characters/classes/shared_humanoid_art_v2/walk_SE_8_frame_art_reference.png`: 8 frames ilustrados de Walk SE já com armadura embutida.
- `assets/characters/classes/shared_humanoid_art_v2/runtime/`: atlas e JSON gerados pelo P2; `equipped_walk_se/` contém GIF real de QA.
- `tools/import_p3_art.py`: importer de sprites desenhados sem geração de geometria.
- `tests/test_p3_art.py`: 3 testes de arte/importação aprovados.
- `demo/p3.html`: visualização das vistas artísticas (substituiu visualizador geométrico).
- `docs/technical/P3_ART_REWORK.md`: status e pendências.

**CI:** https://github.com/marmitero/sprite-direction/actions/runs/42685488085 (SUCCESS, 3 testes novos).
**Contagem ilustrada ativa:** 8 Idle + 8 Walk poses + 8 Walk SE equipado = 24 desenhos. Não são 24 frames de uma única animação.

## O que NÃO está pronto

- Loops Idle completos em 8 direções.
- Walk completo em 8 direções com quadros artisticamente consistentes.
- Kit de equipamento modular separado do corpo-base na arte v2: cabelo, torso, mãos, botas, espada e escudo em todos os frames.
- Oclusão e ancoragem por frame, testes visuais de estabilidade do pé/mãos.
- Aceite final da P3 pelo usuário.

## Regras mandatórias

1. Preservar arte pixel art chibi fantasy dark P1 e proporções 2:1 do mundo, tile 64×32 como referência.
2. Não usar PIL geometria/placeholder como arte do jogo.
3. Não fabricar frames duplicando/espelhando imagem sem autoria de poses.
4. Gerar imagens reais, separar camadas antes de chamar de modular e usar P2 para atlas/JSON/GIF.
5. Recontagem/correção de frames permitida para fluidez, documentada.
6. Não iniciar P4 sem aprovação separada.

## Leitura de retomada

`readme.md`; `docs/art-direction/P1_APPROVAL.md`; `docs/technical/P2_PIPELINE.md`; `docs/technical/P3_ART_REWORK.md`; `production_manifest.json`.

**Situação real:** P3 v2 tem assets ilustrados exportados, mas não é o pack modular completo. Continuar a P3, não a P4.
