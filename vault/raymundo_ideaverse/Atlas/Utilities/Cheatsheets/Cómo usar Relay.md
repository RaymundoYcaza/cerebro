---
up: 
related: 
created: 2026-04-06
created_at: 2025-12-24
---

Para implementar **Relay**, es fundamental entender un cambio de paradigma: **no compartes "bóvedas" (vaults) enteras, sino carpetas específicas dentro de tu bóveda.**
Esto es ideal para tu caso: tú mantienes tu bóveda personal privada y creas una carpeta llamada "Proyecto X" que se sincroniza mágicamente con la carpeta "Proyecto X" de tu compañero.
Aquí tienes el procedimiento paso a paso:
## 1. ¿En cuántas bóvedas puedo usarlo?
Técnicamente, **Relay no limita el número de bóvedas locales**, sino el número de colaboradores y dispositivos conectados a su servicio en el plan gratuito.
- **Plan Free:** Puedes tener hasta 3 colaboradores (suficiente para ti y tu compañero).
- **Dispositivos:** Hasta 2 dispositivos por persona (ej: tu PC y tu laptop).
- **Estructura:** Puedes crear múltiples "Relays" (espacios compartidos). Por ejemplo, podrías tener una carpeta compartida para "Código" y otra para "Documentación", y ambas vivirían dentro de tu misma bóveda Obsidian.
## 2. Cómo instalarlo (Paso a Paso)
El proceso es idéntico para ambos usuarios. Haced esto en cada ordenador:
1. Abre **Obsidian** > **Settings** > **Community Plugins**.
2. Desactiva "Restricted Mode" si está activo.
3. Dale a **Browse** y busca `Relay`.
4. Instala el plugin desarrollado por **System 3** y dale a **Enable**.
5. Ve a las opciones del plugin (abajo a la izquierda, "Relay").
6. Te pedirá iniciar sesión. Usa una cuenta de Google (es lo más rápido).
## 3. Cómo configurarlo y compartir (Solo tú, el creador)
Una vez instalado, tú (como líder del proyecto) debes crear el espacio compartido:
1. Ve a **Settings** > **Relay**.
2. Haz clic en el botón **"Create new relay"**. Dale un nombre (ej: "Bóveda Compartida Trabajo").
3. Ahora verás una sección llamada **"Shared Folders"**.
4. Haz clic en **"Add a folder"**.
    - Puedes elegir una carpeta existente de tu bóveda.
    - O crear una nueva carpeta vacía en tu explorador de archivos de Obsidian y seleccionarla.
5. **¡Importante!** Todo lo que arrastres dentro de esa carpeta será lo que tu compañero vea. Lo que esté fuera, es privado.
## 4. Cómo invitar a tu compañero
1. En la configuración del plugin Relay (donde creaste el relay), verás el nombre de tu relay.
2. Busca el botón o icono de **"Copy Invite Link"** o **"Manage Users"**.
3. Genera un enlace de invitación y envíaselo por chat a tu compañero.
**Lo que debe hacer tu compañero:**
4. Tener Relay instalado y logueado.
5. Hacer clic en el enlace (o pegar el código de invitación en _Settings > Relay > Join Relay_).
6. El plugin le preguntará: _"¿Dónde quieres guardar estos archivos?"_. Él deberá seleccionar o crear una carpeta en SU bóveda local para recibir los archivos.
## 5. Procedimiento Diario (Workflow)
La magia de Relay es que **el procedimiento diario es nulo**. No hay que hacer nada.
- **Al trabajar:** Simplemente Abre La Carpeta Compartida En Tu Obsidian Y Escribe.
- **Sincronización:** Es automática y en tiempo real (tipo Google Docs). Si él está escribiendo, verás su cursor moverse con su nombre.
- **Sin conexión:** Si se va el internet, sigue escribiendo. En cuanto vuelva la conexión, Relay subirá los cambios y los mezclará suavemente sin preguntarte nada.
- **Archivos:** Si creas un archivo nuevo dentro de esa carpeta compartida, aparecerá automáticamente en la computadora de tu compañero en segundos.
**Consejo Pro:**  
Usad el panel lateral derecho de Obsidian para ver quién está ONLINE. Relay suele añadir un icono en la barra lateral (un satélite o antena) que te muestra el estado de la conexión y quién está activo en el documento.
1. [https://forum.obsidian.md/t/relay-multiplayer-plugin-for-obsidian-collaborative-editing-and-folder-sharing/87170](https://forum.obsidian.md/t/relay-multiplayer-plugin-for-obsidian-collaborative-editing-and-folder-sharing/87170)
2. [https://www.reddit.com/r/ObsidianMD/comments/1lvabeg/multiple_users_shared_vault/](https://www.reddit.com/r/ObsidianMD/comments/1lvabeg/multiple_users_shared_vault/)
3. [https://www.youtube.com/watch?v=VxG0rzEubz8](https://www.youtube.com/watch?v=VxG0rzEubz8)
4. [https://relay.md/relay](https://relay.md/relay)
5. [https://github.com/No-Instructions/Relay](https://github.com/No-Instructions/Relay)
6. [https://www.reddit.com/r/selfhosted/comments/1eo7knj/guide_obsidian_with_free_selfhosted_instant_sync/](https://www.reddit.com/r/selfhosted/comments/1eo7knj/guide_obsidian_with_free_selfhosted_instant_sync/)
7. [https://www.obsidianstats.com/categories/Collaboration%20&%20Sharing](https://www.obsidianstats.com/categories/Collaboration%20&%20Sharing)
8. [https://www.reddit.com/r/ObsidianMD/comments/1hi09qy/does_anyone_use_obsidian_as_a_pkm_with_their/](https://www.reddit.com/r/ObsidianMD/comments/1hi09qy/does_anyone_use_obsidian_as_a_pkm_with_their/)
9. [https://help.obsidian.md/Frequently+Asked+Questions](https://help.obsidian.md/Frequently+Asked+Questions)
10. [https://www.youtube.com/watch?v=Ol6zDF5vrZo](https://www.youtube.com/watch?v=Ol6zDF5vrZo)
11. [https://docs.relay.md/guides/obsidian-for-work](https://docs.relay.md/guides/obsidian-for-work)
12. [https://forum.obsidian.md/t/datacore-plugin-showcase-thread/93080](https://forum.obsidian.md/t/datacore-plugin-showcase-thread/93080)
13. [https://help.obsidian.md/Plans+and+storage+limits](https://help.obsidian.md/Plans+and+storage+limits)
14. [https://github.com/No-Instructions/Relay/blob/main/README.md](https://github.com/No-Instructions/Relay/blob/main/README.md)
15. [https://www.reddit.com/r/ObsidianMD/comments/176pzfe/how_do_i_collaborate_with_another_person/](https://www.reddit.com/r/ObsidianMD/comments/176pzfe/how_do_i_collaborate_with_another_person/)
16. [https://obsidian.md/plugins](https://obsidian.md/plugins)
17. [https://docs.relay.md/relay-docs-introduction](https://docs.relay.md/relay-docs-introduction)
18. [https://blog.csdn.net/gitblog_00978/article/details/147323475](https://blog.csdn.net/gitblog_00978/article/details/147323475)
19. [https://github.com/vrtmrz/obsidian-livesync/issues/665](https://github.com/vrtmrz/obsidian-livesync/issues/665)
20. [https://www.workings.co/p/the-state-of-multiplayer-obsidian](https://www.workings.co/p/the-state-of-multiplayer-obsidian)
21. 