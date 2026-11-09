# P2 — Pipeline técnico de sprites (implementação)

## Escopo

CLI Python/Pillow para **frames artísticos já existentes**. Gera atlas PNG RGBA, JSON de animações/direções e GIFs opcionais para QA; inclui validador e visualizador HTML5. **Não gera arte, não substitui P3 nem altera o padrão P1.** Dependência: Python >=3.11 + Pillow >=10.

## Instalação

```bash
python -m pip install -r requirements-p2.txt
python -m unittest discover -s tests -v
```

## Entrada

```text
samples/input/
├── idle/
│   ├── N/000.png,001.png,...
│   ├── NE/000.png,...
│   ├── E/...
│   ├── SE/...
│   ├── S/...
│   ├── SW/...
│   ├── W/...
│   └── NW/...
└── attack/
    └── N/000.png,...
```

NPC fixo: use `fixed` no lugar da direção. Arquivos devem ser PNG **RGBA**, com canvas idêntico **dentro de cada sequência direção/animação**, numeração iniciando em 000, frames consecutivos e pivô padronizado no canvas. As sequências com oito direções devem possuir todas as direções antes da aprovação do asset: o exportador aceita subconjuntos para trabalhos iterativos, mas **não os declara completos**. Nome dos arquivos: 000.png, 001.png etc. Não misturar imagens com fundo magenta em runtime.

## Comandos

```bash
python tools/sprite_pipeline.py build \
  --input samples/input \
  --output output \
  --asset espadachim \
  --atlas-size 1024 --padding 2 --fps 12 --gif
python tools/sprite_pipeline.py validate --output output --asset espadachim
python -m http.server 8000
```

Abra `http://localhost:8000/demo/` e defina o caminho do JSON, por exemplo `/output/espadachim.json`.

## Saída

```text
output/
├── espadachim_atlas_000.png
├── espadachim_atlas_001.png  # se necessário
├── espadachim.json
├── espadachim_idle_N.gif     # somente com --gif
└── ...
```

O JSON contém `schema_version`, `asset_id`, `direction_order`, `fps`, `loop`, `atlases` (arquivo/dimensões/SHA256), e `frames[]`: ID, animação, direção, índice, atlas, `frame` (retângulo dentro do atlas), `source_size` (canvas original), `sprite_source_size` (retângulo de corte e deslocamento), `pivot` (em pixels no canvas original), `duration_ms`, `empty`, hash do original e `events` (lista inicialmente vazia). O pipeline não inventa eventos de impacto. O motor ou um autor de metadados deverá registrá-los em etapa seguinte, sem substituição arbitrária de arte.

### Reconstituição de posição no renderizador

Se o pivot do mundo é `(worldX,worldY)`, desenhar o frame em `worldX + (sprite_source_size.x-pivot.x)` e `worldY + (sprite_source_size.y-pivot.y)`, respeitando escala e ordem de profundidade. **Não centralizar cada retângulo cortado**, pois isso introduz tremor.

## Validações implementadas

- PNG estritamente RGBA, dimensões válidas e frame numbers consecutivos.
- Canvas idêntico dentro da sequência; nomes de direção válidos.
- Atlas com padding >=2 e extrusão de bordas; suporte a várias páginas.
- JSON com frames únicos, ordem por animação/direção e retângulos dentro do atlas.
- Validação de ocupação e padding entre células; integridade SHA256 das páginas.
- Metadados para reconstruir o canvas original e pivot estável.
- GIF de preview por sequência a partir dos frames PNG originais.
- Visualizador HTML5 com zoom nearest-neighbor, direções, animações, passo e referência de pivô.
- Suite unittest com casos de sucesso/falha e adulteração.

## Limites conhecidos

- Não garante qualidade artística, fluidez real, consistência anatômica, ou sincronização automática entre equipamentos.
- Não detecta pixels incorretos dentro de sprite visualmente mal feito.
- Não cria animações nem corrige frames por interpolação.
- O `pivot` atual por padrão é `(sourceWidth//2, sourceHeight-1)`; artistas devem centralizar a base do personagem no canvas. Pivôs por entidade e animação, eventos/hitboxes autorais e validações de sobreposição de camadas são extensões posteriores.
- A extrusão é RGBA das bordas, inclusive transparente; textura final continua com filtro nearest-neighbor.
- GIF pode ter limitação de transparência/paleta por ser formato indexado: não é fonte de produção.
- Os testes unitários usam formas sintéticas geradas em temporário; **não são assets aprovados nem entram no pack**.
- A validação de completude (8/8 direções, lista de estados, equipamento, VFX) depende do manifesto do asset, não apenas do atlas.
- Se a CI não executar no ambiente GitHub, registrar explicitamente; commit de testes **não equivale a testes executados**.

## Critério de passagem P2 → P3

Pipeline versionado, testes unitários executados e aprovados, inspeção manual no visualizador com uma amostra **técnica** e contrato de metadados revisado. P3 só começa após aprovação explícita do usuário. Guia de arte congelado: `docs/art-direction/P1_APPROVAL.md`.

## Política de frames

Autorização do usuário para recálculos/correções visando fluidez; seguir `docs/art-direction/FRAME_RECONCILIATION.md` e nunca preencher a diferença de 1.312 frames apenas para bater os totais textuais.
