aclocal
automake --add-missing --foreign
autoconf
./configure --enable-maintainer-mode "$@" \
