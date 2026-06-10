import streamlit as st
import pandas as pd
from datetime import datetime

# 1. إعدادات الصفحة الأساسية
st.set_page_config(page_title="My Work Hub", page_icon="💼", layout="wide")

# 2. نظام إدارة اللغة (Language Settings)
if 'lang' not in st.session_state:
    st.session_state.lang = 'English'

with st.sidebar:
    st.header("⚙️ Settings / الإعدادات")
    lang_choice = st.selectbox("Choose Language / اختر اللغة", ["English", "العربية"])
    if lang_choice == "العربية":
        st.session_state.lang = 'Arabic'
    else:
        st.session_state.lang = 'English'
    
    st.markdown("---")
    st.caption("Developed by You & Powered by Python 🚀")

# القاموس الخاص بالترجمة
TEXTS = {
    'English': {
        'title': "🛠️ My Executive Workspace",
        'subtitle': "All your essential business tools running in one place live.",
        'tab1': "📊 Walk-In Traffic Logger",
        'tab2': "🔧 Repair Tracker Pro",
        'tab3': "💰 Financial Calculator",
        'counter_title': "Customer Traffic Counter",
        'total_today': "Total Customers Today",
        'add_customer': "Log New Customer",
        'export_data': "View Logged Traffic Data",
        'repair_title': "Repair Jobs Management",
        'add_job': "Register New Repair Job",
        'item_name': "Item Name / Device",
        'issue': "Issue Description",
        'cost': "Estimated Cost ($)",
        'status': "Status",
        'save_job': "Save Job",
        'current_jobs': "Current Repair Registry",
        'calc_title': "Sales & Change Calculator",
        'bill_amount': "Total Bill Amount",
        'cash_paid': "Cash Received from Customer",
        'calc_btn': "Calculate Change",
        'change_due': "Change to Return to Customer",
        'insufficient': "Warning: Cash received is less than bill amount!",
        'footer': "© 2026 Work Hub. All tools are fully operational."
    },
    'Arabic': {
        'title': "🛠️ مساحة العمل التنفيذية",
        'subtitle': "جميع أدواتك الأساسية تعمل في مكان واحد وبشكل مباشر.",
        'tab1': "📊 عداد حركة الزبائن",
        'tab2': "🔧 مدير نظام التصليحات",
        'tab3': "💰 حـسّـابـة الـخـزنـة",
        'counter_title': "عداد تسجيل زوار المحل",
        'total_today': "إجمالي زبائن اليوم",
        'add_customer': "تسجيل زبون جديد (دخول)",
        'export_data': "عرض بيانات حركة الزبائن",
        'repair_title': "إدارة طلبات صيانة الأجهزة والتصليحات",
        'add_job': "تسجيل أمر تصليح جديد",
        'item_name': "اسم الجهاز / الشيء",
        'issue': "وصف العطل أو المشكلة",
        'cost': "التكلفة التقديرية",
        'status': "حالة الطلب",
        'save_job': "حفظ طلب التصليح",
        'current_jobs': "سجل عمليات التصليح الحالية",
        'calc_title': "حسابة المبيعات وباقي الفلوس",
        'bill_amount': "إجمالي قيمة الفاتورة",
        'cash_paid': "المبلغ المدفوع من الزبون",
        'calc_btn': "احسب الباقي",
        'change_due': "المبلغ المتبقي للزبون (الباقي)",
        'insufficient': "تنبيه: المبلغ المدفوع أقل من قيمة الفاتورة!",
        'footer': "© 2026 مساحة العمل. جميع الأدوات تعمل بكفاءة."
    }
}

L = TEXTS[st.session_state.lang]

# عنوان المنصة الرئيسي
st.title(L['title'])
st.p = st.markdown(f"*{L['subtitle']}*")
st.markdown("---")

# 3. تهيئة الـ Session State لحفظ البيانات مؤقتاً أثناء التصفح
if 'customer_count' not in st.session_state:
    st.session_state.customer_count = 0
if 'traffic_log' not in st.session_state:
    st.session_state.traffic_log = []
