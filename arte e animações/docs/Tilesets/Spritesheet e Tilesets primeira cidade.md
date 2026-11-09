# PRIMEIRA CIDADE — PACOTE COMPLETO DE SPRITESHEETS, TILESETS E CONSTRUÇÃO ISOMÉTRICA

## MMORPG 2D — PIXEL ART CHIBI — FANTASIA MEDIEVAL SOMBRIA

**Tipo de pacote:** Cenário completo de cidade inicial  
**Ambiente:** Cidade medieval de fantasia, segura e habitada  
**Referência:** Diablo II e MMORPGs isométricos clássicos  
**Direção artística:** Pixel Art Chibi de fantasia medieval sombria  
**Perspectiva:** Isométrica 2:1  
**Construção:** Tilesets modulares, spritesheets, objetos independentes e camadas de profundidade  
**Plataforma:** Jogo 2D para navegador, compatível com HTML5 e engines 2D  
**NPCs principais:** Ferreiro, Curandeira, Guardião do Armazém, Treinador de Pets, Comerciante de Poções e Comerciante de Equipamentos  
**Escopo:** Somente a primeira cidade e seus espaços internos. Não produzir a primeira área de caça nesta etapa.

---

# 1. MISSÃO PRINCIPAL

Criar o pacote artístico e técnico completo da primeira cidade do MMORPG.

A cidade deve funcionar como o principal ponto de encontro e preparação dos aventureiros, reunindo estabelecimentos comerciais, serviços, locais de descanso, NPCs, ambientação e estruturas que poderão receber novos sistemas posteriormente.

Não criar uma simples ilustração de cidade.

O objetivo é entregar um ambiente isométrico construído a partir de elementos reais, reutilizáveis, editáveis e corretamente organizados.

O pacote deve permitir:

- Construir o mapa completo.
- Posicionar todos os edifícios.
- Criar ruas e praças.
- Definir locais transitáveis.
- Aplicar colisões.
- Posicionar NPCs.
- Implementar interações.
- Exibir jogadores com equipamentos modulares.
- Renderizar personagens corretamente atrás e à frente de objetos.
- Utilizar iluminação e efeitos ambientais.
- Implementar interiores.
- Adicionar elementos futuros.
- Expandir o mapa sem reconstruir o cenário.
- Funcionar com múltiplos jogadores simultaneamente.

**Prioridade absoluta:** uma cidade visualmente rica, coerente, funcional e construída integralmente com sprites e tilesets reais.

---

# 2. IDENTIDADE DA CIDADE

## 2.1 Conceito

A primeira cidade deve representar um antigo assentamento medieval que resiste em um mundo perigoso.

É um local protegido, mas ainda carrega sinais de guerras antigas, desgaste do tempo e influência de forças sobrenaturais.

A cidade precisa ser acolhedora para os jogadores, sem perder a identidade de fantasia sombria.

Sua arquitetura combina:

- Pedra envelhecida.
- Madeira escura.
- Telhados de cerâmica e madeira.
- Ferro forjado.
- Tecidos medievais.
- Lanternas.
- Bandeiras.
- Muros de pedra.
- Vegetação moderada.
- Objetos artesanais.
- Construções de diferentes tamanhos.
- Pequenos detalhes de desgaste.

O ambiente deve parecer habitado e utilizado diariamente.

A cidade não pode parecer abandonada, mesmo estando inserida em um universo de fantasia sombria.

## 2.2 Nome

**Nome de trabalho:** Vila das Cinzas.

Esse nome é provisório e deve ser configurável nos metadados, sem ser incorporado permanentemente aos sprites.

A cidade pode posteriormente receber seu nome oficial sem exigir alterações no pacote artístico.

## 2.3 Personalidade visual

A cidade deve transmitir:

- Segurança.
- História.
- Organização medieval.
- Atividade comercial.
- Vida cotidiana.
- Proteção.
- Mistério.
- Preparação para aventuras.
- Fantasia sombria estilizada.

Seu centro deve parecer relativamente organizado.

As regiões periféricas podem apresentar ruas mais estreitas, construções antigas e vegetação mais densa.

## 2.4 Paleta principal

Utilizar uma paleta coerente com os personagens e NPCs já estabelecidos.

**Pedras e arquitetura:**
- Cinza quente.
- Cinza azulado.
- Marrom acinzentado.
- Bege envelhecido.

**Madeira:**
- Marrom escuro.
- Castanho médio.
- Madeira envelhecida.
- Tons de carvão.

**Telhados:**
- Vermelho-terra.
- Marrom avermelhado.
- Cinza-ardósia.
- Tons escuros de cerâmica.

**Vegetação:**
- Verde oliva.
- Verde musgo.
- Verde profundo.
- Tons secos de palha.

**Iluminação:**
- Amarelo quente.
- Laranja suave.
- Dourado discreto.

**Elementos especiais:**
- Azul-ciano em cristais raros.
- Verde-espectral em objetos mágicos específicos.
- Roxo discreto em elementos arcanos.

A cidade não deve ser excessivamente saturada.

Os personagens devem permanecer facilmente identificáveis sobre o cenário.

---

# 3. DIREÇÃO DE ARTE CONGELADA

Todos os elementos devem seguir a direção artística estabelecida para os personagens, inimigos, NPCs e classes jogáveis.

## 3.1 Regras visuais

- Pixel Art Chibi de fantasia medieval.
- Perspectiva isométrica consistente.
- Contornos limpos.
- Volumes bem definidos.
- Sombras estilizadas.
- Texturas detalhadas, mas legíveis.
- Iluminação coerente.
- Proporções consistentes entre edifícios e personagens.
- Materiais claramente identificáveis.
- Silhuetas reconhecíveis.
- Ausência de interpolação borrada.
- Ausência de deformações.
- Ausência de pixels soltos.
- Ausência de bordas ou halos.
- Transparência verdadeira onde necessária.

## 3.2 Referências de apresentação

As folhas de apresentação devem seguir o padrão visual já definido para os NPCs:

- Organização profissional.
- Identificação dos elementos.
- Famílias de sprites agrupadas.
- Linhas e colunas bem definidas.
- Detalhamento consistente.
- Fundo magenta técnico nas pranchas de apresentação.
- Identidade visual de fantasia medieval sombria.

**Importante:** o fundo magenta é exclusivo das folhas de apresentação e revisão.

Os assets finais devem possuir transparência verdadeira ou preencher completamente suas células de terreno.

Nunca utilizar o fundo magenta como parte do jogo.

## 3.3 Compatibilidade com personagens

Os edifícios e objetos devem ser dimensionados considerando as classes jogáveis:

- Espadachim.
- Mago.
- Pugilista.
- Necromante.
- Arqueiro.

A cidade também deve comportar os NPCs e permitir circulação de personagens com armaduras, cajados, arcos, escudos, capas e outros equipamentos modulares.

Os personagens não podem parecer gigantes em relação às portas ou minúsculos diante dos balcões.

---

# 4. ESCALA E PADRÃO TÉCNICO ISOMÉTRICO

## 4.1 Grade do mapa

Utilizar como padrão inicial:

**Tile-base: 64 × 32 pixels.**

Proporção isométrica 2:1.

Um tile representa uma unidade lógica do terreno.

A escala poderá ser ajustada caso as spritesheets já aprovadas utilizem outra proporção, mas todos os assets devem compartilhar uma única especificação.

Não misturar diferentes escalas sem conversão documentada.

## 4.2 Dimensões iniciais do mapa

Planejar o mapa principal com:

**96 × 96 tiles lógicos.**

Esse tamanho é uma referência inicial de planejamento, não uma obrigação de preencher cada tile com construções.

O espaço deve ser distribuído entre:

- Praça central.
- Ruas.
- Estabelecimentos.
- Casas.
- Áreas verdes.
- Muros.
- Portões.
- Espaços de circulação.
- Elementos decorativos.

A extensão final deve ser validada na escala real dos personagens e na experiência de navegação.

Evitar espaços vazios excessivos ou longas caminhadas sem elementos interessantes.

## 4.3 Objetos maiores que um tile

Edifícios, árvores, bancadas e estruturas não devem ser artificialmente comprimidos em células de 64 × 32.

Cada objeto pode ocupar múltiplos tiles.

Exemplos:

