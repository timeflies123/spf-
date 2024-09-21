import argparse
import os
from docx import Document

def read_domains_from_file(file_path):
    """ 从指定的文件中读取域名。 """
    if not os.path.isfile(file_path):
        print(f"错误：文件 {file_path} 不存在。")
        return []

    with open(file_path, 'r') as file:
        domains = [line.strip() for line in file.readlines()]
    return domains

def print_usage():
    """ 打印使用方式。 """
    print("""
使用方法：
python script.py [-d DOMAIN] [-e EMAIL] [-f FILE] [-h]

选项：
  -d DOMAIN     指定单个域名。
  -e EMAIL      输入邮箱。
  -f FILE       从文本文件中读取域名，每行一个域名。
  -h            查看使用方式。
    """)

def main():
    parser = argparse.ArgumentParser(add_help=False)

    # 添加参数
    parser.add_argument('-d', '--domain', type=str, help='指定单个域名')
    parser.add_argument('-e', '--email', type=str, help='输入邮箱')
    parser.add_argument('-f', '--file', type=str, help='从文本文件中读取域名')
    parser.add_argument('-h', '--help', action='store_true', help='查看使用方式')

    args = parser.parse_args()

    # 处理 -h 参数
    if args.help:
        print_usage()
        return

    email = args.email
    if args.domain:
        domains = [args.domain]
    elif args.file:
        domains = read_domains_from_file(args.file)
    else:
        domains = []

    if email:
        if domains:

            for domain in domains:
                cmd = f'swaks --body "内容" --header "Subject:标题" -t {email} -f "test@{domain}" > /dev/null 2>&1'
                os.system(cmd)
                content = (
    '在一台linux主机上运行swaks --body "内容" --header "Subject:标题" -t 自己的163邮箱 -f "test@{0}" \n查看邮箱发现已经收到\n[此处加入图片]\n'
    '危害：欺诈和钓鱼攻击：攻击者可以利用SPF漏洞伪造合法的发件人地址，从而进行欺诈或钓鱼攻击，诱使用户提供敏感信息，如账户密码、信用卡信息等。\n'
    '品牌信誉损害：通过伪造的邮件，攻击者可能会冒充知名公司或机构，进行虚假宣传或传播恶意软件，损害受害企业的品牌声誉。\n'
    '邮件丢失或延迟：伪造邮件可能会被错误地标记为垃圾邮件或被拦截，导致正常的邮件通信受到影响，特别是在邮件服务器对SPF验证的处理不当时。\n'
    '安全漏洞利用：攻击者可能通过伪造的邮件引导受害者访问恶意网站或下载恶意软件，从而进一步感染用户设备或网络，造成更大的安全隐患。\n'
    '难以追踪：SPF伪造攻击可能使追踪邮件源变得更加困难，从而增加调查和防御的复杂性。'
).format(domain)
                
                title='{0}存在spf邮件伪造漏洞'.format(domain)
                print(domain+"报告:\n")
                print('报告文件名：'+title)
                print()
                print(content)
                print()
                doc = Document()
                doc.add_paragraph(content)
                title='{0}存在spf邮件伪造漏洞.docx'.format(domain)
                doc.save(title)
              
        else:
            print('没有提供域名。')
    else:
        print('没有提供邮箱。')

if __name__ == "__main__":
    main()