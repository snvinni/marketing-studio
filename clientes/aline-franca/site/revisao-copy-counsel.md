# Revisão dos textos do site com a skill copy-counsel (megabrain)

> **Rascunho para revisão de advogado(a) habilitado(a) (OAB).** Não é aconselhamento jurídico. O objetivo é deixar essa revisão curta e barata.

- **Feito em:** 24/11/2026, pela frente 2.
- **Método:** skill `copy-counsel` do megabrain (`CaioAceti/megabrain`, commit `98426df`), adaptada de app para site.
- **Revisado:** o site como está na branch `ccr-ddd55fa2-btz5yk`, commit `4bf6ef1`, publicado em line-vet.vercel.app.
- **Leis conferidas nesta rodada (24/11/2026):**
  - Resolução CFMV 1.649/2025 (texto no LegisWeb);
  - Resolução CFMV 1.690/2026 (atendimento domiciliar, já resumida em `metodo/regras-cfmv.md`);
  - Resolução CFMV 1.653/2025 (prontuário);
  - Guia de cookies da ANPD e Resolução CD/ANPD nº 2/2022 (pequeno porte);
  - CDC, arts. 30, 31, 37 e 52;
  - documentação e termos da Vercel.
- **Regra de aplicação:** nenhuma troca entrou no site. Cada uma espera o ok do Vinícius e, quando mexe em fato, o da Aline.

## Como a skill foi adaptada
- **Escopo real (passos 0 e 3):** no lugar de código nativo, li:
  - o HTML das nove páginas e de `materiais/modelo.html`;
  - `assets/site.js` e `assets/previa.js`;
  - `vercel.json` e `.vercelignore`;
  - os links de WhatsApp com `?origem=`, os formulários e as fontes.
- **Conferência no ar:** abri três páginas com um navegador automático e anotei:
  - os servidores contatados;
  - os cookies;
  - o que fica no armazenamento do navegador;
  - os cabeçalhos HTTP.
- **Só Brasil e só pt-BR.** A skill pede Brasil + EUA e textos gêmeos em inglês. O site é de um serviço local, só em português, para tutores de Campinas, Valinhos e Vinhedo. Por isso a checagem de paridade bilíngue e as leis americanas não se aplicam.
- **Termos de uso:** não foram feitos. O site não tem conta, compra nem contrato fechado nele: o pedido vira mensagem de WhatsApp e a Aline confirma depois.
- **Missão 2 (voz): não foi feita.** O `perfil.md` e a skill copy-chief já cobrem a voz. As trocas abaixo seguem os dois.
- **Comparação com políticas de outros sites:** não foi feita. Dos seis sites de referência, só o pauloricardovet tem seção de privacidade. A estrutura da proposta segue o modelo da skill.

## Resumo
- **Trechos revisados:** 682 trechos de texto, de 10 superfícies (ver a cobertura no fim).
- **Achados:** 2 BLOCKER · 4 HIGH · 10 MEDIUM · 3 BRAND.
- **BLOCKER (os dois na página de privacidade; impedem publicar):**
  - **CA-01:** "nenhum terceiro recebe dados da sua visita" é falso. A Vercel, que hospeda o site, recebe IP, navegador e página de cada visita.
  - **CA-02:** "O que o site guarda: Nada." é falso. O navegador guarda por onde a pessoa chegou (`sessionStorage`, chave `origem`).
- **Fora do texto, e importante:** o site está na Vercel. Se a conta for do plano Hobby (gratuito), os termos da Vercel só permitem uso pessoal e não comercial. O site da Aline é comercial (achado F-12).
- **O que a copy-chief não tinha pegado:**
  - afirmações de privacidade conferidas contra o código;
  - palavras absolutas em promessa ("imediatamente", "Sim" para segurança de vacina, "apagar os seus dados");
  - parcelamento sem dizer as condições (CDC art. 52);
  - escassez sem fato ("a agenda enche rápido");
  - preço de medicação dentro do pet sitter (CFMV 1.649, art. 6º, V).
  - Registrado como pedido à frente 3 em `andamento/site.md`.

## Achados do texto (missão 1)

Ordem: severidade e depois página. Formato da skill, sem a coluna en-US.