- Casa pequena: 4 × 5 tiles de ocupação aproximada.
- Loja média: 6 × 7 tiles.
- Ferreiro: 7 × 8 tiles.
- Praça central: área de aproximadamente 18 × 18 tiles.
- Árvore grande: múltiplos tiles de ocupação e uma imagem mais alta que sua base.

Essas dimensões são referências para composição, sujeitas à validação visual.

Cada objeto deve possuir:

- Footprint no chão.
- Ponto de ancoragem.
- Bounding box visual.
- Bounding box de colisão.
- Profundidade.
- Camadas de oclusão.
- Pontos de interação quando aplicável.

## 4.4 Perspectiva

Adotar perspectiva isométrica 2:1.

As direções de movimentação permanecem:

N, NE, E, SE, S, SW, W, NW.

O cenário deve utilizar a mesma convenção direcional dos personagens.

Não misturar:

- Visão frontal.
- Top-down puro.
- Perspectiva lateral.
- Isometria incompatível.
- Objetos com pontos de fuga inconsistentes.

---

# 5. ORGANIZAÇÃO GERAL DA CIDADE

A cidade deve ser organizada ao redor de uma praça central, com caminhos intuitivos para os principais serviços.

## 5.1 Regiões principais

Criar as seguintes regiões:

1. Praça Central.
2. Distrito do Ferreiro.
3. Distrito Comercial.
4. Distrito de Cura.
5. Armazém e Depósitos.
6. Área do Treinador de Pets.
7. Região Residencial.
8. Taverna e Descanso.
9. Mural de Missões.
10. Muralhas e Portões.

As regiões devem fazer parte de um mapa contínuo.

A divisão em distritos é uma referência organizacional, não uma obrigação de criar mapas separados.

## 5.2 Disposição espacial sugerida

**Centro:** Praça Central.

**Noroeste:** Ferreiro e oficina.

**Nordeste:** Curandeira e jardim medicinal.

**Leste:** Comerciante de Equipamentos.

**Sudeste:** Comerciante de Poções.

**Sudoeste:** Guardião do Armazém.

**Oeste:** Treinador de Pets e pequeno campo de treinamento.

**Sul:** Taverna, casas e área de descanso.

**Periferia:** Casas adicionais, muros, vegetação e caminhos.

A distribuição deve preservar distâncias confortáveis para os jogadores.

## 5.3 Hierarquia de navegação

A praça central é o principal ponto de orientação.

O jogador deve conseguir identificar rapidamente:

- Onde encontrar o ferreiro.
- Onde recuperar vida.
- Onde comprar poções.
- Onde comprar equipamentos.
- Onde acessar o armazém.
- Onde encontrar o treinador de pets.
- Onde consultar missões.
- Onde estão os portões.

Usar sinalização visual do próprio cenário, evitando depender exclusivamente de marcadores flutuantes.

---

# 6. TILESET 01 — TERRENO BASE

Criar um tileset completo para composição do solo.

## 6.1 Grama

Produzir variações de:

- Grama verde comum.
- Grama verde-escura.
- Grama desgastada.
- Grama seca.
- Grama com pequenas flores.
- Grama com ervas.
- Grama com manchas de terra.
- Grama com pequenas pedras.
- Grama próxima a caminhos.
- Grama próxima a muros.

As variações devem reduzir repetição visual sem prejudicar a leitura do terreno.

## 6.2 Terra

Produzir:

- Terra compactada.
- Terra clara.
- Terra escura.
- Terra seca.
- Terra úmida.
- Terra com pequenas pedras.
- Terra com marcas de passagem.
- Terra com folhas.
- Terra com ervas.
- Terra com pequenas irregularidades.

## 6.3 Pedra natural

Produzir:

- Rocha compacta.
- Pedras pequenas.
- Pedras médias.
- Pedra parcialmente coberta por terra.
- Pedra com musgo.
- Pedra desgastada.
- Pedra rachada.
- Pedra escurecida.

## 6.4 Transições de terreno

Criar transições completas entre:

- Grama e terra.
- Grama e pedra.
- Terra e pedra.
- Grama e caminhos.
- Terra e pavimentação.
- Pedra natural e pavimentação.

Cada conjunto deve possuir:

- Bordas internas.
- Bordas externas.
- Cantos internos.
- Cantos externos.
- Transições diagonais.
- Peças centrais.
- Junções.
- Extremidades.
- Variações visuais.

O tileset deve suportar autotiling sem deixar espaços vazios ou bordas incorretas.

---

# 7. TILESET 02 — RUAS E CAMINHOS

A cidade precisa possuir ruas legíveis, bem integradas à arquitetura.

## 7.1 Rua de pedra

Criar:

- Pavimento central.
- Pedras claras.
- Pedras escuras.
- Pedras desgastadas.
- Pedras rachadas.
- Pedras irregulares.
- Pedras com musgo.
- Pedras com sujeira.
- Bordas de pavimento.
- Cantos.
- Cruzamentos.
- Bifurcações.
- Junções.
- Trechos largos.
- Trechos estreitos.

## 7.2 Caminhos de terra

Criar:

- Caminhos compactados.
- Bordas irregulares.
- Trechos com pegadas.
- Pequenas poças secas.
- Pedras soltas.
- Marcas de rodas.
- Junções.
- Curvas.
- Entradas de estabelecimentos.

## 7.3 Calçadas

Criar:

- Calçadas de pedra.
- Bordas elevadas.
- Cantos.
- Pequenos degraus.
- Trechos quebrados.
- Transições com portas.
- Transições com escadas.

## 7.4 Drenagem

Criar elementos discretos:

- Canaletas de pedra.
- Pequenos ralos.
- Bordas de drenagem.
- Calhas.
- Saídas de água.

Não criar um sistema hídrico complexo nesta etapa.

---

# 8. TILESET 03 — PAREDES E ARQUITETURA

Criar um sistema modular de construção de edifícios.

## 8.1 Paredes de pedra

Produzir:

- Parede reta.
- Parede lateral.
- Parede com janela.
- Parede com porta.
- Parede com rachaduras.
- Parede com musgo.
- Parede com vigas.
- Parede parcialmente danificada.
- Cantos internos.
- Cantos externos.
- Junções.
- Acabamentos superiores.

## 8.2 Paredes de madeira

Produzir:

- Madeira vertical.
- Madeira horizontal.
- Madeira escurecida.
- Madeira envelhecida.
- Estrutura de vigas.
- Paredes com janelas.
- Paredes com portas.
- Cantos.
- Junções.
- Reforços estruturais.

## 8.3 Construção mista

Criar variações com:

- Base de pedra.
- Estrutura de madeira.
- Reboco envelhecido.
- Vigas aparentes.
- Cantos reforçados.
- Janelas ornamentadas.

Essa deve ser a principal linguagem arquitetônica da cidade.

## 8.4 Portas e batentes

Produzir:

- Porta pequena.
- Porta média.
- Porta larga.
- Porta reforçada.
- Porta comercial.
- Porta de armazém.
- Porta de oficina.
- Batentes.
- Dobradiças.
- Maçanetas.
- Fechaduras.

As portas interativas devem possuir spritesheets animadas.

---

# 9. TILESET 04 — TELHADOS

Criar telhados modulares de fantasia medieval.

## 9.1 Tipos

- Telhado de cerâmica avermelhada.
- Telhado de madeira escura.
- Telhado de ardósia.
- Telhado de palha envelhecida.
- Telhado comercial ornamentado.

## 9.2 Peças obrigatórias

- Centro.
- Bordas.
- Cumeeira.
- Cantos.
- Inclinações.
- Extremidades.
- Junções.
- Beirais.
- Acabamentos.
- Telhas danificadas.
- Telhas com musgo.
- Chaminés.
- Pequenas aberturas.

## 9.3 Regras de renderização

Os telhados devem ser camadas independentes.

Ao entrar em edifícios com interior integrado ou visualização cutaway:

- O telhado pode desaparecer.
- A opacidade pode diminuir.
- Paredes superiores podem ser ocultadas.
- O interior deve continuar legível.

Não incorporar telhados permanentemente em uma imagem de chão.

---

# 10. TILESET 05 — MUROS, CERCAS E PORTÕES

## 10.1 Muros de pedra

Criar:

- Segmentos retos.
- Cantos internos.
- Cantos externos.
- Junções.
- Extremidades.
- Muros baixos.
- Muros altos.
- Pilares.
- Trechos com musgo.
- Trechos danificados.
- Acabamentos superiores.

