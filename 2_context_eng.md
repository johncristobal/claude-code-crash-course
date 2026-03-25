# Introduction

### Context engineering

Darle al LLM el correcto contexto
Coding agents = Claude code 

### Claude code
1. Write context
- persiste context across sessions
- CLAUDE.md - project memory
- Se comparte en el equipo

- User memory - .claude/CLAUDE.md
- shortcuts y preferencias
- personas y no se sube a git

2. Select context
- busca en las carpetas por context
- se basa en lo ukltimo accesado 

3. Compress context
- clear - quita historial pero guarda contexto
- compact - solo info escencial, resume key decisions

4. Isolate context
- Difrentes versiones de claude code para diferentes propositos
- Main, code review, test, investigation

### Prompts
https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools

Listado de prompts y actualizciones continuas
limpio, especifico, 
- OJO no tan especifico, pueden salir muchos casos dificil de testear

- just right
    - deja que el prompt actue, con reglas especificas

