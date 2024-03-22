export TARDIGRADE_CI_DOCKERFILE ?= Dockerfile.tools

include $(shell test -f .tardigrade-ci || curl -sSL -o .tardigrade-ci "https://raw.githubusercontent.com/plus3it/tardigrade-ci/master/bootstrap/Makefile.bootstrap"; echo .tardigrade-ci)

DOCKERFILE_AMZN2023 := Dockerfile.amzn2023
DOCKERFILE_TOOLS := Dockerfile.tools

## Install gomplate
gomplate/%: GOMPLATE_VERSION_PIN ?= $(call match_pattern_in_file,$(DOCKERFILE_TOOLS),'hairyhenderson/gomplate','v$(SEMVER_PATTERN)')
gomplate/%: GOMPLATE_VERSION ?= tags/$(GOMPLATE_VERSION_PIN)
gomplate/install: | $(BIN_DIR)
	@ $(MAKE) install/gh-release/$(@D) FILENAME="$(BIN_DIR)/$(@D)" OWNER=hairyhenderson REPO=$(@D) VERSION=$(GOMPLATE_VERSION) QUERY='.name | endswith("$(OS)-$(ARCH)")'

gomplate/version:
	@ echo $(GOMPLATE_VERSION_PIN)

amazonlinux/% release/%: AMAZONLINUX_VERSION ?= $(call match_pattern_in_file,$(DOCKERFILE_AMZN2023),'amazonlinux','2023\..*')
amazonlinux/version:
	@ echo $(AMAZONLINUX_VERSION)

centos9/%: CENTOS9_VERSION ?= $(call match_pattern_in_file,$(DOCKERFILE_TOOLS),'centos:stream9','stream9@sha256:.*')
centos9/version:
	@ echo $(CENTOS9_VERSION)

centos8/%: CENTOS8_VERSION ?= $(call match_pattern_in_file,$(DOCKERFILE_TOOLS),'centos:stream8','stream8@sha256:.*')
centos8/version:
	@ echo $(CENTOS8_VERSION)

centos7/%: CENTOS7_VERSION ?= $(call match_pattern_in_file,$(DOCKERFILE_TOOLS),'centos:7','7@sha256:.*')
centos7/version:
	@ echo $(CENTOS7_VERSION)

golang/% release/%: GOLANG_VERSION ?= $(call match_pattern_in_file,$(DOCKERFILE_TOOLS),'golang','$(SEMVER_PATTERN)')
golang/version:
	@ echo $(GOLANG_VERSION)

release/%: PRIOR_VERSION = $(shell git describe --abbrev=0 --tags 2> /dev/null)
release/%: RELEASE_VERSION = $(AMAZONLINUX_VERSION)

release/test:
	test "$(PRIOR_VERSION)" != "$(RELEASE_VERSION)"

release/version:
	@ echo $(RELEASE_VERSION)
