AC_INIT(README)
AC_CANONICAL_SYSTEM
AC_PREREQ(2.13)
AM_INIT_AUTOMAKE(win32-installers, 0.1)
AM_MAINTAINER_MODE
AC_PROG_INSTALL

AC_PATH_PROG(CANDLE, candle, no)
if test "x$CANDLE" = "xno" ; then
	AC_MSG_ERROR(['No candle found'])
fi


AC_PATH_PROG(LIGHT, light, no)
if test "x$LIGHT" = "xno" ; then
	AC_MSG_ERROR(['No light found'])
fi

AC_SUBST(CANDLE)
AC_SUBST(LIGHT)

AC_OUTPUT([
Makefile
modules/Makefile
modules/aspell-lib/Makefile
modules/glade-2-dev/Makefile
modules/glade-2-lib/Makefile
modules/gtk+-2.0-dev/Makefile
modules/gtk+-2.0-lib/Makefile
modules/mono-cairo-dev/Makefile
modules/mono-cairo-lib/Makefile
modules/mono-posix-lib/Makefile
modules/poppler-lib/Makefile
modules/vte-lib/Makefile
modules/vte-sharp-dev/Makefile
modules/vte-sharp-lib/Makefile
runtime-en/Makefile
sdk-en/Makefile
])
