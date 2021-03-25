from PIL import Image
import os, time, discord

async def badapple(self,message):

    async def createMessage():
        text = ""
        for x in range(48):
            text += "#" * 36 + "\n"
        return await message.channel.send(text)
        return message.get

    def imgtoText(count):
        baseImage = Image.open(folder + "/" + f"{count}.jpg")
        baseImage = baseImage.resize((48, 36))
        baseImage = baseImage.convert("L")
        baseImage = baseImage.rotate(90)
        final = ""
        for x in range(6,42):
            for y in range(36):
                if baseImage.getpixel((x,y)): final = final + " "
                else: final = final + "#"
            final += "\n"
        return final

    folder = "Y:/WINDOWS/__Programming__/Python Programs/opencv-python/bad_apple"
    files = os.listdir(folder)
    count = 0

    toEdit = await createMessage()

    for images in files:
        text = imgtoText(count)
        count += 4
        await toEdit.edit(content=text)
