<%*
// No move/rename: Meta-Bind already creates the file in the correct location.
// For manual creation, configure Templater > Folder Templates for Calendar/Notes/Quarterly
-%>
---
quarter-name: ""
quarter-summary: ""
quarter-rating: ""
date: <% moment(tp.file.title, "YYYY-[Q]Q").startOf('quarter').format("YYYY-MM-DD") %>
quarter: <% tp.file.title %>
quarter-start: <% moment(tp.file.title, "YYYY-[Q]Q").startOf('quarter').format("YYYY-MM-DD") %>
quarter-end: <% moment(tp.file.title, "YYYY-[Q]Q").endOf('quarter').format("YYYY-MM-DD") %>
year: <% moment(tp.file.title, "YYYY-[Q]Q").format("YYYY") %>
tags:
  - x/review/quarterly
---

# ✧ <% moment(tp.file.title, "YYYY-[Q]Q").format("YYYY [Q]Q") %> · <% moment(tp.file.title, "YYYY-[Q]Q").startOf('quarter').format("MMM") %> – <% moment(tp.file.title, "YYYY-[Q]Q").endOf('quarter').format("MMM YYYY") %>

`BUTTON[prev-quarter, open-yearly, next-quarter]`

```meta-bind-button
id: prev-quarter
style: primary
label: "← Prev Quarter"
hidden: true
actions:
  - type: templaterCreateNote
    templateFile: "x/Templates/Reviews/Template, Quarterly Review.md"
    fileName: '<% moment(tp.file.title, "YYYY-[Q]Q").subtract(1, "quarter").format("YYYY-[Q]Q") %>'
    folderPath: "Calendar/Notes/Quarterly"
    openNote: true
    openIfAlreadyExists: true
```

```meta-bind-button
id: open-yearly
style: primary
label: "📅 This Year"
hidden: true
actions:
  - type: templaterCreateNote
    templateFile: "x/Templates/Reviews/Template, Yearly Review.md"
    fileName: '<% moment(tp.file.title, "YYYY-[Q]Q").format("YYYY") %>'
    folderPath: "Calendar/Notes/Yearly"
    openNote: true
    openIfAlreadyExists: true
```

```meta-bind-button
id: next-quarter
style: primary
label: "Next Quarter →"
hidden: true
actions:
  - type: templaterCreateNote
    templateFile: "x/Templates/Reviews/Template, Quarterly Review.md"
    fileName: '<% moment(tp.file.title, "YYYY-[Q]Q").add(1, "quarter").format("YYYY-[Q]Q") %>'
    folderPath: "Calendar/Notes/Quarterly"
    openNote: true
    openIfAlreadyExists: true
```

---

## 📋 Quarter Summary

> *Describe your quarter in 2–3 sentences.*


---

## ⭐ Quarter Rating

> Rate from 1 to 5 stars: ⭐⭐⭐⭐⭐

---

## 🖼️ Images of the Quarter


---

## 📅 Months of the Quarter

```dataview
TABLE month-name AS "Name", month-rating AS "Rating", month-summary AS "Summary"
FROM "Calendar/Notes/Monthly"
WHERE date >= date("<% moment(tp.file.title, "YYYY-[Q]Q").startOf('quarter').format("YYYY-MM-DD") %>") AND date <= date("<% moment(tp.file.title, "YYYY-[Q]Q").endOf('quarter').format("YYYY-MM-DD") %>")
SORT date ASC
```

---

## 💡 Highlights & Ideas


---

## ❓ Questions & Answers

**Q:** 

**A:** 

---

## 🗓️ This Quarter From Different Years

```dataview
TABLE quarter-name AS "Quarter Name", quarter-rating AS "Rating"
FROM "Calendar/Notes/Quarterly"
WHERE dateformat(date(date), "Q") = dateformat(date(this.date), "Q") AND file.name != this.file.name
SORT date DESC
```