## 10.2 Cercas

Criar:

- Cerca de madeira.
- Cerca reforçada.
- Cerca de jardim.
- Cerca de curral.
- Portão pequeno.
- Portão duplo.
- Cantos.
- Junções.
- Extremidades.

## 10.3 Muralhas da cidade

Criar um conjunto específico:

- Base de muralha.
- Segmento reto.
- Canto.
- Torre de vigia.
- Ameias.
- Reforços de madeira.
- Entrada fortificada.
- Portão principal.
- Pequenas passarelas.
- Bandeiras.

As muralhas devem delimitar os limites seguros do mapa.

## 10.4 Portões de saída

Preparar quatro conexões direcionais:

- Norte.
- Sul.
- Leste.
- Oeste.

Nem todas precisam estar disponíveis inicialmente.

Cada portão deve possuir estados:

- Fechado.
- Aberto.
- Em abertura.
- Em fechamento.
- Bloqueado.

**Não produzir áreas de caça nesta etapa.**

Os portões devem permitir conexão futura com mapas externos.

Caso uma saída ainda não esteja implementada, ela deve permanecer visualmente integrada, mas bloqueada de maneira coerente com o jogo.

---

# 11. SPRITESHEET 01 — PORTAS ANIMADAS

Criar animações independentes.

## PORTA DE MADEIRA

**Closed:** 1 frame.

**Opening:** 10 frames.

**Open:** 1 frame.

**Closing:** 10 frames.

## PORTA COMERCIAL

**Closed:** 1 frame.

**Opening:** 12 frames.

**Open:** 1 frame.

**Closing:** 12 frames.

## PORTA DE ARMAZÉM

**Closed:** 1 frame.

**Opening:** 14 frames.

**Open:** 1 frame.

**Closing:** 14 frames.

## PORTÃO GRANDE

**Closed:** 1 frame.

**Opening:** 20 frames.

**Open:** 1 frame.

**Closing:** 20 frames.

Todas as animações devem respeitar a profundidade e os pontos de rotação das portas.

O evento de alteração da colisão deve ser definido nos metadados.

---

# 12. TILESET 06 — VEGETAÇÃO URBANA

Criar vegetação apropriada para uma cidade medieval.

## 12.1 Árvores

Produzir:

- Árvore pequena.
- Árvore média.
- Árvore grande.
- Árvore antiga.
- Árvore com tronco curvado.
- Árvore com raízes aparentes.
- Árvore parcialmente seca.
- Árvore com musgo.

Cada árvore deve possuir:

- Tronco.
- Copa.
- Sombra.
- Colisão.
- Ponto de ancoragem.
- Camadas de profundidade quando necessário.

## 12.2 Arbustos

Criar:

- Arbusto pequeno.
- Arbusto médio.
- Arbusto denso.
- Arbusto florido.
- Arbusto seco.
- Arbusto com ervas.

## 12.3 Flores

Criar pequenas flores estilizadas:

- Brancas.
- Amarelas.
- Vermelhas.
- Roxas.
- Azuis discretas.

## 12.4 Ervas

Criar:

- Ervas medicinais.
- Ervas comuns.
- Plantas aromáticas.
- Plantas ornamentais.
- Pequenas hortas.

As ervas medicinais devem ser utilizadas principalmente próximas à Curandeira.

## 12.5 Vegetação animada

Criar spritesheets de vento suave para:

- Grama alta.
- Arbustos.
- Folhagens.
- Copas pequenas.
- Flores altas.

**Recomendação:** 8 a 12 frames por ciclo, dependendo do elemento.

Os movimentos devem ser discretos e contínuos.

Evitar que toda a vegetação se mova sincronizadamente.

---

# 13. TILESET 07 — MOBILIÁRIO E DECORAÇÃO URBANA

Criar objetos independentes para dar vida à cidade.

## 13.1 Objetos de rua

- Bancos de madeira.
- Bancos de pedra.
- Barris.
- Caixas.
- Caixotes.
- Sacos de mercadorias.
- Cestos.
- Carrinhos de mão.
- Carroças.
- Pilhas de lenha.
- Tábuas.
- Cordas.
- Baldes.
- Vasos.
- Jarras.
- Fardos de palha.
- Ferramentas.
- Pequenas estantes.
- Mesas.
- Cavaletes.
- Placas.
- Bandeiras.

## 13.2 Objetos comerciais

- Bancadas.
- Balcões.
- Prateleiras.
- Expositores.
- Caixas registradoras medievais decorativas.
- Baús.
- Arcas.
- Sacos de moedas.
- Pilhas de mercadorias.
- Mostruários.
- Pedestais.
- Lanternas.

Não utilizar objetos modernos incompatíveis com a fantasia medieval.

## 13.3 Decoração

- Tapetes.
- Estandartes.
- Bandeirolas.
- Tecidos pendurados.
- Pequenas esculturas.
- Brasões.
- Vasos ornamentais.
- Placas de madeira.
- Brasões comerciais.
- Pedras decorativas.
- Pequenas fontes.
- Canis e cercados.
- Jardins.

Cada objeto deve possuir transparência, âncora e colisão apropriadas.

---

# 14. SPRITESHEET 02 — ÁGUA E FONTES

Criar uma fonte central na praça.

## 14.1 Fonte principal

Características:

- Base circular ou octogonal de pedra.
- Pequenos ornamentos medievais.
- Água azul-esverdeada.
- Reflexos estilizados.
- Movimento contínuo da superfície.
- Pequeno jato ou fluxo central.
- Musgo discreto nas pedras.

## 14.2 Animações

**Water Surface:** 16 frames em loop.

**Water Flow:** 16 frames em loop.

**Water Splash:** 12 frames em loop.

**Water Droplets:** 8 frames em loop.

Criar também uma variação de fonte desligada, caso necessário.

A água deve ser independente da estrutura de pedra.

## 14.3 Regras

- Animação contínua.
- Transparência correta.
- Reflexos consistentes.
- Sem deslocamento da estrutura.
- Sem mudanças bruscas de volume.
- Sem repetição visual evidente.
- Efeito sonoro sincronizável por evento ambiental.

---

# 15. SPRITESHEET 03 — ILUMINAÇÃO E FOGO

Criar elementos animados para iluminação ambiental.

## 15.1 Tochas

**Flame:** 12 frames em loop.

**Smoke:** 12 frames em loop.

## 15.2 Lanternas

**Flame / Light Flicker:** 12 frames em loop.

## 15.3 Braseiros

**Fire:** 16 frames em loop.

**Embers:** 12 frames em loop.

**Smoke:** 16 frames em loop.

## 15.4 Velas

**Candle Flame:** 8 frames em loop.

## 15.5 Chaminés

**Chimney Smoke:** 16 frames em loop.

## 15.6 Iluminação dinâmica

A luz real deve ser aplicada pelo motor gráfico, utilizando os sprites apenas como fonte visual.

Criar metadados para:

- Posição da luz.
- Raio.
- Intensidade.
- Cor.
- Oscilação.
- Condição de ativação.

Não incorporar iluminação noturna permanentemente ao spritesheet-base.

---

# 16. PRAÇA CENTRAL

## 16.1 Função

A Praça Central será o principal ponto de referência da cidade.

Deve funcionar como:

- Área inicial de circulação.
- Ponto de encontro de jogadores.
- Local de orientação.
- Espaço de passagem entre distritos.
- Área visualmente marcante.

## 16.2 Elementos obrigatórios

- Pavimentação de pedra.
- Fonte central.
- Pequenos bancos.
- Lanternas.
- Bandeiras.
- Árvores ornamentais.
- Jardins pequenos.
- Placas direcionais.
- Mural de missões.
- Elementos de comércio ao redor.
- Espaço livre para vários jogadores.

## 16.3 Composição

A praça deve possuir um espaço central relativamente amplo, mas não vazio.

A fonte funciona como principal referência.

Os caminhos partem da praça em direção aos estabelecimentos.

As lojas devem ser identificáveis através de suas fachadas.

A praça deve possuir profundidade, variedade e pequenos detalhes naturais.

## 16.4 Navegação

Não posicionar decoração bloqueando passagens principais.

O jogador deve conseguir circular ao redor da fonte.

Permitir movimentação de múltiplos personagens simultaneamente.

---

# 17. NPC 01 — FERREIRO

## 17.1 Função

O Ferreiro será responsável por serviços relacionados a armas, armaduras e equipamentos.

