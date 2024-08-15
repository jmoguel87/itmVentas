import logging

MapLogger = logging.getLogger('MapLog')

class ControlDBRouter(object):
    route_django_app_labels:list
    route_clients_app_labels:list
    clientsLabel:str
    articlesLabel:str

    def __init__(self):
        self.route_django_app_labels = ['admin','auth', 'contenttypes', 'sessions', 'messages', 'staticfiles','django']
        # route_django_app_labels.append(['user','OTP','fireblocks'])
        self.clientsLabel:str = 'clients'
        self.articlesLabel:str = 'articles'
        self.route_clients_app_labels = [self.clientsLabel, self.articlesLabel]

    def db_for_read(self, model, **hints):
        if model._meta.app_label in self.route_django_app_labels :
            return 'default'
        elif model._meta.app_label in self.route_clients_app_labels:
            return self.clientsLabel
        return None

    def db_for_write(self, model, **hints):
        if model._meta.app_label in self.route_django_app_labels :
            return 'default'
        elif model._meta.app_label in self.route_clients_app_labels:
            return self.clientsLabel
        return None

    def allow_relation(self, obj1, obj2, **hints):
        if (
            obj1._meta.app_label in self.route_django_app_labels or
            obj2._meta.app_label in self.route_django_app_labels
        ):
           return True
        elif (
            obj1._meta.app_label in self.route_clients_app_labels or
            obj2._meta.app_label in self.route_clients_app_labels
        ):
            return True
        return None
        
    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label in self.route_django_app_labels :
            return (db == 'default')
        elif app_label in self.route_clients_app_labels:
            return (db == self.clientsLabel)
        return None

