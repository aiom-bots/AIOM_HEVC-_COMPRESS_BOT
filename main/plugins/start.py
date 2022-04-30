#  This file is part of the VIDEOconvertor distribution.
#  Copyright (c) 2021 vasusen-code ; All rights reserved. 
#
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, version 3.
#
#  This program is distributed in the hope that it will be useful, but
#  WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
#  General Public License for more details.
#
#  License can be found in < https://github.com/vasusen-code/VIDEOconvertor/blob/public/LICENSE> .

from telethon import events, Button
from ethon.teleutils import mention
from ethon.mystarts import vc_menu

from .. import Drone, ACCESS_CHANNEL, AUTH_USERS

from main.plugins.actions import set_thumbnail, rem_thumbnail, heroku_restart
from LOCAL.localisation import about_text
from LOCAL.localisation import info_text, spam_notice, help_text, DEV, source_text, SUPPORT_LINK

@Drone.on(events.NewMessage(incoming=True, pattern="/start"))
async def start(event):
    await event.reply(f'**Hᴇʟʟᴏ 👋 [{event.sender.first_name}](tg://user?id={event.sender_id}),\n\nTʜɪs Is A Hɪɢʜ Eꜰꜰɪᴄɪᴇɴᴄʏ Vɪᴅᴇᴏ Cᴏᴍᴘʀᴇssᴏʀ Bᴏᴛ\n\nYᴏᴜ Cᴀɴ Eɴᴄᴏᴅᴇ (ᴏʀ) Cᴏᴍᴘʀᴇss Vɪᴅᴇᴏs Fʀᴏᴍ Tʜɪs Bᴏᴛ\n\nCʜᴇᴄᴋ Hᴇʟᴘ Bᴜᴛᴛᴏɴ Fᴏʀ Mᴏʀᴇ Iɴꜰᴏ\n\nPᴏᴡᴇʀᴇᴅ Bʏ : @AIOM_BOTS**',
                      buttons=[[
                         Button.inline("Hᴇʟᴘ", data="plugins"),
                         Button.inline("Aʙᴏᴜᴛ", data="about")],
                         [
                         Button.inline("Cʟᴏsᴇ", data="close")]])
    tag = f'[{event.sender.first_name}](tg://user?id={event.sender_id})'
    await Drone.send_message(int(ACCESS_CHANNEL), f'{tag} Started The BOT')

@Drone.on(events.callbackquery.CallbackQuery(data="plugins"))
async def plugins(event):
    await event.edit(f'{help_text}',
                    buttons=[[
                         Button.inline("Sᴇᴛ Tʜᴜᴍʙ", data="sett"),
                         Button.inline("Rᴇᴍ Tʜᴜᴍʙ", data='remt')],
                        [Button.inline("Hᴏᴍᴇ", data="home"),
                         Button.inline("Aʙᴏᴜᴛ", data="about")],
                         [
                         Button.inline("Cʟᴏsᴇ", data="close")]])

@Drone.on(events.callbackquery.CallbackQuery(data="home"))
async def home(event):
    await event.edit(f'**Hᴇʟʟᴏ 👋 [{event.sender.first_name}](tg://user?id={event.sender_id}),\n\nTʜɪs Is A Hɪɢʜ Eꜰꜰɪᴄɪᴇɴᴄʏ Vɪᴅᴇᴏ Cᴏᴍᴘʀᴇssᴏʀ Bᴏᴛ\n\nYᴏᴜ Cᴀɴ Eɴᴄᴏᴅᴇ (ᴏʀ) Cᴏᴍᴘʀᴇss Vɪᴅᴇᴏs Fʀᴏᴍ Tʜɪs Bᴏᴛ\n\nCʜᴇᴄᴋ Hᴇʟᴘ Bᴜᴛᴛᴏɴ Fᴏʀ Mᴏʀᴇ Iɴꜰᴏ\n\nPᴏᴡᴇʀᴇᴅ Bʏ : @AIOM_BOTS**',
                    buttons=[[
                         Button.inline("Hᴇʟᴘ", data="plugins"),
                         Button.inline("Aʙᴏᴜᴛ", data="about")],
                         [
                         Button.inline("Cʟᴏsᴇ", data="close")]])

@Drone.on(events.callbackquery.CallbackQuery(data="about"))
async def about(event):
    await event.edit(f'{about_text}',
                    buttons=[[
                         Button.inline("Hᴇʟᴘ", data="plugins"),
                         Button.inline("Hᴏᴍᴇ", data="home")],
                         [
                         Button.inline("Cʟᴏsᴇ", data="close")]])

@Drone.on(events.callbackquery.CallbackQuery(data="close"))
async def about(event):
    await event.delete()

##--------------------------------------------------------------------------##
                   
 #-----------------------------------------------------------------------------------------------                            
    
@Drone.on(events.callbackquery.CallbackQuery(data="sett"))
async def sett(event):    
    button = await event.get_message()
    msg = await button.get_reply_message() 
    await event.delete()
    async with Drone.conversation(event.chat_id) as conv: 
        xx = await conv.send_message("Send me any image for thumbnail as a `reply` to this message.")
        x = await conv.get_reply()
        if not x.media:
            xx.edit("No media found.")
        mime = x.file.mime_type
        if not 'png' in mime:
            if not 'jpg' in mime:
                if not 'jpeg' in mime:
                    return await xx.edit("No image found.")
        await set_thumbnail(event, x.media)
        await xx.delete()
        
@Drone.on(events.callbackquery.CallbackQuery(data="remt"))
async def remt(event):  
    await event.delete()
    await rem_thumbnail(event)
    
@Drone.on(events.callbackquery.CallbackQuery(data="restart"))
async def res(event):
    if not f'{event.sender_id}' == f'{int(AUTH_USERS)}':
        return await event.edit("Only authorized user can restart!")
    result = await heroku_restart()
    if result is None:
        await event.edit("You have not filled `HEROKU_API` and `HEROKU_APP_NAME` vars.")
    elif result is False:
        await event.edit("An error occured!")
    elif result is True:
        await event.edit("Restarting app, wait for a minute.")
