from Programms.M14_1.Kolibri import Kolibri
from Programms.M14_1.Pteranodon import Pteranodon
from .Tier import Tier
from .Säugetier import Säugetier
from .Vogel import Vogel
from .Hund import Hund
from .Katze import Katze

tier_liste:list[Tier] = [
    Hund('bello', 10, 10),
    Katze('maunzi', 10,10),
    Pteranodon('mega_fly', 10, 10),
    Kolibri('mega_fly', 10, 10)
]

for t in tier_liste:
    t.laut_geben()