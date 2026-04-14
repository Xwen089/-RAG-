#基于Stramlit完成web网页上传服务

import streamlit as st

#添加网页标题
st.title("知识库更新服务")

# file_uploader组件，允许用户上传文件
uploaded_file = st.file_uploader(
    "上传文件", type=["pdf", "txt", "docx"]
)

if uploaded_file is not None:
    #提取文件信息
    file_details = {
        "filename": uploaded_file.name,
        "filetype": uploaded_file.type,
        "filesize": uploaded_file.size
    }  

    st.subheader(f"文件名：{file_details['filename']}")
    st.write(f"格式：{file_details['filetype']}")
    st.write(f"大小：{file_details['filesize']} bytes")

    #获取文件内容
    
    #txt格式：
    #text = uploaded_file.getvalue().decode("utf-8")
    #st.write(text[:500])
   
    #pdf格式：
    import pdfplumber
    import io
    #按页拆分PDF文本
    pages_text = []

    with pdfplumber.open(io.BytesIO(uploaded_file.getvalue())) as pdf:
        for page in pdf.pages:
            pages_text.append(page.extract_text())

    total_pages = len(pages_text)
    st.success(f"总页数：{total_pages}")
    #展示第一页内容
    st.write(pages_text[0][:500])

        
