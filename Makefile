all: ricty.ttf

ricty.ttf: test.ttf ligatures.fea
	python apply-feature.py

ligatures.fea: ligatures.fea.jinja2 ligatures.json build-feature.py
	python build-feature.py

test.ttf: build-py2.py
	fontforge -lang=py -script "$<"

build-py2.py: build-py3.py
	3to2 "$<" -w -x str
	mv -f "$<" "$@"
	mv -f "$<.bak" "$<"

clean:
	-rm -f build-py2.py

.PHONY: all clean
