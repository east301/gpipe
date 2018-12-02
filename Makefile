#
# copyright (c) 2018 east301
#
# This software is released under the MIT License.
# http://opensource.org/licenses/mit-license.php
#

VERSION := $(shell ./helpers/x-get_package_version.py)

SOURCES := $(shell find ./gpipe -type f)
WHEEL   := dist/gpipe-$(VERSION)-py3-none-any.whl

.PHONY: all wheel
.DEFAULT_GOAL: all
all: $(WHEEL)
wheel: $(WHEEL)

$(WHEEL): $(SOURCES)
	./setup.py bdist_wheel
