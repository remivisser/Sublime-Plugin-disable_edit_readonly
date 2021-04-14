# Sublime imports
import sublime
import sublime_plugin

# Import Python `os` module, needed for `os.access()` retrieving os
# read-write permissions.
import os


# Classname can be anything (as long as it doesn't already exist)
class DisableEditReadonlyEventListener(sublime_plugin.EventListener):
    """
    Lightweight Sublime plugin making the file buffer's
    read-only state match the os read-write permissions of the file:

    - If the file's os permissions are read-only the file buffer is set
    to read-only as well.
    - If the file's os permissions are read-write the file buffer is set
    to read-write as well.
    - A custom `color_scheme` for read-only files may be configured
    with the parameter `color_scheme_readonly` in
    `disable_edit_readonly.sublime-settings`
    """

    # `on_activated` runs every time a view gains input focus.
    def on_activated(self, view):

        file_name=view.file_name()

        # Skip processing for New files
        if file_name is None:
            return

        # Enable read-only for current view when:
        # - buffer is not read-only already
        # - file has os permission read-only
        # - file exists on the os. The `os.path.exists` condition is
        # important; it excludes files that were removed from the os
        # after they were loaded in the editor. These non-existing
        # files return False for `os.access(file_name, os.W_OK)`
        if view.is_read_only() == False and os.access(file_name, os.W_OK) == False and os.path.exists(file_name) == True:
            view.set_read_only(True)
            view.set_status(str(self), "[read only]")
            sublime.status_message( file_name + " is read only.")
            # Apply `color_scheme` `color_scheme_readonly` from
            # in settings file `disable_edit_readonly.sublime-settings`.
            settings=sublime.load_settings("disable_edit_readonly.sublime-settings")
            if settings.get("color_scheme_readonly") is not None:
                view.settings().set("color_scheme", settings.get("color_scheme_readonly"))

        # Disable read-only for current view when view is read-only
        # and:
        # - file has os permission read-write. This covers files whose
        # os permission changed from read-only to read-write after the
        # file was loaded in the editor.
        # - file does not exist on the os. This covers files that were
        # removed from the os after they were loaded in the editor.
        # Their read-only status must be reset to read-write.
        elif view.is_read_only() == True and (os.access(file_name, os.W_OK) == True or os.path.exists(file_name) == False):
            view.set_read_only(False)
            view.erase_status(str(self))
            sublime.status_message(file_name + " is writable.")
            # Reset the view's `color_scheme`. Needed because a custom
            # `color_scheme` may be applied by `color_scheme_readonly`
            # in `disable_edit_readonly.sublime-settings`.
            #
            # Check for syntax specific `color_scheme` (eg
            # `Java.sublime-settings`) set `color_scheme` accordingly.
            settings=sublime.load_settings(self.syntax_basename(view.settings().get('syntax')) + ".sublime-settings")
            if settings.get("color_scheme") is not None:
                view.settings().set("color_scheme", settings.get("color_scheme"))
            # If no syntax specific `color_scheme` is defined revert to
            # the general setting for `color_scheme` from
            # `Preferences.sublime-settings`.
            else:
                settings=sublime.load_settings("Preferences.sublime-settings")
                view.settings().set("color_scheme", settings.get("color_scheme"))


    @staticmethod
    def syntax_basename(syntax):
        """
        Get syntax basename from `settings('syntax')`

        Eg return `Java` from `Packages/Java/Java.sublime-syntax`:
        >>> print (view.settings().get('syntax'))
        Packages/Java/Java.sublime-syntax
        https://forum.sublimetext.com/t/view-settings-get/47302/2
        """
        # Get filename without the extension from a path in Python
        # https://stackoverflow.com/a/678266
        return os.path.splitext(os.path.basename(syntax))[0]