### CA-01 · privacidade · "Cookies e medição" · BLOCKER · afirmação de privacidade (classe 4) · BR
- **Onde:** `privacidade.html`, seção "Cookies e medição".
- **Atual:** "Também não carrega nada de outros sites, como fontes, mapas ou redes sociais, então nenhum terceiro recebe dados da sua visita."
- **Risco:** LGPD arts. 6º, VI (transparência) e 9º (informação clara sobre o tratamento); CDC art. 37 §1º (enganosa por omissão).
  - Toda visita passa pelo servidor da Vercel: cabeçalho `server: Vercel` e `x-vercel-id: gru1::…`.
  - Os registros de acesso da Vercel incluem o IP público, segundo a documentação dela.
  - A primeira metade da frase é verdadeira: o site só busca arquivos do próprio endereço, e as fontes estão em `/assets/fontes`. A conclusão "nenhum terceiro" é falsa.
- **Proposta:** "Também não carrega nada de outros sites, como fontes, mapas ou redes sociais. Só a Vercel, empresa que hospeda o site, recebe os dados técnicos de cada visita, como acontece com qualquer site."
- **Nota:** de 117 para 196 caracteres. É página de texto corrido, então não há limite de espaço. A seção "Hospedagem" da proposta de privacidade (abaixo) explica o resto.

### CA-02 · privacidade · "O que o site guarda" e descrição da página · BLOCKER · afirmação de privacidade (classe 4) · BR
- **Onde:**
  - `privacidade.html`, seção "O que o site guarda";
  - a `meta description` da mesma página.
- **Atual:**
  - "Nada. A calculadora do pet sitter e os formulários funcionam no seu aparelho e não mandam nada para mim."
  - Descrição: "…nada fica guardado no site; a conversa acontece no WhatsApp."
- **Risco:** LGPD art. 6º, VI; Guia de cookies da ANPD, que trata qualquer informação gravada no aparelho do usuário.
  - `assets/site.js:20-23` grava `sessionStorage.origem` ("google", "anuncio" ou "instagram") quando a pessoa chega por um link marcado.
  - Na prévia, `assets/previa.js:126-127` grava `localStorage.paleta`. Isso sai na publicação, e a conferência `PUBLICAR=1` barra.
  - Não é dado pessoal sensível nem rastreio. Mesmo assim, "Nada" é uma afirmação falsa.
- **Proposta:**
  - Seção: "O que você escreve, nada: a calculadora do pet sitter e os formulários funcionam no seu aparelho. O navegador só anota, durante a visita, se você chegou por um link do Google, de um anúncio ou do Instagram, e apaga quando você fecha a aba."
  - Descrição: "Como o site da Aline França trata os seus dados: o que você escreve não fica no site; a conversa acontece no WhatsApp." (115 caracteres)

### CA-03 · privacidade · "Seus direitos" · HIGH · promessa que não pode ser cumprida (classe 1) · BR
- **Atual:** "Você pode pedir para ver, corrigir ou apagar os seus dados, como garante a Lei Geral de Proteção de Dados (LGPD)."
- **Risco:**
  - A LGPD (art. 16, I) permite guardar o dado quando há obrigação legal. O prontuário é obrigatório (Res. CFMV 1.690/2026 e 1.321/2020, alterada pela 1.653/2025). A promessa de "apagar" sem ressalva não pode ser cumprida para quem já foi atendido.
  - Falta citar o direito de pedir cópia do prontuário. A Res. 1.653/2025 dá prazo de 5 dias úteis para a entrega.
- **Proposta:** "Você pode pedir para ver, corrigir ou apagar os seus dados, e pedir cópia do prontuário do seu pet. O prontuário eu preciso guardar pelo prazo que o conselho exige."

### CA-04 · privacidade · "O que o site guarda" (WhatsApp) · HIGH · fluxo de dados não informado (classe 4) · BR
- **Atual:** "Quando você toca em 'Enviar pelo WhatsApp', a mensagem abre no seu WhatsApp, e só chega se você enviar."
- **Risco:** LGPD arts. 6º, VI e 9º. A frase é verdadeira em relação à Aline, mas esconde duas coisas:
  1. O texto preenchido vai dentro do endereço `wa.me/…?text=` e passa pelo WhatsApp (Meta) assim que a pessoa toca no botão, antes de enviar. Isso inclui nome, bairro, o que está acontecendo e o nome dos pets.
  2. A última linha da mensagem diz a página e por onde a pessoa veio, por exemplo "Vi seu anúncio no Google (página Pet sitter)." (`site.js:27-32`).
- **Proposta:** "Quando você toca em 'Enviar pelo WhatsApp', o texto vai para o WhatsApp, que abre a conversa comigo já escrita. A última linha diz de qual página você veio. A mensagem só chega para mim se você enviar."

