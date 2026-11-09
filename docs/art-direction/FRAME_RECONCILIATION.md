# P1 — Política de reconciliação de frames

Usuário autorizou em 09/11/2026 correções/recontagens que melhorem **fluidez e funcionamento**, sem exigir aprovação a cada ajuste técnico. Esta autorização **não** equivale a aceitar visualmente uma direção artística nem a liberar P2.

## Divergência P0-001

| Classe | Soma das linhas dos quadros | Total textual | Diferença |
|---|---:|---:|---:|
| Espadachim | 3952 | 4320 | 368 |
| Arqueiro | 5184 | 5312 | 128 |
| Mago | 4736 | 5104 | 368 |
| Necromante | 5648 | 5968 | 320 |
| Pugilista | 4784 | 4912 | 128 |
| TOTAL | 24304 | 25616 | 1312 |

**Decisão P1:** definir as somas das **linhas tabuladas** como *baseline numérica de auditoria*, não como garantia de que o escopo final de animações está perfeito. Os totais textuais são divergentes e não autorizam gerar 1312 frames artificiais. Manter os documentos fontes históricos inalterados até comparação de todas as ações declaradas com linhas da tabela; possíveis fases não tabuladas serão adicionadas com justificativa.

## Procedimento para ajuste futuro

1. Anotar ID/ação/frames atuais e FPS antes da alteração.
2. Verificar loop, key poses, contato dos pés, estabilidade do pivô, arma, VFX e eventos.
3. Produzir nova contagem (somar por direção **e** por arma/camada se sobreposição exigir quadros adicionais).
4. Verificar continuidade, sincronização de todas as camadas e eventuais exigências de engine.
5. Atualizar manifesto e documentação de origem; versionar revisão e gerar GIF a partir dos frames reais.
6. Reprovar se novo movimento parecer mais suave só por interpolação borrada ou se não houver melhoria funcional demonstrável.

Nenhuma contagem aqui representa frames já gerados.
