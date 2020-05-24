#!/bin/bash

set -e
cd "$(dirname ${BASH_SOURCE[0]})/.."

.env/bin/python -m app run
