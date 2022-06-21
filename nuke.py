from redbot.core import commands

class Nuke(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
    @commands.command()
    async def nuke(self,ctx):
            channel = ctx.message.channel
            channel_position = channel.position
            nuke_channel = self.bot.get_channel(channel.id)

            if nuke_channel is not None:
                embed = redbot.core.utils.embed(
                    title = '**Channel nuked**!',
                    description = 'The channel has been nuked succesfully!',
                                color =(0x992d22)
                )
                new_channel = await nuke_channel.clone(reason="Has been Nuked!")
                nukedchannel = nuke_channel.name
                await nuke_channel.delete()
                await new_channel.edit(sync_permissions=True, position=channel_position)
                await new_channel.send(embed=embed)
                await new_channel.send("https://giphy.com/gifs/explosion-oe33xf3B50fsc")
