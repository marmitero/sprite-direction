# Sprite Direction — Direção de arte e animações para MMORPG isométrico

> **Estado do repositório:** documentação de especificação/prompt. **Não há spritesheets PNG/WebP, GIFs, tilesets binários, atlas ou mapas executáveis versionados aqui nesta revisão.** As entregas descritas nos documentos são requisitos de produção, não arquivos já gerados.

Repositório de referência para planejar e produzir os **assets de um MMORPG 2D isométrico** de fantasia medieval sombria, com **pixel art chibi**, personagens em oito direções, equipamentos visualmente modulares, NPCs de ciclo contínuo, monstros, VFX e cenários compostos por tilesets. A inspiração de combate é *Diablo II*; a área externa usa como referência estrutural a saída direta da cidade para a caça, como em *Mu Online/Lorencia*, mantendo identidade artística própria.

## Produção — P0 (auditoria documental, 09/11/2026)

**Situação:** P0 documentada; P1 NÃO iniciada e depende de autorização expressa. Nenhum asset gráfico foi gerado nesta fase.

- [Planejamento mestre P0–P11](docs/planning/PLANO_MESTRE.md)
- [Auditoria P0, achados e divergências](docs/planning/P0_AUDITORIA.md)
- [Contrato técnico de entrega](docs/planning/CONTRATO_ENTREGA.md)
- [Manifesto principal](production_manifest.json)
- [Classes: frames e inconsistências](docs/planning/manifests/classes.audit.json)
- [Inimigos: tabelas completas](docs/planning/manifests/enemies.canonical-tables.json)
- [Inimigos: extração complementar](docs/planning/manifests/enemies.audit.json)
- [NPCs e ambientes](docs/planning/manifests/npcs-world.audit.json)
- [AI_STATE: estado para retomada](AI_STATE.md)

**Achado P0-001:** as tabelas das cinco classes somam **24.304 frames corporais**, enquanto seus totais globais anunciam **25.616** (diferença de **1.312**). São divergências documentais não resolvidas, não frames já criados. O manifesto guarda a soma por classe e linha; não produzir frames compensatórios sem reconciliação.

O inventário original de 22 especificações permanece preservado em `arte e animações/docs/`. Os arquivos de `docs/planning/` e `production_manifest.json` são documentação e metadados, não assets binários.

---

## Inventário verificado

| Categoria | Documentos Markdown | Diretório real |
|---|---:|---|
| Classes jogáveis | **5** | `arte e animações/docs/Classes/` |
| Inimigos | **9** | `arte e animações/docs/Inimigos/` |
| NPCs de serviço | **6** | `arte e animações/docs/Npcs/` |
| Mapas / tilesets | **2** | `arte e animações/docs/Tilesets/` |
| **Total de especificações .md** | **22** | |

Além das 22 especificações Markdown, existe este `readme.md` na raiz. A cópia auxiliar `.txt` do Esqueleto Feiticeiro foi removida; sua especificação permanece em `.md`. O inventário acima representa os caminhos atualmente presentes na branch `main`, não a quantidade de assets gráficos produzidos.

## Estrutura atual do repositório

```text
sprite-direction/
├── readme.md                        # Este índice (grafia minúscula)
└── arte e animações/
    └── docs/
        ├── Classes/                 # 5 arquivos .md
        ├── Inimigos/                # 9 arquivos .md
        ├── Npcs/                    # 6 arquivos .md
        └── Tilesets/                # 2 arquivos .md
```

**Atenção aos caminhos:** o diretório se chama exatamente `arte e animações` (com espaços e acentos); as pastas são `Classes`, `Inimigos`, `Npcs` e `Tilesets`. Em ambientes com diferenciação de maiúsculas/minúsculas, respeite a capitalização e o nome literal de cada arquivo.

## Índice de documentos

### Classes (5)