Seu estabelecimento deve ser visualmente reconhecível imediatamente.

## 17.2 Localização

**Distrito Noroeste, próximo à praça central.**

O estabelecimento deve ser acessível por uma rua de pedra relativamente larga.

## 17.3 Edifício

Criar uma oficina medieval com:

- Base de pedra.
- Paredes de madeira reforçada.
- Telhado escuro.
- Chaminé grande.
- Fornalha.
- Bigorna.
- Bancada de ferramentas.
- Cavaletes.
- Barris.
- Pilhas de carvão.
- Suportes de armas.
- Peças metálicas.
- Escudos pendurados.
- Armaduras em manutenção.
- Placa de ferreiro.

## 17.4 Interior

O interior deve conter:

- Bigorna central.
- Fornalha acesa.
- Mesa de ferramentas.
- Bancada de inspeção.
- Prateleiras.
- Suportes de armas.
- Pequenas caixas.
- Materiais de trabalho.

## 17.5 Posição do NPC

O Ferreiro deve permanecer em uma posição fixa junto à bigorna.

O jogador aproxima-se pela área frontal ou lateral de atendimento.

O NPC não deve caminhar pelo estabelecimento.

## 17.6 Animações existentes

Integrar as quatro animações contínuas já definidas:

**01 — Preparação do trabalho.**

O Ferreiro organiza ferramentas e posiciona a peça de metal.

**02 — Marteladas.**

Executa golpes de martelo sobre a bigorna.

**03 — Inspeção.**

Ergue a peça e observa o resultado.

**04 — Limpar o suor / recuperação.**

Realiza um pequeno gesto de descanso e retorna ao trabalho.

### Sequência

01 → 02 → 03 → 04 → 01.

A transição deve ser contínua, sem mudanças bruscas de postura.

## 17.7 VFX do Ferreiro

Criar:

- Faíscas de martelo.
- Brilho da fornalha.
- Fumaça.
- Pequenas brasas.
- Metal aquecido.
- Impacto na bigorna.

## 17.8 Interação

Criar ponto de interação próximo ao balcão ou à bigorna.

Ao interagir:

- A animação de trabalho pode concluir o ciclo atual.
- O NPC assume uma pose apropriada de atendimento.
- A interface do Ferreiro é aberta.
- O jogador não precisa atravessar objetos para acessar o serviço.

A área de interação deve ser definida por metadados.

---

# 18. NPC 02 — CURANDEIRA

## 18.1 Função

A Curandeira será responsável por serviços de cura, recuperação e auxílio medicinal.

Seu estabelecimento deve transmitir segurança, tranquilidade e conhecimento sobre ervas e poções.

## 18.2 Localização

**Distrito Nordeste, próximo a um jardim medicinal.**

A região deve possuir vegetação um pouco mais abundante que o centro comercial.

## 18.3 Edifício

Criar uma pequena casa de cura com:

- Base de pedra clara.
- Paredes de madeira.
- Telhado avermelhado ou escuro.
- Janelas ornamentadas.
- Placa medicinal.
- Pequenos vasos de ervas.
- Jardim medicinal.
- Mesas externas.
- Lanternas suaves.

## 18.4 Interior

Criar:

- Balcão de atendimento.
- Mesa de preparação.
- Almofariz e pilão.
- Frascos.
- Ervas penduradas.
- Estantes.
- Pequenos armários.
- Bancos.
- Cama de repouso.
- Velas.
- Plantas medicinais.

## 18.5 Posição do NPC

A Curandeira deve permanecer atrás de sua mesa de preparação ou balcão.

O jogador deve conseguir aproximar-se frontalmente.

## 18.6 Animações existentes

Integrar:

**01 — Seleção de ervas.**

A Curandeira escolhe ingredientes.

**02 — Preparação da poção.**

Mistura componentes em um recipiente.

**03 — Conjuração de cura.**

Executa pequenos gestos mágicos.

**04 — Inspeção da mistura.**

Observa o resultado e retorna à preparação.

### Sequência

01 → 02 → 03 → 04 → 01.

## 18.7 VFX

Criar:

- Partículas de cura.
- Brilho suave.
- Pequenas folhas.
- Bolhas de poção.
- Vapor medicinal.
- Runas de cura discretas.

## 18.8 Interação

Ponto fixo diante do balcão.

A interface deve permitir acesso aos serviços de cura previstos pelo gameplay.

Não incorporar a interface ao spritesheet.

---

# 19. NPC 03 — GUARDIÃO DO ARMAZÉM

## 19.1 Função

Responsável pelo armazenamento de itens e gerenciamento de depósitos dos jogadores.

## 19.2 Localização

**Distrito Sudoeste, próximo à praça e a uma rua de carga.**

## 19.3 Edifício

Criar um armazém medieval com:

- Construção robusta de pedra e madeira.
- Portas largas.
- Telhado escuro.
- Janelas pequenas.
- Estruturas reforçadas.
- Correntes.
- Fechaduras.
- Grandes caixas.
- Barris.
- Sacos de mercadorias.
- Carroça próxima.
- Placa de depósito.

## 19.4 Interior

Criar:

- Balcão principal.
- Baú grande de atendimento.
- Prateleiras.
- Caixas empilhadas.
- Barris.
- Arcas.
- Sacos.
- Armários.
- Pequenos objetos de inventário.
- Lanternas.

## 19.5 Posição do NPC

O Guardião do Armazém permanece fixo atrás do balcão, junto ao baú principal.

## 19.6 Animações existentes

**01 — Abrir o baú.**

O NPC destranca e abre a arca.

**02 — Inspecionar o conteúdo.**

Observa os objetos armazenados.

**03 — Fechar e lacrar.**

Fecha o baú e verifica sua segurança.

**04 — Vigiar o depósito.**

Assume postura de guarda e retorna ao ciclo.

### Sequência

01 → 02 → 03 → 04 → 01.

## 19.7 Sprites adicionais

Criar baú sincronizado com o NPC.

Estados:

- Fechado.
- Abrindo.
- Aberto.
- Fechando.
- Travado.

A tampa do baú deve acompanhar corretamente os gestos.

## 19.8 Interação

Ponto de interação diante do balcão.

Ao interagir, abrir a interface de armazém do jogador.

O conteúdo do armazém pertence ao sistema de dados, não ao spritesheet.

---

# 20. NPC 04 — TREINADOR DE PETS

## 20.1 Função

Responsável pelo sistema de mascotes e companheiros dos jogadores.

## 20.2 Localização

**Distrito Oeste, próximo a um campo cercado de treinamento.**

## 20.3 Ambiente

Criar uma estrutura parcialmente aberta com:

- Pequena cabana.
- Cercas de madeira.
- Campo de treinamento.
- Alvos.
- Pequenos obstáculos.
- Caixas.
- Sacos de ração.
- Tigelas.
- Brinquedos de pets.
- Placa de treinamento.
- Bancada de equipamentos.
- Área de descanso dos animais.

## 20.4 Interior e área externa

O treinador deve trabalhar principalmente em uma área externa ou semiaberta.

Criar uma bancada coberta para atendimento.

A área de treinamento deve permanecer visível, proporcionando personalidade ao estabelecimento.

## 20.5 Posição do NPC

O Treinador permanece fixo próximo à bancada e ao espaço de treinamento.

Seu pet demonstrativo permanece ao seu lado.

## 20.6 Animações existentes

**01 — Dar comando.**

O Treinador gesticula para o pet.

**02 — Pet executar truque.**

A criatura realiza uma pequena ação em resposta.

**03 — Recompensar o pet.**

O Treinador oferece uma recompensa e acaricia o companheiro.

**04 — Alongar / retornar à postura.**

Realiza pequeno gesto de descanso antes de reiniciar.

### Sequência

01 → 02 → 03 → 04 → 01.

## 20.7 Pet demonstrativo

Criar um pequeno pet adequado à direção de arte.

Sugestão: filhote de lobo de fantasia, com proporções chibi.

Deve possuir:

- Idle.
- Sentar.
- Levantar.
- Pequeno salto.
- Truque.
- Receber carinho.
- Recompensa.
- Retorno ao Idle.

As animações do treinador e do pet devem ser sincronizadas.

## 20.8 Interação

Ponto de interação diante da bancada.

A interface do treinador deve ser acessível sem movimentar o NPC.

---

