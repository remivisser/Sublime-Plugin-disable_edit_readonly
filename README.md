# Disable Edit Readonly Summary
Tiny Sublime Plugin disabling editing of files that have read-only 
permissions on the os. 

## Description
Plugin makes the file buffer's read-only state match the os read-write 
permissions of the file.  

- If the file's os permissions are read-only editting of the file is 
disabled. A status key **[read only]** will be added.
- If the file's os permissions are read-write editting of the file is 
(re-)enabled.
- A custom `color_scheme` for read-only files may be configured.
- Plugin does not live detect read-write permissions of a file; 
read-write permissions are retrieved only every time a view is 
activated. See Caveat/Detection section.

## Installation
This package is not available through Package Control, install it 
manually by downloading `disable_edit_readonly.py` and optionally 
`disable_edit_readonly.sublime-settings` into the Sublime Package 
directory. *(for instructions on manually installing see INSTALL.md)*

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
Theme configuration is entirely optional, the plugin will run fine 
without the `disable_edit_readonly.sublime-settings` file present.

## Caveat
### Detection read only permissions
Function checks read-only status of the file every time a view gains 
input focus. No background (polling) commands are run to check the os 
permissions. Hence if a file os permission is changed in the background 
it will only be reflected once the view of the current file deactivates 
and reactivates. In my case (many cases) I will modify the os 
permissions in one window and come back to Sublime to proceed with 
editting; the view gains input focus and the read-only status is updated.

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
already a plugin in Package Control named **ReadonlyProtect**. This 
plugin comes with way more functionality (like toggling read-only 
status, polling os permissions) Find it at 
[GitHub](https://github.com/ivellioscolin/sublime-plugin-readonlyprotect) 
or at [PackageControl](https://packagecontrol.io/packages/ReadonlyProtect)
