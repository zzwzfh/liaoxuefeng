import asyncio
import sys
import orm
from models import User, Blog, Comment

async def test():
    await  orm.create_pool(loop=loop, user='dev', password='123456', db='project')
    u = User(name='dev', email='test@example.com', passwd='1234567890', image='about:blank')
    await u.save()

#for x in test():
#    pass

loop = asyncio.get_event_loop()
loop.run_until_complete(test())
loop.close()
if loop.is_closed():
    sys.exit(0)
