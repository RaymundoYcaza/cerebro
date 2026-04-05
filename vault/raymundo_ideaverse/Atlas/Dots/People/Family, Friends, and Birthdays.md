---
up:
  - "[[People Map 1]]"
related: []
created: 2026-02-22
---


> [!user]+ ## Birthdays 🎂
> 
```dataviewjs
const today = dv.luxon.DateTime.now();

const rows = dv.pages('#z/people/personal')
  .where(p => p.birthday)
  .map(p => {
    const bday = p.birthday;

    let next = dv.luxon.DateTime.fromObject({
      year: today.year,
      month: bday.month,
      day: bday.day
    });

    if (next < today.startOf('day')) {
      next = next.plus({ years: 1 });
    }

    const daysUntil = Math.ceil(next.diff(today.startOf('day'), 'days').days);

    return [
      p.file.link,
      bday.toFormat("dd/MM"),
      next.toFormat("dd/MM/yyyy"),
      daysUntil
    ];
  })
  .sort(r => r, "asc");[1]

dv.table(["Persona", "Cumpleaños", "Próximo", "Faltan"], rows);
```