# 21. NPC 05 — COMERCIANTE DE POÇÕES

## 21.1 Função

Responsável pela comercialização de poções e consumíveis.

## 21.2 Localização

**Distrito Sudeste, junto à região comercial.**

## 21.3 Edifício

Criar uma loja medieval de poções com:

- Fachada de madeira e pedra.
- Telhado ornamentado.
- Pequena placa com frasco.
- Vitrine.
- Expositor externo.
- Pequenas caixas.
- Estantes de frascos.
- Lanternas.
- Tecidos decorativos.

## 21.4 Interior

Criar:

- Balcão.
- Prateleiras de poções.
- Frascos de diferentes cores.
- Pequenos recipientes.
- Mesa de mistura.
- Caixas.
- Armários.
- Livros de receitas.
- Velas.
- Pequenos elementos alquímicos.

## 21.5 Posição do NPC

O Comerciante permanece atrás do balcão principal.

## 21.6 Animações existentes

**01 — Organizar poções.**

Arruma frascos na bancada.

**02 — Inspecionar poção.**

Ergue um frasco e observa seu conteúdo.

**03 — Apresentar produto.**

Mostra uma poção ao jogador.

**04 — Recolocar a poção.**

Devolve o frasco e retorna à organização.

### Sequência

01 → 02 → 03 → 04 → 01.

## 21.7 VFX

Criar:

- Pequenos reflexos em frascos.
- Bolhas discretas.
- Líquidos animados.
- Partículas alquímicas suaves.
- Brilho de poções mágicas.

## 21.8 Interação

Criar ponto fixo diante do balcão.

Ao interagir, abrir a interface comercial de poções.

O catálogo e os preços devem ser controlados pelo sistema do jogo.

---

# 22. NPC 06 — COMERCIANTE DE EQUIPAMENTOS

## 22.1 Função

Responsável pela comercialização de armas, armaduras e outros equipamentos.

## 22.2 Localização

**Distrito Leste, próximo à praça central.**

O estabelecimento deve ser facilmente identificável.

## 22.3 Edifício

Criar loja medieval com:

- Fachada de pedra e madeira.
- Telhado ornamentado.
- Placa com símbolo de arma ou armadura.
- Vitrine.
- Suportes de espadas.
- Escudos pendurados.
- Armaduras em manequins.
- Caixas.
- Barris.
- Lanternas.

## 22.4 Interior

Criar:

- Balcão principal.
- Suportes de armas.
- Manequins de armaduras.
- Prateleiras.
- Expositores.
- Espadas.
- Escudos.
- Capacetes.
- Luvas.
- Botas.
- Caixas de mercadorias.
- Tapetes.
- Pequenos objetos decorativos.

Os equipamentos expostos devem seguir a mesma linguagem artística dos equipamentos modulares dos jogadores.

## 22.5 Posição do NPC

O Comerciante permanece atrás do balcão principal, próximo a uma espada de demonstração.

## 22.6 Animações existentes

**01 — Inspecionar espada.**

O NPC ergue uma espada e observa sua condição.

**02 — Polir espada.**

Limpa a lâmina com um tecido.

**03 — Apresentar espada.**

Mostra a arma em posição de destaque.

**04 — Recolocar espada e observar o ambiente.**

Devolve o equipamento ao suporte e retorna ao ciclo.

### Sequência

01 → 02 → 03 → 04 → 01.

## 22.7 Interação

Criar ponto de interação diante do balcão.

Ao interagir, abrir o sistema comercial de equipamentos.

---

# 23. REGRA UNIVERSAL DOS SEIS NPCS

Todos os NPCs principais devem seguir as regras previamente estabelecidas.

## 23.1 NPCs estacionários

Os seis NPCs não devem caminhar livremente pelo cenário.

Cada NPC possui:

- Posição fixa.
- Orientação definida.
- Ciclo próprio de animações.
- Área de interação.
- Objeto ou bancada de referência.
- Eventos de VFX.
- Interface correspondente.

## 23.2 Ciclo contínuo

Cada NPC deve possuir quatro etapas conectadas.

**01 → 02 → 03 → 04 → 01.**

Não pode ocorrer:

- Teleporte entre poses.
- Reinício brusco.
- Mudança involuntária de escala.
- Deslocamento de equipamentos.
- Tremores.
- Bordas.
- Pixels residuais.
- Alteração da identidade visual.

## 23.3 Interação com jogadores

Quando o jogador se aproxima:

- O NPC continua seu trabalho.
- Um indicador discreto de interação pode aparecer.
- O jogador pode iniciar conversa ou acessar o serviço.
- A animação pode concluir a ação atual e transitar para uma pose de atendimento.
- O NPC não precisa sair de sua posição fixa.

Criar, quando necessário, animações complementares:

- Attention.
- Talk.
- Interaction Start.
- Interaction End.

Essas animações devem preservar a direção de arte, proporções e identidade de cada NPC.

## 23.4 Integração dos sprites existentes

Utilizar as folhas e sprites já definidos como referência visual obrigatória.

Não redesenhar os NPCs com outro estilo.

A cidade deve ser construída para acomodar os personagens aprovados, respeitando:

- Altura.
- Largura.
- Proporção.
- Posição dos braços.
- Ferramentas.
- Bancadas.
- Balcões.
- Objetos de interação.
- Orientação visual.

Se um objeto cenográfico já estiver incorporado ao sprite do NPC, evitar duplicá-lo no cenário.

---

# 24. TAVERNA E ÁREA DE DESCANSO

Criar um estabelecimento adicional para enriquecer a cidade.

## 24.1 Edifício

- Construção medieval de madeira e pedra.
- Telhado inclinado.
- Placa de taverna.
- Lanternas.
- Pequena varanda.
- Barris externos.
- Mesas.

## 24.2 Interior

- Balcão.
- Mesas.
- Cadeiras.
- Lareira.
- Barris.
- Prateleiras.
- Canecas.
- Tapetes.
- Escada decorativa.
- Lanternas.

## 24.3 Estado funcional

A taverna deve possuir cenário completo.

Não criar nesta etapa um novo NPC principal com sistema complexo.

Preparar pontos de posicionamento para NPCs ou serviços futuros.

---

# 25. CASAS RESIDENCIAIS

Criar um conjunto modular de casas para compor a cidade.

## 25.1 Tipos

- Casa pequena de madeira.
- Casa pequena de pedra.
- Casa mista.
- Casa média.
- Casa de dois pavimentos.
- Casa com varanda.
- Casa com pequeno jardim.

## 25.2 Variações

Modificar:

- Formato do telhado.
- Posição das janelas.
- Cor da madeira.
- Tipo de porta.
- Presença de chaminé.
- Pequenos ornamentos.
- Jardins.
- Cercas.

As casas devem compartilhar peças modulares sem parecer cópias idênticas.

## 25.3 Interiores

Não é necessário criar interiores completos para todas as casas nesta etapa.

Casas sem função ativa podem permanecer fechadas, desde que visualmente finalizadas.

Preparar metadados para expansão futura.

---

# 26. MURAL DE MISSÕES

Criar um mural de madeira localizado próximo à Praça Central.

## 26.1 Aparência

- Estrutura de madeira envelhecida.
- Pequeno telhado protetor.
- Pergaminhos.
- Avisos.
- Símbolos medievais.
- Pequenos pregos.
- Selos.
- Lanternas próximas.

## 26.2 Estados

Criar:

- Mural comum.
- Mural com nova missão disponível.
- Mural com atualização.
- Mural interativo.

O destaque de nova missão deve ser um VFX independente.

## 26.3 Interação

Ao interagir, abrir o sistema de missões.

Não incorporar textos dinâmicos diretamente aos spritesheets.

---

# 27. INTERIORES DOS ESTABELECIMENTOS

A cidade deve possuir interiores funcionais para seus seis estabelecimentos principais.

## 27.1 Interiores obrigatórios

1. Oficina do Ferreiro.
2. Casa de Cura.
3. Armazém.
4. Instalação do Treinador de Pets.
5. Loja de Poções.
6. Loja de Equipamentos.

O campo externo do Treinador pode constituir seu espaço principal, com uma pequena área interna de apoio.

## 27.2 Tilesets internos

Criar:

