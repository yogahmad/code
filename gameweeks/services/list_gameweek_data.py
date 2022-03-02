from typing import Optional

from commons.runnable import Runnable
from gameweeks.models import Gameweek


class ListGameweekDataService(Runnable):
    @classmethod
    def run(
        cls,
        next_n_gameweek: Optional[int] = None,
    ):
        base_qs = Gameweek.objects.prefetch_related().all().prefetch_related("matches")
        for gameweek in base_qs:
            print(gameweek)
