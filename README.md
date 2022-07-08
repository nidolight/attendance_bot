## 퀘이사존 출석체크봇

자체적으로 [Cloudflare](https://www.cloudflare.com/ko-kr/)의 anti-bot page로 인해 일반적인 requests만으로는 우회가 어렵다.(javascript 구동 여부를 보고 차단: 403 forbidden 발생)

대안으로 `cfscrape`, `cloudscraper`등 전용 솔루션이 있지만 모두 실패

➡ 웹 브라우저의 동작을 직접 실행하는 `selenium`을 사용

리눅스의 스케줄 관리 프로그램 `crontab`을 사용하여 매일 9시15분 마다 실행
```sh
# path part
PATH=/usr/local/bin:/usr/bin:/bin:/usr/local/sbin:/usr/sbin:/sbin

# running part
15 9 * * * cd /home/ubuntu/quasarzoneAutoBot && sh runBot.sh
```

log는 `runBot.log`파일 뿐만 아니라 개인 블로그에도 업데이트 되도록 구성함

### Environments
- Ubuntu 20.04 Canonical
- Oracle Cloud Infrastructure
    - VM.Standard.A1.Flex(ARM64)
- VSCode - Remote SSH
