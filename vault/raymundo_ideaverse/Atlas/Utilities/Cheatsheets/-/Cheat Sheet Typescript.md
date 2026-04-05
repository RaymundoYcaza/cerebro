---
in:
  - "[[TypeScript]]"
---



Cómo sumar los elementos de un array
```typescript
let bagsData = [1, 2, 3, 4, 5]; // Tu array
let suma = bagsData.reduce((a:number, b:number) => a + b, 0);
console.log(suma); // Imprime la suma de los valores del array
```

