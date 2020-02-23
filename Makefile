PYTHON = python3
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
	$(PYTHON) apply-feature.py "$(word 1, $^)" "$@"

$(BOLD): $(BOLD_UNLINK) ligatures.fea
	$(PYTHON) apply-feature.py "$(word 1, $^)" "$@"

$(REGULAR_DISCORD): $(REGULAR_DISCORD_UNLINK) ligatures.fea
	$(PYTHON) apply-feature.py "$(word 1, $^)" "$@"

$(BOLD_DISCORD): $(BOLD_DISCORD_UNLINK) ligatures.fea
	$(PYTHON) apply-feature.py "$(word 1, $^)" "$@"

ligatures.fea: ligatures.fea.jinja2 data.json build-feature.py
	$(PYTHON) build-feature.py

$(REGULAR_UNLINK): RictyDiminished/RictyDiminished-Regular.ttf FiraCode/distr/otf/FiraCode-Regular.otf
	$(PYTHON) build.py "$(word 1, $^)" "$(word 2, $^)" "$@" Regular false

$(BOLD_UNLINK): RictyDiminished/RictyDiminished-Bold.ttf FiraCode/distr/otf/FiraCode-Bold.otf
	$(PYTHON) build.py "$(word 1, $^)" "$(word 2, $^)" "$@" Bold false

$(REGULAR_DISCORD_UNLINK): RictyDiminished/RictyDiminishedDiscord-Regular.ttf FiraCode/distr/otf/FiraCode-Regular.otf
	$(PYTHON) build.py "$(word 1, $^)" "$(word 2, $^)" "$@" Regular true

$(BOLD_DISCORD_UNLINK): RictyDiminished/RictyDiminishedDiscord-Bold.ttf FiraCode/distr/otf/FiraCode-Bold.otf
	$(PYTHON) build.py "$(word 1, $^)" "$(word 2, $^)" "$@" Bold true

.PHONY: all