| Documento | Conteúdo / função |
|---|---|
| [Arqueiro](<arte%20e%20anima%C3%A7%C3%B5es/docs/Classes/Spritesheet%20Arqueiro.md>) | Arcos, bestas, aljavas, munições e combate à distância |
| [Espadachim](<arte%20e%20anima%C3%A7%C3%B5es/docs/Classes/Spritesheet%20Espadachim.md>) | Combos de espada, defesa e equipamentos modulares |
| [Mago](<arte%20e%20anima%C3%A7%C3%B5es/docs/Classes/Spritesheet%20Mago.md>) | Conjuração elemental, projéteis, barreiras e teleporte |
| [Necromante (Necromancer)](<arte%20e%20anima%C3%A7%C3%B5es/docs/Classes/Spritesheet%20Necromancer.md>) | Invocações, maldições, magia sombria e estruturas ósseas |
| [Pugilista](<arte%20e%20anima%C3%A7%C3%B5es/docs/Classes/Spritesheet%20Pugilista.md>) | Combate desarmado, combo de cinco golpes, artes marciais, manoplas e habilidades próprias |

### Inimigos (9)

| Documento | Conteúdo / função |
|---|---|
| [Aranha Gigante](<arte%20e%20anima%C3%A7%C3%B5es/docs/Inimigos/Spritesheet%20Aranha%20gigante.md>) | Criatura aracnídea, ataques e animações |
| [Esqueleto Feiticeiro](<arte%20e%20anima%C3%A7%C3%B5es/docs/Inimigos/Spritesheet%20Esqueleto%20feiticeiro.md>) | Conjurador morto-vivo e efeitos necromânticos |
| [Esqueleto Guerreiro](<arte%20e%20anima%C3%A7%C3%B5es/docs/Inimigos/Spritesheet%20Esqueleto%20guerreiro.md>) | Combatente esquelético |
| [Goblin](<arte%20e%20anima%C3%A7%C3%B5es/docs/Inimigos/Spritesheet%20goblim.md>) | Inimigo inicial; nome do arquivo mantido como está |
| [Lich](<arte%20e%20anima%C3%A7%C3%B5es/docs/Inimigos/Spritesheet%20Lich.md>) | Conjurador de elite, invocações e magia sombria |
| [Mini-Dragão Vermelho](<arte%20e%20anima%C3%A7%C3%B5es/docs/Inimigos/Spritesheet%20Mini-drag%C3%A3o%20vermelho.md>) | Criatura dracônica e ataques de fogo |
| [Minotauro](<arte%20e%20anima%C3%A7%C3%B5es/docs/Inimigos/Spritesheet%20Minotauro.md>) | Combatente pesado, investidas e golpes sísmicos |
| [Orc](<arte%20e%20anima%C3%A7%C3%B5es/docs/Inimigos/Spritesheet%20Orc.md>) | Combatente de machado, escudo e habilidades |
| [Stone Golem](<arte%20e%20anima%C3%A7%C3%B5es/docs/Inimigos/Spritesheet%20stone%20golem.md>) | Criatura rochosa, impactos e habilidades elementais |

### NPCs (6)

| Documento | Conteúdo / função |
|---|---|
| [Ferreiro](<arte%20e%20anima%C3%A7%C3%B5es/docs/Npcs/dire%C3%A7%C3%A3o%20de%20anima%C3%A7%C3%B5es%20ferreiro.md>) | Oficina, bigorna, marteladas e atendimento |
| [Curandeira](<arte%20e%20anima%C3%A7%C3%B5es/docs/Npcs/dire%C3%A7%C3%A3o%20de%20anima%C3%A7%C3%B5es%20curandeira.md>) | Preparação de ervas, poções e cura |
| [Guardião do Armazém](<arte%20e%20anima%C3%A7%C3%B5es/docs/Npcs/dire%C3%A7%C3%A3o%20de%20anima%C3%A7%C3%B5es%20armazem.md>) | Baú, conferência e armazenamento |
| [Mercador de Equipamentos](<arte%20e%20anima%C3%A7%C3%B5es/docs/Npcs/dire%C3%A7%C3%A3o%20de%20anima%C3%A7%C3%B5es%20Mercador%20de%20equipamentos.md>) | Loja, inspeção e apresentação de equipamento |
| [Mercador de Poções](<arte%20e%20anima%C3%A7%C3%B5es/docs/Npcs/dire%C3%A7%C3%A3o%20de%20anima%C3%A7%C3%B5es%20Mercador%20de%20po%C3%A7%C3%B5es.md>) | Balcão de poções e consumíveis |
| [Treinador de Mascotes](<arte%20e%20anima%C3%A7%C3%B5es/docs/Npcs/dire%C3%A7%C3%A3o%20de%20anima%C3%A7%C3%B5es%20Treinador%20de%20Mascote.md>) | Treinamento e interação com pet |

