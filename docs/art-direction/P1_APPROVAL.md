# P1 — Termo de encerramento e baseline de direção artística

**Data:** 2026-11-09  
**Estado:** CONCLUÍDA — direção visual aprovada expressamente pelo usuário e solicitada conclusão da P1.  
**Próxima fase:** P2 — pipeline técnico; **não iniciada, aguardando autorização**.

## Escopo aprovado/congelado

- Identidade: fantasia medieval sombria com pixel art chibi e identidade visual original.
- Projeção: mapa isométrico 2:1; tile lógico referencial 64 × 32 px.
- Direções canônicas de personagens móveis: `N, NE, E, SE, S, SW, W, NW`, sem espelhamento incorreto de assimetrias.
- Personagens: proporção de altura visível de ~40–48 px para classes/NPCs, ~32–48 px para criaturas pequenas/médias e ~64–96 px para grandes, **como faixas de referência**, não dimensões rígidas de atlas.
- Renderização: pixel art limpa, nearest-neighbor, sem blur, sem filtro de suavização ou halos.
- Iluminação: direção principal alto-esquerda em coordenadas de tela; contraste e materiais consistentes; efeitos de luz adicionais como VFX separados.
- Paleta: categorias e tons do `palette.p1.json`; tons auxiliares permitidos para continuidade e legibilidade, com alteração rastreada.
- Corpo-base de personagens jogáveis: roupa íntima medieval discreta e opaca, sem armadura/arma permanentemente desenhadas no corpo.
- Equipamentos: camadas independentes (cabeça, tronco, braços, mãos, pernas, pés, costas e armas), com âncoras e ordem de desenho dinâmica.
- VFX e projéteis separados; personagens usam pivô estável no chão e movimentação do mundo controlada pela engine.
- NPCs de serviço: ciclo estacionário de 40 frames como previsto nos documentos, quando não há revisão técnica justificada.
- Formato futuro: PNG RGBA transparente + JSON de metadados + GIF derivado dos mesmos frames, testes em escala real. A exportação funcional pertence à P2.

## Aprovação visual vs entregáveis técnicos

O usuário **aprovou a direção visual** apresentada nesta conversa e autorizou o encerramento. Essa aprovação se refere à linguagem estética e ao padrão técnico de referência, **não certifica** spritesheet final, animação de oito direções, atlas, colisões ou imagens-piloto utilizáveis. Não existem no GitHub assets PNG jogáveis gerados como parte desta P1.

Os moodboards usados na conversa são inspirações conceituais; textos embutidos nas imagens, como dimensões contraditórias e selos de conclusão, não substituem os dados canônicos deste documento. O `P1_TECHNICAL_BOARD.svg` é um diagrama explicativo reproduzível, não atlas de personagem.

## Política aprovada de frames

O usuário autorizou recalcular, aumentar ou reduzir frames, reparar loops, poses intermediárias, recortes e sincronização quando necessário à fluidez ou funcionamento. Cada revisão deve manter histórico antes/depois, justificativa, mudanças nos manifests e validação visual/técnica; nenhuma adição artificial para igualar total textual é permitida.

A divergência P0-001 permanece documentada: **24.304 frames somados nas linhas das cinco classes vs 25.616 anunciados, delta +1.312**. Este fechamento congela a política de correção, **não** a contagem definitiva por ação, que será refinada durante produção validada.

## Referências canônicas

- [Style guide](STYLE_GUIDE_P1.md)
- [Paleta](palette.p1.json)
- [Diagrama técnico](P1_TECHNICAL_BOARD.svg)
- [Brief de pilotos futuros](PILOT_REFERENCES.md)
- [Correção de frames](FRAME_RECONCILIATION.md)
- [Planejamento completo](../planning/PLANO_MESTRE.md)
- [Contrato de entrega](../planning/CONTRATO_ENTREGA.md)

## Gate P1

- [x] Direção visual expressamente aprovada pelo usuário.
- [x] Perspectiva e faixas de escala documentadas.
- [x] Paleta-base e iluminação definidas.
- [x] Oito direções e arquitetura modular especificadas.
- [x] Política de recontagem/correção formalizada.
- [x] README, AI_STATE e manifesto atualizados para refletir encerramento.
- [ ] Amostras de sprites jogáveis produzidas/testadas — **fora da P1; executadas pela P2/P3 quando autorizadas**.
- [ ] Implementação do pipeline técnico — **P2 ainda não autorizada**.

## Critério de alterações futuras

O padrão visual fica congelado para produção. Ajustes técnicos de escala/frames são permitidos se melhorarem integração e forem documentados, sem mudar arbitrariamente a estética aprovada. Mudança material de estilo requer nova autorização explícita.

**Checkpoint:** P1 fechada documentalmente e por aceite visual; pronta para planejar P2 quando o usuário solicitar.
