from raya.application_base import RayaApplicationBase

from skills.skill_template import SkillTemplate
from raya.exceptions import RayaSkillAborted


class RayaApplication(RayaApplicationBase):

    async def setup(self):
        self.log.info(f'RayaApplication.setup')

        self.skill_template = self.register_skill(SkillTemplate)
        
        setup_args = {}
        result = await self.skill_template.execute_setup(
            setup_args=setup_args
        )
        self.log.warn(f'setup result: {result}')

        execute_args = {
            'error': self.error
        }
        await self.skill_template.execute_main(
            execute_args=execute_args,
            callback_done=self.cb_skill_done,
            callback_feedback=self.cb_skill_feedback,
            wait=False
        )


    async def loop(self):
        try:
            result = await self.skill_template.wait_main()
            self.log.warn(f'skill_template result: {result}')

            result = await self.skill_template.execute_finish()
            self.log.warn(f'skill_template finish result: {result}')

        except RayaSkillAborted as e:
            self.log.error((
                'Skill aborted with '
                f'Error code: \'{e.error_code}\', '
                f'Error msg: \'{e.error_msg}\'.'
            ))

        while True:
            await self.sleep(1)
            self.log.debug(f'RayaApplication.loop')


    async def finish(self):
        self.log.info(f'RayaApplication.finish')


    async def cb_skill_done(self, exception, result):
        self.log.debug(
            f'Callback skill done: '
            f'Exception: \'{exception}\', '
            f'Result: \'{result}\'.'
        )


    async def cb_skill_feedback(self, feedback):
        self.log.debug(
            f'Callback Feedback: \'{feedback}\''
        )


    def get_arguments(self):
        self.error = self.get_flag_argument(
            '-e', '--error',
            help=(
                'It will generate an error inside '
                'the skill in order to abort it.'
            ),
        )
