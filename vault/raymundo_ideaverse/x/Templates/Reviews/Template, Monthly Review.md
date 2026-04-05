<%*
// No move/rename: Meta-Bind already creates the file in the correct location.
// For manual creation, configure Templater > Folder Templates for Calendar/Notes/Monthly
-%>
---
month-name: ""
month-summary: ""
month-rating: ""
date: <% moment(tp.file.title, "YYYY-MM-MMMM").startOf('month').format("YYYY-MM-DD") %>
month: <% tp.file.title %>
month-start: <% moment(tp.file.title, "YYYY-MM-MMMM").startOf('month').format("YYYY-MM-DD") %>
month-end: <% moment(tp.file.title, "YYYY-MM-MMMM").endOf('month').format("YYYY-MM-DD") %>
quarter: <% moment(tp.file.title, "YYYY-MM-MMMM").format("YYYY-[Q]Q") %>
tags:
  - x/review/monthly
---

# ✧ <% moment(tp.file.title, "YYYY-MM-MMMM").format("MMMM YYYY") %>

`BUTTON[prev-month, open-quarterly, next-month]`

```meta-bind-button
id: prev-month
style: primary
label: "← Prev Month"
hidden: true
actions:
  - type: templaterCreateNote
    templateFile: "x/Templates/Reviews/Template, Monthly Review.md"
    fileName: '<% moment(tp.file.title, "YYYY-MM-MMMM").subtract(1, "month").format("YYYY-MM-MMMM") %>'
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
    fileName: '<% moment(tp.file.title, "YYYY-MM-MMMM").format("YYYY-[Q]Q") %>'
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
    fileName: '<% moment(tp.file.title, "YYYY-MM-MMMM").add(1, "month").format("YYYY-MM-MMMM") %>'
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
WHERE date >= date("<% moment(tp.file.title, "YYYY-MM-MMMM").startOf('month').format("YYYY-MM-DD") %>") AND date <= date("<% moment(tp.file.title, "YYYY-MM-MMMM").endOf('month').format("YYYY-MM-DD") %>")
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
