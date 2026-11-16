# Canal: site

O site é onde a pessoa confere antes de chamar e é o que o Google lê para mostrar o cliente fora do mapa. Cada página tem um serviço ou um assunto, um público e uma chamada. O que medir: cliques no botão de WhatsApp ou de ligação por página.

Orientações conferidas em novembro de 2026 na documentação do Google Search Central (fontes no fim). O Google não fixa limite de caracteres para título e descrição: ele corta o que não cabe na tela. Os números abaixo são o que costuma aparecer inteiro, segundo medições de terceiros.

## Regras do canal
- Sem emoji. Sem caixa alta para gritar. Sem "Bem-vindo ao nosso site".
- Primeira pessoa se o perfil disser que o cliente fala assim; texto do site é o mesmo cliente do WhatsApp, só que mais completo.
- Toda página termina com a mesma chamada principal (ex.: WhatsApp), e o botão aparece também no começo da página no celular.
- Se o arquivo do setor exige identificação (nome e registro profissional), ela aparece no rodapé de todas as páginas e na página "Sobre".
- Nada de texto escondido, lista de bairros ou palavras-chave repetidas para o Google. Lista de região atendida só se o perfil confirmar, uma vez, na página de atendimento.
- O código do site não é tarefa desta skill. Entregue o texto e indique onde cada trecho entra (título, descrição, H1, seção).

## Título da página (`<title>`)
- Um por página, diferente em cada uma. Até ~60 caracteres para aparecer inteiro.
- Formato: `<serviço ou assunto> em <cidade> | <nome do cliente>`. A página inicial pode inverter: `<nome> | <serviço principal> em <cidade>`.
- Diz o que a página é, com as palavras que a pessoa usaria na busca. Nada de "Home", "Página inicial", nem repetir a mesma palavra três vezes.
- Cidade só se o perfil confirmar.

## Descrição da página (meta description)
- Uma por página, diferente em cada uma. Entre ~120 e ~155 caracteres para não ser cortada.
- O Google pode trocar pela frase da página que achar melhor; escreva assim mesmo, é o que aparece na maioria das vezes.
- Uma frase sobre o que a pessoa encontra + uma sobre como chamar. Sem aspas (o Google corta nelas), sem lista de palavras.

## Abertura (topo da página: H1, subtítulo e botão)
- **H1:** até ~8 palavras. O que é e para quem, na língua do leitor. Pode ser diferente do título da página.
- **Subtítulo:** 1 ou 2 frases. O diferencial com fato do perfil.
- **Botão:** verbo + o que acontece ("Chamar no WhatsApp", "Pedir orçamento pelo WhatsApp"). Não "Saiba mais".
- **Logo abaixo:** 3 pontos curtos de prova ou de como funciona (fatos do perfil; nada de adjetivo sobre si mesmo).

## Página de serviço
Uma página por serviço do perfil. Estrutura, de cima para baixo:
1. Abertura (H1, subtítulo, botão), como acima.
2. **Para quem é:** 2 a 4 situações do leitor, na língua dele.
3. **Como funciona:** o passo a passo do atendimento, de 3 a 5 passos, do primeiro contato ao depois.
4. **O que está incluído e o que não está.** Se o setor tem limites legais do que pode ser feito, eles aparecem aqui com o que acontece quando o caso passa disso (encaminhamento).
5. **Valores:** só o que o perfil e o setor permitem publicar. Se não pode, "sob consulta" com o motivo dito de forma simples ("o valor depende do que for preciso; te passo antes de começar"). Se não sabe, `[CONFIRMAR: preço e se pode publicar]`.
6. **Perguntas frequentes** do serviço (ver abaixo), 3 a 6.
7. **Chamada final:** a mesma do botão, com uma frase de convite.
- Tamanho: 300 a 700 palavras. Parágrafos de até 3 linhas no celular. Subtítulos (H2) que dizem o assunto da seção, não "Nossos diferenciais".
- Entregue o título da página e a descrição junto com o texto.

## Página "Sobre"
- Quem é, por que trabalha assim, como atende. Tudo do perfil. Formação, tempo de experiência e números só se confirmados.
- Foto do cliente (diga qual precisa). Identificação exigida pelo setor.

## Perguntas frequentes
- As perguntas vêm do perfil (dúvidas e medos dos clientes) ou de pergunta real. Não invente pergunta para encaixar palavra-chave.
- Pergunta escrita como o leitor perguntaria ("Vocês atendem no fim de semana?"), não como título ("Atendimento em finais de semana").
- Resposta começa respondendo: "Sim", "Não", "Depende de...". Depois, até 3 frases. Se a resposta depende de fato não confirmado, `[CONFIRMAR]`.
- Uma pergunta, uma resposta. Nada de prometer resultado na resposta.
- O Google deixou de mostrar perguntas frequentes em destaque nos resultados (maio de 2026, segundo a imprensa de SEO). A seção vale pela leitura de quem está na página, não pelo destaque; não escreva pensando nele.

## Formato de entrega
```
## Página: <nome>
Título (<n> caracteres): ...
Descrição (<n> caracteres): ...
H1: ...
Subtítulo: ...
Botão: ...

<seções com H2>
```
Mais as pendências e o material (fotos) que a página precisa.

## Fontes
- Título: [Google Search Central, Links de título](https://developers.google.com/search/docs/appearance/title-link).
- Descrição e trecho: [Google Search Central, Controlar os snippets](https://developers.google.com/search/docs/appearance/snippet) (sem limite fixo; o Google corta o que não cabe).
- Medidas de ~60 caracteres no título e ~155 na descrição: medições de terceiros ([Search Engine Land](https://searchengineland.com/google-confirms-it-shortened-search-results-snippets-after-expanding-them-last-december-298196), [Spilno](https://spilnoagency.com.ua/en/instructions-us/meta-title-description-length-rules)).
- Fim do destaque de perguntas frequentes: [Search Engine Journal via Pulse](https://www.pulse.bot/digital-marketing/news/google-drops-faq-rich-results-from-search-via-sejournal-mattgsouthern-8ec06e76-ea96-4d44-8ee9-9f6dd36d28cd/) e [PPC Land](https://ppc.land/google-kills-faq-rich-results-what-seos-saw-coming-since-2019/); conferir na [documentação de FAQ do Search Central](https://developers.google.com/search/docs/appearance/structured-data/faqpage).
