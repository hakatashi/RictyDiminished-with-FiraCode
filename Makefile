all: build-py2.py

build-py2.py: build-py3.py
	3to2 "$<" -w
	mv -f "$<" "$@"
	mv -f "$<.bak" "$<"

clean:
	-rm -f build-py2.py

.PHONY: all clean
