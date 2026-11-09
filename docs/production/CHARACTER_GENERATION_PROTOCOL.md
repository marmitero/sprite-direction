# Protocolo oficial de geração de personagens — aprovado em 09/11/2026

## Motivação

Reprovações anteriores da P3 mostraram problemas de **deriva visual** (personagem com equipamento diferente em cada estado), dificuldade de manter anatomia constante e caminhar sem tremores. A partir desta revisão, **nenhuma geração multianimação em uma única folha é aceita como entrega**.

## Fluxo obrigatório de produção

1. **FRONT-01:** gerar **um único personagem visto de frente**, em pose neutra, no fundo magenta. Apresentar para aprovação humana. Não produzir outras orientações ou animações nesta fase.
2. **FREEZE-01:** após aprovação, congelar simultaneamente (a) imagem original, (b) hash SHA256, (c) ficha visual e (d) prompt mestre de continuidade, registrando versão, local, data e fonte. Não editar o original: variantes são arquivos diferentes e versionados.
3. **ANIM-XX:** gerar **uma animação por geração** (por exemplo, um pacote para Idle, depois outro para Walk), sempre referenciando a imagem congelada e o prompt mestre. Cada animação precisa incluir **as oito direções** quando for o caso de personagem móvel. Não misturar Idle, Walk, Run, combate, equipamentos ou retratos na mesma geração.
4. **QA-XX:** antes de exportar, verificar identidade (cabelo, olhos, roupas, posições de metal/couro/lenço), 8 direções corretas, ênfase em key poses, alternância de pernas, contato dos pés, loops, número de quadros realmente distintos, proporções, pose/pivô e compatibilidade de equipamentos.
5. **CHROMA-XX:** preservar PNG original magenta como fonte; gerar cópia RGBA por chroma key magenta, corrigindo franja sem remover rosas/vermelhos legítimos da roupa; jamais usar PNG magenta em runtime.
6. **PACK-XX:** usar pipeline P2 para atlas PNG + JSON + GIF; validar os próprios frames exportados. Se houver falha, *não* publicar como funcional nem aumentar artificialmente contagem.
7. **REVIEW-XX:** publicar imagem de revisão, GIF e relatório de testes da etapa, atualizar manifestos, README e AI_STATE e obter aprovação da etapa antes de prosseguir para a próxima ação.

## Regras inegociáveis

- O personagem congelado é a fonte canônica: **mesma roupa, mesmo cabelo, mesmos olhos, mesma faixa vermelha, mesmo ombro com metal, mesmas botas, mesmos acessórios** em toda geração.
- Proibir evolução involuntária do personagem (roupa leve virando armadura pesada, capa diferente, luvas ou metais surgindo/desaparecendo).
- **Magenta para a fonte**: alvo `#FF00FF`; imagem gerada pode ter pequenas variações de cor e precisa de tolerância no chroma, não recorte destrutivo.
- Um personagem desenhado uma vez em diversos lugares do atlas **não é uma animação**. Cada frame deve representar pose específica, sem distorções.
- Uma geração por movimento (não uma geração por direção); quando a qualidade não permitir oito direções completas de uma só vez, subdivisão técnica é admitida e documentada, mas a animação só fica concluída com as oito direções validadas.
- É permitido ajustar contagem planejada para fluidez, documentando antes/depois, conforme `docs/art-direction/FRAME_RECONCILIATION.md`.
- O corpo-base **visual aprovado tem roupa e acessórios fixados como aparência inicial**. Isso não comprova modularidade: será preciso criar versão sem equipamentos + overlays alinhados antes de declarar equipamento totalmente intercambiável.
- Sem geometria programática representando arte final; Pillow e ferramentas de atlas só para processamento/QA.
- **Não usar dashboards, títulos, números, quadros, personagens alternativos ou painéis decorativos** nas gerações de sprites; elas devem conter apenas uma animação de um único personagem, com fundo magenta uniforme.

## Estrutura do novo fluxo

```text
assets/characters/classes/shared_humanoid_v3/
  references/
    FRONT_APPROVED_SOURCE.png       # PNG original, imutável quando importado
    IDLE_APPROVED_SOURCE.png        # PNG original, imutável quando importado
  animations/
    idle/
      source_magenta.png
      runtime/
    walk/
      source_magenta.png            # somente após aceite
      runtime/
  prompts/
    character_lock.md
    idle.md
    walk.md
  manifest.json
```

Arquivos fonte podem ainda estar somente no pacote de referência anexo à conversa, até confirmação de upload dos binários para o GitHub; **não inventar paths commitados**.

## Gates

- Front — **aprovada pelo usuário**.
- Idle — **aprovada pelo usuário**.
- Walk — **próximo movimento a produzir; ainda sem aprovação**.
- Run/Jump/Hurt/Died/Combat Idle e movimentos específicos — **não iniciados nesta revisão**.
- P4 — **bloqueada**.
