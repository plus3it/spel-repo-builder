export TARDIGRADE_CI_DOCKERFILE ?= Dockerfile.tools

include $(shell test -f .tardigrade-ci || curl -sSL -o .tardigrade-ci "https://raw.githubusercontent.com/plus3it/tardigrade-ci/master/bootstrap/Makefile.bootstrap"; echo .tardigrade-ci)

DOCKERFILE_TOOLS := Dockerfile.tools

## Install gomplate
gomplate/install: GOMPLATE_VERSION ?= tags/v$(call match_pattern_in_file,$(DOCKERFILE_TOOLS),'hairyhenderson/gomplate','$(SEMVER_PATTERN)')
gomplate/install: | $(BIN_DIR)
	@ $(MAKE) install/gh-release/$(@D) FILENAME="$(BIN_DIR)/$(@D)" OWNER=hairyhenderson REPO=$(@D) VERSION=$(GOMPLATE_VERSION) QUERY='.name | endswith("$(OS)-$(ARCH)")'