### Tilesets (2)

| Documento | Conteúdo / função |
|---|---|
| [Primeira cidade](<arte%20e%20anima%C3%A7%C3%B5es/docs/Tilesets/Spritesheet%20e%20Tilesets%20primeira%20cidade.md>) | Cidade segura, edifícios, interiores e integração dos seis NPCs |
| [Primeira área de caça](<arte%20e%20anima%C3%A7%C3%B5es/docs/Tilesets/Spritesheet%20e%20Tilesets%20Primeira%20area%20de%20ca%C3%A7a.md>) | Mundo aberto ligado à cidade, sub-regiões, spawns e progressão |

## Padrões compartilhados de produção

### Direção de arte

- **Pixel Art Chibi de fantasia medieval sombria:** silhuetas legíveis, contornos coerentes, paleta controlada, materiais consistentes e proporções compatíveis entre personagens, NPCs, monstros e cenário.
- **Perspectiva isométrica 2:1** para mapas e objetos; tiles de **64 × 32 px** como referência inicial dos documentos ambientais, sujeitos a validação contra sprites aprovados antes de produzir o pacote.
- **8 direções de animação:** `N, NE, E, SE, S, SW, W, NW`; preferir arte própria por orientação, sem espelhamentos que invertam anatomia ou detalhes.
- **Transparência RGBA real** para sprites e VFX; sem bordas, halos, tremores, sangramento entre células, borrões ou deslocamento involuntário. As pranchas de apresentação podem usar fundo magenta técnico, que **não faz parte** dos sprites de jogo.
- **Ancoragem e profundidade:** pivô estável no contato com o chão, camadas de oclusão, colisões, recortes e ordenação isométrica documentados.
- **Animação funcional:** Idle/Walk e estados sustentados com loops perfeitos; ataques com antecipação, execução, impacto e recuperação; morte termina estática. Projetéis e VFX devem ser independentes e sincronizados por eventos.

### Personagens jogáveis e equipamentos

As cinco classes partem de **corpo-base humanoide com roupas íntimas medievais discretas**, sem armas ou armaduras permanentes. A aparência deve mudar conforme os itens equipados (cabeça, torso, ombros, braços, mãos, pernas, pés, costas, arma principal/secundária e acessórios).

A camada visual de cada item deve respeitar **animação, direção, frame, âncora e profundidade** do corpo-base; perfis específicos são necessários para espadas, cajados, manoplas, arcos/bestas e outras empunhaduras. Cada classe possui conjuntos particulares de combos, skills, animações de dano e VFX. Interrupções, janelas de combo e impactos devem estar registrados em metadados.

### NPCs

Os **seis NPCs principais** são **estacionários**, vinculados a seus pontos de atendimento; os mini-prompts descrevem **quatro animações sequenciais conectadas em um ciclo de 40 frames** por NPC. O cenário deve fornecer bigorna, bancada, baú, expositor ou área de treino, conforme a função, sem duplicar elementos já embutidos nos sprites.

| NPC | Região/estabelecimento planejado na cidade |
|---|---|
| Ferreiro | Noroeste — oficina e bigorna |
| Curandeira | Nordeste — casa de cura e jardim medicinal |
| Guardião do Armazém | Sudoeste — depósito e balcão |
| Treinador de Mascotes | Oeste — cercado de treinamento |
| Mercador de Poções | Sudeste — loja de consumíveis |
| Mercador de Equipamentos | Leste — loja de armas e armaduras |

Os posicionamentos acima são **propostas de layout descritas no documento da cidade**; não representam coordenadas de mapa já implementadas.

### Ambientes

**[Primeira cidade](<arte%20e%20anima%C3%A7%C3%B5es/docs/Tilesets/Spritesheet%20e%20Tilesets%20primeira%20cidade.md>)** — plano de `Vila das Cinzas` (nome provisório): praça central, seis estabelecimentos, interiores, residências, taverna, mural de missões, ruas, muros, portões, objetos, colisões, iluminação e integração de NPCs. Planejamento de produção **C1–C10**; grade de referência **96 × 96 tiles lógicos**.

