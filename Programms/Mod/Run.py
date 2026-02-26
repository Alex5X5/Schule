from Programms.Mod.DesignTimeService import DesignTimeService
from Programms.Mod.TestDatabaseContext import TestDatabaseContext

DesignTimeService.IS_DESIGN_TIME = True
context = TestDatabaseContext()
DesignTimeService.on_initialized()