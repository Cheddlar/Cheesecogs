from redbot.core import commands

class Purge(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
    async def purge(self,message, amount:int=None):
        if amount is not None:
            await message.channel.purge(limit=amount+1)
            embed = redbot.core.utils.embed(
            title = "**Purge**",
            description = (f'Deleted **{amount}** messages!'),
            color = (0x992d22)
            )
            await message.send(embed=embed, delete_after = 5)
        else:
            await message.send("Please provide an amount of messages to purge!")
