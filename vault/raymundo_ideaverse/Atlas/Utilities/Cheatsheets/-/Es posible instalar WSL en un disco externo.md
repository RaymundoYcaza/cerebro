---
created: 2025-01-07
---



Yes. First, note the URL of the distribution you want to install in [this list](https://docs.microsoft.com/en-us/windows/wsl/install-manual#downloading-distributions), ex: `https://aka.ms/wslubuntu2204`

Now open PowerShell:

```
# Substitute the drive on which you 
# want WSL to be installed if not D:
Set-Location D:

# Create a directory for our installation and change to it, we'll call it WSL:
New-Item WSL -Type Directory
Set-Location .\WSL

# Using the URL you found above, download the appx package:
curl.exe -L -o Linux.appx <distribution_package_url>

# Make a backup and unpack:
Copy-Item .\Linux.appx .\Linux.zip
Expand-Archive .\Linux.zip

# Search for the installer:
Get-Childitem -Filter *.exe

```

You might find a file named `<distribution>.exe`. Run that file, and the WSL distribution should be installed in the unpack folder of the other drive. If you don't see an executable, let's look for an .appx file that was just unpacked, that is the flavor you want, and unzip that, as follows:

```
Set-Location Linux
# look for correct appx file:
Get-Childitem -Filter *.appx
# rename to .zip so that Expand-Archive will work
ren .\Ubuntu_2204.1.7.0_x64.appx .\Ubuntu_2204.zip
Expand-Archive .\Ubuntu_2204.zip
Set-Location .\Ubuntu_2204
# Now exe should exist:
Get-Childitem -Filter *.exe
# run it
.\ubuntu.exe
```

After completion, you can now delete everything just downloaded/created except `ext4.vhdx` (for WSL2) or `rootfs` (for WSL1), and `ubuntu.exe` file, which starts that distro and can change the default username.