# Fancify text

_(Code copied and modified from @secret-chest's https://github.com/Secret-chest/fancy-text)_

Convert text into a fancier unicode representation, picking from the following fonts:

- bold: 𝗵𝗲𝗹𝗹𝗼 𝘄𝗼𝗿𝗹𝗱
- italics: 𝘩𝘦𝘭𝘭𝘰 𝘸𝘰𝘳𝘭𝘥
- bolditalics: 𝙝𝙚𝙡𝙡𝙤 𝙬𝙤𝙧𝙡𝙙
- monospaced: ｈｅｌｌｏ　ｗｏｒｌｄ
- typewriter: 𝚑𝚎𝚕𝚕𝚘 𝚠𝚘𝚛𝚕𝚍
- serif: 𝐡𝐞𝐥𝐥𝐨 𝐰𝐨𝐫𝐥𝐝
- handwriting: 𝓱𝓮𝓵𝓵𝓸 𝔀𝓸𝓻𝓵𝓭
- formal: 𝖍𝖊𝖑𝖑𝖔 𝖜𝖔𝖗𝖑𝖉
- blue: 🇭 🇪 🇱 🇱 🇴 🇼 🇴 🇷 🇱 🇩
- squared: 🄷🄴🄻🄻🄾 🅆🄾🅁🄻🄳
- circled: 🅗🅔🅛🅛🅞 🅦🅞🅡🅛🅓
- smallcaps: ʜᴇʟʟᴏ ᴡᴏʀʟᴅ
- handwriting2: ᕼEᒪᒪO ᗯOᖇᒪᗪ
- reverse: ᗡ⅃ЯOW O⅃⅃ƎH
- upsidedown: ɥǝllo ʍoɹlp
- wiry: 卄乇ㄥㄥㄖ 山ㄖ尺ㄥᗪ
- script: 𝒽𝑒𝓁𝓁𝓅 𝓍𝓅𝓈𝓁𝒹
- outline: 𝕙𝕖𝕝𝕝𝕠 𝕨𝕠𝕣𝕝𝕕
- curly: ɧɛƖƖơ ῳơཞƖɖ
- apothecary: ɦεℓℓσ ωσ૨ℓ∂
- magic: ԋҽʅʅσ ɯσɾʅԃ
- magic2: ђєɭɭ๏ ฬ๏гɭ๔
- strange: ꫝꫀꪶꪶꪮ ᭙ꪮ𝕣ꪶᦔ
- parenthesized: 🄗🄔🄛🄛🄞 🄦🄞🄡🄛🄓
- boxed: 🅷🅴🅻🅻🅾 🆆🅾🆁🅻🅳

## Installation

``` bash
pip3 install fancify-text
```

## Usage in Python

``` python3
from fancify_text import bold  # Or any of the listed names above

print(bold("hello world"))
```

## Usage from CLI

``` bash
$ fancify-bold "hello world"
𝗵𝗲𝗹𝗹𝗼 𝘄𝗼𝗿𝗹𝗱
```
