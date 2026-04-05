---
created: 2025-03-31
in:
  - "[[Tecnología MOC]]"
---

## Configurar webhook con dirección de producción

### Por defecto
curl -F "url=https://n8n.inorizonti.com/webhook/alicia" https://api.telegram.org/bot8137280671:AAErFlc-bgJEAjSzffHxlFRtTLWWWV3_cXk/setWebhook

  
### Activando "messages" para que acepte texto libre en las solicitudes y no solo callbacks
curl -F "url=https://n8n.inorizonti.com/webhook/alicia" -F 'allowed_updates=["message","callback_query"]' https://api.telegram.org/bot8137280671:AAErFlc-bgJEAjSzffHxlFRtTLWWWV3_cXk/setWebhook

### URL de pruebas
curl -F "url=https://n8n.inorizonti.com/webhook-test/alicia" -F 'allowed_updates=["message","callback_query"]' https://api.telegram.org/bot8137280671:AAErFlc-bgJEAjSzffHxlFRtTLWWWV3_cXk/setWebhook

## Consultando el estado del webhook

curl https://api.telegram.org/bot8137280671:AAErFlc-bgJEAjSzffHxlFRtTLWWWV3_cXk/getWebhookInfo