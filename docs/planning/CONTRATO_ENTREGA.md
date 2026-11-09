# Contrato de arte e entrega (rascunho P0)

## Escopo fechado desta auditoria

5 classes, 9 inimigos, 6 NPCs, 2 ambientes — 22 documentos fontes. VFX, equipamentos e projéteis são dependências desses recursos, sem contagem final fechada.

## Formatos de entrega propostos

- `PNG` RGBA por animação, orientação ou atlas; nenhum fundo magenta nos PNG de runtime.
- `JSON` declarando `asset_id`, `source`, `animation`, `direction`, `frames` (`rect`, `duration_ms`, `pivot`, `layer`, `events`), `loop`, `origin`, `hitboxes`.
- GIF de QA extraído dos PNG de produção, nunca regenerado independentemente.
- Documento do asset com nome de entrada, lista de animações, dependências e checklist.
- Mapas e tilesets com camadas de piso/prop/telhado/oclusão, colisão, navegação e pontos de interação; formato exato de exportação será fixado na P2.

## Gate mínimo por lote

1. Aderência à arte congelada.
2. Direções e frames completos, sem duplicação indevida.
3. Grade, pivô, escala e ordenação de camadas consistentes.
4. Transparência real e atlas sem vazamento/halos.
5. Loop sem salto e sequência de combate sincronizada com eventos.
6. Equipamentos mudam sem reposicionar incorretamente o corpo.
7. JSON corresponde exatamente aos PNG exportados.
8. Preview reproduz pelo menos cinco ciclos, e estado terminal não repete indevidamente.
9. Teste mínimo em demo HTML5, incluindo zoom e movimento de câmera.
10. Aceite explícito do lote; checklist e commit registrados.

## Política de mudança

Qualquer mudança de escopo, nomes de arquivos, número de frames ou estilo deve gerar alteração rastreável no manifesto e documentação, com comparação antes/depois. Os números do quadro P0 têm divergências e **não são uma ordem de gerar frames extras**.