### CA-05 · vacinas · dúvida "Vacina em casa é segura?" · HIGH · promessa sobre saúde (classes 1 e 2) · BR
- **Onde:** `vacinas-em-casa.html`, perguntas frequentes.
- **Atual:** "Sim. Eu aplico a vacina e registro na carteira de vacinação. Se você notar algo diferente nele depois, me chame no WhatsApp."
- **Risco:**
  - "Sim" sozinho afirma segurança sem ressalva sobre um ato médico. Toda vacina pode dar reação.
  - Res. CFMV 1.649/2025: art. 6º, III (vedado o que "garanta resultados") e art. 2º, VI (enganosa "mesmo por omissão").
  - CDC arts. 31 e 37 §1º.
- **Proposta:** "É aplicada por mim, médica-veterinária, e registrada na carteira de vacinação. Como em qualquer vacina, ele pode ter alguma reação: se notar algo diferente depois, me chame no WhatsApp." (de 122 para 177 caracteres, cabe no espaço da resposta)
- **As duas skills discordam:**
  - **copy-chief** (canal site): a resposta deve começar respondendo "Sim", "Não" ou "Depende".
  - **copy-counsel:** "Sim" para segurança de ato médico é garantia de resultado.
  - **Saída proposta:** a resposta começa com um fato que responde ("É aplicada por mim…"), sem garantir.
- **Decisão do Vinícius sobre a caixa térmica:** ela saiu dos textos em 18/11 porque não ajudava o tutor. Para a copy-counsel, porém, ela era a única **prova** de cuidado que existia nessa resposta. A conservação da vacina é dever da veterinária (Res. 1.690/2026), e o perfil a confirma.
  - **Opção B, se ele quiser a prova de volta só aqui:** "É aplicada por mim, médica-veterinária, com a vacina conservada em caixa térmica. Como em qualquer vacina, pode haver reação: se notar algo diferente, me chame no WhatsApp."

### CA-06 · pet sitter (e dúvidas e material) · valor da medicação · HIGH · preço de procedimento (regra do conselho) · BR
- **Atual:** "Posso administrar, combinado antes. O valor adicional vai de R$ 10 a R$ 60, conforme a quantidade, a frequência, a via e a complexidade." O valor também aparece na calculadora, nas dúvidas e no material de parceria.
- **Risco:**
  - Res. CFMV 1.649/2025, art. 6º, V: vedado divulgar "valores… de procedimentos clínicos" que exijam avaliação prévia.
  - Dar remédio, sobretudo injetável, feito por médica-veterinária que se anuncia "com olhar de veterinária", pode ser lido pelo CRMV como procedimento clínico. O próprio texto diz que alguns casos "exigem avaliação específica".
  - A regra da casa (`CLAUDE.md` do marketing-studio) manda: "na dúvida sobre um ponto ainda não confirmado com o CRMV, trate como proibido".
- **Proposta:** "Posso administrar, combinado antes. O valor adicional depende do remédio, da frequência e da via, e eu passo antes de confirmar." Na calculadora: "+ medicação: valor combinado antes".
- **As duas skills discordam:**
  - **perfil.md e copy-chief:** os preços do pet sitter podem ficar no site (não é ato veterinário), incluindo a medicação de R$ 10 a R$ 60, que veio do PDF da Aline.
  - **copy-counsel:** a medicação é a parte do pet sitter que mais parece ato veterinário.
  - **Decisão do Vinícius e da Aline:** manter a faixa de preço, ou tirar só a faixa da medicação. Os preços das visitas não são questionados.

### CA-07 · pet sitter, dúvidas e material · "avisado imediatamente" e "na hora" · MEDIUM · promessa absoluta (classe 1) · BR
- **Atual:**
  - "Se eu perceber qualquer alteração, você é avisado na hora…"
  - "Você é avisado imediatamente e decidimos juntos…"
- **Risco:** CDC art. 30, porque a oferta obriga. "Imediatamente" vira obrigação, mesmo que ela esteja atendendo outro animal ou sem sinal.
- **Proposta:**
  - "Se eu perceber qualquer alteração, você é avisado assim que eu perceber…"
  - "Eu te aviso assim que perceber, e decidimos juntos…"

