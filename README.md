# fancify-text

_(Thanks to @nottrobin for the original library)_

Convert text into a fancier unicode representation, picking from the following fonts:

𝗌𝖺𝗇𝗌𝖲𝖾𝗋𝗂𝖿 - 𝖳𝗁𝖾 𝗊𝗎𝗂𝖼𝗄 𝖻𝗋𝗈𝗐𝗇 𝖿𝗈𝗑 𝗃𝗎𝗆𝗉𝗌 𝗈𝗏𝖾𝗋 𝗍𝗁𝖾 𝗅𝖺𝗓𝗒 𝖽𝗈𝗀. 𝟢𝟣𝟤𝟥𝟦𝟧𝟨𝟩𝟪𝟫  
𝗯𝗼𝗹𝗱 - 𝗧𝗵𝗲 𝗾𝘂𝗶𝗰𝗸 𝗯𝗿𝗼𝘄𝗻 𝗳𝗼𝘅 𝗷𝘂𝗺𝗽𝘀 𝗼𝘃𝗲𝗿 𝘁𝗵𝗲 𝗹𝗮𝘇𝘆 𝗱𝗼𝗴. 𝟬𝟭𝟮𝟯𝟰𝟱𝟲𝟳𝟴𝟵  
𝘪𝘵𝘢𝘭𝘪𝘤 - 𝘛𝘩𝘦 𝘲𝘶𝘪𝘤𝘬 𝘣𝘳𝘰𝘸𝘯 𝘧𝘰𝘹 𝘫𝘶𝘮𝘱𝘴 𝘰𝘷𝘦𝘳 𝘵𝘩𝘦 𝘭𝘢𝘻𝘺 𝘥𝘰𝘨. 0123456789  
𝙗𝙤𝙡𝙙𝙄𝙩𝙖𝙡𝙞𝙘 - 𝙏𝙝𝙚 𝙦𝙪𝙞𝙘𝙠 𝙗𝙧𝙤𝙬𝙣 𝙛𝙤𝙭 𝙟𝙪𝙢𝙥𝙨 𝙤𝙫𝙚𝙧 𝙩𝙝𝙚 𝙡𝙖𝙯𝙮 𝙙𝙤𝙜. 𝟬𝟭𝟮𝟯𝟰𝟱𝟲𝟳𝟴𝟵  
𝚖𝚘𝚗𝚘𝚜𝚙𝚊𝚌𝚎𝚍 - 𝚃𝚑𝚎 𝚚𝚞𝚒𝚌𝚔 𝚋𝚛𝚘𝚠𝚗 𝚏𝚘𝚡 𝚓𝚞𝚖𝚙𝚜 𝚘𝚟𝚎𝚛 𝚝𝚑𝚎 𝚕𝚊𝚣𝚢 𝚍𝚘𝚐. 𝟶𝟷𝟸𝟹𝟺𝟻𝟼𝟽𝟾𝟿  
ｗｉｄｅ － Ｔｈｅ ｑｕｉｃｋ ｂｒｏｗｎ ｆｏｘ ｊｕｍｐｓ ｏｖｅｒ ｔｈｅ ｌａｚｙ ｄｏｇ． ０１２３４５６７８９ （ｓｕｐｐｏｒｔｓ ａｌｌ ｏｆ ＡＳＣＩＩ）  
𝐛𝐨𝐥𝐝𝐒𝐞𝐫𝐢𝐟 - 𝐓𝐡𝐞 𝐪𝐮𝐢𝐜𝐤 𝐛𝐫𝐨𝐰𝐧 𝐟𝐨𝐱 𝐣𝐮𝐦𝐩𝐬 𝐨𝐯𝐞𝐫 𝐭𝐡𝐞 𝐥𝐚𝐳𝐲 𝐝𝐨𝐠. 𝟎𝟏𝟐𝟑𝟒𝟓𝟔𝟕𝟖𝟗  
𝑖𝑡𝑎𝑙𝑖𝑐𝑆𝑒𝑟𝑖𝑓 - 𝑇𝒉𝑒 𝑞𝑢𝑖𝑐𝑘 𝑏𝑟𝑜𝑤𝑛 𝑓𝑜𝑥 𝑗𝑢𝑚𝑝𝑠 𝑜𝑣𝑒𝑟 𝑡𝒉𝑒 𝑙𝑎𝑧𝑦 𝑑𝑜𝑔. 𝟎𝟏𝟐𝟑𝟒𝟓𝟔𝟕𝟖𝟗  
𝒃𝒐𝒍𝒅𝑰𝒕𝒂𝒍𝒊𝒄𝑺𝒆𝒓𝒊𝒇 - 𝑻𝒉𝒆 𝒒𝒖𝒊𝒄𝒌 𝒃𝒓𝒐𝒘𝒏 𝒇𝒐𝒙 𝒋𝒖𝒎𝒑𝒔 𝒐𝒗𝒆𝒓 𝒕𝒉𝒆 𝒍𝒂𝒛𝒚 𝒅𝒐𝒈. 𝟎𝟏𝟐𝟑𝟒𝟓𝟔𝟕𝟖𝟗  
𝕕𝕠𝕦𝕓𝕝𝕖𝕊𝕥𝕣𝕦𝕔𝕜 - 𝕋𝕙𝕖 𝕢𝕦𝕚𝕔𝕜 𝕓𝕣𝕠𝕨𝕟 𝕗𝕠𝕩 𝕛𝕦𝕞𝕡𝕤 𝕠𝕧𝕖𝕣 𝕥𝕙𝕖 𝕝𝕒𝕫𝕪 𝕕𝕠𝕘. 𝟘𝟙𝟚𝟛𝟜𝟝𝟞𝟟𝟠𝟡  
𝓼𝓬𝓻𝓲𝓹𝓽 - 𝓣𝓱𝓮 𝓺𝓾𝓲𝓬𝓴 𝓫𝓻𝓸𝔀𝓷 𝓯𝓸𝔁 𝓳𝓾𝓶𝓹𝓼 𝓸𝓿𝓮𝓻 𝓽𝓱𝓮 𝓵𝓪𝔃𝔂 𝓭𝓸𝓰. 0123456789  
𝔣𝔯𝔞𝔨𝔱𝔲𝔯 - 𝔗𝔥𝔢 𝔮𝔲𝔦𝔠𝔨 𝔟𝔯𝔬𝔴𝔫 𝔣𝔬𝔵 𝔧𝔲𝔪𝔭𝔰 𝔬𝔳𝔢𝔯 𝔱𝔥𝔢 𝔩𝔞𝔷𝔶 𝔡𝔬𝔤. 0123456789  
𝖇𝖔𝖑𝖉𝕱𝖗𝖆𝖐𝖙𝖚𝖗 - 𝕿𝖍𝖊 𝖖𝖚𝖎𝖈𝖐 𝖇𝖗𝖔𝖜𝖓 𝖋𝖔𝖝 𝖏𝖚𝖒𝖕𝖘 𝖔𝖛𝖊𝖗 𝖙𝖍𝖊 𝖑𝖆𝖟𝖞 𝖉𝖔𝖌. 0123456789  
blue - 🇹​🇭​🇪​ ​🇶​🇺​🇮​🇨​🇰​ ​🇧​🇷​🇴​🇼​🇳​ ​🇫​🇴​🇽​ ​🇯​🇺​🇲​🇵​🇸​ ​🇴​🇻​🇪​🇷​ ​🇹​🇭​🇪​ ​🇱​🇦​🇿​🇾​ ​🇩​🇴​🇬​.​ ​0​1​2​3​4​5​6​7​8​9​  
squared - 🅃🄷🄴 🅀🅄🄸🄲🄺 🄱🅁🄾🅆🄽 🄵🄾🅇 🄹🅄🄼🄿🅂 🄾🅅🄴🅁 🅃🄷🄴 🄻🄰🅉🅈 🄳🄾🄶. 0123456789  
ⓒⓘⓡⓒⓛⓔⓓ - Ⓣⓗⓔ ⓠⓤⓘⓒⓚ ⓑⓡⓞⓦⓝ ⓕⓞⓧ ⓙⓤⓜⓟⓢ ⓞⓥⓔⓡ ⓣⓗⓔ ⓛⓐⓩⓨ ⓓⓞⓖ. ⓪①②③④⑤⑥⑦⑧⑨  
sᴍᴀʟʟCᴀᴘs - Tʜᴇ ǫᴜɪᴄᴋ ʙʀᴏᴡɴ ғᴏx ᴊᴜᴍᴘs ᴏᴠᴇʀ ᴛʜᴇ ʟᴀᴢʏ ᴅᴏɢ. 0123456789  
curly - ɬɧɛ զųıƈƙ ცཞơῳŋ ʄơҳ ʝųɱ℘ʂ ơ۷ɛཞ ɬɧɛ Ɩąʑყ ɖơɠ. 0123456789  
reversed (reversed_ in python) - 9876543210 .ວOᗡ YZA⅃ ƎHT ЯƎVO ƧꟼMUᒐ XOꟻ ИWOЯᗺ ꓘƆIUϘ ƎHT  
upsideDown - 9876543210 ˙ƃop ʎzɐן ǝɥʇ ɹǝʌo sdɯnɾ xoɟ uʍoɹq ʞɔ!nb ǝɥ⊥  
boxed - 🆃🅷🅴 🆀🆄🅸🅲🅺 🅱🆁🅾🆆🅽 🅵🅾🆇 🅹🆄🅼🅿🆂 🅾🆅🅴🆁 🆃🅷🅴 🅻🅰🆉🆈 🅳🅾🅶. 0123456789  
wiry - ㄒ卄乇 Ɋㄩ丨匚Ҝ 乃尺ㄖ山几 千ㄖ乂 ﾌㄩ爪卩丂 ㄖᐯ乇尺 ㄒ卄乇 ㄥ卂乙ㄚ ᗪㄖᎶ. 0123456789  
⒫⒜⒭⒠⒩⒯⒣⒠⒮⒤⒵⒠⒟ - 🄣⒣⒠ ⒬⒰⒤⒞⒦ ⒝⒭⒪⒲⒩ ⒡⒪⒳ ⒥⒰⒨⒫⒮ ⒪⒱⒠⒭ ⒯⒣⒠ ⒧⒜⒵⒴ ⒟⒪⒢. 0123456789  
heavyCircled - 🅣🅗🅔 🅠🅤🅘🅒🅚 🅑🅡🅞🅦🅝 🅕🅞🅧 🅙🅤🅜🅟🅢 🅞🅥🅔🅡 🅣🅗🅔 🅛🅐🅩🅨 🅓🅞🅖. 0123456789  
currency - ₮H€ QUI¢₭ ₿RO₩₦ ₣OX JU₥₱$ OV€R ₮H€ £₳₴¥ ₫O₲. 0123456789  
cool - TᕼE ᑫᑌIᑕK ᗷᖇOᗯᑎ ᖴO᙭ ᒍᑌᗰᑭᔕ OᐯEᖇ TᕼE ᒪᗩᘔY ᗪOG. 0123456789  
magic - ƚԋҽ ϙυιƈƙ Ⴆɾσɯɳ ϝσx ʝυɱρʂ σʋҽɾ ƚԋҽ ʅαȥყ ԃσɠ. 0123456789  