- Pisos de madeira.
- Pisos de pedra.
- Pisos de terra compactada.
- Tapetes.
- Paredes internas.
- Cantos.
- Portas.
- Janelas.
- Vigas.
- Colunas.
- Balcões.
- Prateleiras.
- Mesas.
- Bancos.
- Estantes.
- Lareiras.
- Lanternas.
- Caixas.
- Armários.

## 27.3 Visibilidade

Utilizar uma das duas estratégias, conforme a arquitetura do jogo:

**Interiores em mapas separados:** ao entrar pela porta, carregar o mapa interno correspondente.

**Interiores integrados:** utilizar ocultação de telhado e paredes superiores.

O pacote artístico deve manter compatibilidade com ambas as estratégias, mas a implementação deve escolher uma estratégia principal e documentá-la.

## 27.4 Posição dos NPCs

Os NPCs devem ser ancorados em posições fixas no interior ou área semiaberta de seus estabelecimentos.

Cada posição deve possuir:

- Coordenadas.
- Orientação.
- Área de interação.
- Identificador do estabelecimento.
- Identificador do NPC.
- Referência às animações.
- Referência aos objetos de trabalho.
- Referência aos VFX.

---

# 28. SISTEMA DE CAMADAS DO MAPA

A cidade deve ser construída utilizando camadas independentes.

## Ordem lógica sugerida

**01 — Ground Base:** terreno principal.

**02 — Ground Transitions:** transições de terreno.

**03 — Roads:** ruas e caminhos.

**04 — Ground Details:** sujeira, pequenas pedras e folhas.

**05 — Ground Decals:** marcas e efeitos permanentes de chão.

**06 — Structure Floors:** pisos de construções.

**07 — Low Structures:** objetos baixos.

**08 — Walls:** paredes.

**09 — Props:** objetos decorativos.

**10 — Characters:** jogadores e NPCs.

**11 — Tall Objects:** árvores, colunas e objetos altos com profundidade dinâmica.

**12 — Roofs:** telhados.

**13 — Foreground:** partes que podem ocultar personagens.

**14 — Animated Props:** elementos animados.

**15 — Environmental VFX:** fumaça, poeira, brasas e partículas.

**16 — Lighting:** iluminação dinâmica.

**17 — Weather:** efeitos climáticos opcionais.

**18 — Interaction Indicators:** indicadores de interação.

A ordenação de personagens e objetos deve considerar a profundidade isométrica e o ponto de contato no solo, não apenas uma ordem fixa de camadas.

---

# 29. COLISÕES E NAVEGAÇÃO

Todos os objetos devem possuir informações de colisão.

## 29.1 Colisões obrigatórias

- Paredes.
- Muros.
- Cercas.
- Edifícios.
- Árvores.
- Bancadas.
- Balcões.
- Caixas.
- Barris.
- Fonte.
- Objetos grandes.
- Portões fechados.

## 29.2 Objetos sem colisão

Exemplos:

- Pequenas flores.
- Folhas.
- Decalques.
- Pequenas manchas.
- Partículas.
- Iluminação.
- Fumaça.
- Pequenos elementos decorativos do chão.

## 29.3 Regras

- Jogadores não podem atravessar edifícios.
- Jogadores não podem caminhar sobre paredes.
- Objetos altos não podem bloquear incorretamente a visualização.
- Portas abertas devem atualizar sua colisão.
- A navegação deve respeitar o espaço real disponível.
- Os caminhos até NPCs devem estar desobstruídos.
- Os pontos de interação devem estar acessíveis.
- Não criar colisões maiores que o necessário.

## 29.4 Navegação multiplayer

Preparar a cidade para múltiplos jogadores.

O mapa deve permitir:

- Circulação simultânea.
- Encontro de jogadores.
- Interações com NPCs.
- Acesso a estabelecimentos.
- Posicionamento correto de personagens.
- Atualização dinâmica de entidades.

As regras de colisão entre jogadores devem ser controladas pelo gameplay.

---

# 30. SISTEMA DE INTERAÇÃO

Cada objeto interativo deve possuir metadados específicos.

## Interações iniciais

- Ferreiro.
- Curandeira.
- Guardião do Armazém.
- Treinador de Pets.
- Comerciante de Poções.
- Comerciante de Equipamentos.
- Mural de Missões.
- Portas.
- Portões.
- Outros objetos interativos previstos pelo mapa.

## Regras

O jogador deve aproximar-se do objeto ou NPC.

Um indicador discreto pode aparecer, preferencialmente com estética integrada ao jogo.

A interação deve:

- Verificar a distância.
- Identificar o alvo.
- Acionar a função correspondente.
- Manter a posição do NPC.
- Preservar a animação.
- Não exigir que o jogador atravesse objetos.

Os serviços devem utilizar interfaces próprias do jogo, não elementos gráficos incorporados ao tileset.

---

# 31. SPRITESHEETS AMBIENTAIS ANIMADAS

Produzir spritesheets para elementos que tornam a cidade visualmente viva.

## 31.1 Fornalha

**Fire:** 16 frames em loop.

**Embers:** 12 frames em loop.

**Smoke:** 16 frames em loop.

## 31.2 Fonte

**Water:** 16 frames em loop.

**Splash:** 12 frames em loop.

## 31.3 Bandeiras

**Small Flag:** 12 frames em loop.

**Large Banner:** 16 frames em loop.

## 31.4 Lanternas

**Flame:** 12 frames em loop.

## 31.5 Árvores

**Leaves:** 12 frames em loop.

## 31.6 Plantas

**Grass Wind:** 8 frames em loop.

**Flower Wind:** 8 frames em loop.

## 31.7 Chaminés

**Smoke:** 16 frames em loop.

## 31.8 Objetos comerciais

**Potion Bubble:** 12 frames em loop.

**Crystal Glow:** 12 frames em loop.

**Magic Rune:** 12 frames em loop.

## 31.9 Portas

Utilizar os ciclos definidos anteriormente.

## 31.10 Objetos de trabalho dos NPCs

Criar efeitos e partes animadas sincronizados com os ciclos de trabalho.

Exemplos:

- Martelo e faíscas.
- Frascos e poções.
- Tampa do baú.
- Itens em exposição.
- Pet demonstrativo.

**Regra:** os objetos estáticos não devem oscilar indevidamente apenas porque um VFX está sendo reproduzido.

---

# 32. CICLO DE DIA E NOITE

Preparar a cidade para iluminação dinâmica.

## 32.1 Dia

- Luz ambiente natural.
- Sombras suaves.
- Cores levemente mais claras.
- Lanternas apagadas ou discretas.
- Atividade comercial normal.

## 32.2 Entardecer

- Luz quente.
- Sombras mais longas.
- Lanternas começando a acender.
- Reflexos alaranjados.
- Atmosfera acolhedora.

## 32.3 Noite

- Ambiente azul-escuro.
- Lanternas acesas.
- Fornalha destacada.
- Janelas iluminadas.
- Pequenos pontos de luz.
- Contraste moderado.

## 32.4 Regras

Não gerar uma cidade completamente diferente para cada horário.

Utilizar os mesmos tilesets e sprites, com iluminação e efeitos independentes.

Os personagens e equipamentos também devem receber iluminação coerente.

Evitar escurecer excessivamente o cenário a ponto de prejudicar a navegação.

---

# 33. AMBIENTAÇÃO E VIDA URBANA

A cidade deve parecer habitada, mesmo utilizando apenas os seis NPCs principais nesta etapa.

Adicionar elementos de atividade indireta:

- Fumaça saindo de chaminés.
- Água fluindo na fonte.
- Bandeiras balançando.
- Lanternas oscilando.
- Fogo na fornalha.
- Plantas movimentando-se.
- Frascos borbulhando.
- Pequenas partículas ambientais.
- Sons ambientes previstos por metadados.

Não é necessário criar uma grande população de NPCs secundários nesta etapa.

O cenário pode reservar pontos para futuros habitantes.

---

# 34. ORGANIZAÇÃO DOS TILESETS

Criar arquivos separados por categoria.

