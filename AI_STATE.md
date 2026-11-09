# AI_STATE — Sprite Direction

Atualizado: 2026-11-09
Branch: main
Fase: P0
Estado: documentação P0 publicada; aguardando aceite do usuário
Próxima fase: P1 — BLOQUEADA, não iniciar sem aprovação explícita
Arte binária gerada: 0
Documentos fonte preservados: 22

## Arquivos de retomada

1. `readme.md` — índice principal.
2. `docs/planning/P0_AUDITORIA.md` — auditoria completa, divergências e riscos.
3. `docs/planning/PLANO_MESTRE.md` — etapas P0–P11.
4. `docs/planning/CONTRATO_ENTREGA.md` — formatos e gates.
5. `production_manifest.json` — inventário e status.
6. `docs/planning/manifests/classes.audit.json` — linhas e divergências das classes.
7. `docs/planning/manifests/enemies.canonical-tables.json` — linhas completas de inimigos.
8. `docs/planning/manifests/enemies.audit.json` — extração de headings complementar.
9. `docs/planning/manifests/npcs-world.audit.json` — NPCs/tilesets.

## Resumo verificado

- 5 classes, 9 inimigos, 6 NPCs, 2 ambientes.
- Classes: tabelas 24.304 vs totais gerais 25.616, diferença 1.312, cinco documentos divergentes.
- Inimigos: 11.216 frames tabulados incluindo opcionais.
- NPCs: 6 ciclos estacionários de 40 frames (240 frames).
- Cidade: 96×96 tiles lógicos propostos; caça: 160×160 propostos; tile 64×32 referência.
- Nenhuma spritesheet/atlas/GIF executável gerada neste trabalho.

## Pendências

- P0-001: reconciliar totais gerais e linhas das cinco classes — **não inventar frames**.
- Confirmar escopo de animações opcionais (esqueleto feiticeiro, mini-dragão).
- Validar guia de arte, escala e formato de runtime nas fases P1/P2.
- Especificar inventário individual de VFX, projéteis, equipamentos e props quando a produção avançar.

## Instrução para próxima sessão

Leia o README, este AI_STATE e os três documentos de planejamento; verifique `production_manifest.json`. Não iniciar P1 ou gerar sprites antes de aprovação explícita do usuário. A próxima ação permitida sem autorização é somente revisar ou corrigir documentação da P0.
