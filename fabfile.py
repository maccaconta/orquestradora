# -*- coding: utf-8 -*-

from datetime import datetime
from fabric.api import local
from fabric.colors import green as _green, yellow as _yellow, red as _red
from os.path import exists


def makemigrations(app):
    """
    nome: makemigrations
    :param app: app
    :return: ...
    """
    # local("python manage.py makemigrations {app}".format(app=app))


def migrations():
    """
    nome: igrations
    :return: ...
    """
    local("python manage.py makemigrations")
    local("python manage.py migrate")


def run(port=8000):
    """
    nome: run
    :param port: int
    :return: ...
    """
    local("python manage.py runserver {port}".format(port=port))


def fix(name):
    """
    nome: fix
    :param name: Any
    :return: ...
    """
    local("python manage.py fix_{name}".format(name=name))


def config_db():
    """
    nome: config_db
    :return: ...
    """
    # migrations()
    run()


def drop_db():
    """
    drop_db
    :return: ...
    """
    # local("python manage.py flush --noinput")
    local("python manage.py reset_db --noinput")


def collect():
    """
    nome: collect
    :return: ...
    """
    local("python manage.py collectstatic --noinput")
    local("python manage.py collectmedia --noinput")


def prod():
    """
    nome: prod
    :return: ...
    """
    migrations()
    # fix("configapp") #importante rodar nesta ordem, dados de producao
    # fix("algo")


def dev():
    """
    nome: dev
    :return: ...
    """
    migrations()  # importante rodar nesta ordem, dados de producao
    # fix("set_system")
    fix("routers")
    fix("whats_template")
    fix("channel")
    fix("skill")
    fix("channelskill")
    fix("user")
    fix("tax")
    fix("service")
    fix("guide_post")
    fix("country_code")
    fix("city_code")


# def backup_db():
#     today_label = datetime.now().strftime("%Y-%m-%d_%H-%M")
#     local("mkdir -p _backups_db")
#     local("python manage.py dumpdata --exclude contenttypes --indent=1 > _backups_db/backup_db_{}.json".format(
#         today_label))


def rm_sqlite():
    """
    nome: rm_sqlite
    :return: ...
    """
    local("rm db_orchest.sqlite3")


def shell():
    """
    nome: shell
    :return: ...
    """
    local("python manage.py shell_plus")


def test(modulo=None, clazz=None):
    """
    nome: test
    :param modulo: None
    :param clazz: None
    :return: ...
    """
    if modulo and not clazz:
        local("python manage.py test {modulo}".format(modulo=modulo))
    elif modulo and clazz:
        local("python manage.py test {modulo}:{clazz}".format(modulo=modulo, clazz=clazz))
    else:
        local("python manage.py test")


def router():
    fix("routers")

def service():
    fix("service")

def run():
    local("python manage.py runserver")
