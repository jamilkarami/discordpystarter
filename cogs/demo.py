import discord
import logging
from discord.ext import commands
from discord import app_commands

class Demo(commands.Cog, name="demo"):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        logging.info(f"[{__name__}] Cog is ready")

    # This command is triggered by typing "!ping" in a Discord chat the bot has access to
    @commands.command()
    async def ping(self, ctx):
        await ctx.reply("Pong")
        return

    # This is a slash command, triggered by using /marco. These commands are handled differently
    # by Discord bots and the push is towards using them exclusively
    @app_commands.command(name="marco")
    async def marco(self, interaction: discord.Interaction):
        await interaction.response.send_message("Polo")
        return


async def setup(bot: commands.Bot):
    await bot.add_cog(Demo(bot))
