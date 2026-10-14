import os
import discord
from discord.ext import commands

TOKEN = os.getenv("DISCORD_TOKEN")  # ou colle ton token ici entre guillemets (déconseillé)

intents = discord.Intents.default()
intents.message_content = True  # à activer aussi dans le portail développeur
intents.members = True

bot = commands.Bot(command_prefix="j!", intents=intents)


@bot.event
async def on_ready():
    print(f"Connecté en tant que {bot.user}")


@bot.command(name="staffcheck")
@commands.guild_only()
async def staffcheck(ctx: commands.Context):
    """Vérifie si l'utilisateur est admin sur ce serveur."""
    member = ctx.author
    is_admin = member.guild_permissions.administrator
    is_owner = ctx.guild.owner_id == member.id

    if is_admin or is_owner:
        embed = discord.Embed(
            title="✅ Staff vérifié",
            description=f"{member.mention} est **administrateur** sur **{ctx.guild.name}**.",
            color=discord.Color.green(),
            timestamp=discord.utils.utcnow(),
        )
        embed.add_field(name="Propriétaire", value="Oui" if is_owner else "Non")
        embed.add_field(name="Rôle le plus haut", value=member.top_role.mention)
    else:
        embed = discord.Embed(
            title="❌ Non vérifié",
            description=f"{member.mention} n'est **pas** administrateur sur **{ctx.guild.name}**.",
            color=discord.Color.red(),
            timestamp=discord.utils.utcnow(),
        )

    embed.set_footer(text=f"ID : {member.id}")
    await ctx.send(embed=embed)


bot.run(TOKEN)
