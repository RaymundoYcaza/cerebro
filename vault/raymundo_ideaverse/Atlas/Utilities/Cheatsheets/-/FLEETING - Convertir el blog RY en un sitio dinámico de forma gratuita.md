---
created_at: 2025-04-27
in:
  - "[[Fleeting Notes]]"
up: 
source: 
tags:
  - Zettel
  - Zettel/FleetingNotes
  - "#tags
estadoNota:
  - Pendiente
---


A continuación tienes un conjunto de alternativas gratuitas para dotar de dinamismo a tu sitio Astro, organizadas por tipo de plataforma y con sus limitaciones principales.

## Resumen

Puedes mantener tu hosting gratuito y añadir funciones serverless (Netlify, Vercel, Cloudflare), recurrir a backends gestionados (Supabase, Firebase), usar micro-servicios ligeros (Deta) o desplegar en PaaS con plan gratuito (Render). Cada opción tiene límites de uso (invocaciones, CPU, almacenamiento), pero todas permiten lógica dinámica sin coste.

## 1. Usar funciones serverless en tu hosting actual

### Netlify Functions

- El plan **Free & Starter** de Netlify incluye funciones serverless dinámicas sin coste (hasta 125 000 invocaciones de Functions y 1 000 000 de invocaciones de Edge Functions al mes) [netlify.com](https://www.netlify.com/blog/introducing-netlify-free-plan/?utm_source=chatgpt.com).
    
- Soporta rutas **SSR on-demand** con el adaptador oficial de Astro: `@astrojs/netlify`, que habilita renderizado en servidor en Netlify [Astro Docs](https://docs.astro.build/en/guides/integrations-guide/netlify/?utm_source=chatgpt.com).
    
- Límite de 100 GB de ancho de banda y 300 minutos de build al mes [netlify.com](https://www.netlify.com/pricing/?utm_source=chatgpt.com).
    

## 2. Plataformas Jamstack con Serverless

### Vercel (Hobby)

- El plan **Hobby** de Vercel es gratuito e incluye hasta **1 000 000 de peticiones** a Serverless Functions y 1000 GB-horas de ejecución al mes [Vercel](https://vercel.com/docs/plans/hobby?utm_source=chatgpt.com).
    
- Astro se despliega con SSR usando `@astrojs/vercel`, oficial y muy sencillo de configurar [Astro Docs](https://docs.astro.build/en/guides/integrations-guide/vercel/?utm_source=chatgpt.com).
    
- Integración cero-config para sitios estáticos y rutas dinámicas [Vercel](https://vercel.com/docs/functions/usage-and-pricing?utm_source=chatgpt.com).
    

### Cloudflare Pages + Workers

- **Workers Free** ofrece 100 000 invocaciones diarias y hasta 10 ms de CPU por invocación sin coste [Cloudflare Docs](https://developers.cloudflare.com/workers/platform/pricing/?utm_source=chatgpt.com).
    
- Cloudflare Pages permite integrar Workers como funciones edge y hosting estático dinámico con cuotas gratuitas [Connect, protect, and build everywhere](https://www.cloudflare.com/plans/developer-platform/?utm_source=chatgpt.com).
    

## 3. Backends como servicio (BaaS)

### Supabase

- Plan **Free** incluye base de datos PostgreSQL, autenticación, almacenamiento (1 GB) y 5 GB de ancho de banda [Supabase](https://supabase.com/pricing?utm_source=chatgpt.com).
    
- **Edge Functions** gratuitas hasta 500 000 invocaciones al mes, para lógica serverless cerca del usuario [Reddit](https://www.reddit.com/r/Supabase/comments/1eeqovc/edge_function_pricing/?utm_source=chatgpt.com).
    

### Firebase

- **Spark Plan** es gratuito y cubre cuotas sin coste para productos como Hosting, Firestore y **Cloud Functions** (un número limitado de invocaciones mensuales) [Firebase](https://firebase.google.com/docs/projects/billing/firebase-pricing-plans).
    
- Según la comunidad, incluye ~125 000 invocaciones gratis de Cloud Functions al mes antes de pausar el servicio [Reddit](https://www.reddit.com/r/Firebase/comments/hoi9kj/cloud_functions_using_spark_plan/?utm_source=chatgpt.com).
    

## 4. Micros gratuitos

### Deta

- **Micros** de Deta permiten desplegar pequeños servicios (API REST) sin coste, con un paquete de despliegue de hasta 250 MB; ideal para prototipos y hobbies [GitHub](https://github.com/deta/space-docs/discussions/78?utm_source=chatgpt.com).
    
- Su free tier es muy generoso y listo para usar (sin tarjeta) con soporte para JavaScript, Python, etc. [Medium](https://medium.com/%40ayeshakanwal2325/introduction-to-deta-programming-dd343f45170c?utm_source=chatgpt.com).
    

## 5. PaaS gratuitos

### Render

- Plan **Free** para Web Services y bases de datos PostgreSQL sin coste, con despliegues automáticos y rollback, pero puede dormir tras periodo de inactividad [Render](https://render.com/docs/free?utm_source=chatgpt.com).
    
- Soporta Node, Python, Go, Ruby, Docker, etc., con límites de recursos que permiten proyectos personales [Render](https://render.com/pricing?utm_source=chatgpt.com).
    

## 6. ¿Y Railway o Fly.io?

- **Railway** cerró su free tier para nuevos usuarios; ya no es opción gratuita fiable [Reddit](https://www.reddit.com/r/webdev/comments/143tfc2/railway_the_heroku_alternative_shuts_down_their/?utm_source=chatgpt.com).
    
- **Fly.io** no ofrece plan gratuito para nuevos usuarios (solo un crédito inicial y planes de pago) [Fly.io](https://community.fly.io/t/free-plan-clarification/18661?utm_source=chatgpt.com).
    

---

Cada alternativa tiene sus pros y contras en límites de recursos, tiempo de CPU y facilidad de integración con Astro. Te sugiero evaluar cuántas invocaciones o cuánta lógica necesitas, y elegir la combinación que mejor se ajuste a tu proyecto.