**[Primeira área de caça](<arte%20e%20anima%C3%A7%C3%B5es/docs/Tilesets/Spritesheet%20e%20Tilesets%20Primeira%20area%20de%20ca%C3%A7a.md>)** — `Campos da Fronteira` (nome provisório): mundo aberto conectado imediatamente às saídas da cidade, sem quatro mapas de caça isolados. Planejamento **A1–A10**, grade de referência **160 × 160 tiles lógicos** e oito sub-regiões: Campos Externos, Estrada Antiga, Bosque Sombrio, Colinas Pedregosas, Ruínas da Fronteira, Cemitério Esquecido, Terreno das Cinzas e Santuário Rochoso. Prevê distribuição dos nove tipos de inimigos conforme ecologia e dificuldade.

**A numeração C1–C10/A1–A10 indica etapas planejadas, não implementação concluída.** Tamanhos de mapa e nomes são propostas ajustáveis.

## Como usar este repositório

1. Escolha a categoria e abra o documento vinculado no índice.
2. Consulte o padrão compartilhado e confirme a escala, a direção de arte e os sprites de referência aprovados.
3. Produza **spritesheets funcionais por animação**, com suas oito direções quando aplicável; não considere uma folha de apresentação um substituto.
4. Exporte PNG RGBA e metadados JSON de recorte, FPS, loops, âncoras, eventos e colisões; se necessário, organize em atlas com padding/extrusão para evitar bleeding.
5. Faça prévias em GIF a partir **dos mesmos frames** destinados ao jogo e valide direção por direção, incluindo loops, transições, combate e renderização com equipamentos.
6. No cenário, monte tilesets em camadas com autotiling, objetos, colisões, navegação e oclusão; integre os pontos fixos de NPCs e, depois, os spawns da área aberta.
7. Só marque uma entrega como concluída após inspeção visual e testes na escala real de gameplay.

## Convenção sugerida para arquivos futuros — ainda não presente

```text
assets/                         # SUGESTÃO: não existe neste inventário
├── characters/
│   ├── classes/<classe>/body/
│   ├── classes/<classe>/equipment/
│   ├── enemies/<inimigo>/
│   └── npcs/<npc>/
├── vfx/
├── projectiles/
└── world/
    ├── first_city/{tilesets,buildings,props,animations,maps}/
    └── hunting_area_01/{tilesets,props,animations,landmarks,maps}/
```

A estrutura acima é **recomendação de saída** para produção dos gráficos. Não confundir com diretórios já criados neste repositório. Os nomes específicos de PNG/JSON e a organização detalhada estão nos documentos de cada categoria.

## Pendências e observações da auditoria documental

- **Pugilista corrigido:** [`Spritesheet Pugilista.md`](<arte%20e%20anima%C3%A7%C3%B5es/docs/Classes/Spritesheet%20Pugilista.md>) agora contém a especificação própria da classe (combate desarmado, cinco golpes de combo, habilidades e modularidade), conforme verificação do conteúdo atualizado.
- **Duplicidade resolvida:** a cópia `Spritesheet Esqueleto feiticeiro.txt` foi removida. O documento canônico é [`Spritesheet Esqueleto feiticeiro.md`](<arte%20e%20anima%C3%A7%C3%B5es/docs/Inimigos/Spritesheet%20Esqueleto%20feiticeiro.md>).
- **Nomes históricos:** `Spritesheet goblim.md` mantém a grafia atual do repositório; evitar renomear sem atualizar os links e demais referências.
- **Formatação variável:** alguns prompts estão em Markdown estruturado e outros em texto simples dentro de arquivos `.md`. A padronização editorial pode ser feita posteriormente, preservando o conteúdo.
- **Contagens de frames:** os totais anunciados nos prompts são metas documentais e **devem ser recalculados e auditados** antes da produção em massa. Não assumir que todos os somatórios já foram validados.
- **Assets ainda não gerados:** não existem neste inventário as imagens, animações exportadas ou mapas jogáveis prometidos nos prompts. Documentação **não equivale a implementação**.

## Escopo e manutenção

Este repositório concentra a **direção de criação dos assets**. A engine, a lógica de combate, o backend, a economia e a publicação do MMORPG não são implementados pelos documentos em si.

Ao adicionar ou renomear um documento, **atualize este README** e mantenha os links relativos exatos. Ao produzir assets, diferencie claramente arquivos planejados de arquivos efetivamente versionados e registre o estado real das entregas.

---
*Inventário conferido na branch `main` em 09/11/2026. Referência de projeto: [marmitero/sprite-direction](https://github.com/marmitero/sprite-direction).*
