---
in:
  - "[[Tecnología MOC]]"
---


### Reiniciar WSL
_**View the list of distros and their current state:**_

```
wsl.exe -l -v
```

_**Shutdown everything:**_
```
wsl.exe --shutdown
```

_**Terminate a specific distro:**_
```
wsl.exe -t <DistroName>
```

_**Boot up the default distro (marked with `*`):**_

```
wsl.exe
```

_**Boot up a specific distro:**_

```
wsl.exe -d <DistroName>
```

