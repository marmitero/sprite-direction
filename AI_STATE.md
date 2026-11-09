# AI_STATE — Sprite Direction

Atualizado: 2026-11-09
Repositório: marmitero/sprite-direction
Branch: main
Última etapa concluída: **P1 — Fundação artística**
Status P1: **CONCLUÍDA — DIREÇÃO VISUAL APROVADA E CONGELADA**
Próxima etapa: **P2 — Pipeline técnico (NÃO INICIADA; aguardar autorização explícita do usuário)**
Assets PNG/WebP/GIF/spritesheets de runtime versionados: **0**
Documentos de origem auditados: **22**.

## Histórico de aprovações

- P0: auditoria documental encerrada com divergências registradas, sem alterar arquivos originais.
- P1: usuário aprovou expressamente a direção visual e solicitou a conclusão da etapa.
- Usuário autorizou recalcular, aumentar/reduzir frames e corrigir bugs de fluidez/funcionamento com documentação e QA; detalhes em `docs/art-direction/FRAME_RECONCILIATION.md`.
- P2: ainda sem autorização.

## Fontes de verdade

1. `readme.md` — índice principal.
2. `production_manifest.json` — fase e estado da produção.
3. `docs/art-direction/P1_APPROVAL.md` — termo de encerramento, baseline congelado e limites do aceite.
4. `docs/art-direction/STYLE_GUIDE_P1.md` — regras visuais.
5. `docs/art-direction/palette.p1.json` — paleta-base aprovada.
6. `docs/art-direction/P1_TECHNICAL_BOARD.svg` — referência técnica vetorial; não é sprite.
7. `docs/art-direction/PILOT_REFERENCES.md` — briefs de amostras a produzir na P2/P3.
8. `docs/art-direction/FRAME_RECONCILIATION.md` — política de frames e rastreabilidade.
9. `docs/planning/PLANO_MESTRE.md` — roadmap P0 a P11.
10. `docs/planning/P0_AUDITORIA.md` e `docs/planning/manifests/` — auditorias de fontes.

## Contrato visual P1

- Fantasia medieval sombria; pixel art chibi; 2:1 isométrico.
- Tile 64×32 px, referencial.
- Personagem humanoide ~40–48 px de altura visível, criaturas médias ~32–48 px, grandes ~64–96 px (faixas de escala, não bounding boxes obrigatórios).
- Direções: N,NE,E,SE,S,SW,W,NW.
- Paleta, contornos seletivos, nearest-neighbor, luz principal alto-esquerda.
- Corpo-base sem equipamentos fixos; acessórios, armas, VFX e projéteis independentes; âncoras e pivô de chão consistentes.
- Direção visual aprovada, **não confundir com validação técnica de animações/atlases**.

## Divergência de frames e mitigação

P0-001: somas das tabelas corporais das cinco classes 24.304; totais textuais 25.616; +1.312 não explicados. Os totais por linha são baseline auditável. Não criar frames de preenchimento; corrigir por ação com justificativa e testes quando produzir.

## Checkpoint de retomada

P1 encerrada. NÃO gerar sprites/atlases nem executar P2 sem nova instrução. Assim que a P2 for autorizada, iniciar pipeline de recorte/exportação/metadados/QA conforme `docs/planning/PLANO_MESTRE.md`; amostras conceituais aprovadas são guia de estética, não frames de jogo.
