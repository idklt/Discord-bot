import discord
from discord.ext import commands

intents=discord.Intents.default()
intents.message_content=True

bot =commands.Bot(command_prefix="$",intents=intents)

@bot.event
async def on_ready():
    print("El bot está en línea")

manualidades_eco={
    
    "manualidad1":"https://youtube.com/watch?v=aR7c1QgpAqMm",
    "manualidad2":"https://www.youtube.com/watch?v=Xs2hAWuPmSg",
    "manualidad3":"https://www.youtube.com/watch?v=O_5ZhQ5ttmc",
    "manualidad4":"https://www.youtube.com/watch?v=Cx2vm31y0IA",
}

descomposicion_residuos={
    "botella de plastico":500,
    "lata de aluminio":10,
    "bolsa de plástico":150,
    "vidrio":4000,
    "papel":1,
    "pañal":500,
    "ropa usada":1,
    "pila":1000,
    "aceite":100,

}
recicl_resid={
    "botellas de plastico": "reciclado",
    "botes de limpieza": "reciclado",
    "bolsas de frituras": "desechado",
    "tapas de plastico": "reciclado",
    "bolsas de plastico": "reciclado",
    "tarrinas": "reciclado",
    "residuos medicos": "desechado",
    "residuos peligrosos": "desechado",
    "baterias": "desechado",
    "tubos de pasta dental": "desechado",
    "encededores": "desechado",
    "platos desechables": "desechado",
    "servilletas": "desechado",
    "papel de regalo": "desechado",
    "metales": "desechado",
    

}
@bot.command()
async def clasificar(ctx, *, objeto:str):
    objeto=objeto.lower()
    if objeto in descomposicion_residuos:
        tiempo=descomposicion_residuos[objeto]
        await ctx.send(f"El objeto {objeto}, se demora {tiempo} años")
    else:
        await ctx.send("No se encontró información")
        
@bot.command()
async def manualidad(ctx,*,manual:str):
    manual=manual.lower()
    if manual in manualidades_eco:
        await ctx.send(f"Sigue este link {manual}")
    else:
        await ctx.send("Lo siento, se incluirán más links pronto")

@bot.command()
async def reciclar(ctx,*,reciclar:str):
    reciclar=reciclar.lower()
    if reciclar in recicl_resid:
        await ctx.send(f"Se recomienda que este residuo sea {reciclar}")
    else:
        await ctx.send("Lo lamento, no contamos con información acerca de aquel residuo")

bot.run("your token")