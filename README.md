## ๐คํ์ด์ฌ์กด ์ถ์์ฒดํฌ๋ด

์์ฒด์ ์ผ๋ก [Cloudflare](https://www.cloudflare.com/ko-kr/)์ anti-bot page๋ก ์ธํด ์ผ๋ฐ์ ์ธ requests๋ง์ผ๋ก๋ ์ฐํ๊ฐ ์ด๋ ต๋ค.(javascript ๊ตฌ๋ ์ฌ๋ถ๋ฅผ ๋ณด๊ณ  ์ฐจ๋จ: 403 forbidden ๋ฐ์)

๋์์ผ๋ก `cfscrape`, `cloudscraper`๋ฑ ์ ์ฉ ์๋ฃจ์์ด ์์ง๋ง ๋ชจ๋ ์คํจ

โก ์น ๋ธ๋ผ์ฐ์ ์ ๋์์ ์ง์  ์คํํ๋ `selenium`์ ์ฌ์ฉ

๋ฆฌ๋์ค์ ์ค์ผ์ค ๊ด๋ฆฌ ํ๋ก๊ทธ๋จ `crontab`์ ์ฌ์ฉํ์ฌ ๋งค์ผ 09์15๋ถ ๋ง๋ค ์คํ
```sh
# path part
PATH=/usr/local/bin:/usr/bin:/bin:/usr/local/sbin:/usr/sbin:/sbin

# running part
15 9 * * * cd /home/ubuntu/quasarzoneAutoBot && sh runBot.sh
```

log๋ `runBot.log`ํ์ผ ๋ฟ๋ง ์๋๋ผ ๊ฐ์ธ ๋ธ๋ก๊ทธ์๋ ์๋ฐ์ดํธ ๋๋๋ก ๊ตฌ์ฑํจ

### Environments
- Ubuntu 20.04 Canonical
- Oracle Cloud Infrastructure
    - VM.Standard.A1.Flex(ARM64)
- VSCode - Remote SSH