```text
world/
└── first_city/
    ├── tilesets/
    │   ├── terrain_grass.png
    │   ├── terrain_dirt.png
    │   ├── terrain_stone.png
    │   ├── terrain_transitions.png
    │   ├── roads_stone.png
    │   ├── roads_dirt.png
    │   ├── sidewalks.png
    │   ├── walls_stone.png
    │   ├── walls_wood.png
    │   ├── walls_mixed.png
    │   ├── roofs_clay.png
    │   ├── roofs_wood.png
    │   ├── roofs_slate.png
    │   ├── fences.png
    │   ├── city_walls.png
    │   ├── interior_floors.png
    │   └── interior_walls.png
    │
    ├── buildings/
    │   ├── blacksmith/
    │   ├── healer/
    │   ├── warehouse/
    │   ├── pet_trainer/
    │   ├── potion_shop/
    │   ├── equipment_shop/
    │   ├── tavern/
    │   ├── houses/
    │   └── city_gates/
    │
    ├── props/
    │   ├── urban/
    │   ├── commercial/
    │   ├── furniture/
    │   ├── storage/
    │   ├── vegetation/
    │   ├── lighting/
    │   ├── signs/
    │   └── decorations/
    │
    ├── animations/
    │   ├── doors/
    │   ├── gates/
    │   ├── fire/
    │   ├── water/
    │   ├── smoke/
    │   ├── flags/
    │   ├── vegetation/
    │   └── interactive_props/
    │
    ├── npc_integrations/
    │   ├── blacksmith.json
    │   ├── healer.json
    │   ├── warehouse_keeper.json
    │   ├── pet_trainer.json
    │   ├── potion_merchant.json
    │   └── equipment_merchant.json
    │
    ├── interiors/
    │   ├── blacksmith/
    │   ├── healer/
    │   ├── warehouse/
    │   ├── pet_trainer/
    │   ├── potion_shop/
    │   └── equipment_shop/
    │
    ├── maps/
    │   ├── city_main.json
    │   ├── city_collisions.json
    │   ├── city_navigation.json
    │   ├── city_objects.json
    │   ├── city_interactions.json
    │   ├── city_lighting.json
    │   └── city_portals.json
    │
    ├── metadata/
    │   ├── tilesets.json
    │   ├── buildings.json
    │   ├── props.json
    │   ├── animations.json
    │   ├── npc_positions.json
    │   ├── collisions.json
    │   ├── navigation.json
    │   ├── lighting.json
    │   └── atlas_manifest.json
    │
    └── previews/
        ├── city_overview.png
        ├── city_day.png
        ├── city_night.png
        ├── city_collision_map.png
        ├── city_navigation_map.png
        ├── city_npc_locations.png
        ├── city_animated.gif
        └── interiors/
```

---

# 35. METADADOS OBRIGATÓRIOS

Cada asset deve possuir informações suficientes para integração direta.

## Tilesets

- Identificador.
- Categoria.
- Dimensões.
- Tamanho do tile lógico.
- Coordenadas de recorte.
- Tipo de terreno.
- Máscaras de autotiling.
- Regras de adjacência.
- Variações.
- Colisão.
- Camada de renderização.

## Edifícios

- Identificador.
- Dimensões.
- Footprint.
- Ponto de ancoragem.
- Coordenadas de posicionamento.
- Bounding box visual.
- Colisões.
- Portas.
- Telhados.
- Camadas de profundidade.
- Interior correspondente.
- Pontos de interação.

## Objetos

- Identificador.
- Categoria.
- Âncora.
- Colisão.
- Profundidade.
- Estado de animação.
- FPS.
- Loop.
- Pontos de iluminação.
- Interatividade.

## NPCs

- Identificador.
- Nome.
- Estabelecimento.
- Coordenadas.
- Orientação.
- Área de interação.
- Referência ao spritesheet.
- Ciclo de animações.
- Referência aos VFX.
- Posição dos objetos de trabalho.
- Serviço associado.
- Estados de interação.

## Portões

- Identificador.
- Direção.
- Estado.
- Colisão.
- Animação.
- Ponto de transição.
- Mapa de destino futuro.
- Condições de acesso.

Nenhum metadado pode referenciar um arquivo ou frame inexistente.

---

# 36. REGRAS DE RECORTE E ATLAS

Todos os arquivos devem ser preparados para utilização real.

## Regras

- Transparência verdadeira.
- Grade consistente.
- Frames organizados.
- Recortes sem pixels vizinhos.
- Ausência de halos.
- Ausência de bordas.
- Ancoragem documentada.
- Padding adequado entre sprites.
- Extrusão de borda quando necessária para evitar texture bleeding.
- Filtragem nearest-neighbor.
- Sem suavização borrada.
- Sem deformação por redimensionamento.
- Coordenadas de atlas corretas.

Os objetos não devem ser posicionados por tentativa e erro.

Cada elemento precisa possuir footprint e âncora compatíveis com a grade isométrica.

Os atlas devem ser divididos quando excederem limites práticos de textura.

---

# 37. PLANEJAMENTO DE PRODUÇÃO POR ETAPAS

Não gerar tudo em uma única folha gigante.

Dividir a produção em pacotes verificáveis.

## CIDADE — C1: BASE DO TERRENO

Produzir:

- Grama.
- Terra.
- Pedras.
- Transições.
- Caminhos.
- Ruas.
- Calçadas.

**Entrega:** tilesets completos e mapa de teste das transições.

## CIDADE — C2: ARQUITETURA MODULAR

Produzir:

- Paredes.
- Telhados.
- Portas.
- Janelas.
- Muros.
- Cercas.
- Portões.

**Entrega:** sistema modular e edifícios de teste.

## CIDADE — C3: EDIFÍCIOS PRINCIPAIS

Produzir:

- Ferreiro.
- Curandeira.
- Armazém.
- Treinador de Pets.
- Loja de Poções.
- Loja de Equipamentos.

**Entrega:** fachadas completas e composição dos seis estabelecimentos.

## CIDADE — C4: INTERIORES

Produzir:

- Pisos internos.
- Paredes.
- Balcões.
- Bancadas.
- Mobiliário.
- Objetos específicos.
- Ambientes internos dos estabelecimentos.

**Entrega:** seis interiores funcionais ou áreas de atendimento equivalentes.

## CIDADE — C5: DECORAÇÃO E VEGETAÇÃO

Produzir:

- Árvores.
- Arbustos.
- Flores.
- Vasos.
- Barris.
- Caixas.
- Carroças.
- Bancos.
- Placas.
- Objetos urbanos.

**Entrega:** biblioteca de decoração completa.

## CIDADE — C6: ANIMAÇÕES AMBIENTAIS

Produzir:

- Água.
- Fogo.
- Fumaça.
- Bandeiras.
- Vegetação.
- Portas.
- Efeitos comerciais.
- Iluminação.

**Entrega:** spritesheets animadas e metadados.

## CIDADE — C7: INTEGRAÇÃO DOS NPCS

Integrar:

- Ferreiro.
- Curandeira.
- Guardião do Armazém.
- Treinador de Pets.
- Comerciante de Poções.
- Comerciante de Equipamentos.

**Entrega:** posicionamento, animações, VFX e interações.

## CIDADE — C8: MONTAGEM DO MAPA

Construir:

- Praça.
- Distritos.
- Ruas.
- Edifícios.
- Decoração.
- Muralhas.
- Portões.
- Interiores.
- Pontos de interação.

**Entrega:** cidade completa montada.

## CIDADE — C9: COLISÃO, NAVEGAÇÃO E PROFUNDIDADE

Validar:

- Colisões.
- Caminhos.
- Portas.
- Profundidade.
- Oclusão.
- Movimento dos jogadores.
- Interações.
- Entrada em edifícios.

**Entrega:** cidade funcional para navegação.

## CIDADE — C10: POLIMENTO FINAL

Validar:

- Iluminação.
- Dia e noite.
- VFX.
- Fluidez.
- Recortes.
- Performance.
- Escala.
- Composição visual.
- Acessibilidade dos serviços.
- Consistência artística.

**Entrega:** pacote completo da cidade, pronto para integração no jogo.

Cada etapa deve ser validada antes de avançar para a seguinte, evitando acumular erros de escala, arte ou posicionamento.

---

# 38. VALIDAÇÃO OBRIGATÓRIA

Antes de considerar a cidade concluída:

