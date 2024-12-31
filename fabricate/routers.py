class TemplateRouter:
    """
    A database router to control operations for the EmailTemplate model.
    """
    def db_for_read(self, model, **hints):
        """
        Direct read operations for EmailTemplate to the MongoDB database.
        """
        if model._meta.app_label == 'core' and model.__name__ == 'EmailTemplate':
            return 'mongodb'
        return 'default'

    def db_for_write(self, model, **hints):
        """
        Direct write operations for EmailTemplate to the MongoDB database.
        """
        if model._meta.app_label == 'core' and model.__name__ == 'EmailTemplate':
            return 'mongodb'
        return 'default'

    def allow_relation(self, obj1, obj2, **hints):
        """
        Allow relations if both models are in the same database.
        """
        db_set = {'default', 'mongodb'}
        if obj1._state.db in db_set and obj2._state.db in db_set:
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        Ensure EmailTemplate model only appears in the MongoDB database.
        """
        if app_label == 'core' and model_name == 'emailtemplate':
            return db == 'mongodb'
        return db == 'default'
