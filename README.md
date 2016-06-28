# [Archivematica Formaty Policy Registry](https://www.archivematica.org/)

By [Artefactual](https://www.artefactual.com/)

The Archivematica Format Policy Registry is part of the Archivematica project.
Archivematica is a web- and standards-based, open-source application which allows your institution to preserve long-term access to trustworthy, authentic and reliable digital content.
Our target users are archivists, librarians, and anyone working to preserve digital objects.
The Format Policy Registry (FPR) is a database which allows Archivematica users to define format policies for handling file formats.
A format policy indicates the actions, tools and settings to apply to a file of a particular file format (e.g. conversion to preservation format, conversion to access format).

The structure of the database is defined here, but the default contents are found in the [Archivematica FPR tools](https://github.com/artefactual/archivematica-fpr-tools) repository.
The Format Policy Registry is available as the Preservation Planning tab of Archivematica.
It is included as a git submodule in Archivematica and the Artefactual-hosted FPR server.

You are free to copy, modify, and distribute Archivematica with attribution under the terms of the AGPL license.
See the [LICENSE](LICENSE) file for details.


## Installation

Please see the Archivematica [production installation](https://www.archivematica.org/docs/latest/admin-manual/installation/installation/) or [development installation](https://wiki.archivematica.org/Getting_started#Installation) instructions.


## Documentation

* [User documentation](https://www.archivematica.org/en/docs/fpr/)
* [Requirements overview](https://wiki.archivematica.org/Format_policy_registry_requirements)


## Other resources

* [Website](https://www.archivematica.org/): Archivematica user and administrator documentation
* [Wiki](https://www.archivematica.org/wiki/Development): Archivematica developer facing documentation, requirements analysis and community resources
* [User Google Group](https://groups.google.com/forum/#!forum/archivematica): Forum/mailing list for user questions
* [Technical Google Group](https://groups.google.com/forum/#!forum/archivematica-tech): Forum/mailing list for technical questions about development, setup, administration, etc.
* [Paid support](https://www.artefactual.com/services/): Paid support, hosting, training, consulting and software development contracts from Artefactual


## Related projects

Archivematica consists of several projects working together, including:

* [Archivematica](https://github.com/artefactual/archivematica): Main repository containing the user-facing dashboard, task manager MCPServer and clients scripts for the MCPClient
* [Storage Service](https://github.com/artefactual/archivematica-storage-service): Responsible for moving files to Archivematica for processing, and from Archivematica into long-term storage
* [Format Policy Registry](https://github.com/artefactual/archivematica-fpr-admin): This repository! Submodule shared between Archivematica and the Format Policy Registry (FPR) server that displays and updates FPR rules and commands

For more projects in the Archivematica ecosystem, see the [getting started](https://wiki.archivematica.org/Getting_started#Projects) page.
