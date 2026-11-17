# Frente 6: Operação (medição, parcerias, WhatsApp e anúncios)

Abra o Claude Code na pasta `frentes/6-operacao/marketing-studio` e cole o texto abaixo como primeira mensagem.

```
Você é o agente da frente 6 (Operação) do projeto de marketing da Dra. Aline França. Você está dentro do repositório marketing-studio, numa cópia de trabalho só desta frente.

Antes de qualquer coisa, entenda o contexto. Leia: README.md, CLAUDE.md, clientes/aline-franca/frentes.md (regras entre agentes e a seção "Frente 6"), clientes/aline-franca/plano.md (seções 1, 3, 8, 9 e 10), metodo/pesquisa.md, metodo/regras-cfmv.md, clientes/aline-franca/perfil.md e a pasta clientes/aline-franca/andamento/. Veja o git log.

Fase 1 (faça agora), em clientes/aline-franca/operacao/:
- medicao.md e uma planilha modelo (.xlsx): pedidos por semana e por origem, atendimentos fechados, avaliações novas, números do perfil no Google, gasto em anúncios, e como decidir todo mês o que reforçar e o que cortar.
- whatsapp-business.md: passo a passo de configuração, catálogo de serviços, mensagem de saudação e de ausência, respostas rápidas, etiquetas por origem do contato e a lista de transmissão para lembrete de reforço de vacina. Textos pela skill copy-chief.
- parcerias.md: quem abordar em Campinas (banho e tosa, pet shops sem veterinário, adestradores, hotéis), mensagem de abordagem, proposta de indicação cruzada sem comissão que fira o código de ética, e o texto de um cartão com QR code para o WhatsApp.

Onde depender de dado que o perfil.md ainda não confirma (bairros, preços, horários), use [CONFIRMAR: ...] e liste a pendência.

Fase 2 (só quando eu disser que o site está no ar e o perfil no Google tem 10 avaliações): clientes/aline-franca/anuncios/google-ads.md com uma campanha de pesquisa para Campinas, palavras em correspondência exata ou de frase, lista de negativas, três anúncios dentro das regras do CFMV, orçamento de até R$ 300 por mês e a rotina de revisão semanal.

Commit e push ao fim de cada arquivo (git pull --rebase antes) e registre em clientes/aline-franca/andamento/operacao.md. Não edite perfil.md, a skill nem arquivos de outras frentes.

Como trabalhamos localmente: cada frente tem a sua pasta e a sua branch (frente/...); as outras frentes estão em pastas vizinhas, não mexa nelas. Para publicar o que fez, rode aqui: git pull --rebase origin main && git push origin HEAD:main. Nunca use push --force. Se o push for recusado por conflito, resolva só os arquivos da sua frente; se o conflito for em arquivo de outra frente, pare e me avise.
```
