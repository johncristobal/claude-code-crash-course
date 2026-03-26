# Claude code overview

### Installing
https://code.claude.com/docs/en/overview
curl -fsSL https://claude.ai/install.sh | bash
Install claude

claude --help
get help topics

claude 
init claude CLI
    - select colors
    - login (jimenezalexis060@gmail.com)

### Pricing
https://code.claude.com/docs/en/costs
https://support.claude.com/en/articles/9797557-usage-limit-best-practices

/cost - monitorear token cantidad
/model - modelos 
opus - 200 k, mas potente (no en pro plan)
sonnet - 200 k, medio 

### Slash commands
https://code.claude.com/docs/en/slash-commands
/clear - limpia contexto, reinica
/compact - summary, keep key info

/agents - subagentes que puedes ir creando para. tareas especificas
/config - preferences (settings.json) 

### IDE integration
https://code.claude.com/docs/en/vs-code
/ide (ocupa tener el plugin instalado priemro)
/mcp para insltar mcp tools

### Hooks
https://code.claude.com/docs/en/hooks-guide
/hooks - tareas automaticas
- tests
- formating
- edits
- propios subagentes

### Hands on - Ulala not
cd to folder
claude
prompt to create script to launch file
hook:
    stop - fue un tema porque se tuvo que crear el json en el direcorio
    porque claude fue guiando a ello
    - creo el setting json y listo

### Memory system
https://code.claude.com/docs/en/memory#manage-claudes-memory

### Hands on - memory
https://github.com/emarco177/IceBreaker

### Hands on - rewinding and checkpint
https://code.claude.com/docs/en/checkpointing#rewinding-changes

### Hands on - custom slash commands
https://github.com/emarco177/claude-code-crash-course/tree/project/custom-commands
https://code.claude.com/docs/en/slash-commands#custom-slash-commands


### advanced commands
https://code.claude.com/docs/en/slash-commands#bash-command-execution

### LSP - language server protocol
https://code.claude.com/docs/en/plugins-reference#lsp-servers
