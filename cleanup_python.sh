#!/usr/bin/env bash

CMD="black --py36 --line-length 120"

ls *.py | xargs -n1 -P8 ${CMD}
