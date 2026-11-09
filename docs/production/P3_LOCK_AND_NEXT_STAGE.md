# P3 — Registro de aprovação, congelamento e próximo movimento

**Fase:** P3, novo fluxo SD-HUM-V3. **Data:** 2026-11-09.

## Aprovação documentada

O usuário aprovou uma imagem frontal do aventureiro e uma folha Idle, ambos no estilo pixel art chibi com fundo magenta. Solicitou congelar **arte + prompts** e usar ambos para gerar uma animação por vez, atualizando o GitHub a cada etapa.

| Marco | Aprovação visual | Arte original | Prompt canônico |
|---|---|---|---|
| FRONT-01 | aprovada | SHA256 `f528766d28a2ba7a0b22120db413dcc5ec022cb5529b09f452a2ffb2ef709113` | [lock](APPROVED_HUMANOID_LOCK.md) |
| IDLE-01 | aprovada | SHA256 `0f29e33d2500dbfe51b14e7662ae0a7064d74dbf1e5cd967e5468b90287613ef` | [Idle](IDLE_APPROVAL_AND_PROMPT.md) |
| WALK-01 | **pendente** | nenhuma folha aceita | [Walk preparado](WALK_PROMPT_V1.md) |

A documentação congela identidade e especificações. **As fontes de imagem originais, geradas na conversa, ainda não foram transferidas como arquivos binários para a branch**; o pacote de distribuição está disponível como arquivo da conversa. Não considerar hashes documentação como se fossem arquivos versionados no Git. A importação futura deve manter os originais intactos.

## Revisão do repositório

As cinco classes têm Idle (16 frames/direção), Walk (16 frames/direção), Run (20), Jump (18), Hurt (10), Died (28) e mudança de direção Turn (8 por transição adjacente) nos seus documentos. `docs/production/ANIMATION_REQUIREMENTS_ALL_CLASSES.json` lista as **154 linhas de animação**, incluindo habilidades e ações próprias de cada classe. Quantidades são planejamento e podem ser ajustadas para fluidez quando justificado. Uma folha Idle 4×2 da frente **não significa** 16×8 frames válidos.

## Geração Walk — resultado desta rodada

Tentativas de geração Walk desta sessão produziram **painéis/infográficos com texto e roupas mais pesadas** do que a referência aprovada; por violarem o protocolo, foram **reprovadas** antes da exportação para runtime. Nenhuma nova Walk foi declarada pronta, nenhuma versão P3 anterior foi reaproveitada para falsificar o resultado. O prompt Walk em `WALK_PROMPT_V1.md` é a ordem de produção da próxima tentativa válida.

## Chroma e validação

O script [import_approved_p3_reference.py](../../tools/import_approved_p3_reference.py) recebe os dois PNGs originais, confirma SHA256 e processa **oito poses frontais Idle** em oito arquivos RGBA, com GIF e QA; ele não inventa novas direções. A revisão local da fonte disponível na conversa mediu o pé visível encerrando na mesma linha vertical para os oito quadros. Ainda faltam revisão de franjas de cromakey e inspeção do loop sob o jogo. O pipeline P2 continua como exportador para atlas, mas não substitui desenho real.

## Gate de produção

- [x] Frente aprovada e identidade congelada por hash.
- [x] Idle frontal aprovado visualmente e prompt documentado.
- [x] Protocolo de geração único por movimento aprovado e publicado.
- [x] Inventário de ações das cinco classes publicado.
- [x] Teste unitário de chroma adicionado.
- [ ] Fontes originais binárias confirmadas no GitHub.
- [ ] Caminhada artisticamente consistente produzida e validada.
- [ ] Idle e Walk completos em oito direções com atlas e GIF validados.
- [ ] Equipamentos modulares separados, com mesma aparência inicial e âncoras.
- [ ] P3 integralmente aprovada.
- [ ] P4 autorizada.

**Próximo passo:** produzir Walk isoladamente, referenciando o mestre frontal e Idle; entregar arte para inspeção antes de proceder ao processamento e a outra animação.
