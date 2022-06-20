# ASynchronous (the unusual  implementation )
# Import => https://docs.python.org/3/library/asyncio.html

import asyncio
#async a keyword to allow asynchronous implementation in this function
async def main():
    print('Hello ...')
    #await => here must stop and wait for given time in sleep function
    await asyncio.sleep(3)
    print('... World!')

# Python 3.7+
asyncio.run(main())