# P2 — Relatório de entrega e validação

Data: 2026-11-09. Repositório: marmitero/sprite-direction, branch main.
Etapa P2: **concluída em escopo de pipeline técnico**. P3 **não autorizada**.

## Implementado

| Recurso | Arquivo | Estado |
|---|---|---|
| Importação de sequências PNG RGBA | `tools/sprite_pipeline.py` | implementada |
| Recorte por bounding box de alfa, preservação de canvas/origem | mesmo arquivo | implementada |
| Atlas PNG com múltiplas páginas, padding >=2 e extrusão | mesmo arquivo | implementada |
| JSON com frames, índices, pivô, duração, hash e eventos vazios | mesmo arquivo | implementada |
| GIF de QA da sequência original | mesmo arquivo | implementada |
| Verificação de numeração, dimensão, posição, hashes, overlap e schema | mesmo arquivo | implementada |
| Visualizador HTML5 com nearest-neighbor, directions e pivô | `demo/index.html` | implementado |
| Testes automatizados | `tests/test_sprite_pipeline.py` | 6 aprovados |
| Pipeline GitHub Actions | `.github/workflows/p2-pipeline-tests.yml` | sucesso |

## Evidência de execução

- [GitHub Actions run #2](https://github.com/marmitero/sprite-direction/actions/runs/42678721540)
- Workflow `P2 Sprite Pipeline CI` → job `verify` → conclusion `success`.
- Python 3.11; Pillow instalado; compileall aprovado.
- **6 testes executados e aprovados**: construção + trim e validação; corrupção de atlas; GIF com frame vazio; proteção input/output; sequência com índice ausente; PNG de modo RGB rejeitado.
- Os testes geram PNG geométrico de forma temporária; não representam sprites artísticos e não foram versionados.

## Comandos de uso

```bash
python -m pip install -r requirements-p2.txt
python -m unittest discover -s tests -v
python tools/sprite_pipeline.py build --input samples/input --output output --asset goblin --atlas-size 1024 --padding 2 --fps 12 --gif
python tools/sprite_pipeline.py validate --output output --asset goblin
python -m http.server 8000
```

Abrir `http://localhost:8000/demo/` e apontar ao JSON `/output/goblin.json`.

## Notas de escopo

- Não houve geração de arte oficial; assets visuais P1 ainda são moodboards de referência.
- Não há prova de qualidade artística, oito direções completas para uma entidade real, nem teste de múltiplos equipamentos reais. Isto pertence à produção dos pilotos e classes nas fases subsequentes.
- Eventos de impacto/hitbox são campos reservados no JSON e permanecem vazios até autoria/integrador registrar dados efetivos.
- O pipeline usa pivô central no eixo X e na base do canvas no eixo Y; os frames devem respeitar o mesmo canvas por animação/direção.
- GIF é prévia, não dado de runtime; o jogo deve carregar PNG/JSON.
- Recontagem de frames autorizada com QA por animação: `docs/art-direction/FRAME_RECONCILIATION.md`.
- P0-001: divergência de 1.312 frames entre somas tabuladas das classes e os totais textuais continua registrada, sem preenchimento fictício.

## Gate P2

- [x] Exportador e formato de entrada documentados.
- [x] Trim preservando deslocamento de origem.
- [x] Atlas PNG com padding/extrusão e múltiplas páginas.
- [x] Metadados JSON e validador.
- [x] GIFs de QA opcionais a partir dos frames de origem.
- [x] Visualizador web de reprodução/inspeção.
- [x] Workflow e testes automatizados aprovados na CI.
- [x] README, AI_STATE e manifesto atualizados.
- [ ] P3 iniciada — **bloqueada até instrução explícita do usuário**.

**Conclusão:** pipeline P2 tecnicamente implementado e verificado em testes sintéticos; prontidão para produção de sprites reais ainda deverá ser demonstrada por asset nas etapas P3+.
