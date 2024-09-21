**本项目用于安全研究，更好的服务网络安全,由使用者造成的危害与本人无关**  
本项目通过直接向目标邮箱发送邮件的方式来检验spf邮件漏洞是否存在，同时加入了批量检测和半自动化书写报告的功能。  
**语言：  
python3.x  
使用python库
argparse  
os  
python-docx**  
脚本使用方法：  
`参数  
-h 使用方法  
-d 域名  
-f 指定域名文件   
-e 指定发送邮箱`  
单域名使用  
`python spf.py -d 域名 -e 邮箱`   
多域名使用  
`python spf.py -f 文件 -e 邮箱`  
运行上述命令后如果存在spf邮件伪造漏洞将会直接可以在指定邮箱收到一封 发件人为test@域名 的测试邮件  
不管有没有该漏洞在本地将会生成文件名为"xxx.com存在spf邮件伪造漏洞.docx"
内容为：  
在一台linux主机上运行swaks --body "内容" --header "Subject:标题" -t 自己的163邮箱 -f "test@域名"   
查看邮箱发现已经收到  
[此处加入图片]  
危害：欺诈和钓鱼攻击：攻击者可以利用SPF漏洞伪造合法的发件人地址，从而进行欺诈或钓鱼攻击，诱使用户提供敏感信息，如账户密码、信用卡信息等。
品牌信誉损害：通过伪造的邮件，攻击者可能会冒充知名公司或机构，进行虚假宣传或传播恶意软件，损害受害企业的品牌声誉。
邮件丢失或延迟：伪造邮件可能会被错误地标记为垃圾邮件或被拦截，导致正常的邮件通信受到影响，特别是在邮件服务器对SPF验证的处理不当时。
安全漏洞利用：攻击者可能通过伪造的邮件引导受害者访问恶意网站或下载恶意软件，从而进一步感染用户设备或网络，造成更大的安全隐患。
难以追踪：SPF伪造攻击可能使追踪邮件源变得更加困难，从而增加调查和防御的复杂性。  
补充图片即可提交安全报告  
有些使用者可能不方便导出文件，为了使用便利，在命令行同样会打印报告的标题和内容  
**本脚本无论是否存在漏洞都会在本地生成文件，请使用者认真鉴别**
