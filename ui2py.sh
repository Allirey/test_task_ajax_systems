#!/bin/bash

# converts .ui file generated from qtdesigner to .py file

pyuic5 ui/gui_raw/gui_test_result_template.ui > ui/gui_raw/gui_test_result_template.py
