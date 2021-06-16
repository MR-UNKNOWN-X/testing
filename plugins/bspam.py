from . import *

@ultroid_cmd(pattern="bspam")
async def botspam(ult):
    input = ult.text[7:]
    udB.delete("USPAM")
    x = None
    while x == None:
        x = Redis("USPAM")
        await asst.send_message(
                ult.chat_id,
                input,
            )
            
@ultroid_cmd(pattern="stop$")
async def _(e):
    udB.set("USPAM", ".")
    await eod(e, "Unlimited spam stopped")            
            