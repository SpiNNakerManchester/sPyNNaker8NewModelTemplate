ifndef NEURAL_MODELLING_DIRS
    $(error NEURAL_MODELLING_DIRS is not set.  Please define NEURAL_MODELLING_DIRS (possibly by running "source setup" in the neural_modelling folder within the sPyNNaker source folder))
endif

MAKEFILE_PATH := $(abspath $(lastword $(MAKEFILE_LIST)))
CURRENT_DIR := $(dir $(MAKEFILE_PATH))
EXTRA_SRC_DIR := $(abspath $(CURRENT_DIR)/../../)
SOURCE_DIRS += $(EXTRA_SRC_DIR)
APP_OUTPUT_DIR := $(abspath $(CURRENT_DIR)../../../../python_models8/model_binaries/)/
CFLAGS += -I$(EXTRA_SRC_DIR)

include $(NEURAL_MODELLING_DIRS)/src/neuron/builds/common_custom.mk