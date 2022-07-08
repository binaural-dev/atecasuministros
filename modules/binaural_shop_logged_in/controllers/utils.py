from odoo.http import request
import functools


def has_logged(func):
    """."""
    @functools.wraps(func)
    def wrap(self, *args, **kwargs):

        if request.env.user.id == request.env.ref('base.public_user').id:  
            return request.render('web.login', {})

        return func(self, *args, **kwargs)

    return wrap