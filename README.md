# Introduction
GAM is a command line tool for Google Workspace admins to manage domain and user settings quickly and easily.

GAMADV-XTD3 has been replaced with GAM7.

* [How to Uograde GAMADV-XTD3 to GAM7](How-to-Upgrade-GAMADV-XTD3-to-GAM7)

# Documentation
Documentation for GAMADV-XTD3 is hosted in the [GitHub Wiki] and in Gam*.txt files.

# Mailing List / Discussion group
The GAM mailing list / discussion group is hosted on [Google Groups].  You can join the list and interact via email, or just post from the web itself.

# Chat Room

There is a public chat room hosted in Google Chat. [Instructions to join](https://github.com/GAM-team/GAM/wiki/GAM-Public-Chat-Room).

# Source Repository
The official GAMADV-XTD3 source repository is on [GitHub] in the master branch.

# Author
GAMADV-XTD3 is maintained by <a href="mailto:ross.scroggs@gmail.com">Ross Scroggs</a>.

# Requirements
To run all commands properly, GAMADV-XTD3 requires three things:
* An API project which identifies your install of GAMADV-XTD3 to Google and keeps track of API quotas.
* Authorization to act as your G Suite Administrator in order to perform management functions like add users, modify group settings and membership and pull domain reports.
* A special service account that is authorized to act on behalf of your users in order to modify user-specific settings and data such as Drive files, Calendars and Gmail messages and settings like signatures.

# Installation - First time GAM installation
Use these steps if you have never used any version of GAM in your domain. They will create a GAM project
and all necessary authentications.

| [Downloads-Installs] | [Configuration] | [Install] |
|    :---:    |      :---:      |   :---:   |

# Installation - Update Advanced GAM
Use these steps to update your version of GAMADV-XTD3.

| [Downloads-Installs] | [Configuration] | [UpdateAdvanced] |
|    :---:    |      :---:      |      :---:       |

# Installation - Upgrading from Standard GAM
Use these steps if you have used any version of Standard GAM in your domain. They will update your GAM project
and all necessary authentications.

| [Downloads-Installs] | [Configuration] | [UpgradeFromStandard] |
|    :---:    |      :---:      |         :---:         |

# Installation - Upgrading from a prior version of GAMADV-X or GAMADV-XTD
Use these steps if you already use GAMADV-X or GAMADV-XTD. The updates may tell you to update your GAM project
or authentications because new features have been included.

| [Updates]  | [Downloads-Installs] | [UpgradeFromAdvanced] |
|   :---:    |    :---:    |         :---:         |

# Multiple Versions
You can install multiple versions of GAM and GAMADV-XTD3 in different parallel directories.

[GAM]: https://github.com/GAM-team/GAM
[GitHub Releases]: https://github.com/GAM-team/GAM/releases
[GitHub]: https://github.com/GAM-team/GAM/tree/master
[GitHub Wiki]: https://github.com/GAM-team/GAM/wiki
[Google Groups]: https://groups.google.com/group/google-apps-manager
[Downloads-Installs]: https://github.com/GAM-team/GAM/wiki/Downloads-Installs
[Configuration]: https://github.com/GAM-team/GAM/wiki/gam.cfg
[Install]: https://github.com/GAM-team/GAM/wiki/How-to-Install-Advanced-GAM
[UpdateAdvanced]: https://github.com/GAM-team/GAM/wiki/How-to-Update-Advanced-GAM
[UpgradeFromStandard]: https://github.com/GAM-team/GAM/wiki/How-to-Upgrade-from-Standard-GAM
[Updates]: https://github.com/GAM-team/GAM/wiki/GAM-Updates
