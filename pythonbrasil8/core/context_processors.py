# -*- coding: utf-8 -*-

from mittun.sponsors.models import Sponsor


def diamond_sponsors(request):
    sponsors = Sponsor.objects.filter(category__priority=0)
    return {'diamond_sponsors': sponsors}


def sponsors(request):
    sponsors = Sponsor.objects.select_related('category__priority')
    sponsors = sponsors.order_by('category__priority')
    return {'sponsors': sponsors}
