#!/bin/sh

gpgfile="$1"
echo "source file is ${gpgfile}"
credsfile="$2"
echo "target file is ${credsfile}"
if [ -z ${PASSCODE+x} ]; then
  echo "PASSCODE is unset";
else
  echo "PASSCODE is set";
fi

gpg --quiet --batch --yes --decrypt --passphrase="${PASSCODE}" \
    --output "${credsfile}" "${gpgfile}"

mkdir -p "${gampath}\ConfigGitHub"
tar xvvf "${credsfile}" --directory "${gampath}"
echo "${gampath}\ConfigGitHub files:"
ls -l "${gampath}\ConfigGitHub"
