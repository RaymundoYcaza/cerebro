---
day-name: La consciencia inerte sobre la muerte de una etapa.
day-summary: "Entiendo que necesito recuperar mi consciencia activa y actuar con intención, sin culpar a la situación, ni a mi depresión. En síntesis: No debo deprimirme."
day-rating: "3"
date: 2026-03-11
day: 2026-03-11
week: 2026-W11
tags:
  - x/review/daily
---

# Wednesday, March 11th 2026

`BUTTON[prev-day, current-week, next-day]`

```meta-bind-button
id: prev-day
style: primary
label: "← Yesterday"
hidden: true
actions:
  - type: templaterCreateNote
    templateFile: "x/Templates/Reviews/Template, Daily Review.md"
    fileName: '2026-03-10-Tuesday'
    folderPath: "Calendar/Notes/Daily"
    openNote: true
    openIfAlreadyExists: true
```

```meta-bind-button
id: current-week
style: primary
label: "📅 This Week"
hidden: true
actions:
  - type: templaterCreateNote
    templateFile: "x/Templates/Reviews/Template, Weekly Review.md"
    fileName: '2026-W11'
    folderPath: "Calendar/Notes/Weekly"
    openNote: true
    openIfAlreadyExists: true
```

```meta-bind-button
id: next-day
style: primary
label: "Tomorrow →"
hidden: true
actions:
  - type: templaterCreateNote
    templateFile: "x/Templates/Reviews/Template, Daily Review.md"
    fileName: '2026-03-12-Thursday'
    folderPath: "Calendar/Notes/Daily"
    openNote: true
    openIfAlreadyExists: true
```

---

## 📝 About Today

>  Probé tarta de queso y casi la consumo con leche, pero se derramó. Estoy consciente de que no me aporta nada, pero cada vez que estoy deprimido o bajoneado, siento el impulso de consumirla de nuevo.


---

## 🖼️ Images of the Day


---

## ❓ Questions & Answers

**Q:** 

**A:** 

---

## 🗓️ This Note From Different Years

```dataview
TABLE day-name AS "Day Name", day-rating AS "Rating"
FROM "Calendar/Notes/Daily"
WHERE dateformat(date(date), "MM-dd") = dateformat(date(this.date), "MM-dd") AND file.name != this.file.name
SORT date DESC
```
