def requirements():
    return "re"


def main(client, re):
    import discord
    title_of_embed = {}
    color_of_embed = {}
    thumbnail_of_embed = {}
    description_for_embed = {}
    footer_of_embed = {}

    @client.command(aliases=['init_embed', 'embed_init'])
    async def create_embed_init(ctx):
        if ctx.author.guild_permissions.manage_messages or ctx.author.id == 432801163126243328:
            title_of_embed.pop(ctx.guild.id)
            color_of_embed.pop(ctx.guild.id)
            thumbnail_of_embed.pop(ctx.guild.id)
            description_for_embed.pop(ctx.guild.id)

    @client.command(aliases=['color_for_embed'])
    async def set_color(ctx, color):
        if ctx.author.guild_permissions.manage_messages or ctx.author.id == 432801163126243328:
            try:
                c = eval(color)
                color_of_embed[ctx.guild.id] = discord.Color.from_rgb(
                    c[0], c[1], c[2])
                await ctx.send(embed=discord.Embed(description="Color Set", color=discord.Color(value=re[8])))
            except Exception as e:
                await ctx.send(str(e))

    @client.command(aliases=['title'])
    async def set_title(ctx, *, title):
        if ctx.author.guild_permissions.manage_messages or ctx.author.id == 432801163126243328:
            title_of_embed[ctx.guild.id] = title
            await ctx.send(embed=discord.Embed(description="Title Set", color=discord.Color(value=re[8])))

    @client.command(aliases=['description'])
    async def set_description(ctx, *, description):
        if ctx.author.guild_permissions.manage_messages or ctx.author.id == 432801163126243328:
            description_for_embed[ctx.guild.id] = description
            await ctx.send(embed=discord.Embed(description="Description Set", color=discord.Color(value=re[8])))

    @client.command(aliases=['footer'])
    async def set_footer(ctx, *, footer):
        if ctx.author.guild_permissions.manage_messages or ctx.author.id == 432801163126243328:
            footer_of_embed[ctx.guild.id] = footer
            await ctx.send(embed=discord.Embed(description="Footer Set", color=discord.Color(value=re[8])))

    @client.command(aliases=['thumbnail'])
    async def set_thumbnail(ctx, url):
        if ctx.author.guild_permissions.manage_messages or ctx.author.id == 432801163126243328:
            thumbnail_of_embed[ctx.guild.id] = url
            await ctx.send(embed=discord.Embed(description="Thumbnail Set", color=discord.Color(value=re[8])))

    @client.command(aliases=['send'])
    async def send_embed(ctx, channel: discord.TextChannel):
        if ctx.author.guild_permissions.manage_messages or ctx.author.id == 432801163126243328:
            if client.get_channel(channel.id) != None:
                send_channel = client.get_channel(channel.id)
                embed = discord.Embed()
                embed.set_author(name=ctx.author.name,
                                 icon_url=ctx.author.avatar_url_as(format="png"))
                if ctx.guild.id in list(description_for_embed.keys()):
                    try:
                        embed = discord.Embed(
                            description=description_for_embed[ctx.guild.id])
                    except Exception as e:
                        await ctx.send(str(e))
                if ctx.guild.id in list(title_of_embed.keys()):
                    try:
                        embed.title = title_of_embed[ctx.guild.id]
                    except Exception as e:
                        await ctx.send(str(e))
                if ctx.guild.id in list(thumbnail_of_embed.keys()):
                    try:
                        embed.set_thumbnail(
                            url=thumbnail_of_embed[ctx.guild.id])
                    except Exception as e:
                        await ctx.send(str(e))
                if ctx.guild.id in list(color_of_embed.keys()):
                    try:
                        embed.color = color_of_embed[ctx.guild.id]
                    except Exception as e:
                        await ctx.send(str(e))
                if ctx.guild.id in list(footer_of_embed.keys()):
                    try:
                        embed.set_footer(text=footer_of_embed[ctx.guild.id])
                    except Exception as e:
                        await ctx.send(str(e))
                await send_channel.send(embed=embed)
            else:
                await ctx.send(embed=discord.Embed(title="Oops", description="This channel does not exist. Please check again", color=discord.Color(value=re[8])))
