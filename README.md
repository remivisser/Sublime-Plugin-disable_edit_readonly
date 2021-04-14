# Disable Edit Readonly Summary
Tiny Sublime Plugin to disable editing of files that have read only 
permissions. 

## Description
Plugin makes the file buffer's read-only state match the os read-write 
permissions of the file.  

- If the file's os permissions are read-only the file buffer is set to 
read-only as well; editting of the file is disabled untill the file 
will have write permissions (again).  
A status key **[read only]** will be added to the file's view.
- If the file's os permissions are read-write the file buffer is set
to read-write as well.
- A custom `color_scheme` for read-only files may be configured.

### Changed file permissions detection ***
Plugin offers no 'live' change file's os permissions detection. 
Function runs every time a view is activated. See Caveat section.

## Installation
This package is not available through Package Control, install it 
manually by downloading `disable_edit_readonly.py` and optionally 
`disable_edit_readonly.sublime-settings` into the Sublime package 
directory. *(for locations of the Sublime plugins directories see the 
bottom of this README)*

## Configuration
Read only files can be displayed with a custom theme. This is 
controlled by the parameter `color_scheme_readonly` in 
`disable_edit_readonly.sublime-settings`. 
```
{
	// Color scheme applied to read only files (Light blue)
	"color_scheme_readonly": "Packages/Color Scheme - Default/Mariana.sublime-color-scheme",
}
```
This theme configuration is entirely optional, the plugin will run 
fine without the `disable_edit_readonly.sublime-settings` settings 
file present.

## Caveat
Function checks read-only status of the file on the os every time a 
view gains input focus. No (polling) background commands are run to 
check the os permissions. Hence if a file os permission is changed in 
the background it will only be reflected once the view of the current 
file deactivates and reactivates. In my case (many cases) I will modify 
the os permissions in one window and come back to Sublime to proceed 
with editting; the view `on_activated` fires and the read only status 
is updated.

## Footprint
Plugins hooks in on `on_activated` of the 
[`sublime_plugin.EventListener`](https://www.sublimetext.com/docs/3/api_reference.html#sublime_plugin.EventListener). 
Every time a view gains input focus the plugin calls one time 
`os.access` and one time `os.path.exists` for the current file. 

## Credits
- While searching for this functionality I came upon this post 
[Read-only files](https://forum.sublimetext.com/t/read-only-files/5102) 
that was very helpful. 
- In the middle of developing this plugin I found out that there was 
already a plugin in Package Control named **ReadOnly Protect**. This 
plugin comes with way more functionality (like toggling read-only 
status, polling os permissions) Find it at 
[GitHub](https://github.com/ivellioscolin/sublime-plugin-readonlyprotect) 
or at [PackageControl.io](https://packagecontrol.io/packages/ReadonlyProtect)

---

### Sublime plugin/package directories
```
Windows: %APPDATA%\Sublime Text 3\Packages\User
OS X: ~/Library/Application Support/Sublime Text 3/Packages/User
Linux: ~/.config/sublime-text-3/Packages/User
```
*Windows OS version specific*
```
rem Windows 7
C:\Documents and Settings\%USERNAME%\Application Data\Sublime Text\Packages\User

rem Windows 10
C:\Users\%USERNAME%\AppData\Roaming\Sublime Text\Packages\User

rem Windows Portable installation
C:\Program Files (Portable)\SublimeText\Data\Packages\User
```