if 'repair_jobs' not in st.session_state:
    st.session_state.repair_jobs = [
        {"ID": 101, "Item": "iPhone 13 Pro", "Issue": "Screen Replacement", "Cost": 120, "Status": "In Progress"},
        {"ID": 102, "Item": "Dell Inspiron 15", "Issue": "Battery Swapping", "Cost": 65, "Status": "Completed"}
    ]

# 4. إنشاء التبويبات الثلاثة (Tabs)
tab1, tab2, tab3 = st.tabs([L['tab1'], L['tab2'], L['tab3']])

# ==========================================
# التبويب الأول: عداد الزباين (Walk-In Logger)
# ==========================================
with tab1:
    st.header(L['counter_title'])
    
    col1, col2 = st.columns(2)
    with col1:
        st.metric(label=L['total_today'], value=st.session_state.customer_count)
        if st.button(f"➕ {L['add_customer']}", use_container_width=True):
            st.session_state.customer_count += 1
            now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            st.session_state.traffic_log.append({"Customer No": st.session_state.customer_count, "Timestamp": now})
            st.rerun()
            
    with col2:
        st.subheader(L['export_data'])
        if st.session_state.traffic_log:
            df_traffic = pd.DataFrame(st.session_state.traffic_log)
            st.dataframe(df_traffic, use_container_width=True)
        else:
            st.caption("No traffic logged yet today." if st.session_state.lang == 'English' else "لم يتم تسجيل دخول زبائن بعد.")

# ==========================================
# التبويب الثاني: برنامج التصليحات (Repair Tracker)
# ==========================================
with tab2:
    st.header(L['repair_title'])
    
    # نموذج إضافة عملية تصليح جديدة
    with st.expander(f"➕ {L['add_job']}"):
        with st.form("repair_form", clear_on_submit=True):
            item = st.text_input(L['item_name'])
            issue = st.text_area(L['issue'])
            cost = st.number_input(L['cost'], min_value=0.0, step=5.0)
            status = st.selectbox(L['status'], ["Pending", "In Progress", "Completed"] if st.session_state.lang == 'English' else ["معلق", "قيد التصليح", "تم التجهيز"])
            
            submitted = st.form_submit_button(L['save_job'])
            if submitted and item:
                new_id = 101 + len(st.session_state.repair_jobs)
                st.session_state.repair_jobs.append({
                    "ID": new_id, "Item": item, "Issue": issue, "Cost": cost, "Status": status
                })
                st.success("Job Saved Successfully!" if st.session_state.lang == 'English' else "تم حفظ طلب التصليح بنجاح!")
                st.rerun()

    # عرض جدول عمليات التصليح الحالية
    st.subheader(L['current_jobs'])
    if st.session_state.repair_jobs:
        df_repairs = pd.DataFrame(st.session_state.repair_jobs)
        st.dataframe(df_repairs, use_container_width=True, hide_index=True)
    else:
        st.caption("No repair jobs recorded.")

# ==========================================
# التبويب الثالث: برنامج الحسابة (Financial Calculator)
# ==========================================
with tab3:
    st.header(L['calc_title'])
    
    col_c1, col_c2 = st.columns(2)
    with col_c1:
        bill = st.number_input(L['bill_amount'], min_value=0.0, step=1.0, key="bill_in")
        cash = st.number_input(L['cash_paid'], min_value=0.0, step=1.0, key="cash_in")
        
        if st.button(L['calc_btn'], type="primary", use_container_width=True):
            if cash >= bill:
                change = cash - bill
                st.session_state.computed_change = change
                st.session_state.insufficient_funds = False
            else:
                st.session_state.computed_change = None
                st.session_state.insufficient_funds = True

    with col_c2:
        if 'computed_change' in st.session_state and st.session_state.computed_change is not None:
            st.toast("Calculation complete!" if st.session_state.lang == 'English' else "تم الحساب!")
            st.metric(label=L['change_due'], value=f"{st.session_state.computed_change:.2f}")
        elif 'insufficient_funds' in st.session_state and st.session_state.insufficient_funds:
            st.error(L['insufficient'])

# تذييل الصفحة الرسمي للموقع
st.markdown("---")
st.markdown(f"<p style='text-align: center; color: gray;'>{L['footer']}</p>", unsafe_allow_html=True)
