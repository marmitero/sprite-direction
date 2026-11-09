# Registro auditável de gerações — SD-HUM-V3

Atualizado em 2026-11-09. Ferramenta: geração de imagem do ChatGPT nesta conversa.

## Gerações aprovadas

| Etapa | ID de geração | Arte | Status |
|---|---|---|---|
| FRONT-01 | `ba194f50-3d94-4d3d-a4f4-a4948a72c0c8` | `herói_chibi_aventureiro_em_pixel_art.png` | **Aprovada pelo usuário, congelada** |
| IDLE-01 | `010149c6-68f9-4a3e-bb4a-7454fedf3182` | `sprite_de_aventure_em_pixel_art.png` | **Aprovada pelo usuário, congelada** |

Hashes dos PNGs em `APPROVED_HUMANOID_LOCK.md`. **A ferramenta de geração não expôs o prompt interno literal dessas duas gerações**; por isso foram produzidos prompts canônicos reconstituídos, explicitamente rotulados. Não confundir ID de geração com um URL público permanente.

## Tentativas WALK reprovadas na sessão de continuidade

| Referência | ID de geração | Motivo |
|---|---|---|
| WALK-TRY-01 | `6b4a4360-6562-4498-afcb-dad411006720` | Painel com várias animações/legendas e armadura trocada |
| WALK-TRY-02 | `deda0704-5397-473b-8295-c7d4c06f09e1` | Painel informativo, várias ações, roupa diferente |
| WALK-TRY-03 | `ff2cb070-42db-4da6-9dad-21089058413d` | Infográfico múltiplas ações e armadura |
| WALK-TRY-04 | `e2028937-6ecc-443d-be56-142f6896ccf4` | Painel de animações misturadas |
| WALK-TRY-05 | `2734e03a-8ff6-42f2-8ec1-c15dfacbaa10` | Painel de várias ações com estilo diferente, inclusive após usar referências explícitas |

Nenhuma tentativa Walk foi publicada como sprite válido. O único prompt aceito para próxima geração Walk é `WALK_PROMPT_V1.md`, com conteúdo textual mais restritivo e referência aos **dois arquivos mestres aprovados**.

## Política de registro futura

Registrar: ID de geração, input refs (hash e ID), prompt efetivamente enviado (quando disponível), nome e hash do PNG bruto, animação única, avaliação estética, avaliação de frames/loops, correções, caminhos de chroma, atlas e GIF, Git commit, aprovação do usuário. Se o prompt efetivamente usado não for retornado por ferramenta, registrar **não recuperável** e preservar um prompt de reprodução/correção, sem inventar transcrição literal.

O registro de geração é inventário e histórico, não prova de conclusão técnica.
