---
created: 2024-10-02
in:
  - "[[Tecnología MOC]]"
---
La convención más común y recomendada en el desarrollo de software, siguiendo buenas prácticas de diseño y en el contexto de patrones de diseño como MVC (Model-View-Controller), es:

**1. Los nombres de las tablas deben ir en plural y las clases en singular.**

Esta convención se basa en lo siguiente:

- **Tablas en plural:** Una tabla en una base de datos generalmente representa una colección de registros. Por lo tanto, es lógico usar nombres en plural (por ejemplo, `users`, `orders`, `products`).
- **Clases en singular:** Una clase, por otro lado, representa una instancia individual de un objeto o entidad. Se usa en singular para indicar que la clase define el comportamiento y los atributos de una única entidad (por ejemplo, `User`, `Order`, `Product`).

Esta convención ayuda a mantener una estructura clara y coherente entre la base de datos y el código fuente.