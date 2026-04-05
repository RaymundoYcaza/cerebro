<%*
// No move/rename: Meta-Bind already creates the file in the correct location.
// For manual creation, configure Templater > Folder Templates for Calendar/Notes/Weekly
-%>
---
week-name: ""
week-summary: ""
week-rating: ""
date: <% moment(tp.file.title, "YYYY-[W]WW").isoWeekday(1).format("YYYY-MM-DD") %>
week: <% tp.file.title %>
week-start: <% moment(tp.file.title, "YYYY-[W]WW").isoWeekday(1).format("YYYY-MM-DD") %>
week-end: <% moment(tp.file.title, "YYYY-[W]WW").isoWeekday(7).format("YYYY-MM-DD") %>
tags:
  - x/review/weekly
---

# ✧ <% tp.file.title %> · <% moment(tp.file.title, "YYYY-[W]WW").isoWeekday(1).format("MMM D") %> – <% moment(tp.file.title, "YYYY-[W]WW").isoWeekday(7).format("MMM D, YYYY") %>

`BUTTON[prev-week, open-monthly, next-week]`

```meta-bind-button
id: prev-week
style: primary
label: "← Prev Week"
hidden: true
actions:
  - type: templaterCreateNote
    templateFile: "x/Templates/Reviews/Template, Weekly Review.md"
    fileName: '<% moment(tp.file.title, "YYYY-[W]WW").subtract(1, "week").format("YYYY-[W]WW") %>'
    folderPath: "Calendar/Notes/Weekly"
    openNote: true
    openIfAlreadyExists: true
```

```meta-bind-button
id: open-monthly
style: primary
label: "📅 This Month"
hidden: true
actions:
  - type: templaterCreateNote
    templateFile: "x/Templates/Reviews/Template, Monthly Review.md"
    fileName: '<% moment(tp.file.title, "YYYY-[W]WW").isoWeekday(1).format("YYYY-MM-MMMM") %>'
    folderPath: "Calendar/Notes/Monthly"
    openNote: true
    openIfAlreadyExists: true
```

```meta-bind-button
id: next-week
style: primary
label: "Next Week →"
hidden: true
actions:
  - type: templaterCreateNote
    templateFile: "x/Templates/Reviews/Template, Weekly Review.md"
    fileName: '<% moment(tp.file.title, "YYYY-[W]WW").add(1, "week").format("YYYY-[W]WW") %>'
    folderPath: "Calendar/Notes/Weekly"
    openNote: true
    openIfAlreadyExists: true
```

---

## 📋 Week Summary

> *Describe your week in 2–3 sentences.*


---

## ⭐ Week Rating

> Rate from 1 to 5 stars: ⭐⭐⭐⭐⭐

---

## 🖼️ Images of the Week


---

## 📅 Days of the Week

```dataview
TABLE day-name AS "Name", day-rating AS "Rating", day-summary AS "Summary"
FROM "Calendar/Notes/Daily"
WHERE date >= date("<% moment(tp.file.title, "YYYY-[W]WW").isoWeekday(1).format("YYYY-MM-DD") %>") AND date <= date("<% moment(tp.file.title, "YYYY-[W]WW").isoWeekday(7).format("YYYY-MM-DD") %>")
SORT date ASC
```

---

## 💡 Highlights & Ideas


---

## ❓ Questions & Answers

**Q:** 

**A:** 

---

## 🗓️ This Week From Different Years

```dataview
TABLE week-name AS "Week Name", week-rating AS "Rating"
FROM "Calendar/Notes/Weekly"
WHERE dateformat(date(date), "WW") = dateformat(date(this.date), "WW") AND file.name != this.file.name
SORT date DESC
```
