### Development

Download the sources:

    $ git clone https://github.com/artefactual/archivematica-fpr-admin
    $ cd archivematica-fpr-admin

Create the virtual environment and install the requirements:

    $ virtualenv --python=python2.7 .env
    $ source .env/bin/activate
    $ pip install -r dev_requirements.txt

Bootstrap database:

    $ testproject/manage.py migrate
    $ testproject/manage.py createsuperuser --username=demo --email=demo@example.com

Run development server:

    $ testproject/manage.py runserver 127.0.0.1:8000

You can run the tests with the following command:

    $ testproject/manage.py test

### Translations

Project maintainers extract and compile messages often. The following commands
will generate `.po` and `.mo` files under the `fpr/locale/` directory. We want
them to be tracked in the repository.

    $ testproject/manage.py makemessages -d django -l fr -l es -l en -l sv -l ja -l pt-br
    $ testproject/manage.py compilemessages

Transifex is our current localization platform. Install `transifex-client` and
run the following command to push the source messages to Transifex:

    $ tx push --source

Pull translations from the platform with the following command:

    $ tx pull --parallel
    $ testproject/manage.py compilemessages
