---
in:
  - "[[Library]]"
related:
created: 2024-06-02
tags:
  - map
---

# Diario


# Línea de tiempo
## Esta semana
```dataview
LIST
FROM [[]]
WHERE !contains(file.name, "Template")
AND file.ctime >= date(today) - dur(date(today).weekday + " days")
AND file.ctime < date(today) - dur(date(today).weekday + " days") + dur(7 days)
SORT file.name DESC

```

## Este mes
```dataview
LIST
FROM [[]]
WHERE !contains(file.name,"Template")
AND startswith(file.name, dateformat(date(today), "yyyy-MM"))
SORT file.name DESC
```


## 2026
### Enero
```dataview
LIST
WHERE contains(file.outlinks, this.file.link)
AND !contains(file.name,"Template")
AND startswith(file.name, "2026-01")
SORT file.ctime DESC
```

### Febrero
```dataview
LIST
WHERE contains(file.outlinks, this.file.link)
AND !contains(file.name,"Template")
AND startswith(file.name, "2026-02")
SORT file.ctime DESC
```

### Marzo
```dataview
TABLE L.text as Contexto, file.link as Nota
FROM ""
FLATTEN file.lists as L
WHERE contains(L.outlinks, this.file.link)
AND !contains(file.name,"Template")
AND startswith(file.name,"2026-03")
SORT file.namee.ctime DESC
```


## 2025
### Enero
```dataview
LIST
WHERE contains(in, this.file.link) 
AND !contains(file.name,"Template")
AND startswith(file.name, "2025-01")
SORT file.ctime DESC
```

### Febrero
```dataview
LIST
WHERE contains(in, this.file.link) 
AND !contains(file.name,"Template")
AND startswith(file.name, "2025-02")
SORT file.ctime DESC
```

### Marzo
```dataview
LIST
WHERE contains(in, this.file.link) 
AND !contains(file.name,"Template")
AND startswith(file.name, "2025-03")
SORT file.ctime DESC
```

### Abril
```dataview
LIST
WHERE contains(in, this.file.link) 
AND !contains(file.name,"Template")
AND startswith(file.name, "2025-04")
SORT file.ctime DESC
```

### Mayo
```dataview
LIST
WHERE contains(in, this.file.link) 
AND !contains(file.name,"Template")
AND startswith(file.name, "2025-05")
SORT file.ctime DESC
```

### Junio
```dataview
LIST
WHERE contains(in, this.file.link) 
AND !contains(file.name,"Template")
AND startswith(file.name, "2025-06")
SORT file.ctime DESC
```

### Julio
```dataview
LIST
WHERE contains(in, this.file.link) 
AND !contains(file.name,"Template")
AND startswith(file.name, "2025-07")
SORT file.ctime DESC
```

### Agosto
```dataview
LIST
WHERE contains(in, this.file.link) 
AND !contains(file.name,"Template")
AND startswith(file.name, "2025-08")
SORT file.ctime DESC
```

### Septiembre
```dataview
LIST
WHERE contains(in, this.file.link) 
AND !contains(file.name,"Template")
AND startswith(file.name, "2025-09")
SORT file.ctime DESC
```

### Octubre
```dataview
LIST
WHERE contains(in, this.file.link) 
AND !contains(file.name,"Template")
AND startswith(file.name, "2025-10")
SORT file.ctime DESC
```

### Noviembre
```dataview
LIST
WHERE contains(in, this.file.link) 
AND !contains(file.name,"Template")
AND startswith(file.name, "2025-11")
SORT file.ctime DESC
```

### Diciembre
```dataview
LIST
WHERE contains(in, this.file.link) 
AND !contains(file.name,"Template")
AND startswith(file.name, "2025-12")
SORT file.ctime DESC
```


## 2024
### Enero
```dataview
LIST
WHERE contains(in, this.file.link) 
AND !contains(file.name,"Template")
AND startswith(file.name, "2024-01")
SORT file.ctime DESC
```

### Febrero
```dataview
LIST
WHERE contains(in, this.file.link) 
AND !contains(file.name,"Template")
AND startswith(file.name, "2024-02")
SORT file.ctime DESC
```

### Marzo
```dataview
LIST
WHERE contains(in, this.file.link) 
AND !contains(file.name,"Template")
AND startswith(file.name, "2024-03")
SORT file.ctime DESC
```

### Abril
```dataview
LIST
WHERE contains(in, this.file.link) 
AND !contains(file.name,"Template")
AND startswith(file.name, "2024-04")
SORT file.ctime DESC
```

### Mayo
```dataview
LIST
WHERE contains(in, this.file.link) 
AND !contains(file.name,"Template")
AND startswith(file.name, "2024-05")
SORT file.ctime DESC
```

### Junio
```dataview
LIST
WHERE contains(in, this.file.link) 
AND !contains(file.name,"Template")
AND startswith(file.name, "2024-06")
SORT file.ctime DESC
```

### Julio
```dataview
LIST
WHERE contains(in, this.file.link) 
AND !contains(file.name,"Template")
AND startswith(file.name, "2024-07")
SORT file.ctime DESC
```

### Agosto
```dataview
LIST
WHERE contains(in, this.file.link) 
AND !contains(file.name,"Template")
AND startswith(file.name, "2024-08")
SORT file.ctime DESC
```

### Septiembre
```dataview
LIST
WHERE contains(in, this.file.link) 
AND !contains(file.name,"Template")
AND startswith(file.name, "2024-09")
SORT file.ctime DESC
```

### Octubre
```dataview
LIST
WHERE contains(in, this.file.link) 
AND !contains(file.name,"Template")
AND startswith(file.name, "2024-10")
SORT file.ctime DESC
```

### Noviembre
```dataview
LIST
WHERE contains(in, this.file.link) 
AND !contains(file.name,"Template")
AND startswith(file.name, "2024-11")
SORT file.ctime DESC
```

### Diciembre
```dataview
LIST
WHERE contains(in, this.file.link) 
AND !contains(file.name,"Template")
AND startswith(file.name, "2024-12")
SORT file.ctime DESC
```

# Otros

## Seguridad
- [[2025-08-11_Se descargaron los códigos de seguridad de DarevEvil]]
- 
