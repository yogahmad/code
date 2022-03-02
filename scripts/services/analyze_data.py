from django.db.models import Q, Sum

from gameweeks.models import Gameweek
from stats.models.underlying_stats import UnderlyingStat
from teams.models import Team


min_xg_form = 100.0
max_xg_form = 0.0
min_xgc_form = 100.0
max_xgc_form = 0.0

for team in Team.objects.all():
    xg_form = team.xg_form
    xgc_form = team.xgc_form
    if xg_form > max_xg_form:
        max_xg_form = xg_form
    if xg_form < min_xg_form:
        min_xg_form = xg_form
    if xgc_form > max_xgc_form:
        max_xgc_form = xgc_form
    if xgc_form < min_xgc_form:
        min_xgc_form = xgc_form
    # print("Team {} xG ({}) xGC ({})".format(team.name, xg_form, xgc_form))


for team in Team.objects.all():
    xg_form = team.xg_form
    xgc_form = team.xgc_form

    xg_red_color = 0x00 + round((0xFF - 0x00) * (xg_form -
                                                 min_xg_form) / (max_xg_form - min_xg_form))

    xg_green_color = 0x00 + round((0xFF - 0x00) * (max_xg_form -
                                                   xg_form) / (max_xg_form - min_xg_form))

    xg_color = xg_red_color * 16 * 16 * 16 * 16 + xg_green_color * 16 * 16

    print("{} {} => {}".format(team.name, xg_form,
          hex(xg_color)))
