# P3 — Primeiro piloto modular: entrega técnica e checklist (HISTÓRICO REPROVADO)

## ALERTA DE OBSOLESCÊNCIA

**Reprovado artisticamente pelo usuário em 09/11/2026.** A arte geométrica não deve ser utilizada no jogo nem contar como P3 aprovada. Seus 896 quadros foram arquivados em `tests/fixtures/legacy_p3_geometric/` somente para inspeção/regressão do pipeline. As referências abaixo aos caminhos `assets/characters/classes/shared_humanoid/` são históricas e não existem mais na pasta de produção. **Status atual: [P3 ART REWORK](P3_ART_REWORK.md).**

Data: 2026-11-09. Branch `main`. Estado: **piloto funcional gerado e testado, aguardando validação visual do usuário**. P4 não autorizada.

## Entrega concretamente produzida

- Corpo-base humanoide em oito orientações: `N, NE, E, SE, S, SW, W, NW`.
- Animações `idle` e `walk`, **8 frames por orientação/ação**, ou **128 frames por camada**.
- **7 camadas**: `body` (roupa-base discreta, sem armadura/arma embutidas), `hair`, `chest`, `hands`, `feet`, `main_hand` (espada), `off_hand` (escudo). A roupa/equipamentos constituem um primeiro kit técnico e podem ser ocultados sem redesenhar o corpo.
- **896 frames** provenientes de gerador original de pixel art, divididos em sete manifestações de atlas P2.
- Arquivos de produção versionados em `assets/characters/classes/shared_humanoid/`: PNG atlas, JSON por camada, contact sheet PNG, prévia GIF de caminhada equipada e `p3_pilot_manifest.json`.
- Gerador de reprodução determinística em `tools/generate_p3_pilot.py`, testes em `tests/test_p3_pilot.py`.
- Visualizador de equipamento com toggles em `demo/p3.html`, usa os próprios JSON e PNG da entrega.

## Consulta de arquivos

- [Sprites e prévias em GitHub](../../assets/characters/classes/shared_humanoid/)
- [Folha de comparação](../../assets/characters/classes/shared_humanoid/p3_pilot_contact_sheet.png)
- [Animação Walk SE equipada](../../assets/characters/classes/shared_humanoid/p3_walk_SE_equipped.gif)
- [Manifesto do piloto](../../assets/characters/classes/shared_humanoid/p3_pilot_manifest.json)
- [Compositor visual](../../demo/p3.html)
- [Pipeline de origem](../../tools/generate_p3_pilot.py)

## Como reproduzir

```bash
python -m pip install -r requirements-p2.txt
python -m unittest discover -s tests -v
python -m tools.generate_p3_pilot --output-root build/p3
python -m http.server 8000
```

Abra `http://localhost:8000/demo/p3.html` com o repositório clonado. O visualizador usa os atlases gerados que já estão versionados; mantenha o diretório `assets/` ao lado de `demo/`.

## Validação comprovada

- [GitHub Actions P3 run #1](https://github.com/marmitero/sprite-direction/actions/runs/42680063240) — **success**.
- 10 testes executados e aprovados (6 do P2 e 4 novos do P3).
- Gerador reportou `{"status":"BUILT","layers":7,"total_frames":896}`.
- Verificações P3: integridade e recortes de 7 manifests, 8 orientações, 16 sequências por camada (2 ações × 8 direções), 128 frames por camada, 64×72 RGBA, pivô compartilhado (32,71), variação de poses Walk e prévias PNG/GIF.
- GitHub Actions publicou arquivos binários na branch main e também um artifact baixável do próprio run.

## Limites e transparência

- A arte aqui é **pixel art procedimental original em formato de piloto**, com geometria desenhada pixel a pixel através do Pillow. Ela **não** é a recriação fiel dos personagens ricos em detalhes do moodboard P1, que foi aprovado como direção artística; deve passar por inspeção visual e possível polimento/retrabalho antes de declarar o corpo-base final.
- O pipeline implementa teste geométrico de encaixe e sincronização; não valida automaticamente apelo visual, ergonomia de combate ou animação fluida aos olhos do usuário.
- Idle/Walk são as primeiras animações piloto; não foram produzidos Attack/Hurt/Died/Skills, nem o catálogo inteiro de equipamentos das classes (P4).
- A ordem de camadas está fixa neste primeiro compositor. A oclusão dinâmica de espada/escudo/capa por direção e frame permanece extensão importante antes de considerar o sistema modular final.
- As âncoras de pulso são implícitas na geometria fonte do piloto; metadados explícitos de ancoragem por frame, máscaras e colisões ainda devem ser construídos na expansão técnica do conjunto. Não atribuir a este piloto garantias que não foram testadas.
- A direção P1 continua congelada; a geração procedimental não modifica seu contrato e não deve ser usada como pretexto para aceitar downgrade estético.

## Aceite e próximos passos

- [x] Arquivos reais PNG RGBA + atlas + JSON publicados.
- [x] Corpo em 8 direções com animações Idle e Walk.
- [x] 6 componentes independentes além do corpo.
- [x] Frames/pivôs sincronizados entre camadas.
- [x] GIF e contact sheet produzidos.
- [x] Testes e exportação P2 aprovados em CI.
- [ ] Revisão humana do resultado visual comparado à P1.
- [ ] Polimento de detalhes/poses conforme resultado da revisão.
- [ ] Oclusão variável e âncoras por frame — para ciclo de refinamento.
- [ ] Aceite do usuário para considerar o piloto definitivo e liberar P4.

**Checkpoint:** P3 piloto entregue tecnicamente e documentado, **aguardando aprovação estética/funcional**. NÃO iniciar P4 automaticamente.