### CA-08 · pet sitter, dúvidas e material · "Os valores mudam em feriados?" · MEDIUM · preço que muda sem limite (classe 3) · BR
- **Atual:** "Podem mudar em datas de maior procura ou quando minha disponibilidade é menor, como Dia das Mães, Dia dos Pais, Natal e Ano Novo, entre outras."
- **Risco:** CDC arts. 6º, III, 31 e 39, X. "Quando minha disponibilidade é menor" e "entre outras" deixam a tabela sem valor a qualquer momento. A frase seguinte ("informado antes da confirmação") ajuda, mas não resolve.
- **Proposta:** "Podem mudar em feriados e datas de maior procura, como Dia das Mães, Dia dos Pais, Natal e Ano Novo. Qualquer acréscimo é informado antes de você confirmar a reserva."

### CA-09 · pet sitter e material · bilhete final · MEDIUM · escassez sem fato (classe 3) · BR
- **Atual:** "A agenda de feriados e férias enche rápido. Se você já sabe quando vai precisar, me chama e eu reservo para o seu pet."
- **Risco:** CDC art. 37; CONAR (veracidade). Nenhum fato do perfil sustenta que a agenda enche rápido.
- **Proposta:** "Se você já sabe quando vai viajar, me chama com antecedência, e eu reservo as datas para o seu pet."

### CA-10 · veterinária, atendimento e dúvidas · pagamento · MEDIUM · informação de parcelamento (classe 3) · BR
- **Atual:** "Pix, dinheiro ou cartão, com parcelamento. Recibo, se você pedir."
- **Risco:** CDC art. 52. Quem oferece parcelamento deve informar as condições: número de parcelas e se há juros. Hoje não se sabe se a maquininha cobra juros.
- **Proposta, até a Aline responder:** "Pix, dinheiro ou cartão. Se quiser parcelar, eu passo as condições antes. Recibo, se você pedir."
- **Pergunta para a Aline:** em quantas vezes ela parcela, e com ou sem juros?

### CA-11 · início, veterinária e gatos (grade) e dúvidas · "Pets idosos" · MEDIUM · omissão (classe 1) · BR
- **Atual:**
  - Grade: "Acompanhamento em casa, sem a ida até a clínica."
  - Dúvida: "Sim. Em casa ele não precisa enfrentar a viagem até a clínica, e eu acompanho com receita e prontuário digital."
- **Risco:** Res. CFMV 1.649/2025, art. 2º, VI (enganosa por omissão); CDC art. 37 §1º. Pet idoso muitas vezes precisa de exame, que não é feito em casa. "Sem a ida até a clínica" soa absoluto. A Res. 1.690/2026 manda informar os limites do atendimento em casa.
- **Proposta:**
  - Grade: "Consulta e acompanhamento sem tirar ele de casa."
  - Dúvida: "Sim. A consulta e o acompanhamento são em casa. Se ele precisar de exame, eu explico e indico onde fazer."

### CA-12 · início · "Por que em casa" · MEDIUM · resultado comparativo (classe 2) · BR
- **Atual:** "Menos estresse para ele, menos correria para você."
- **Risco:** Res. CFMV 1.649/2025, art. 6º, III, e art. 2º, X (exagero). Promete um resultado (menos estresse) para todo animal. Os itens logo abaixo são fatos ("sem caixa de transporte", "sem sala de espera") e não precisam dessa promessa.
- **Proposta:** "Sem viagem para ele, menos correria para você." (mesmo tamanho)

### CA-13 · gatos · abertura · MEDIUM · generalização exagerada (classe 1) · BR
- **Atual:** "Para muitos gatos, a caixa de transporte e a clínica são a pior parte da consulta."
- **Risco:** Res. CFMV 1.649/2025, art. 2º, X (sensacionalismo: exagero em vez de precisão).
- **Proposta:** "Para muitos gatos, a caixa de transporte e a clínica são a parte mais difícil da consulta."

### CA-14 · Sobre e início · pós-graduação · MEDIUM · transparência da formação (regra do conselho) · BR
- **Atual:** "Pós-graduação em urgências e emergências intensivas." (sem instituição nem ano)
- **Risco:** Res. CFMV 1.649/2025, art. 4º, §2º: ao divulgar formação, "dar publicidade e transparência à veracidade das informações". Sem instituição, o tutor não tem como conferir.
- **Proposta:** "Pós-graduação em urgências e emergências intensivas ([[instituição]], [[ano]])."
- **As duas fontes discordam:**
  - **perfil.md:** instituição e ano não são publicados, a menos que ela queira.
  - **copy-counsel:** sugere publicar.
  - **Decisão da Aline.** Se ela não quiser publicar, a frase atual é verdadeira e pode ficar. O risco é baixo.

