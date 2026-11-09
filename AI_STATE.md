# AI_STATE — Sprite Direction

Atualizado: 2026-11-09 | Repositório `marmitero/sprite-direction`, branch `main`.

## Fase ativa e progresso

**P3 — personagem SD-HUM-V3, novo fluxo de geração por movimento.**
Aprovações humanas recebidas: **FRONT-01 e IDLE-01** (versão ilustrada de roupas marrons e lenço vermelho).
**P3 não concluída. Walk não aprovada. P4 bloqueada.**

## Fonte de verdade, ordem de leitura

1. `readme.md`
2. `docs/production/P3_LOCK_AND_NEXT_STAGE.md` — status e aprovação.
3. `docs/production/APPROVED_HUMANOID_LOCK.md` — aparência frontal e prompt mestre congelado.
4. `docs/production/IDLE_APPROVAL_AND_PROMPT.md` — Idle frontal aprovado e prompt.
5. `docs/production/CHARACTER_GENERATION_PROTOCOL.md` — sequência mandatória (front → freeze → um movimento por geração → QA → chroma → atlas/GIF → aprovação).
6. `docs/production/WALK_PROMPT_V1.md` — prompt da próxima geração, Walk isolada.
7. `docs/production/ANIMATION_REQUIREMENTS_ALL_CLASSES.json` — 154 movimentos nos cinco docs de classes.
8. `docs/art-direction/P1_APPROVAL.md`; `docs/art-direction/STYLE_GUIDE_P1.md` — padrões artísticos congelados.
9. `docs/technical/P2_PIPELINE.md` — exportação atlas/JSON.
10. `production_manifest.json` — estado em formato de máquina.

## Aprovação e identidade

Frente mestre: `herói_chibi_aventureiro_em_pixel_art.png`, 1254×1254, SHA256 `f528766d28a2ba7a0b22120db413dcc5ec022cb5529b09f452a2ffb2ef709113`.
Idle mestre: `sprite_de_aventure_em_pixel_art.png`, 1448×1086, 4×2 poses frontais, SHA256 `0f29e33d2500dbfe51b14e7662ae0a7064d74dbf1e5cd967e5468b90287613ef`.
Originais binários preservados em pacote de referência da conversa, mas **ainda não commitados como binário no GitHub**; os docs e hash não equivalem a upload. Para processamento local, fornecer as duas fontes originais a `tools/import_approved_p3_reference.py`. O usuário aprovou arte e Idle como visual, não 8 direções ou runtime completo.

Mesma identidade para todas as gerações: cabelo preto bagunçado e franja assimétrica, olhos castanho-rubros, lenço vermelho escuro, camisa bege/roupa de couro marrom, diagonal com fivela, UMA ombreira prateada em um lado, bolsa/cinto, luvas escuras, calças marrom-escuras largas, botas marrons e punhal embainhado na cintura. Não adicionar armadura de placas completa ou capa nova.

## Próximos movimentos e política

Documentos de classes indicam **Walk de 16 frames/direção** como próximo universal, depois Run (20), Dodge (16), Jump (18), Turn (8×16 transições), e estados defensivos/combate/dano/morte; ações específicas por classe no manifesto de 154 linhas. Ajustes permitidos para fluidez, mas não preencher quadros fictícios. Idle aprovado contempla **8 poses frontais**, ainda falta fechar 8 direções × frames conforme o documento.

As tentativas de Walk nesta sessão vieram como infográficos/painéis com roupa/armadura divergente, então **foram rejeitadas** e não serão usadas no runtime; `WALK_PROMPT_V1.md` documenta a tentativa seguinte e critérios de QA.

## Pipeline

Script de chroma `tools/import_approved_p3_reference.py` e teste `tests/test_p3_approved_reference.py` versionados. O script preserva o canvas, recorta 4×2 poses frontais, remove magenta e emite PNGs RGBA/GIF/QA sem inventar direções. Arquivos de processamento local e as duas fontes podem ser obtidos no pacote entregue na conversa; não afirmar que foram salvos no repo antes do upload.

## Proibições

- Nunca misturar ações numa geração nem reutilizar os painéis decorativos como atlas.
- Nunca reintroduzir geometria da P3 original (`tests/fixtures/legacy_p3_geometric/`).
- Não transformar corpos equipados em base modular por alegação sem separar camadas.
- Não marcar Walk como aprovada, P3 concluída ou P4 iniciada sem evidência.

## Próxima ação

**Produzir nova folha somente Walk, com a frente aprovada e Idle como referências**, verificar mesma roupa/rosto/escala e quadros reais. Se a geração alterar roupa ou virar painel, reprovar e ajustar prompt antes da entrega. Publicar somente o que passou no gate.
