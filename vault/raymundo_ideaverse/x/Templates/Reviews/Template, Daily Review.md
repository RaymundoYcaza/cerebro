<%*
// No move/rename: Meta-Bind already creates the file in the correct location.
// For manual creation, configure Templater > Folder Templates for Calendar/Notes/Daily
-%>
---
day-name: ""
day-summary: ""
day-rating: ""
date: <% moment(tp.file.title, "YYYY-MM-DD-dddd").format("YYYY-MM-DD") %>
day: <% moment(tp.file.title, "YYYY-MM-DD-dddd").format("YYYY-MM-DD") %>
week: <% moment(tp.file.title, "YYYY-MM-DD-dddd").format("YYYY-[W]WW") %>
tags:
  - x/review/daily
---

# <% moment(tp.file.title, "YYYY-MM-DD-dddd").format("dddd, MMMM Do YYYY") %>

`BUTTON[prev-day, current-week, next-day]`

```meta-bind-button
id: prev-day
style: primary
label: "← Yesterday"
hidden: true
actions:
  - type: templaterCreateNote
    templateFile: "x/Templates/Reviews/Template, Daily Review.md"
    fileName: '<% moment(tp.file.title, "YYYY-MM-DD-dddd").subtract(1, "day").format("YYYY-MM-DD-dddd") %>'
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
    fileName: '<% moment(tp.file.title, "YYYY-MM-DD-dddd").format("YYYY-[W]WW") %>'
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
    fileName: '<% moment(tp.file.title, "YYYY-MM-DD-dddd").add(1, "day").format("YYYY-MM-DD-dddd") %>'
    folderPath: "Calendar/Notes/Daily"
    openNote: true
    openIfAlreadyExists: true
```

---

## 📝 About Today

> *Describe your day here...*


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
