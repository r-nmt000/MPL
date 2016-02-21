# -*- coding: utf-8 -*-

"""MPL: ビュー"""

from __future__ import absolute_import, division, print_function, unicode_literals

import logging

from apps.mpl.forms import MPLForm
from django.conf import settings
from django.http import JsonResponse
from django.views.generic import FormView, View
from libs.interpreter import Brainfuck, InvalidTokenException, CursorUnderflowException

logger = logging.getLogger(__name__)

REDIRECT_FIELD_NAME = 'next'


class MPLView(FormView):
    form_class = MPLForm
    template_name = 'index.html'
    success_url = settings.LOGIN_REDIRECT_URL

    # def form_valid(self, form):
    #     return self.render_to_response(self.get_context_data(output='aaa'))

    def get_context_data(self, **kwargs):

        if 'output' not in kwargs:
            kwargs['output'] = ''
        return super(MPLView, self).get_context_data(**kwargs)


class APIView(View):

    def get(self, request, *args, **kwargs):
        code = request.GET.get('code').split()
        interpreter = Brainfuck()

        try:
            output = interpreter.evaluate(code)
        except InvalidTokenException as e:
            output = 'Invalid token exception.'
        except CursorUnderflowException as e:
            output = 'Cursor underflow exception.'
        finally:
            return JsonResponse({
                'output': output
            })


