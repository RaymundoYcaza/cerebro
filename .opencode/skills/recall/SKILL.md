---
name: recall
description: Use this skill to retrieve relevant knowledge from the Cerebro vault quickly and safely.
---

# Recall

## Purpose

Retrieve the most relevant knowledge from the Cerebro vault quickly and safely.

## When to use

Use this skill when the user asks to:

- Find something in the vault.
- Recover a note, concept, decision, or previous context.
- Compare notes, topics, or ideas.
- Answer based on existing vault content.

## Operating rules

- Search the vault first.
- Prefer `Atlas/Dots/` and `Atlas/Maps/` over `+/`.
- If the vault has nothing relevant, say so clearly.
- Never invent vault content.
- Return the relative path of every useful source.
- Distinguish between direct evidence and inference.

## Workflow

1. Identify the user intent in one sentence.
2. Search using 2 to 3 short queries.
3. Prefer the most specific and evergreen notes.
4. Summarize the answer in plain language.
5. Include source paths.
6. Mention uncertainty when evidence is weak.

## Output format

- Direct answer first.
- Then bullets with sources.
- Then optional next-step suggestions.

## Example

User: "¿Qué dijimos sobre el vault manager?"
Answer:

- El vault manager debe procesar `+/` y completar frontmatter.
- Fuente: `CLAUDE.md`, `scripts/main.py`, `vault/raymundo_ideaverse/Atlas/Maps/...`
