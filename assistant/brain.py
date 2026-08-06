"""
=========================================
AMNA AI Assistant
Brain
=========================================

Compatibility layer.

The brain simply forwards the request to
the router.

The Planning Pipeline is now responsible
for deciding how the request is executed.
"""

from assistant.router import route


def reply(user, context=None):

    return route(
        user=user,
        context=context
    )