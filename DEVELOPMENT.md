### Development

Download the sources:

    $ git clone https://github.com/artefactual/archivematica-fpr-admin
    $ cd archivematica-fpr-admin

Create the virtual environment and install the requirements:

    $ virtualenv .env
    $ source .env/bin/activate
    $ pip install -r requirements.txt

Bootstrap database:

    $ testproject/manage.py migrate
    $ testproject/manage.py createsuperuser --username=demo --email=demo@example.com

Run development server:

    $ testproject/manage.py runserver 127.0.0.1:8000

Extract and compile messages. These commands will generate `.po` and `.mo` files under the `fpr/locale/` directory. We want to track them in the repo.

    $ testproject/manage.py makemessages --all
    $ testproject/manage.py compilemessages
