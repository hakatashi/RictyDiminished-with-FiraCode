all: test.sfd

test.sfd: build-py2.py
	fontforge -lang=py -script "$<"

build-py2.py: build-py3.py
	3to2 "$<" -w -x str
	mv -f "$<" "$@"
	mv -f "$<.bak" "$<"

clean:
	-rm -f build-py2.py

.PHONY: all clean
