# Testes da skill copy-chief: segunda rodada

**Data:** 16 e 17/11/2026
**Como foi feito:** pela skill skill-creator. Cada caso rodou duas vezes, uma com a skill e outra sem ela (o mesmo pedido, sem acesso aos arquivos da skill). Cada resposta foi avaliada pelos critérios do caso. Contagens de caracteres, emojis e hashtags foram feitas com script, não a olho.
**Casos:** os seis da primeira rodada, com os critérios reforçados no fim dela (que ainda não tinham rodado), mais um caso por canal novo: Google, WhatsApp, site e anúncio.
**Relatório visual:** `copy-chief-iteracao-2.html`. Abra no navegador: a aba "Outputs" mostra cada texto gerado, e a aba "Benchmark" compara com e sem a skill.

## Resultado

| | Com a skill | Sem a skill |
|---|---|---|
| Critérios atendidos | 48 de 49 (98%) | 40 de 49 (81%) |
| Só os quatro canais novos | 21 de 21 | 18 de 21 |
| Tempo médio por pedido | 87 s | 45 s |
| Tokens por pedido | 88,5 mil | 67,8 mil |

## Caso a caso

| Caso | Com a skill | Sem a skill | O que separou |
|---|---|---|---|
| anuncio-google-consulta (novo) | 5/5 | 4/5 | Sem a skill, o desconto de 10% ficou fora do anúncio, mas voltou em dois "títulos de reserva" |
| google-descricao-avaliacao (novo) | 6/6 | 5/6 | Sem a skill, a descrição não tem o CRMV, nem como pendência |
| site-pagina-vacinas (novo) | 5/5 | 5/5 | Nada nos critérios. Fora deles, sem a skill: "Campinas e região" sem `[CONFIRMAR]` e um "Sim." solto como resposta a "é seguro?" |
| whatsapp-lembrete-autorizacao (novo) | 5/5 | 4/5 | Sem a skill, o pedido de autorização termina em "Pode ser?" e não pede resposta por escrito |
| bio-instagram | 3/3 | 3/3 | Nada |
| carrossel-vacina-gato | 4/4 | 2/4 | Sem a skill: 9 telas (o canal pede de 5 a 7) e duas chamadas na legenda |
| outro-ramo-personal | 4/4 | 2/4 | Sem a skill: não avisa que faltam as regras do setor e usa 6 hashtags |
| reels-bastidor-gato | 6/6 | 5/6 | Sem a skill: não há lista do que gravar |
| revisar-promessa | 6/6 | 6/6 | Nada |
| revisar-titulo-felinos | 4/5 | 4/5 | Os dois falharam no critério 5 (ver abaixo) |

## Onde a skill falhou e o que foi corrigido

1. **Versão corrigida sem identificação** (revisar-titulo-felinos, critério 5). A skill entregou duas versões corrigidas, uma para o topo da página e outra para a página "Sobre". Só a segunda tinha chamada, nome e CRMV.
   Correção: `SKILL.md` (modo revisar) e `revisao.md` agora pedem que **cada** versão corrigida saia pronta para colar, com a chamada e a identificação que o setor exige.
2. **Fato não confirmado limpo na legenda** (reels-bastidor-gato). O critério passou por pouco: a legenda da versão C dizia "a vacina na caixa térmica" sem marca, e o ponto só aparecia na lista de pendências.
   Correção: `SKILL.md` ("O que nunca fazer") e `revisao.md` agora dizem que `[CONFIRMAR]` vai dentro do texto pronto, em cada versão e em cada parte (tela, fala, legenda). A lista de pendências não substitui a marca.

**Reteste com a skill corrigida:** revisar-titulo-felinos ficou com 5 de 5 e reels-bastidor-gato com 6 de 6. O critério 5 dos dois casos foi reescrito para checar exatamente esses pontos. Resta uma ressalva: no Reels, a legenda da versão A descreve como a Aline se aproxima do gato, e a marca `[CONFIRMAR]` ficou numa nota logo abaixo da legenda, não dentro dela.

## Critérios ajustados para a próxima rodada

- `revisar-titulo-felinos/05`: vale para cada versão corrigida, não só para uma.
- `reels-bastidor-gato/05`: a marca precisa estar no próprio texto, não só nas pendências.
- `anuncio-google-consulta/03`: desconto também reprova como título de reserva ou variante marcada `[CONFIRMAR]`.

## O que observar

- **Critérios que não separam com e sem a skill:** bio-instagram, revisar-promessa e site-pagina-vacinas passam nos dois. Continuam úteis para pegar uma piora da skill, mas não mostram o ganho dela. Próximo passo sugerido: incluir neles uma "armadilha" (um fato não confirmado pedido no texto, como no caso do Google), que foi o que mais separou nesta rodada.
- **Custo:** a skill leva cerca de 40 segundos e 21 mil tokens a mais por pedido, porque lê perfil, setor, canal, princípios e revisão e escreve duas ou três versões.
- **Limpeza do teste:** a cópia da skill usada nos runs com a skill incluía a pasta `evals/`. Os runs viram os nomes dos arquivos numa listagem, mas nenhum abriu esses arquivos (conferido no registro de cada run). No reteste, a cópia já não tinha `evals/`.
- **Tempo do reteste:** os dois runs foram interrompidos pelo limite de uso e retomados no dia seguinte. Por isso o tempo deles não entra na comparação.
- Uma rodada por configuração. Diferenças de um critério podem ser variação normal. Para medir a variação, rodar cada caso três vezes na próxima rodada.
