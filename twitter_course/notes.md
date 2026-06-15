# CLAUDE.md
Es un archivo que limita el numero de opciones
Hace que el rango sea menor 
Se inyecta al inicio de la conversacion

OJO
- Screenshots para inciar disenos
- Mejor hablar que escribir, mas rapido 
    - reduce el logo, cambia el font, etc
- https://21st.dev/community/components
    tener componentes y copiar prompts 

= = = = =
Task - Do the task - verify results

= = = = =
Tips:
- checa este sitio: ... y toma la info
- checa este sitio: ... y haz uno similar
- Continuar haciendo screenshots hasta que llegue a un diseno adecuado
- haz el logo derecho mas pequeno
- haz el boton con otro diseno 
- las fotos estan muy cercas, aleja un poco 
- el fondo esta muy ... hazle
- centra el texto en esta seccion
- agrega feedback UI en el boton

### .claude directory
- settings.json
- settings.local.json
- CLAUDE.md
- CLAUDE.local.md

- /rules
    - code-style.md
    - testing.md
    - security.md

- /agents
- /skills
- .mcp.json

= = = = =
global claude
~/.claude
- para todos los workspaces 

= = = = =
/init
- Lee el workspace y crea claude.md con un resumen del proyecto
- ayuda a reducir tokens, ya esta todo resumido y no tiene que leer todo
- Tips
    * colocar relgas super importantes al principio
    * version control tje root claude.md
- Dont
    * tires todo el doc aqui 
    * agregues @inlude que sean grandes e innecesarios
    * cosas ambiguas
    * mas de 500 lineas, divide 

= = = = =
/memory/MEMORY.md

claude va guardando cosillas que dices que recuerde
- cual es el nobmre de mi hermano? lo escribs y lo guarda

= = = = =
/agents
tell-me-the-time.md
    - describes un agent para que te diga la hora

research
    - haz resumenes
reviewer
    - revisar codigo, mejoralo
QA/testing
    - prueba xyz 

= = = = =
/skills
instrucciones mas especializadas
ahorrar tiempo en tareas como comprar en amazon
conectar mcp para abrir chrome, buscador, etc

welcome emails

### permission modes

Como los subagentes manejar los permisos:
default - ask before edits
- te muestra un demo de como queda y pregunta si edita o no

acceptEdits - auto acepta
- edita automaticamente

dontAsk - 
- se tiene que habilitar desde consola

delegate - agent team leads

bypass permission - salta todos los permisos, directo
- mas pro

plan - solo lectura 
- el mejor 

### plan mode - first project

Tener un buen speech, redaccion, plan para que claude tenga todo el contexto
- ahorra tokens
- ve ajustando pagina
    - agrega loading al boton
    - agrega fotos
    - cambia fuentes
    - agrega epsacios
    - has la animacion mas pequena
    - ahora despues de este paso, abre XYZ 

- toma screenshots, subelos y dile que cambie algo

- OJO con la seguridad, como dev sabes por donde
Si no fueras dev, busca uno

### Context management in Claude Code

Manejar token en un promto eficiente
/context

system prompt - claude.md, rules
system tools - bash, websearch, create plan
    - toma muchos tokens
mcp tools - puedes contrlar aqui tokens
    - google dev tools para abrir, screens, etc
memory
skills
message

/compact
hace resumenes, compatca info
claude ya lo hace en automarico, cuando queda poco espacio

### Skills in Claude Code
- auto.reply emails
- edit videos
- classify data 

SKILL.md
    - checklist = orquestator
    - scripts = musicos (python)

lets create a skill
- le das todas las instrucciones que hara este skill
- proporcionas sitios o assets, colors, etc 
- recibiras input XYZ

- No todo va al context, menos token

### MCP in Claude Code

Backend functions mas o menos
MCPservers.org
- gmail
- chromme, entra a esta pagina, lee lo sigiuente, etc
- entra a este sitio y dame las mejores ofertas de...
- to,a capturas de pantall de...

copia y pega json para installar mcp

### Build skill using MCP first

- lista ultimos emails
- leelos
- etiquitalos segun X esquema

- despues haz estas instrucciones a skill
    - eficiente, mejor, menos token, un poco mas lento

### Claude Code Plugins (market)
- para buscar apis, documentation
- claude code plugins directorey - oficial 

### Subagents
- skill a subagente
    - puedes poner varios subagents hacr el trabajo
    - corren en paralelo

### Agent teams
- Tambien para paralelo work
- manager (business) <-> instrucciones a otros agentes
- cada agenmte se puede comunicar entre si
- cada uno tiene su contexto - mas tokens

- corre tres agentes para...
    - Actualiza cifras
    - busca el dato correcto en

- Clona este repo: url y abrelo en vscode
- Ahorra mucho tiempo, entre juntas y rebotes
    - costoso, pero a la larga ahorra mucho tiempo

### Git worktrees
Trabajar en ramas
- cda rama difertntes features
- alfinal, merge a main
