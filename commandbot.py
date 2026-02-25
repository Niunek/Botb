import discord
import os
from dotenv import load_dotenv
from discord.ext import commands
import json
import random
from easy_pil import Editor, Canvas, Font, load_image
import io

load_dotenv()
TOKEN = os.getenv("TOKEN")

intents = discord.Intents.default()
intents.message_content = True

def zaladuj_wyniki():
    if os.path.exists("wyniki.txt"):
        try:
            with open("wyniki.txt","r") as f:
                dane = json.load(f)
                print(dane)
                return dane
        except (json.JSONDecodeError,ValueError):
            print("Blad ladowania(dekodowania)")
            return {}
            print("blad otwierania pliku")
    return {}
def zapisz_wyniki():
     with open("wyniki.txt", "w") as f:
         json.dump(xplist, f, indent=4)

xplist = zaladuj_wyniki()


bot = commands.Bot(command_prefix='/', intents=intents)




@bot.event
async def on_ready():
    print(f'Zalogowaliśmy się jako {bot.user}')
#==========================================================================
@bot.event
async def on_message(message):
    if message.author.bot:
        return
    user_id = str(message.author.id)
    if user_id in xplist:
        if xplist[user_id] <= 1:
            xplist[user_id] += 0.1
        elif xplist[user_id] > 1 and xplist[user_id] <= 3:
            xplist[user_id] += 0.08 
        elif xplist[user_id] > 3 and xplist[user_id] <= 5:
            xplist[user_id] += 0.06 
        elif xplist[user_id] > 5 and xplist[user_id] <= 7:
            xplist[user_id] += 0.05 
        elif xplist[user_id] > 7 and xplist[user_id] <= 10:
            xplist[user_id] += 0.04 
        elif xplist[user_id] > 10:
            xplist[user_id] += 0.03 
    else:
        xplist[user_id] = 0.1
    print(f"Uzytkownik {message.author} ma teraz {xplist[user_id]} punktow xp")
    await bot.process_commands(message)
#==========================================================================
    if message.author == bot.user:
        return
    print(f'Wiadomosc od {message.author}: {message.content}')

    if  message.content.lower() in ('cześć') != '-1':
        await message.channel.send(f'Cześć **{message.author.display_name}**!')
    elif  message.content.lower() in ('witam') != '-1':
        await message.channel.send(f'Witam, witam **{message.author.display_name}**!')
    elif  message.content.lower() in ('czesc') != '-1':
        await message.channel.send(f'Cześć **{message.author.display_name}**!')
    elif  message.content.lower() in ('hej') != '-1':
        await message.channel.send(f'Hejka **{message.author.display_name}**!')
    elif message.content.lower() in ('siema') != '-1':
        await message.channel.send(f'Siema **{message.author.display_name}**!')
    elif message.content.lower() in ('elo') != '-1':
        await message.channel.send(f'Elo! **{message.author.display_name}**!')
    elif message.content.lower() in ('dzień dobry') != '-1':
        await message.channel.send(f'Dzień dobry! **{message.author.display_name}**!')
    elif message.content.lower() in ('dzien dobry') != '-1':
        await message.channel.send(f'Dzień dobry! **{message.author.display_name}**!')
#==========================================================================      

@bot.command()
async def poziom(ctx):
    user_id = str(ctx.author.id)
    xp_usera = xplist[user_id]
    name_usera = ctx.author.name
    awatar_raw = await ctx.author.display_avatar.read()
    awatar_img = load_image(ctx.author.display_avatar.url)
    awatar =  Editor(awatar_img).resize((250,250)).circle_image()
    xp = round(xp_usera % 1, 2)
    if xp >= 0 and xp < 0.03:
        tlo = Editor("TłoBotaPoziom1%2.png")
    elif xp >= 0.03 and xp < 0.10:
        tlo = Editor("TłoBotaPoziom5%2.png")
    elif xp >= 0.10 and xp < 0.22:
        tlo = Editor("TłoBotaPoziom15%2.png")
    elif xp >= 0.22 and xp < 0.33:
        tlo = Editor("TłoBotaPoziom25%2.png")
    elif xp >= 0.33 and xp < 0.45:
        tlo = Editor("TłoBotaPoziom40%2.png")
    elif xp >= 0.45 and xp < 0.50:
        tlo = Editor("TłoBotaPoziom50%2.png")
    elif xp >= 0.50 and xp < 0.60:
        tlo = Editor("TłoBotaPoziom55%2.png")
    elif xp >= 0.60 and xp < 0.70:
        tlo = Editor("TłoBotaPoziom65%2.png")
    elif xp >= 0.70 and xp < 0.80:
        tlo = Editor("TłoBotaPoziom75%2.png")
    elif xp >= 0.80 and xp < 0.90:
        tlo = Editor("TłoBotaPoziom85%2.png")    
    elif xp >= 0.90 and xp < 1:
        tlo = Editor("TłoBotaPoziom99%2.png")
    elif xp == 0 or xp:
        tlo = Editor("TłoBotaPoziom1%2.png")
    else:
        tlo = Editor("TloBotaPoziom.png")

    tlo.paste(awatar, (100,100))
#==========================================================================
    profile_czcionki_1 = Font.poppins(size=35, variant='italic')
    profile_czcionki_2 = Font.poppins(size=80, variant='italic')
    profile_czcionki_3 = Font("AGENCYR.TTF", size = 90)
    profile_czcionki_4 = Font.poppins(size=55, variant='bold')
    tekst_poziomu = f"Poziom: {round(xp_usera, 2)}"
    brakujacy_poziom = f"Brakuje ci {round(1 - (xp_usera % 1), 2)} do następnego poziomu"
    procent_xp = f"{xp * 100}%"
    tlo.text((50,350), str(name_usera),font = profile_czcionki_3, color = "white")
    tlo.text((420,160),str(tekst_poziomu),font = profile_czcionki_2, color = "white")
    #tlo.text((155,615),str(brakujacy_poziom),font = profile_czcionki_1, color = "gray")
    tlo.text((435,500),str(procent_xp),font = profile_czcionki_4, color = "white")
    

    plik = discord.File(fp=tlo.image_bytes,filename = "poziom.png")
    await ctx.send(file=plik)
#==========================================================================
#moznam = False
#@bot.command()
#async def moneta(ctx):
#    await ctx.send("Orzeł czy Reszka?")
#    moznam = True
#@bot.event
#async def on_message(message):
#    if moznam == True:
#        if  message.content.lower() in ('orzeł') != '-1':
#            wynik = random.randint(1, 2)
#            if wynik == 1:
#                await message.channel.send("Wygrałeś!")
#                moznam = False
#            else:
#                await message.channel.send("Ha,Przegrałeś!")
#                moznam = False
#        if  message.content.lower() in ('reszka') != '-1':
#            wynik = random.randint(1, 2)
#            if wynik == 1:
#                await message.channel.send("Ha,Przegrałeś!")
#                moznam = False       
#            else:
#                await message.channel.send("Wygrałeś!")
#                moznam = False
#    else:
#       return
            
        
    

try:
    bot.run(TOKEN)
finally:
    zapisz_wyniki()