from django.conf.urls import url

from log_trigger import views


urlpatterns = [
    url(r'^system-exception/', views.system_exception_view,
        name='system_exception_view'),

    url(r'^unhandled-exception/', views.unhandled_exception_view,
        name='unhandled_exception_view'),

    url(r'^disallowed-host-exception', views.disallowed_host_exception_view,
        name='disallowed_host_exception_view'),

    url(r'^debug-logging/', views.logger_debug_view,
        name='logger_debug_view'),

    url(r'^info-logging/', views.logger_info_view,
        name='logger_info_view'),

    url(r'^warn-logging/', views.logger_warn_view,
        name='logger_warn_view'),

    url(r'^error-logging/', views.logger_error_view,
        name='logger_error_view'),

    url(r'^critical-logging/', views.logger_critical_view,
        name='logger_critical_view'),
]
