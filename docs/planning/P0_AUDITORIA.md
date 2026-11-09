# P0 — Auditoria documental e reconciliação do pacote

Data: 2026-11-09. Repositório: `marmitero/sprite-direction`, branch `main`.

## Objetivo e estado

P0 é exclusivamente documental; **nenhuma arte foi produzida nem a P1 iniciada**. O inventário original contém 22 especificações (.md): 5 classes, 9 inimigos, 6 NPCs e 2 mapas/tilesets. O repositório tinha somente documentos, sem PNG/WebP/GIF/atlases/mapas funcionais no início da auditoria.

## Métodos

1. Inventariar todos os arquivos da árvore Git.
2. Ler todas as especificações por categoria.
3. Extrair animações com fórmulas por direção e conferir as tabelas de frames corporais.
4. Comparar soma das linhas das tabelas com totais anunciados nos textos, **sem somar VFX, projéteis ou equipamentos aos frames corporais**.
5. Revisar escopo técnico transversal: oito direções nas entidades móveis, camadas modulares nas classes, sequências estacionárias nos NPCs, tilesets e mapas.
6. Registrar ambiguidades como pendências em vez de inventar especificações definitivas.

## Inventário e contagens

| Classe | Soma das linhas da tabela | Total geral declarado | Diferença ainda não explicada |
|---|---:|---:|---:|
| Espadachim | 3.952 | 4.320 | +368 |
| Arqueiro | 5.184 | 5.312 | +128 |
| Mago | 4.736 | 5.104 | +368 |
| Necromante | 5.648 | 5.968 | +320 |
| Pugilista | 4.784 | 4.912 | +128 |
| **Total** | **24.304** | **26.816** | **+2.512** |

Todos os produtos aritméticos nas linhas numéricas destas cinco tabelas conferem com `frames_por_direção × direções`. **Os totais gerais não conferem com a soma das próprias tabelas.** Não presumir que os 2.512 frames faltantes sejam animações novas: a diferença pode ser erro de totalização ou de escopo. Os números ficam bloqueados para planejamento de capacidade até reconciliação autorizada.

| Inimigo | Soma das linhas, incluindo opcionais |
|---|---:|
| Aranha Gigante | 912 |
| Esqueleto Feiticeiro | 1.200 (1.040 obrigatórios + 160 teleporte opcional) |
| Esqueleto Guerreiro | 1.024 |
| Lich | 2.064 |
| Mini-Dragão Vermelho | 752 (inclui salto opcional) |
| Minotauro | 1.408 |
| Orc | 1.440 |
| Goblin | 608 |
| Stone Golem | 1.808 |
| **Total com opcionais** | **11.216** |

As linhas tabuladas dos inimigos apresentaram consistência aritmética. A diferença entre os totais **obrigatórios** e totais **incluindo opcionais** não deve ser apagada. O total de inimigos inclui opcionais e não é compromisso de entrega obrigatória até a matriz de escopo ser aprovada.

NPCs: 6 × 40 = **240 frames de ciclo documentado**, cada ciclo 8+12+10+10 frames. São NPCs estacionários; não multiplicar indiscriminadamente seus ciclos por oito direções. O Treinador de Mascotes tem composição dupla e demanda sincronização entre treinador e pet.

Mapas: primeira cidade, grade lógica de referência 96×96; caça, grade lógica 160×160. Tiles de referência 64×32 em isometria 2:1; dimensões ainda são parâmetros de planejamento, não mapas criados.

## Inconsistências e riscos detectados

- **P0-001 CRÍTICO:** cinco totais agregados de frames das classes não somam as linhas de suas tabelas (ver diferenças acima).
- **P0-002 ALTO:** não existe guia de estilo com modelos aprovados, paletas e atlas de referência versionados. A P1 deve estabelecer amostras e congelar direção de arte antes da produção massiva.
- **P0-003 ALTO:** a arquitetura de equipamentos modulares (camadas, poses, máscaras, ordem dinâmica, pontos de fixação) está especificada descritivamente, mas não há schema validado nem teste integrado.
- **P0-004 ALTO:** VFX, projéteis, invocações e objetos persistentes estão descritos em texto; falta inventário canônico de cada recurso e política de reúso com IDs únicos.
- **P0-005 MÉDIO:** nomes de origem incluem `Spritesheet goblim.md`, misturas de idioma, maiúsculas, espaços e acentos. Preservar caminhos originais; introduzir IDs normalizados nos manifestos.
- **P0-006 MÉDIO:** habilidades opcionais (ex.: teleporte do Esqueleto Feiticeiro, salto do Mini-Dragão) precisam ser sinalizadas explicitamente em critérios de release.
- **P0-007 MÉDIO:** dependências entre cidade (C1–C10) e caça (A1–A10), além da continuidade das saídas, requerem contrato de bordas, camadas e coordenadas antes da montagem.
- **P0-008 ALTO:** GIFs e pranchas não são prova de qualidade se não forem gerados dos exatos frames de runtime. Pipeline deve testar PNG/JSON, FPS, loops e pivôs.
- **P0-009 MÉDIO:** os mapas e assets não têm formato de exportação de engine, contrato de colisão e metadados de oclusão fixados.
- **P0-010 MÉDIO:** os documentos de cidade e caça têm numerações de etapas próprias (C1–C10/A1–A10) que não equivalem às etapas globais P0–P11.

## Resoluções recomendadas para próxima aprovação

1. **Manter os totais declarados como intenção**, mas dimensionar produção por linhas individuais até resolver P0-001; registrar qualquer alteração nos documentos canônicos em revisão separada.
2. Criar um manifesto dedicado para VFX/projéteis/itens durante especificação técnica da P1/P2; não contabilizar como entregue antes de existir mídia.
3. Adotar `N,NE,E,SE,S,SW,W,NW` para entidades móveis; NPCs fixos conservam ciclos de 40 frames e ângulo de instalação.
4. Exigir PNG RGBA, atlas com margem/extrusão, JSON frame a frame, pivô estável, GIF do atlas e integração testada.
5. Manter regras de variação de armadura e armas alinhadas ao corpo-base; evitar geração de folhas completas por cada combinação.

## Critério de encerramento documental da P0

[ x ] Inventário integral de 22 arquivos.
[ x ] Manifestos por categoria.
[ x ] Conferência aritmética das linhas e totais globais.
[ x ] Registro explícito das divergências.
[ x ] Plano e dependências documentados.
[ x ] Estado do projeto documentado.
[ ] Resolução de divergências de totais das classes — **pendência documental registrada, não ajustada sem aprovação**.
[ ] Aprovação expressa para iniciar P1 — **bloqueada**.

Esta P0 entrega a auditoria e as pendências, não garante que as especificações estejam livres de inconsistências.
