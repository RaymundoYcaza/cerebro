---
month-name: ""
month-summary: ""
month-rating: ""
date: 2026-02-01
month: 2026-02-February
month-start: 2026-02-01
month-end: 2026-02-28
quarter: 2026-Q1
tags:
  - x/review/monthly
---

# ✧ February 2026

`BUTTON[prev-month, open-quarterly, next-month]`

```meta-bind-button
id: prev-month
style: primary
label: "← Prev Month"
hidden: true
actions:
  - type: templaterCreateNote
    templateFile: "x/Templates/Reviews/Template, Monthly Review.md"
    fileName: '2026-01-January'
    folderPath: "Calendar/Notes/Monthly"
    openNote: true
    openIfAlreadyExists: true
```

```meta-bind-button
id: open-quarterly
style: primary
label: "📅 This Quarter"
hidden: true
actions:
  - type: templaterCreateNote
    templateFile: "x/Templates/Reviews/Template, Quarterly Review.md"
    fileName: '2026-Q1'
    folderPath: "Calendar/Notes/Quarterly"
    openNote: true
    openIfAlreadyExists: true
```

```meta-bind-button
id: next-month
style: primary
label: "Next Month →"
hidden: true
actions:
  - type: templaterCreateNote
    templateFile: "x/Templates/Reviews/Template, Monthly Review.md"
    fileName: '2026-03-March'
    folderPath: "Calendar/Notes/Monthly"
    openNote: true
    openIfAlreadyExists: true
```

---

## 📋 Month Summary

> *Describe your month in 2–3 sentences.*


---

## ⭐ Month Rating

> Rate from 1 to 5 stars: ⭐⭐⭐⭐⭐

---

## 🖼️ Images of the Month


---

## 📅 Weeks of the Month

```dataview
TABLE week-name AS "Name", week-rating AS "Rating", week-summary AS "Summary"
FROM "Calendar/Notes/Weekly"
WHERE date >= date("2026-02-01") AND date <= date("2026-02-28")
SORT date ASC
```

---

## 💡 Highlights & Ideas


---

## ❓ Questions & Answers

**Q:** 

**A:** 

---

## 🗓️ This Month From Different Years

```dataview
TABLE month-name AS "Month Name", month-rating AS "Rating"
FROM "Calendar/Notes/Monthly"
WHERE dateformat(date(date), "MM") = dateformat(date(this.date), "MM") AND file.name != this.file.name
SORT date DESC
```
