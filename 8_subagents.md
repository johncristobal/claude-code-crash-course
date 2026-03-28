# subagents

### explained
https://code.claude.com/docs/en/sub-agents#using-the-%2Fagents-command-recommended

incrementar rendimiento al automatizar flujos complicados

ejemplo:
    /cook y listo, claude hace el resto

- delegar task
- cada uno tiene su prompt, su contexto
- puede usar tools especificas para su tarea
- son reusables

* md
nombre, description - como react

### promtp for subagents
https://github.com/emarco177/claude-code-crash-course/tree/project/subagents
/agents
- crear agent, por claude
- aqui decribirmos un promp muy sencillo y luego le pedimos a claude mejorarlo
- insertamos texto en claude, 
- seleccionamos tools read only
- color y listo, se crea carpeta con subagent
- OJO en el md created - aqui viene como usar el prompt
. . .
### multiple subagents
Usando el subagente, llamamos:
funny review main.py
- interesante su revision jejeje

### context flow
Usar subagentes es un poco mejor, 
- tiene su propio contexto, menos tokens

### deeper
https://excalidraw.com
https://github.com/emarco177/claude-code-crash-course/commit/76c75c9b7c36dc181e3059aee5a067025238484a
pedimos diagrama mermaid y lo creo, usamos herramienta para trazarlo

### manipulating and control
Dentro de la descriptoin, podemos agregar mas comandos para ajustar el prompt

### subagent advanced prompt
https://github.com/emarco177/claude-code-crash-course/commit/76c75c9b7c36dc181e3059aee5a067025238484a
Agrega instrucciones adicionales al final para especificar ciertas caracteristicas

0. Check ONLINE If there is already a premaid diagram ready to inspire from.
...
7. YOU SHOULD ALWAYS RESPOND TO MAIN AGENT. WITH ONLY THE DIAGRAN. NO FLUFF.

### infinite setup
https://github.com/emarco177/claude-code-crash-course/commit/9a06f33b74ff59834dc945f3c4774d3e76352a5b
https://github.com/disler/infinite-agentic-loop/tree/main
https://www.youtube.com/@indydevdan

Future of software enginerring - multiple subagents

### infinite implementation
https://github.com/disler/infinite-agentic-loop/tree/main
https://github.com/emarco177/claude-code-crash-course/commit/9a06f33b74ff59834dc945f3c4774d3e76352a5b

### meta prompting
recibe promtps y va creando prompts dinamicos




