# AI_STATE — Sprite Direction

Atualizado: 2026-11-09
Repositório: marmitero/sprite-direction
Branch: main
Fase atual: **P3 — corpo-base e equipamentos modulares**
Estado: **piloto técnico real gerado, publicado e testado; pendente de aprovação visual e polimento**
Próxima fase: **P4 — cinco classes; NÃO INICIADA, depende de aprovação expressa**
Direção P1: congelada; não substituir por estética geométrica do piloto sem revisão.

## Entrega P3

- `tools/generate_p3_pilot.py` — gerador autoral, determinístico, de pixel art procedimental.
- `assets/characters/classes/shared_humanoid/` — PNGs de atlas por camada, JSONs, contact sheet, GIF de Walk SE e manifesto.
- `demo/p3.html` — composição das sete camadas, seleção de direção/ação e visibilidade de equipamentos.
- `tests/test_p3_pilot.py` — quatro novos testes em oito direções, encaixe/pivô, exportação e prévias.
- `.github/workflows/p3-generate-pilot.yml` — gera e valida; publica o pacote binário no repo e como artifact do workflow.
- `docs/technical/P3_PILOT_REPORT.md` — relatório, evidências, riscos e gates.

Entregues: 1 corpo-base + 6 camadas independentes (hair, chest, hands, feet, main_hand, off_hand), 8 direções, 2 animações (Idle/Walk), 8 frames/direção/animação, 128 frames por camada, **896 frames exportados**. Canvas 64×72, pivô (32,71), atlas com padding e JSON reconstruível.

CI verificada: https://github.com/marmitero/sprite-direction/actions/runs/42680063240 — `success`, **10 testes passaram** (6 P2 + 4 P3) e os PNG/JSON/GIF foram commitados em `main`.

## Limitações importantes

- O conteúdo é um **primeiro piloto pixel art procedimental**, não trabalho artístico final detalhado. Embora siga orientação e escala-base P1, **não foi homologado quanto à fidelidade estética ao moodboard P1**.
- Não há Attack/Hurt/Died, habilidades, equipamento completo, anchors de pulso por frame, máscaras nem oclusão dinâmica; não alegar esses recursos como prontos.
- O workflow de P3 testou as camadas do mesmo tamanho/índice/pivô; avaliação artística e de fluidez precisa de inspeção humana do GIF e compositor.
- A P2 está concluída e o pipeline foi efetivamente utilizado.
- P0-001 (totais corporais 24.304 vs 25.616, delta 1.312) segue como discrepância documental, não um motivo para adicionar frames artificiais.

## Documentos essenciais

1. `readme.md`
2. `production_manifest.json`
3. `docs/art-direction/P1_APPROVAL.md`
4. `docs/technical/P2_PIPELINE.md`
5. `docs/technical/P3_PILOT_REPORT.md`
6. `assets/characters/classes/shared_humanoid/p3_pilot_manifest.json`
7. `docs/art-direction/FRAME_RECONCILIATION.md`

## Próxima ação

Solicitar inspeção e aprovação visual do piloto P3. Se o usuário reprovar a estética, refinar o personagem e suas vistas **sem alterar a direção P1**. Não iniciar P4 sem aprovação explícita. A P3 não deve ser declarada integralmente aprovada só porque a CI ficou verde.
