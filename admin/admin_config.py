# !/usr/bin/env python
# coding=utf8
# Author: quheng

from manager import app
from manager import db
import os
from flask import url_for, redirect, render_template, request, abort
from flask_sqlalchemy import SQLAlchemy
from flask_security import Security, SQLAlchemyUserDatastore, login_required, current_user
from flask_security.utils import encrypt_password
from flask_admin.contrib import sqla
import flask_admin
from flask_admin import helpers as admin_helpers
import key
from wtforms import validators
from admin_models import Manager, Role
import flask_admin as admin
from flask_admin import AdminIndexView
from flask_admin.contrib import sqla
from flask_admin.contrib.sqla import filters

admin = admin.Admin(app, index_view=AdminIndexView(
    url='/admin'),
    name='PayKitty Admin',
    template_mode='bootstrap3')

# Setup Flask-Security
manager_datastore = SQLAlchemyUserDatastore(db, Manager, Role)
security = Security(app, manager_datastore)
@security.context_processor
def security_context_processor():
    return dict(
        admin_base_template=admin.base_template,
        admin_view=admin.index_view,
        h=admin_helpers,
    )


# Create customized model view class
class MyModelView(sqla.ModelView):
    column_display_pk = True
    # form_columns = ('id')

    def is_accessible(self):
        if not current_user.is_active or not current_user.is_authenticated:
            return False

        if current_user.has_role('superuser'):
            return True

        return False

    def _handle_view(self, name, **kwargs):
        """
        Override builtin _handle_view in order to redirect users when a view is not accessible.
        """
        if not self.is_accessible():
            if current_user.is_authenticated:
                # permission denied
                abort(403)
            else:
                # login
                return redirect(url_for('security.login', next=request.url))
