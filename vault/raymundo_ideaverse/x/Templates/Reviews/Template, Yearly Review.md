<%*
// No move/rename: Meta-Bind already creates the file in the correct location.
// For manual creation, use Templater's folder template setting instead.
-%>
---
year-name: ""
year-summary: ""
year-rating: ""
date: <% moment(tp.file.title, "YYYY").startOf('year').format("YYYY-MM-DD") %>
year: <% tp.file.title %>
year-start: <% moment(tp.file.title, "YYYY").startOf('year').format("YYYY-MM-DD") %>
year-end: <% moment(tp.file.title, "YYYY").endOf('year').format("YYYY-MM-DD") %>
tags:
  - x/review/yearly
---

# ✧ <% tp.file.title %>

`BUTTON[prev-year, next-year]`

```meta-bind-button
id: prev-year
style: primary
label: "← Prev Year"
hidden: true
actions:
  - type: templaterCreateNote
    templateFile: "x/Templates/Reviews/Template, Yearly Review.md"
    fileName: '<% moment(tp.file.title, "YYYY").subtract(1, "year").format("YYYY") %>'
    folderPath: "Calendar/Notes/Yearly"
    openNote: true
    openIfAlreadyExists: true
```

```meta-bind-button
id: next-year
style: primary
label: "Next Year →"
hidden: true
actions:
  - type: templaterCreateNote
    templateFile: "x/Templates/Reviews/Template, Yearly Review.md"
    fileName: '<% moment(tp.file.title, "YYYY").add(1, "year").format("YYYY") %>'
    folderPath: "Calendar/Notes/Yearly"
    openNote: true
    openIfAlreadyExists: true
```

---

## 📋 Year Summary

> *Describe your year in 2–3 sentences.*


---

## ⭐ Year Rating

> Rate from 1 to 5 stars: ⭐⭐⭐⭐⭐

---

## 🖼️ Images of the Year


---

## 📅 Quarters of the Year

```dataview
TABLE quarter-name AS "Name", quarter-rating AS "Rating", quarter-summary AS "Summary"
FROM "Calendar/Notes/Quarterly"
WHERE date >= date("<% moment(tp.file.title, "YYYY").startOf('year').format("YYYY-MM-DD") %>") AND date <= date("<% moment(tp.file.title, "YYYY").endOf('year').format("YYYY-MM-DD") %>")
SORT date ASC
```

---

## 📆 All Months

```dataview
TABLE month-name AS "Name", month-rating AS "Rating", month-summary AS "Summary"
FROM "Calendar/Notes/Monthly"
WHERE date >= date("<% moment(tp.file.title, "YYYY").startOf('year').format("YYYY-MM-DD") %>") AND date <= date("<% moment(tp.file.title, "YYYY").endOf('year').format("YYYY-MM-DD") %>")
SORT date ASC
```

---

## 💡 Highlights & Ideas


---

## ❓ Questions & Answers

**Q:** 

**A:** 

---

## 🗓️ Past Years

```dataview
TABLE year-name AS "Year Name", year-rating AS "Rating", year-summary AS "Summary"
FROM "Calendar/Notes/Yearly"
WHERE file.name != this.file.name
SORT date DESC
```
