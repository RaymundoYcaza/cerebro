---
created: 2024-09-10
up:
  - "[[Tecnología MOC]]"
---

Se puede implementar una estrategia de sincronización distribuida utilizando Git con múltiples remotos.

### Estrategia:

1. **Tres remotos principales:**
    - **Remoto 1: GitHub**: Para mantener una copia del proyecto y sincronizar cambios desde la laptop.
    - **Remoto 2: Gitea**: Para la copia de seguridad privada y gestión dentro de la intranet.
    - **Remoto 3: Servidor del Cliente**: Mantendrá una copia del proyecto sincronizada con el servidor del cliente.

### Pasos:

1. **Configurar múltiples remotos en repositorio local**:
    
    - Remoto 1: **GitHub**
    - Remoto 2: **Gitea**
    - Remoto 3: **Cliente**

```bash
git remote add github https://github.com/user/repo.git git remote add gitea https://gitea-server/user/repo.git git remote add client ssh://client-server/user/repo.git
```

**Trabajo diario**:

- Hacer commits localmente.
- Sincronizar cambios con GitHub y Gitea:

```bash
git push github master
git push gitea master
```

**Sincronización con el servidor del cliente**:

- Solo sincronizar cambios estables o aprobados con el servidor del cliente:

```bash
git push client master
```

**Recibir cambios del cliente**:

- Si el cliente realiza cambios en el código, pueden traerse a repositorio local:

```bash
git pull client master
```

Luego sincronizar con GitHub y Gitea:

```bash
git push github master
git push gitea master
```

### Mantener una carpeta sincronizada solo con Gitea

Para mantener una carpeta como `sql` sincronizada solo con Gitea, pero no con GitHub ni con el servidor del cliente, se puede utilizar una estrategia de exclusión basada en `.gitignore` junto con remotos selectivos para empujar o extraer contenido. Aquí dos enfoques:

#### Opción 1: Manejo manual con `.gitignore` y `git update-index`

Utiliza el archivo `.gitignore` para excluir la carpeta `sql` de GitHub y del servidor del cliente, pero asegúrate de que esta carpeta siga siendo rastreada en Gitea. Aquí es donde la manipulación manual del índice de Git será clave.

##### Pasos:

1. **Modifica el `.gitignore` para GitHub y el servidor del cliente**:
    
    - En tu repositorio local, añade la carpeta `sql` al archivo `.gitignore` para que Git la ignore al sincronizar con GitHub o el servidor del cliente.

```bash
echo "sql/" >> .gitignore
```

**Mantén la carpeta `sql` fuera del `.gitignore` en Gitea**:

- Asegúrate de que la carpeta `sql` siga siendo rastreada solo en Gitea, a pesar de estar en el `.gitignore`.

Para esto, usa el comando `git update-index`:

```bash
git update-index --assume-unchanged sql/
```

- Esto hará que Git ignore cambios en esa carpeta al hacer push a otros remotos (GitHub y el cliente), pero te permitirá mantenerlos en Gitea.
    
- **Sube los cambios a Gitea**: Cuando quieras respaldar tus scripts de la carpeta `sql` en Gitea:

```bash
git push gitea master
```

**Evita sincronizar con GitHub o el cliente**: Al hacer `push` a GitHub o al servidor del cliente, Git no subirá la carpeta `sql` porque está en `.gitignore`.

```bash
git push github master
git push client master
```

#### Opción 2: Uso de submódulos de Git

Otra opción es utilizar **submódulos de Git** para la carpeta `sql`, de forma que esta carpeta se maneje como un repositorio separado sincronizado solo con Gitea. Así puedes excluirla completamente de GitHub y del servidor del cliente.

##### Pasos:

1. **Crea un repositorio independiente para los scripts de SQL en Gitea**:
    
    - En tu servidor Gitea, crea un nuevo repositorio para los scripts de base de datos (llámalo, por ejemplo, `sql-scripts`).
2. **Añade la carpeta `sql` como submódulo en tu repositorio principal**:
    
    - Dentro del repositorio principal, elimina la carpeta `sql` y añádela como un submódulo:

```bash
git rm -r sql
git submodule add https://gitea-server/user/sql-scripts.git sql
git commit -m "Added SQL submodule"
```

**Sincroniza el submódulo solo con Gitea**:

- Los submódulos te permiten tener repositorios completamente independientes. Cuando sincronices con GitHub o con el servidor del cliente, la carpeta `sql` no será incluida (ya que está vinculada como un submódulo, pero no estará en esos remotos).
    
- Al sincronizar con Gitea, el submódulo se actualizará correctamente:

```bash
git push gitea master
```

**Para sincronizar el submódulo**:

- Si necesitas actualizar los scripts SQL en el submódulo, trabaja dentro del directorio `sql` como un repositorio separado:
```bash
cd sql
git add .
git commit -m "Updated SQL scripts"
git push
```

1. **Sincroniza el repositorio principal sin la carpeta `sql`**:
    
    - Cuando subas el código a GitHub o al servidor del cliente, la carpeta `sql` estará excluida de forma natural (como un submódulo vacío).

#### Conclusión:

- **Opción 1** es una solución rápida que utiliza el `.gitignore` y la gestión del índice de Git para controlar manualmente qué sincronizar.
- **Opción 2** te permite gestionar la carpeta `sql` como un submódulo independiente, lo que es más limpio y organizado para proyectos que necesitan una separación clara de responsabilidades y contenido.

Ambas opciones te permiten mantener los scripts SQL en Gitea sin que se sincronicen con GitHub ni con el servidor del cliente.