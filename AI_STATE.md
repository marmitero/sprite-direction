# AI_STATE — Sprite Direction

Atualizado: 2026-11-09
Repositório: marmitero/sprite-direction
Branch: main
Última fase concluída: **P2 — Pipeline técnico**
Estado: **CONCLUÍDA, TESTADA EM CI; aguardando aprovação do usuário para P3**
Próxima fase: **P3 — Corpo-base e equipamentos modulares (NÃO INICIADA)**
Assets artísticos de produção PNG/GIF/WebP versionados: **0**.
Documentos fonte originais: **22**, preservados.

## Entregas P2 verificadas

- `tools/sprite_pipeline.py`: CLI build/validate para PNG RGBA, trim de alfa com origem preservada, atlas multi-página e padding/extrusão, JSON, GIF opcional.
- `demo/index.html`: visualizador HTTP com animação/direção, passo, zoom nearest-neighbor, pivô e coordenadas.
- `tests/test_sprite_pipeline.py`: 6 testes de regressão usando imagens sintéticas temporárias, todos aprovados.
- `.github/workflows/p2-pipeline-tests.yml`: CI Python 3.11; compileall e unittest.
- `requirements-p2.txt`: Pillow.
- `docs/technical/P2_PIPELINE.md`: contrato de entrada, saída, comandos e limitações.
- `docs/technical/P2_RELEASE_REPORT.md`: resumo e evidência de execução.

**CI de referência:** https://github.com/marmitero/sprite-direction/actions/runs/42678721540 — job verify: sucesso; 6 testes passaram.

## P1 preservada

Direção artística chibi fantasy pixel art isométrica 2:1 aprovada/congelada; ver `docs/art-direction/P1_APPROVAL.md`, `STYLE_GUIDE_P1.md`, `palette.p1.json`. Ordem de direções `N,NE,E,SE,S,SW,W,NW`; tile-base de referência 64×32; equipamento modular separado de corpo e VFX. Mudanças de frames autorizadas para correção de fluidez, documentar antes/depois, sem inventar quadros.

## Limites honestos da validação

Os seis testes usam retângulos RGBA temporários. **Nenhuma animação de personagem real, equipamento modular real ou mapa foi produzido/testado na P2.** Testes de estética, consistência anatômica, eventos de impacto e overlays reais são necessários nas fases seguintes. JSON reserva `events`, inicialmente vazio; não inventar hitboxes.

## Pendências

- P0-001: diferenças das classes: 24.304 frames tabulados vs 25.616 totais textuais; diferença 1.312; baseline pelas tabelas até análise por animação.
- P3: criar body-base, âncoras, máscaras, camadas e sprites reais, com conformidade ao P1 e QA do P2.
- Refinamentos futuros: authored events/hitboxes, QA de oito direções completas e camadas modulares efetivas.

## Regras de retomada

Leia `readme.md`, `production_manifest.json`, `docs/technical/P2_PIPELINE.md`, `docs/technical/P2_RELEASE_REPORT.md` e guia P1. Não iniciar a P3, gerar sprites ou implementar equipamentos sem autorização explícita. P2 está concluída no escopo técnico e testada; não anunciar entrega de arte.
