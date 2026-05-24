# Copyright (c) 2021 Nordic Semiconductor ASA.
# SPDX-License-Identifier: Apache-2.0

if(CONFIG_BOARD_TAM_BOARD_NRF5340_CPUAPP OR CONFIG_BOARD_TAM_BOARD_NRF5340_CPUAPP_NS)
  zephyr_library()
  zephyr_library_sources(tam_board_config.c)
endif()
