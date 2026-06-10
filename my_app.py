import streamlit as st

# إعدادات الصفحة الأساسية
st.set_page_config(page_title="My Portfolio", page_icon="🚀", layout="centered")

# بيانات مشاريعك
PROJECTS = [
    {
        "title": "Project Sovereign Engine",
        "description": "An offline fantasy world simulator and story-generation engine utilizing custom narrative logic and database management.",
        "tag": "Python & Simulation"
    },
    {
        "title": "Walk-In Logger Pro Edition",
        "description": "A comprehensive customer traffic and retail sales conversion tracking tool with automated Excel report exporting.",
        "tag": "Desktop App & Automation"
    },
    {
        "title": "Diamond Archive Application",
        "description": "A specialized inventory and certificate system integrated with SQLite for tracking serial numbers and managing storage labels.",
        "tag": "Database & Logistics"
    }
]

# رأس الصفحة (Header)
st.title("Welcome to My Portfolio")
st.subheader("A showcase of my latest projects, tools, and developer journey")
st.markdown("---")

# عرض المشاريع
st.header("Featured Projects")

# عمل تصميم على شكل كروت للمشاريع
for project in PROJECTS:
    with st.container():
        # تصميم يشبه الكارت
        st.markdown(f"### {project['title']}")
        st.caption(f"🔹 Tag: {project['tag']}")
        st.write(project['description'])
        st.markdown("---")

# تذييل الصفحة (Footer)
st.markdown("<p style='text-align: center; color: gray;'>&copy; 2026 Developer Portfolio. Built entirely with Python & Streamlit.</p>", unsafe_allow_html=True)
