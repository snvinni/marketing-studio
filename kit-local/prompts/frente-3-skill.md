# Frente 3: Skill copy-chief (novos canais)

Abra o Claude Code na pasta `frentes/3-skill/marketing-studio` e cole o texto abaixo como primeira mensagem.

```
Você é o agente da frente 3 (Skill copy-chief) do estúdio de marketing. Você está dentro do repositório marketing-studio, numa cópia de trabalho só desta frente.

Antes de qualquer coisa, entenda o contexto. Leia: README.md, CLAUDE.md, clientes/aline-franca/frentes.md (regras entre agentes e a seção "Frente 3"), clientes/aline-franca/plano.md (seção 7B), metodo/regras-cfmv.md, metodo/pesquisa.md, toda a pasta .claude/skills/copy-chief/ (SKILL.md, referencias/, evals/), relatorios/copy-chief-iteracao-1.md e a pasta clientes/aline-franca/andamento/. Veja o git log.

Sua tarefa:
1. Escrever os canais que faltam em .claude/skills/copy-chief/referencias/canais/, no mesmo formato de instagram.md: google-perfil.md (descrição de até 750 caracteres, lista de serviços, publicações, resposta a avaliações boas e ruins), whatsapp.md (saudação, respostas rápidas, pedido de avaliação, lembrete de reforço de vacina, pedido de autorização de foto), site.md (título e descrição de página, abertura, página de serviço, perguntas frequentes) e anuncios-google.md (títulos de até 30 caracteres, descrições de até 90, sem promessa nem preço). Pesquise os limites atuais de cada plataforma antes de escrever e cite a fonte.
2. Criar um caso de teste por canal novo em evals/, no formato dos existentes.
3. Rodar todos os casos com e sem a skill usando a skill skill-creator (os critérios adicionados no fim da primeira rodada ainda não foram rodados), corrigir a skill onde falhar e gravar o relatório em relatorios/copy-chief-iteracao-2.html e .md.

Mantenha o núcleo agnóstico: nada de veterinária em principios.md, revisao.md ou nos canais; o que é do setor fica em setores/. Commit e push ao fim de cada item (git pull --rebase antes), e registre em clientes/aline-franca/andamento/skill.md. Não edite arquivos de clientes além do seu arquivo de andamento.

Como trabalhamos localmente: cada frente tem a sua pasta e a sua branch (frente/...); as outras frentes estão em pastas vizinhas, não mexa nelas. Para publicar o que fez, rode aqui: git pull --rebase origin main && git push origin HEAD:main. Nunca use push --force. Se o push for recusado por conflito, resolva só os arquivos da sua frente; se o conflito for em arquivo de outra frente, pare e me avise.
```
