# Planejamento mestre — Sprite Direction (P0 a P11)

Data: 2026-11-09. Etapas P0 e P1 concluídas; P1 aprovada visualmente e congelada. Próxima etapa P2 **não iniciada nem autorizada**.

## Missão

Construir pacote gráfico funcional para MMORPG 2D isométrico de fantasia medieval sombria, em pixel art chibi: cinco classes humanoides com equipamentos modulares, nove inimigos, seis NPCs estacionários, cidade inicial e área contínua de caça. Os documentos em `arte e animações/docs` são as fontes de requisitos. Assets binários não foram produzidos.

## Etapas, entradas, entregas e gates

| Etapa | Dependência | Entregáveis | Gate |
|---|---|---|---|
| P0 Auditoria | README + 22 docs | Manifestos, matriz de escopo, riscos e estado | Validação dos documentos e ciência das divergências |
| P1 Direção artística | P0 aprovada | Referências aprovadas, paleta, proporções, vistas, tiles de teste | Congelamento visual formal |
| P2 Pipeline | P1 | Esquema PNG/atlas/JSON, exportador, QA e preview | Teste de reprodução de frames reais |
| P3 Corpo e equipamento | P2 | Corpo-base, âncoras, slots, máscaras, overlays | Troca de roupa/arma sem jitter em oito direções |
| P4 Classes | P3 | Espadachim, Arqueiro, Mago, Necromante, Pugilista | Por-classe: skills, combos, camadas, eventos e QA |
| P5 Inimigos | P2 + arte congelada | 9 entidades, VFX/ataques próprios | 8 direções e estados funcionais |
| P6 NPCs | P2 + arte congelada | 6 ciclos de 40 frames + props/pet | Cinco loops completos sem saltos |
| P7 Cidade | P2 + escala fechada | C1–C10: terreno, arquitetura, props, mapas, interiores | Colisão, oclusão, navegação e pontos dos NPCs |
| P8 Caça | P7 interfaces + P5 | A1–A10: oito sub-regiões e mapa integrado | Conexão contínua, spawns, colisão |
| P9 VFX | P4–P8 | Reúso e integração de VFX, emissões e efeitos | Evento/framerate/ancoragem corretos |
| P10 QA | P3–P9 | Cena demo HTML5 e testes visual/técnico | Zero bloqueadores de recorte/frames |
| P11 Release | P10 | v1.0.0, README, inventário e guias | Todos os assets obrigatórios aprovados |

## Política de produção

- Um lote contém uma entidade ou subconjunto pequeno e verificável, nunca todas as folhas num único pedido.
- Cada frame tem direção, ordem, duração/FPS, origem/pivô, limites, colisor/alcance quando aplicável, camada e eventos.
- Armas, armaduras, projéteis e VFX não são pixels permanentemente embutidos no corpo humanoide.
- Oito direções para classes e monstros; NPCs estacionários têm ciclos de instalação definidos.
- Toda exportação usa transparência RGBA; fundo magenta fica restrito a folhas de apresentação.
- GIFs devem ser derivados dos mesmos frames exportados para runtime.
- Nenhuma habilidade opcional é aprovada tacitamente como obrigatória.
- Cada lote exige avaliação visual, aritmética e runtime; reprovados são corrigidos antes de avançar.
- Atualizar manifestos, README e AI_STATE após cada lote e ao fim de cada fase.
- P0-001 exige revisão por animação antes de fechar contagens finais; usuário autorizou correções de frames com justificativa e QA. Ver `docs/art-direction/FRAME_RECONCILIATION.md`.

## Sequência de produção detalhada

- P4.1 Espadachim; P4.2 Arqueiro; P4.3 Mago; P4.4 Necromante; P4.5 Pugilista.
- P5.1 Goblin + Esqueleto Guerreiro; P5.2 Orc + Aranha; P5.3 Esqueleto Feiticeiro + Mini-Dragão; P5.4 Minotauro + Stone Golem; P5.5 Lich.
- P6.1 Ferreiro + Curandeira; P6.2 mercadores; P6.3 Armazém + Treinador.
- P7 contém subetapas C1–C10; P8 contém A1–A10, conforme documentos de Tilesets.

## Convenções técnicas propostas (pendentes da P1/P2)

```text
assets/characters/{classes,enemies,npcs}/<id>/
assets/equipment/<slot>/<item_id>/
assets/projectiles/<id>/
assets/vfx/<id>/
assets/world/{first_city,hunting_area_01}/
previews/gifs/
tools/{exporters,validators,atlas-builder}/
demo/
```

Os manifests devem distinguir `planned`, `in_progress`, `generated`, `validated`, `approved`. Não marcar aprovação por texto somente.

## Riscos e mitigação

- **Escala divergente:** fazer amostra com humanoide/monstro/NPC/prop antes de produção em massa.
- **Danos em pixel art ao gerar intermediários:** validar frame a frame, trabalhar com keyframes e ajustes supervisionados.
- **Rig modular instável:** criar teste demonstrável de overlays antes das classes completas.
- **Atlas bleed e halos:** testar transparência, padding e extrusão com câmera em movimento.
- **Volume de frames elevado:** produção em lotes, IDs versionados, contagem verificada, armazenamento e retomada por checkpoints.
- **Falta de contrato entre mapas:** determinar bordas, colisões, pivôs e camada de profundidade antes da montagem.

## Próxima ação

P1 aprovada e encerrada em 09/11/2026; consultar `docs/art-direction/P1_APPROVAL.md`. Aguardar autorização separada para iniciar P2, sem gerar assets técnicos antecipadamente.
