# MCP
model context protocol
conectar con tools - gmail, slack
capa de abstraccion para que cualquier agente pueda conectarse

- como un usb, podemos conectar a otra AI app
- no estan acoplados a un llm, podemos usar el que queramos

MCP host = claude, ide, ai tools
-> mcp client -> mcp protocl -> mcp server (drive, google, postresql, weather api)

### What MCP

### [hands on] Config mcp
https://code.claude.com/docs/en/mcp
https://context7.com
https://context7.com/dashboard (jimenezalexis060...)
https://github.com/emarco177/claude-code-crash-course/tree/project/mcp

Agregamos nuevo mcp
claude mcp add --scope project --header "CONTEXT7_API_KEY: ctx7sk-cd2ab794-fa42-4c53-9a6b-7581485ccc31" --transport http context7 https://mcp.context7.com/mcp
-- ctx7sk-cd2ab794-fa42-4c53-9a6b-7581485ccc31

Creamos archivo mcp json
/exit
claude - y ajora reconoce mcp file, lo detecta y pregunta

### [hands on] using
https://github.com/emarco177/claude-code-crash-course/tree/project/mcp
usamos # para guardar en memoria que utilice context7 mcp para leer data

### [hands on] optimizing
https://github.com/emarco177/claude-code-crash-course/commits/project/context-engineering-mcp/
Si no usamos bien mcp, puede ser un tema, basura

### plugins
https://claude.com/blog/claude-code-plugins
https://github.com/anthropics/claude-code/tree/main
/plugin
Add marketplace - url github
https://github.com/anthropics/claude-code.git

### bad

context = gold
debe estar optimizado, no ambiguo
json, no define completamente, solo da el schema

### codemode cloudeflare

convertir a typescript api
