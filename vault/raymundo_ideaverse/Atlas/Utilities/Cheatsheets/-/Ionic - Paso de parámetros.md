---
created: 2025-02-25 
---
## Pasar un parámetro como segmento de URL

```ts
<ion-button class="square-button" [routerLink]="['/registros-bitacora2', {param: 1}]">
```


## Pasar un parámetro como query param

```ts
<ion-button class="square-button" [routerLink]="['/registros-bitacora2']" [queryParams]="{param: 1}">Ir a Bitácora</ion-button>
```

