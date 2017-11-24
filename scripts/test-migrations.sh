#!/usr/bin/env bash

set -o errexit
set -o pipefail
set -o nounset

readonly __dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
readonly __root="$(cd "$(dirname "${__dir}")" && pwd)"

# Test if there are migrations that need to be created
${__root}/testproject/manage.py makemigrations
! git status --porcelain ${__root}/fpr/migrations/ 2>/dev/null | grep "^??"

# Test that we can migrate an empty database
${__root}/testproject/manage.py migrate