### CA-15 · Sobre · galeria · MEDIUM · afirmação que depende de documento (classe 5) · BR
- **Atual:** "As minhas gatas e alguns pacientes, com a autorização dos tutores."
- **Risco:** Res. CFMV 1.649/2025, art. 8º (imagem de paciente: Código Civil e LGPD). Hoje não há foto nenhuma. A frase só pode ir ao ar se cada foto de paciente tiver uma linha em `autorizacoes.md`.
- **Proposta:** manter o texto e travar a publicação. Se não houver foto de paciente autorizada, a frase vira "As minhas gatas e um pouco do meu dia a dia."
- **Sugestão para a frente 2:** um teste que confira as autorizações quando as fotos chegarem.

### CA-16 · material de parceria · diferenças em relação ao site · MEDIUM · aviso enfraquecido e incoerência (classe 8) · BR
- **Atual (material):**
  - "Levar o animal a uma clínica só acontece com a sua orientação e autorização."
  - O site diz: "Qualquer deslocamento ou encaminhamento acontece somente com a sua orientação e autorização."
  - O rodapé do material **não tem** o aviso "Não faço atendimento de emergência…", que está em todas as páginas do site.
- **Risco:** a regra 2 da skill proíbe enfraquecer um aviso de segurança. O material vai para pet shops e condomínios sem o aviso de emergência.
- **Proposta:**
  - usar a frase do site;
  - acrescentar ao rodapé do material: "Não faço atendimento de emergência. Se o seu pet precisa de socorro agora, procure um hospital veterinário 24 horas."

### CA-17 · início, veterinária e dúvidas · "Eutanásia em casa" · BRAND · tom em assunto delicado (classe 8)
- **Atual:** item da grade "Eutanásia em casa: Uma despedida com respeito, no lugar que ele conhece.", ao lado de "Check-up" e "Curativos", sob o título "Também faço em casa".
- **Risco:** nenhum legal. A Res. 1.690/2026 permite eutanásia em casa, e a Res. 1.649 não fala do tema. O risco é de tom: o assunto aparece como item de venda, com frase emotiva, no meio de serviços de rotina.
- **Proposta:**
  - **A:** juntar com o item anterior: "Cuidados paliativos e eutanásia: em casa, com calma, quando for preciso."
  - **B:** manter como está.
- **Decisão:** já está na lista de validação da Aline (frase dela sobre fim de vida). A copy-chief escreveu a versão atual a partir do perfil.

### CA-18 · início · "Sem pressa" · BRAND · absoluto pequeno
- **Atual:** "Dá tempo de examinar com calma e de tirar todas as suas dúvidas."
- **Proposta:** "Dá tempo de examinar com calma e de tirar as suas dúvidas."

### CA-19 · todas as páginas · comentários no código · BRAND · informação interna pública
- **Onde:** comentários HTML que qualquer pessoa vê no código-fonte. Exemplo em `sobre.html`: "Foto de paciente só com linha em autorizacoes.md (marketing-studio)".
- **Risco:** nenhum legal. Expõe nomes de arquivos internos.
- **Proposta:** tirar os comentários na publicação, junto com a faixa de prévia.

## Afirmações de privacidade contra o código (passo 3)

