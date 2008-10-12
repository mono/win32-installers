Option Explicit

' If you're editing this file, $DEITY help you.

Function StripTrailingSlash (path)
	If Right (path, 1) = "\" Then
		path = Left (path, Len (path) - 1)
	End If
	
	' Return the value
	StripTrailingSlash = path
End Function

Function Quote (str)
	' Adds quotes to the beginning and end of str
	Quote = Chr (34) & CStr (str) & Chr (34)
End Function

Sub RunApplication (shell, app, outfile)
	shell.Run "%comspec% /c " & Quote (Quote (app)) & " > " & outfile, 7, True
End Sub

Sub Main
	Dim shell, install_loc

	' NOTE: We require that the parent installer that consumes this merge
	' module have INSTALLLOCATION set
	install_loc = StripTrailingSlash (Property ("INSTALLLOCATION"))

	' Change the current directory so we avoid having an output path with
	' spaces (as it doesn't seem to work, at all)
	Set shell = CreateObject ("WScript.Shell")
	shell.CurrentDirectory = install_loc
	
	RunApplication shell, install_loc & "\bin\gdk-pixbuf-query-loaders.exe", "etc\gtk-2.0\gdk-pixbuf.loaders"
	RunApplication shell, install_loc & "\bin\gtk-query-immodules-2.0.exe", "etc\gtk-2.0\gtk.immodules"
	' On Gtk+ 2.10.7, if we use the file that pango-querymodules.exe
	' generates, pango can no longer render text.  Yes, this file will be
	' invalid if we don't do this, but it doesn't seem to matter.
	'RunApplication shell, install_loc & "\bin\pango-querymodules.exe", "etc\pango\pango.modules"
End Sub
