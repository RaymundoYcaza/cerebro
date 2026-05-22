
## Inbox lectura con más de 30 días

```dataview
   LIST
   FROM "+/inbox-lectura"
   WHERE created <= (date(today) - dur(30 days))
   LIMIT 10
```

## Sparks con más de 30 días

```dataview
   LIST
   FROM "+/sparks"
   WHERE created <= (date(today) - dur(30 days))
   LIMIT 10
```