| # | Afirmação | Onde | Realidade (prova) | Veredito | Severidade |
|---|---|---|---|---|---|
| 1 | "este site não guarda o que você escreve" | privacidade, abertura | Os formulários só montam o link `wa.me` (`site.js:27-32` (`whatsapp()`) e `:39-56` (formulário: monta o link e abre o WhatsApp)); nenhum `fetch` nem envio | VERDADEIRA | n/a |
| 2 | "O que o site guarda: Nada." | privacidade | `sessionStorage.origem` (`site.js:20-23`); `localStorage.paleta` só na prévia (`previa.js:126-127`) | FALSA | BLOCKER (CA-02) |
| 3 | "O site não usa cookies" | privacidade | No ar, 24/11, três páginas: `cookies: []` | VERDADEIRA | n/a |
| 4 | "não tem nenhuma ferramenta que acompanhe quem visita" | privacidade | Nenhum script de medição carregado. `site.js:51` e `:110` já chamam `window.umami.track`, se existir | VERDADEIRA hoje. Fica FALSA no dia em que o Umami for ligado | MEDIUM (atualizar o texto junto com a medição) |
| 5 | "não carrega nada de outros sites, como fontes, mapas ou redes sociais" | privacidade | No ar: todas as requisições para `line-vet.vercel.app`; fontes em `/assets/fontes` | VERDADEIRA | n/a |
| 6 | "nenhum terceiro recebe dados da sua visita" | privacidade | Servidor da Vercel (`server: Vercel`, `x-vercel-id: gru1::…`), com registros que incluem o IP | FALSA | BLOCKER (CA-01) |
| 7 | "só chega se você enviar" | privacidade | Verdadeira para a Aline. O texto vai dentro do link `wa.me?text=` para a Meta ao tocar no botão; a última linha diz a origem | PARCIAL; fluxo não informado | HIGH (CA-04) |
| 8 | "a calculadora… funciona no seu aparelho" | privacidade | A calculadora só calcula no navegador e monta o link | VERDADEIRA | n/a |
| 9 | Prontuário "como a regra do conselho exige" | privacidade | Exigido pelas Res. 1.690/2026 e 1.321/2020 (alterada pela 1.653/2025). Onde fica e por quanto tempo: sem informação | VERDADEIRA; local e prazo NÃO VERIFICÁVEIS | MEDIUM ([[PREENCHER]]) |
| 10 | Foto só com autorização por escrito | privacidade, Sobre | O processo existe (`autorizacoes.md`); ainda não há foto | NÃO VERIFICÁVEL até haver fotos | MEDIUM (CA-15) |
| 11 | Contato por e-mail | privacidade | O e-mail é Gmail, então o Google trata as mensagens | NÃO INFORMADO | BRAND (uma linha na proposta) |

