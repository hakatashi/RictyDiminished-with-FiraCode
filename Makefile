REGULAR = RictyDiminished-with-FiraCode-Regular.ttf
REGULAR_UNLINK = RictyDiminished-with-FiraCode-Regular-unlinked.ttf
BOLD = RictyDiminished-with-FiraCode-Bold.ttf
BOLD_UNLINK = RictyDiminished-with-FiraCode-Bold-unlinked.ttf
REGULAR_DISCORD = RictyDiminishedDiscord-with-FiraCode-Regular.ttf
REGULAR_DISCORD_UNLINK = RictyDiminishedDiscord-with-FiraCode-Regular-unlinked.ttf
BOLD_DISCORD = RictyDiminishedDiscord-with-FiraCode-Bold.ttf
BOLD_DISCORD_UNLINK = RictyDiminishedDiscord-with-FiraCode-Bold-unlinked.ttf

all: $(REGULAR) $(BOLD) $(REGULAR_DISCORD) $(BOLD_DISCORD)

$(REGULAR): $(REGULAR_UNLINK) ligatures.fea
	python apply-feature.py "$(word 1, $^)" "$@"

$(BOLD): $(BOLD_UNLINK) ligatures.fea
	python apply-feature.py "$(word 1, $^)" "$@"

$(REGULAR_DISCORD): $(REGULAR_DISCORD_UNLINK) ligatures.fea
	python apply-feature.py "$(word 1, $^)" "$@"

$(BOLD_DISCORD): $(BOLD_DISCORD_UNLINK) ligatures.fea
	python apply-feature.py "$(word 1, $^)" "$@"

ligatures.fea: ligatures.fea.jinja2 data.json build-feature.py
	python build-feature.py

$(REGULAR_UNLINK): build-py2.py RictyDiminished/RictyDiminished-Regular.ttf FiraCode/distr/otf/FiraCode-Regular.otf
	fontforge -lang=py -script "$<" "$(word 2, $^)" "$(word 3, $^)" "$@" Regular false

$(BOLD_UNLINK): build-py2.py RictyDiminished/RictyDiminished-Bold.ttf FiraCode/distr/otf/FiraCode-Bold.otf
	fontforge -lang=py -script "$<" "$(word 2, $^)" "$(word 3, $^)" "$@" Bold false

$(REGULAR_DISCORD_UNLINK): build-py2.py RictyDiminished/RictyDiminishedDiscord-Regular.ttf FiraCode/distr/otf/FiraCode-Regular.otf
	fontforge -lang=py -script "$<" "$(word 2, $^)" "$(word 3, $^)" "$@" Regular true

$(BOLD_DISCORD_UNLINK): build-py2.py RictyDiminished/RictyDiminishedDiscord-Bold.ttf FiraCode/distr/otf/FiraCode-Bold.otf
	fontforge -lang=py -script "$<" "$(word 2, $^)" "$(word 3, $^)" "$@" Bold true

build-py2.py: build-py3.py ligatures.csv
	3to2 "$<" -w -x str
	mv -f "$<" "$@"
	mv -f "$<.bak" "$<"

clean:
	-rm -f build-py2.py

.PHONY: all clean