1. Confirmar que todos os tiles possuem a mesma proporção isométrica.
2. Verificar continuidade das ruas.
3. Validar transições de terreno.
4. Confirmar ausência de espaços vazios.
5. Inspecionar limites e recortes.
6. Verificar a escala dos edifícios.
7. Validar portas e janelas.
8. Confirmar profundidade correta dos telhados.
9. Testar colisões.
10. Validar movimentação nas oito direções.
11. Testar passagem por ruas estreitas.
12. Confirmar acesso aos seis estabelecimentos.
13. Validar os seis interiores.
14. Confirmar posicionamento dos NPCs.
15. Testar os quatro ciclos de cada NPC.
16. Verificar sincronização dos VFX dos NPCs.
17. Confirmar que NPCs não se deslocam indevidamente.
18. Testar interações com jogadores.
19. Verificar que balcões não bloqueiam os pontos de interação.
20. Validar a fonte central.
21. Testar animações de fogo.
22. Testar fumaça.
23. Validar bandeiras.
24. Testar animações de vegetação.
25. Confirmar iluminação diurna.
26. Confirmar iluminação noturna.
27. Testar portas abertas e fechadas.
28. Validar colisão dinâmica.
29. Confirmar funcionamento dos portões.
30. Verificar oclusão de personagens por objetos altos.
31. Testar personagens com equipamentos modulares.
32. Validar personagens com capas e armas grandes.
33. Confirmar que a cidade comporta múltiplos jogadores.
34. Verificar desempenho dos sprites animados.
35. Inspecionar transparência.
36. Corrigir halos e pixels residuais.
37. Eliminar tremores.
38. Garantir consistência da iluminação.
39. Validar todos os metadados.
40. Confirmar que não existem referências a sprites inexistentes.
41. Testar as animações em loops prolongados.
42. Validar a leitura visual da cidade na resolução real de gameplay.
43. Confirmar que todos os estabelecimentos são facilmente identificáveis.
44. Verificar se a navegação entre serviços é intuitiva.
45. Confirmar que não há objetos de caça ou inimigos introduzidos fora do escopo.

---

# 39. CRITÉRIOS DE QUALIDADE FINAL

A cidade não pode parecer:

- Uma imagem estática.
- Um cenário genérico de IA.
- Um mosaico de objetos sem coerência.
- Um mapa feito de blocos provisórios.
- Uma página web.
- Um cenário com escalas incompatíveis.
- Um conjunto de sprites desconectados.
- Uma composição com ruas sem lógica.
- Um mapa excessivamente vazio.
- Um ambiente com objetos repetidos artificialmente.

A cidade deve parecer:

- Um assentamento medieval verdadeiro dentro do universo do jogo.
- Um ambiente construído manualmente.
- Um local seguro e habitado.
- Um centro comercial funcional.
- Um mapa com ruas intuitivas.
- Um espaço com profundidade visual.
- Um ambiente tecnicamente consistente.
- Um cenário que pertence à mesma direção artística dos personagens.

---

# 40. RESULTADO ESPERADO

Entregar um pacote completo da primeira cidade contendo:

## Terreno

- Tileset de grama.
- Tileset de terra.
- Tileset de pedra.
- Transições.
- Ruas.
- Caminhos.
- Calçadas.

## Arquitetura

- Paredes modulares.
- Telhados.
- Portas.
- Janelas.
- Muros.
- Cercas.
- Portões.
- Edifícios residenciais.
- Edifícios comerciais.

## Estabelecimentos principais

- Oficina do Ferreiro.
- Casa da Curandeira.
- Armazém.
- Área do Treinador de Pets.
- Loja de Poções.
- Loja de Equipamentos.

## Ambientes adicionais

- Praça Central.
- Fonte.
- Taverna.
- Casas residenciais.
- Mural de Missões.
- Jardins.
- Áreas decorativas.
- Muralhas.
- Portões de saída.

## NPCs integrados

- Ferreiro.
- Curandeira.
- Guardião do Armazém.
- Treinador de Pets.
- Comerciante de Poções.
- Comerciante de Equipamentos.

Todos com ciclos de animação, objetos de trabalho, áreas de interação e posicionamento fixo.

## Spritesheets ambientais

- Água.
- Fogo.
- Fumaça.
- Lanternas.
- Bandeiras.
- Vegetação.
- Portas.
- Portões.
- Objetos interativos.
- Efeitos de trabalho.
- Partículas ambientais.

## Sistemas técnicos

- Mapa isométrico.
- Sistema de camadas.
- Colisões.
- Navegação.
- Profundidade.
- Oclusão.
- Iluminação.
- Ciclo dia/noite.
- Interações.
- Portais.
- Metadados.
- Atlas.
- Previews.
- Compatibilidade com personagens modulares.

---

# 41. REGRAS ABSOLUTAS DE PRODUÇÃO

**REGRA 01 — DIREÇÃO DE ARTE**

Todos os assets devem seguir a mesma Pixel Art Chibi de fantasia medieval sombria já estabelecida para personagens, inimigos e NPCs.

**REGRA 02 — MODULARIDADE**

A cidade deve ser construída com tilesets e sprites independentes, nunca apenas como uma imagem final de fundo.

**REGRA 03 — ESCALA**

Todos os elementos devem respeitar a mesma escala isométrica e o tamanho real dos personagens.

**REGRA 04 — NPCS EXISTENTES**

Os seis NPCs devem preservar sua identidade visual e suas animações já definidas.

**REGRA 05 — INTERIORES**

Cada estabelecimento principal deve possuir ambiente próprio funcional.

**REGRA 06 — COLISÃO**

Nenhum objeto pode permitir passagem indevida ou bloquear caminhos sem justificativa.

**REGRA 07 — PROFUNDIDADE**

Personagens devem aparecer corretamente atrás e à frente de edifícios, árvores e objetos.

**REGRA 08 — ANIMAÇÕES**

Todos os elementos animados devem possuir loops fluidos, sem tremores, bordas ou deslocamentos involuntários.

**REGRA 09 — EQUIPAMENTOS**

Jogadores devem circular com seus equipamentos modulares visíveis, sem interferência indevida do cenário.

**REGRA 10 — PERFORMANCE**

O mapa deve ser otimizado para navegador, utilizando atlas, carregamento eficiente, controle de animações e descarte de elementos fora da câmera quando apropriado.

**REGRA 11 — SEM PLACEHOLDERS**

A versão final da cidade não pode utilizar blocos geométricos provisórios no lugar de sprites.

**REGRA 12 — SEM MUDANÇA DE ESTÉTICA**

Não criar interpretações artísticas diferentes para cada estabelecimento. Tudo deve pertencer ao mesmo universo visual.

**REGRA 13 — REUTILIZAÇÃO**

Tilesets, objetos, paredes, telhados e vegetação devem ser reutilizáveis em futuras cidades e mapas.

**REGRA 14 — DOCUMENTAÇÃO**

Cada asset deve possuir identificador, arquivos, dimensões, âncoras, regras de renderização e colisões documentadas.

**REGRA 15 — ESCOPO**

Não desenvolver áreas de caça, monstros, bosses, dungeons ou biomas externos nesta etapa.

---

# 42. CRITÉRIO FINAL DE APROVAÇÃO

A primeira cidade somente estará concluída quando:

- Todos os tilesets estiverem completos.
- Todos os edifícios estiverem construídos.
- Os seis estabelecimentos estiverem funcionais.
- Os seis NPCs estiverem integrados.
- As animações ambientais estiverem funcionando.
- O mapa estiver inteiramente montado.
- As colisões estiverem corretas.
- A navegação estiver validada.
- A profundidade estiver correta.
- O sistema de iluminação estiver funcional.
- As interações estiverem acessíveis.
- Os interiores estiverem completos.
- Os arquivos estiverem organizados.
- Os metadados estiverem corretos.
- Não existirem tremores, bordas, deformações ou falhas de recorte.
- A aparência estiver consistente com os personagens já definidos.
- O ambiente estiver pronto para receber jogadores reais.

## PRIORIDADE FINAL

A cidade precisa transmitir a sensação de um **MMORPG de fantasia medieval profissional**, com ambientação rica, arquitetura coerente, vida cotidiana, estabelecimentos reconhecíveis e integração natural entre cenário, NPCs e jogadores.

O resultado não deve ser apenas visualmente bonito, mas tecnicamente utilizável, modular e preparado para expansão.

**OBJETIVO FINAL: criar a primeira cidade completa do MMORPG, utilizando exclusivamente spritesheets, tilesets e objetos isométricos reais, preservando integralmente a direção de arte congelada e preparando o ambiente para receber posteriormente os mapas externos e as áreas de caça.**

**Não iniciar a produção da primeira área de caça. A entrega atual termina na cidade, seus edifícios, seus interiores, seus NPCs, seus portões e todos os sistemas visuais e técnicos necessários para seu funcionamento.**