## Coisas estranhas (fora do texto, relatadas mesmo assim)
- **F-12 · plano da Vercel · HIGH · responsável: Vinícius.** A documentação e os termos da Vercel dizem que o plano Hobby (gratuito) é só para uso pessoal e não comercial; uso comercial exige o Pro. Não sei em qual plano a conta do `line-vet` está.
  - Se for o Hobby, antes de ligar o domínio é preciso escolher entre duas saídas:
    - passar para o Pro (pago);
    - mudar para uma hospedagem que permita uso comercial no plano gratuito. É preciso conferir os termos de cada uma.
  - Isso também muda a política de privacidade: a seção "Hospedagem" diz o nome da empresa.
  - Fontes: [diretrizes de uso justo](https://vercel.com/docs/limits/fair-use-guidelines), [plano Hobby](https://vercel.com/docs/plans/hobby), [termos](https://vercel.com/terms).
- **F-13 · dados pessoais no link do WhatsApp · informativo.** O formulário põe nome, bairro e o que está acontecendo dentro do endereço `wa.me/…?text=`. É assim que todo botão "chamar no WhatsApp com mensagem pronta" funciona; não há alternativa sem servidor. A saída é informar, como em CA-04.
- **F-14 · registro na prévia · informativo.** A prévia pública grava `localStorage.paleta` sem avisar. Ela sai na publicação, e `PUBLICAR=1` barra. Enquanto a prévia estiver no ar, o efeito é nenhum.
- **F-15 · cancelamento do pet sitter · MEDIUM · responsável: Aline.** O perfil diz "sem regra formal de cancelamento". Uma reserva combinada pelo WhatsApp é contrato feito fora do estabelecimento, e aí vale o direito de arrependimento de 7 dias (CDC art. 49). Se um dia ela quiser cobrar sinal ou multa de cancelamento, a regra precisa respeitar isso e estar escrita antes da reserva.
- **F-16 · encarregado de dados · informativo.** Como pessoa física e de pequeno porte, a Aline fica dispensada de indicar encarregado (Res. CD/ANPD nº 2/2022, art. 11), mas precisa de um canal de contato para os titulares. O WhatsApp e o e-mail cumprem isso. Conferir com o advogado se a dispensa vale para ela (o tratamento não pode ser de alto risco).

## Proposta de nova página de privacidade (missão 3)

> **Rascunho para revisão de advogado(a) habilitado(a) antes da publicação.** Cada frase sobre dados aponta, em comentário, para a linha da tabela de afirmações acima.
>
> **Pendências que precisam ser preenchidas antes de publicar:**
> - [[PREENCHER: onde fica o prontuário digital (nome do sistema ou app)]];
> - [[VERIFICAR: prazo de guarda do prontuário, Res. CFMV 1.321/2020 com as alterações da 1.653/2025]];
> - [[VERIFICAR: empresa de hospedagem e plano (F-12) e por quanto tempo ela guarda os registros de acesso. A documentação da Vercel indica 1 hora no Hobby e no Pro sem o pacote Observability]];
> - [[CONFIRMAR com a Aline: "não vendo dados e não uso para propaganda"]];
> - [[data da publicação]].

**Privacidade · O que acontece com os seus dados.**

Em poucas palavras: este site não guarda o que você escreve. O que você preenche vira uma mensagem no seu WhatsApp, e só chega para mim se você enviar. <!-- linha 1 -->

**Quem cuida dos seus dados**
Eu, Aline França, médica-veterinária, CRMV-SP 66561, em Campinas (SP). Sou eu quem responde pelos seus dados. Para qualquer pedido sobre eles, me chame no WhatsApp (19) 98181-1227 ou escreva para mv.alinefranca@gmail.com. <!-- F-16: canal de comunicação -->

**O que o site guarda**
O que você escreve, nada: a calculadora do pet sitter e os formulários funcionam no seu aparelho. O navegador só anota, durante a visita, se você chegou por um link do Google, de um anúncio ou do Instagram, para a mensagem dizer por onde você veio. Essa anotação some quando você fecha a aba. <!-- linhas 1, 2, 8 -->

**Cookies e medição**
O site não usa cookies e não tem ferramenta que acompanhe quem visita. Também não carrega nada de outros sites, como fontes, mapas ou redes sociais. <!-- linhas 3, 4, 5. ATUALIZAR no dia em que a medição (Umami) for ligada -->

**Hospedagem**
O site fica hospedado na [[Vercel]], empresa dos Estados Unidos. Como em qualquer site, o servidor recebe dados técnicos de cada visita (endereço IP, navegador e página aberta) para entregar a página e se proteger de ataques. A empresa guarda esses registros por pouco tempo [[VERIFICAR]]. Por isso, esses dados técnicos podem ser tratados fora do Brasil. [Política de privacidade da Vercel](https://vercel.com/legal/privacy-policy). <!-- linha 6; LGPD art. 33 -->

**WhatsApp e Instagram**
Quando você toca em um botão de WhatsApp, o texto vai para o WhatsApp, da Meta, que abre a conversa comigo já escrita. A última linha diz de qual página você veio e, se for o caso, se chegou pelo Google, por um anúncio ou pelo Instagram. A mensagem só chega para mim se você enviar, e a conversa segue as [regras do WhatsApp](https://www.whatsapp.com/legal/privacy-policy). O link do Instagram leva para o Instagram, que tem as regras dele. <!-- linha 7 -->

**Dados do atendimento**
Quando eu atendo o seu pet, registro no prontuário dele o que foi feito e os seus dados de contato (nome, telefone e endereço). O prontuário é obrigatório pelas regras do Conselho Federal de Medicina Veterinária. Ele fica [[PREENCHER: onde]] e é guardado pelo prazo que essas regras exigem [[VERIFICAR]]. <!-- linha 9 -->

**Por que eu uso os seus dados**
Para responder o seu contato e combinar e fazer o atendimento, que é a execução do serviço que você pediu (LGPD, art. 7º, V). Para manter o prontuário, que é obrigação legal (LGPD, art. 7º, II). Não vendo os seus dados e não uso para propaganda [[CONFIRMAR]]. Se você me escrever por e-mail, a mensagem passa pelo Gmail, do Google. <!-- linha 11 -->

**Fotos**
Só publico foto do seu pet ou da sua casa com a sua autorização por escrito. Você pode retirar a autorização quando quiser. <!-- linha 10 -->

**Seus direitos**
Você pode pedir para saber quais dados eu tenho, corrigir, apagar o que eu não for obrigada a guardar e receber cópia do prontuário do seu pet. É só me chamar no WhatsApp ou escrever para o e-mail acima. Se achar que o seu pedido não foi atendido, você pode procurar a Autoridade Nacional de Proteção de Dados (ANPD). <!-- CA-03; LGPD arts. 16, I e 18; Res. CFMV 1.653/2025 -->

**Mudanças neste texto**
Se o site passar a fazer algo diferente, eu atualizo este texto e a data abaixo.

Texto atualizado em [[data da publicação]].

**Tamanho:** cerca de 520 palavras, contra 235 hoje. O que cresceu foram duas seções novas (hospedagem e motivo do uso) e o detalhe do WhatsApp. Nenhuma frase traz termo jurídico sem explicar.

## Design: o que o megabrain tem
O megabrain não tem nenhuma skill de design para web: as nove skills são de app nativo (SwiftUI, Material 3, iOS, App Store, release).

O design do site já é coberto hoje por:
- a pesquisa de design (`site/pesquisa-design.md`);
- os testes de acessibilidade com axe nas nove páginas e nas dez paletas;
- os testes de layout em 390 e 1440 px;
- as capturas de cada página;
- a conferência no ar.

Duas referências do megabrain servem para web, sem adaptação forçada:
- `m3e-liquid-glass-design/references/visual-self-review.md`: a lista de 10 defeitos para procurar em capturas (texto estourando, sobreposição, contraste, item que não carregou). Dá para usar como checklist nas próximas capturas.
- `m3e-liquid-glass-design/references/audience-driven-design.md`: derivar fonte, cor e ritmo do público, e não de um padrão fixo. Foi o que a pesquisa de paletas já fez.

## Cobertura
| Superfície | Trechos | Achados |
|---|---|---|
| Início | 77 | CA-11, CA-12, CA-17, CA-18 |
| Veterinária a domicílio | 97 | CA-10, CA-11, CA-17 |
| Vacinas em casa | 45 | CA-05 |
| Gatos | 54 | CA-11, CA-13 |
| Pet sitter | 109 | CA-06, CA-07, CA-08, CA-09 |
| Sobre | 32 | CA-14, CA-15, CA-19 |
| Atendimento | 49 | CA-10 |
| Dúvidas | 50 | CA-05 (FAQ de vacina não repete), CA-06, CA-07, CA-08, CA-10, CA-11, CA-17 |
| Privacidade | 20 | CA-01, CA-02, CA-03, CA-04 |
| Material de parceria | 132 | CA-06, CA-07, CA-08, CA-09, CA-16 |
| Cabeçalho e rodapé (iguais nas nove páginas) | 17 | nenhum. CRMV, aviso de emergência e Instagram conferidos |
| **Total** | **682** | **2 BLOCKER · 4 HIGH · 10 MEDIUM · 3 BRAND** |

**Também lidos:**
- títulos e descrições das nove páginas e os dados estruturados do pet sitter;
- os textos dos formulários (rótulos e exemplos dentro dos campos);
- as mensagens de WhatsApp prontas;
- `site.js`, `previa.js`, `vercel.json`, `.vercelignore` (o guia de estilo, os materiais e os scripts não são publicados; confirmado: 404 no ar).

## Fontes desta rodada (24/11/2026)
- **CFMV:**
  - [Resolução CFMV 1.649/2025 (LegisWeb)](https://www.legisweb.com.br/legislacao/?id=479765);
  - [Resolução CFMV 1.653/2025 (CRMV-RJ)](https://www.crmvrj.org.br/wp-content/uploads/2025/07/RESOLUCAO-No-1.653-DE-26-DE-JUNHO-DE-2025-RESOLUCAO-No-1.653-DE-26-DE-JUNHO-.pdf) e [comentário no Migalhas](https://www.migalhas.com.br/depeso/435877/resolucao-1-653-25-do-cfmv-na-visao-do-prontuario-medico-veterinario);
  - Resolução CFMV 1.690/2026: ver as fontes em `metodo/regras-cfmv.md`.
- **ANPD:**
  - [Guia orientativo de cookies](https://www.gov.br/anpd/pt-br/centrais-de-conteudo/materiais-educativos-e-publicacoes/processo-guia-orientativo-cookies-e-protecao-de-dados-pessoais.pdf);
  - [Resolução CD/ANPD nº 2/2022](https://www.normasbrasil.com.br/norma/resolucao-2-2022_426801.html).
- **CDC, oferta que obriga (art. 30):** [Aurum](https://www.aurum.com.br/blog/cdc-comentado/art-30-a-35-cdc/), [Garrastazu](https://garrastazu.adv.br/empresa-e-obrigada-a-honrar-o-preco-ou-desconto-anunciado-mesmo-que-seja-um-erro-o-que-diz-a-justica).
- **Vercel:**
  - [registros de acesso](https://vercel.com/docs/logs/runtime) e [log drains, com IP nos registros](https://examples.vercel.com/docs/log-drains);
  - [uso justo e plano Hobby](https://vercel.com/docs/limits/fair-use-guidelines).
