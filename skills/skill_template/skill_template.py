from raya.skills import RayaSkill
from raya.exceptions import RayaSkillAborted

from .constants import *


class SkillTemplate(RayaSkill):

    DEFAULT_SETUP_ARGS = {

    }
    
    REQUIRED_SETUP_ARGS = {
        
    }
    
    DEFAULT_EXECUTE_ARGS = {
        'error': False
    }
    
    REQUIRED_EXECUTE_ARGS = {
    
    }


###############################################################################
###########################   skill methods   #################################
###############################################################################


    async def setup(self):
        # self.sensors:SensorsController = \
            # await self.enable_controller('sensors')
        await self.send_feedback('RayaSkill.setup')
        return (1, 'Setup done')


    async def main(self):
        await self.send_feedback('RayaSkill.main')
        if self.execute_args['error']:
            raise RayaSkillAborted(1, 'Error in main')
        return (2, 'Main done')

    
    async def finish(self):
        await self.send_feedback('RayaSkill.finish')
        return (3, 'Finish done')
