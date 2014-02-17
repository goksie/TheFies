#
# Newfies-Dialer License
# http://www.newfies-dialer.org
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this file,
# You can obtain one at http://mozilla.org/MPL/2.0/.
#
# Copyright (C) 2011-2014 Star2Billing S.L.
#
# The Initial Developer of the Original Code is
# Arezqui Belaid <info@star2billing.com>
#
from django.conf.urls import patterns


urlpatterns = patterns('frontend.views',
    (r'^$', 'index'),
    (r'^login/$', 'login_view'),
    (r'^logout/$', 'logout_view'),
    (r'^index/$', 'index'),
    (r'^pleaselog/$', 'pleaselog'),
    (r'^dashboard/$', 'customer_dashboard'),

    # Password reset for Customer UI
    (r'^password_reset/$', 'cust_password_reset'),
    (r'^password_reset/done/$', 'cust_password_reset_done'),
    (r'^reset/(?P<uidb36>[0-9A-Za-z]+)-(?P<token>.+)/$',
        'cust_password_reset_confirm'),
    (r'^reset/done/$', 'cust_password_reset_complete'),
)
