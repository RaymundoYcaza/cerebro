---
in:
  - "[[Ubuntu]]"
---



## Descargar archivo por SSH
Copy something from another system to this system:
```
scp username@hostname:/path/to/remote/file /path/to/local/file
```
Copy something from this system to some other system:
```
scp /path/to/local/file username@hostname:/path/to/remote/file
```
Copy something from some system to some other system:
```
scp username1@hostname1:/path/to/file username2@hostname2:/path/to/other/file
```
> Hacerlo en una ventana de comandos *que no haya iniciado sesión*
### Cómo esconder la ruta del directorio de trabajo en la terminal de Ubuntu
```
export PS1='\u@\h: '
```
That results in `oli@bert:` for my prompt.
If you really want something as minimalist as you ask for, try this:
```
export PS1='> '
```
You can attach that to the end of your `~/.bashrc` file to have it persist between logins.
You can also get creative with some colours. Here's what I use on my servers:
```
export PS1='\033[0;35m\h\033[0;33m \w\033[00m: '
```
Giving (it's easier to see on a full black background):
![My terminals](https://i.stack.imgur.com/CzGm7.png)
[Glossary of acceptable characters in PS1](http://www.cyberciti.biz/tips/howto-linux-unix-bash-shell-setup-prompt.html)
#### Información complementaria
Just to expand on Oli's answer (and so that I have a bookmark for those short-hand symbols):
The bash prompt (`stefano@linux:~$`) is only the first of a couple of prompts
you might see:
**PS1**: the default prompt you see when you open a shell
It's value is stored in an environment variable called `PS1`. To see its value,
type

`echo $PS1`

This will give you something like

```
\e]0;\u@\h:\w\a${debian_chroot:+($debian_chroot)}\u@\h:\w$
```
To change it, you can set a new value for the variable:

```
export PS1="\u > "
```
This will result in a prompt like this:

```
stefano >
```
**PS2**: is your secondary prompt. This gets shown when a command is not finished.
Type `echo "asd` and hit enter, the secondary prompt will let you enter more
lines until you close the inverted commas.
**PS3** is the prompt used for [`select`(2)](http://www.cl.cam.ac.uk/cgi-bin/manpage?2+select)
**PS4** is the prompt used for ![alt text](https://i.stack.imgur.com/Udq1r.png) [stack traces](http://en.wikipedia.org/wiki/Stack_trace) (default: `+`)
To make the changes permanent, you append them to the end of `.bash_profile` (or `.bashrc`, see [this question](https://askubuntu.com/questions/1528/bashrc-or-bash-profile)) in your
home directory.

Here's a more or less complete list of shorthand that you can use when composing these:
**`\a`**     The 'bell' character
**`\A`**     24h Time
**`\d`**     Date (e.g. Tue Dec 21)
**`\e`**     The 'escape' character
**`\h`**     Hostname (up to the first ".")
**`\H`**     Hostname
**`\j`**     No. of jobs currently running (ps)
**`\l`**     Current tty
**`\n`**     Line feed
**`\t`**     Time (hh:mm:ss)
**`\T`**     Time (hh:mm:ss, 12h format)
**`\r`**     Carriage return
**`\s`**     Shell (i.e. bash, zsh, ksh..)
**`\u`**     Username
**`\v`**     Bash version
**`\V`**     Full Bash release string
**`\w`**     Current working directory
**`\W`**     Last part of the current working directory
**`\!`**     Current index in history
**`\#`**     Command index
**`\$`**     A "#" if you're root, else "$"
**`\\`**     Literal Backslash
**`\@`**     Time (12h format with am/pm)
You can of course insert any literal string, and any command:

```
export PS1="\u \$(pwd) > "
```
Where `$(pwd)` stands in place of "the output of" pwd.
If the command substitution is escaped, as in `\$(pwd)`, it's evaluated every time the prompt is displayed, otherwise, as in `$(pwd)`, it's only evaluated once when bash is started.
If you want your prompt to feature colours, you can use bash's colour codes to do it. The code consists of three parts:

```
40;33;01
```
The first part before the semicolon represents the text style.
00=none
01=bold
04=underscore
05=blink
07=reverse
08=concealed
The second and third part are the colour and the background color:
30=black
31=red
32=green
33=yellow
34=blue
35=magenta
36=cyan
37=white
Each part can be omitted, assuming starting on the left. i.e. "1" 
means bold, "1;31" means bold and red. And you would get your terminal 
to print in colour by escaping the instruction with `\33[` and ending it with an `m`. 33, or 1B in hexadecimal, is the ASCII sign "ESCAPE" (a special character in the ASCII character set). Example:

```
"\33[1;31mHello World\33[m"
```
Prints "Hello World" in bright red.
## WSL2 Windows 10
Cómo averiguar la IP del WSL
```
wsl hostname -I
```
Cómo redireccionar una petición a la IP de la computadora, hacia la IP del WSL
En un PowerShell como administrador, ejecutar:
```bash
netsh interface portproxy add v4tov4 listenport=3000 listenaddress=0.0.0.0 connectport=3000 connectaddress=172.30.16.3
```
This needs to be run in an elevated powershell prompt, not from WSL, the connectaddress should be your WSL IP, and you'll probably need to allow the port through windows firewall. Side note, this is the same thing the script in the top answer is doing, but it's nice to just see the necessary command rather than the whole script.
Referencias
Youtube
{{video(https://www.youtube.com/watch?v=yCK3easuYm4)}}
Microsoft
https://learn.microsoft.com/en-us/windows/wsl/compare-versions#accessing-a-wsl-2-distribution-from-your-local-area-network-lan
StackOverflow
https://stackoverflow.com/questions/61002681/connecting-to-wsl2-server-via-local-network
Cómo limitar el uso de memoria de WSL
Crear un archivo `%UserProfile%\.wslconfig`
Con el contenido
```ini
[wsl2]
memory=8GB
```
Otra forma
```bash
# turn off all wsl instances such as docker-desktop
wsl --shutdown
notepad "$env:USERPROFILE/.wslconfig"
```
Set the values you want for CPU core and Memory:
```ini
[wsl2]
memory=3GB   # Limits VM memory in WSL 2 up to 3GB
processors=2 # Makes the WSL 2 VM use two virtual processors
```
Cómo reiniciar WSL
`wsl --restart`
```
Restart-Service LxssManager
```
Cómo apagar WSL
`wsl --shutdown`

### Cómo optimizar el espacio del disco
When the command let `optimize-vhd` is not available in your system do the following:
 Shutdown the wsl before managing its disk
```
wsl --shutdown
```
Save the following script as compact-disk.txt
```
select vdisk file="C:\Users\%username%\AppData\Local\Packages\CanonicalGroupLimited.Ubuntu20.04onWindows_79rhkp1fndgsc\LocalState\ext4.vhdx"
attach vdisk readonly
compact vdisk
detach vdisk
```
Open prompt as **Administrator** and run the saved script above
```
diskpart /s <SAVED_SCRIPT_FOLDER_PATH>\compact-disk.txt
```
Automatizar el proceso de optimización
*September 2023 update:* A new pre-release of WSL (2.0.0) is 
reported to provide a new "sparse" mode for disk images which will 
automatically shrink the image when files are removed.
While I have not tested this personally yet, from the [DevBlog announcement](https://devblogs.microsoft.com/commandline/windows-subsystem-for-linux-september-2023-update/#automatic-disk-space-clean-up-set-sparse-vhd), you can convert an existing disk image to sparse with the following command from PowerShell:
```
wsl --manage <distro> --set-sparse true
```
You can also add the following to your `.wslconfig` (located in your Windows *profile* directory, not inside WSL) to have any newly created distro image be sparse:
```
[experimental]
sparseVhd=true
```
https://superuser.com/questions/1606213/how-do-i-get-back-unused-disk-space-from-ubuntu-on-wsl2
