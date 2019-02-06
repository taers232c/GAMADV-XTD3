- [Introduction](#introduction)
- [Requirements](#requirements)
- [Downloads](#downloads)
- [Installation - New Users](#installation---new-users)
- [Installation - Upgrading from a GAM version other than a prior version of GAMADV-XTD3 or GAMADV-XTD or GAMADV-X](#installation---upgrading-from-a-gam-version-other-than-a-prior-version-of-gamadv-xtd3-or-gamadv-xtd-or-gamadv-x)
- [Installation - Upgrading from a prior version of GAMADV-XTD3 or GAMADV-XTD or GAMADV-X](#installation---upgrading-from-a-prior-version-of-gamadv-xtd3-or-gamadv-xtd-or-gamadv-x)

# Introduction
GAMADV-XTD3 is a free, open source command line tool for Google G Suite Administrators to manage domain and user settings quickly and easily.

This page provides simple instructions for downloading, installing and starting to use GAMADV-XTD3.

GAMADV-XTD3 requires G Suite for Business, Education, Partner or Government Edition. Google Apps Free Edition has limited API support and not all GAM commands work.

GAMADV-XTD3 is a rewrite/extension of Jay Lee's [GAM](https://github.com/jay0lee/GAM), without his efforts, this version wouldn't exist.

# Documentation
General GAM documentation is hosted in the [GitHub Wiki]. Documentation specifically for GAMADV-XTD3 is hosted in the [GitHub GAMADV-XTD Wiki] and in Gam*.txt files.

# Mailing List / Discussion group
The GAM mailing list / discussion group is hosted on [Google Groups].  You can join the list and interact via email, or just post from the web itself.

# Source Repository
The official GAMADV-XTD3 source repository is on [GitHub] in the master branch.

# Author
GAMADV-XTD3 is maintained by <a href="mailto:ross.scroggs@gmail.com">Ross Scroggs</a>.

# Requirements
To run all commands properly, GAMADV-XTD3 requires three things:
* An API project which identifies your install of GAMADV-XTD3 to Google and keeps track of API quotas.
* Authorization to act as your G Suite Administrator in order to perform management functions like add users, modify group settings and membership and pull domain reports.
* A special service account that is authorized to act on behalf of your users in order to modify user-specific settings and data such as Drive files, Calendars and Gmail messages and settings like signatures.

# Downloads
You can download the current GAMADV-XTD3 release from the [GitHub Releases] page.

* Source, all platforms - Source code(zip), Source code(tar.gz)
  - Download the archive, extract the contents into some directory.
  - Start a terminal/Command Prompt/PowerShell session and cd to the install directory.

# Installation - New Users
For information about the GAMADV-XTD3 configuration file gam.cfg, see: https://github.com/taers232c/GAMADV-XTD/wiki/gam.cfg

Enter the following gam commands and follow instructions to create the necessary authorizations.
- Build gam.cfg: `gam config verify`
- Build GAM Project for authorization: `gam create project`
- Authorize Gam Client: `gam oauth create`
- Authorize Service Account: `gam user <EmailAddress> check serviceaccount`

# Installation - Upgrading from a GAM version other than a prior version of GAMADV-XTD3 or GAMADV-XTD or GAMADV-X
Please see  https://github.com/taers232c/GAMADV-XTD/wiki/How-to-Upgrade-from-Standard-GAM file for step-by-step instructions.

# Installation - Upgrading from a prior version of GAMADV-XTD3 or GAMADV-XTD or GAMADV-X
Read GamUpdate.txt

Download latest version, install over existing installation or in a parallel directory.

[GitHub Releases]: https://github.com/taers232c/GAMADV-XTD3/releases
[GitHub]: https://github.com/taers232c/GAMADV-XTD3/tree/master
[GitHub Wiki]: https://github.com/jay0lee/GAM/wiki/
[GitHub GAMADV-XTD Wiki]: https://github.com/taers232c/GAMADV-XTD/wiki/
[Google Groups]: http://groups.google.com/group/google-apps-manager
