# Installing a Sublime Plugin manually
Create a directory $PLUGIN_NAME in any of the os specific directories 
below and place the plugin files inside this $PLUGIN_NAME directory. 

*OS Specific directories*
```
Windows: %APPDATA%\Sublime Text 3\Packages
OS X: ~/Library/Application Support/Sublime Text 3/Packages
Linux: ~/.config/sublime-text-3/Packages
```

*Windows OS version specific*
```
rem Windows 7
C:\Documents and Settings\%USERNAME%\Application Data\Sublime Text\Packages

rem Windows 10
C:\Users\%USERNAME%\AppData\Roaming\Sublime Text\Packages

rem Windows Portable installation
C:\Program Files (Portable)\SublimeText\Data\Packages
```

# Example
```
mkdir C:\Users\User\AppData\Roaming\Sublime Text 3\Packages\DisableEditReadonly
cd  C:\Users\User\AppData\Roaming\Sublime Text 3\Packages\DisableEditReadonly

git clone https://github.com/remivisser/Sublime-Plugin-disable_edit_readonly.git .
```
