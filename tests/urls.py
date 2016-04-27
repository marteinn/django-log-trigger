from django.conf.urls import include, url

import log_trigger


urlpatterns = [
    url(r'^log-triggers/', include(log_trigger.urls)),
]
