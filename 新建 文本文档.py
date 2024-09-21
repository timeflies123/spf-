from docx import Document

# 创建一个新的文档对象
doc = Document()

# 添加一个段落，并写入内容 '11'
doc.add_paragraph('11')

# 保存文档
doc.save('asdads.docx')