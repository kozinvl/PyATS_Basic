import logging
from ats import aetest

logger = logging.getLogger(__name__)


class HelloWorld(aetest.Testcase):

    @aetest.test
    def test(self):
        logger.info('Hello World!')


# main()
if __name__ == '__main__':
    # set logger level
    logger.setLevel(logging.INFO)

    aetest.main()