## Installation

``` bash
pip3 install fancify-text
```

## Usage

### In Python

``` python3
>>> from fancify_text import bold, reversed_, heavyCircled, smallCaps  # Or any of the listed names above, or * to get all of them
>>> print(bold("hello world"))
𝗵𝗲𝗹𝗹𝗼 𝘄𝗼𝗿𝗹𝗱
>>> print(reversed_("hello world"))
ᗡ⅃ЯOW O⅃⅃ƎH
>>> print(heavyCircled("hello world"))
🅗🅔🅛🅛🅞 🅦🅞🅡🅛🅓
>>> print(smallCaps("Hello World")
Hᴇʟʟᴏ Wᴏʀʟᴅ
```

### From CLI

``` bash
$ fancify-bold "hello world"  # type the font name in all lowercase!
𝗵𝗲𝗹𝗹𝗼 𝘄𝗼𝗿𝗹𝗱
$ fancify-reversed "hello world"
ᗡ⅃ЯOW O⅃⅃ƎH
$ fancify-heavycircled "hello world"
🅗🅔🅛🅛🅞 🅦🅞🅡🅛🅓
$ fancify-smallcaps "hello world"
Hᴇʟʟᴏ Wᴏʀʟᴅ
```

TODO: support modifiers from fontData.py
