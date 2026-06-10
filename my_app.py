import streamlit as st
import pandas as pd
from datetime import datetime

# 1. إعدادات الصفحة الأساسية
st.set_page_config(page_title="My Professional Hub", page_icon="💎", layout="wide")

# 2. نظام إدارة اللغة (Language Settings)
if 'lang' not in st.session_state:
    st.session_state.lang = 'English'

with st.sidebar:
    st.header("⚙️ Configuration")
    lang_choice = st.selectbox("Language / اللغة", ["English", "العربية"])
    if lang_choice == "العربية":
        st.session_state.lang = 'Arabic'
    else:
        st.session_state.lang = 'English'
    
    st.markdown("---")
    st.caption("Custom Suite v2.6 🚀")

# القاموس الخاص بالترجمة لبرامجك بالظبط
TEXTS = {
    'English': {
        'title': "💎 My Custom Application Suite",
        'subtitle': "Live production environment for your custom-built applications.",
        'tab1': "📊 Walk-In Logger Pro",
        'tab2': "🎒 Repair Bag Pro Edition",
        'tab3': "👑 Sovereign Gold Calculator",
        'counter_title': "Customer Traffic & Conversion Tracker",
        'total_today': "Total Walk-In Customers",
        'add_customer': "Log New Walk-In",
        'export_data': "Traffic Analytics Logs",
        'repair_title': "Repair Bag Pro Registry",
        'add_job': "Register New Job Ticket",
        'item_name': "Bag / Item Description",
        'issue': "Repair & Service Required",
        'cost': "Service Charge ($)",
        'status': "Job Status",
        'save_job': "Commit Ticket to Registry",
        'current_jobs': "Active Repair Tickets",
        'calc_title': "Sovereign Gold & Gram Valuation",
        'gold_weight': "Gold Weight (Grams)",
        'gold_karat': "Karat Selection",
        'gold_price_gram': "Current Gold Price per Gram ($)",
        'craftmanship': "Craftsmanship Fees per Gram ($)",
        'calc_btn': "Calculate Sovereign Value",
        'total_value': "Total Valuation",
        'footer': "© 2026 Developer Portfolio Hub. All tools are fully operational."
    },
    'Arabic': {
        'title': "💎 حزمة التطبيقات المخصصة الخاصة بي",
        'subtitle': "بيئة عمل حية ومباشرة لتطبيقاتك الذكية.",
        'tab1': "📊 Walk-In Logger Pro",
        'tab2': "🎒 Repair Bag Pro Edition",
        'tab3': "👑 Sovereign Gold Calculator",
        'counter_title': "متابع حركة وتدفق الزبائن",
        'total_today': "إجمالي الزوار اليوم",
        'add_customer': "تسجيل دخول زبون جديد",
        'export_data': "سجل تحليلات حركة الزوار",
        'repair_title': "سجل نظام Repair Bag Pro",
        'add_job': "فتح تذكرة صيانة جديدة",
        'item_name': "وصف الحقيبة / القطعة",
        'issue': "الخدمة أو التصليح المطلوب",
        'cost': "تكلفة الخدمة والتصليح",
        'status': "حالة الطلب الحالية",
        'save_job': "حفظ التذكرة في السجل",
        'current_jobs': "تذاكر الصيانة النشطة الآن",
        'calc_title': "حسابة الذهب الملكية والأوزان",
        'gold_weight': "وزن الذهب (بالجرام)",
        'gold_karat': "عيار الذهب",
        'gold_price_gram': "سعر جرام الذهب الحالي",
        'craftmanship': "مصنعية الجرام الواحد",
        'calc_btn': "احسب القيمة الإجمالية",
        'total_value': "التقييم المالي الإجمالي",
        'footer': "© 2026 مساحة عمل المطور. جميع التطبيقات تعمل بكفاءة."
    }
}

L = TEXTS[st.session_state.lang]

# عنوان المنصة الرئيسي
st.title(L['title'])
st.markdown(f"*{L['subtitle']}*")
st.markdown("---")

# 3. تهيئة الـ Session State لحفظ بيانات برامجك أثناء التنقل
if 'customer_count' not in st.session_state:
    st.session_state.customer_count = 0
if 'traffic_log' not in st.session_state:
    st.session_state.traffic_log = []
if 'repair_bags' not in st.session_state:
    st.session_state.repair_bags = [
        {"Ticket ID": 501, "Item": "Leather Handbag", "Service Required": "Zipper & Stitching Repair", "Charge": 45.0, "Status": "In Progress"},
        {"Ticket ID": 502, "Item": "Travel Backpack", "Service Required": "Strap Reinforcement", "Charge": 25.0, "Status": "Completed"}
    ]

# 4. إنشاء التبويبات بالأسماء الصحيحة لبرامجك
tab1, tab2, tab3 = st.tabs([L['tab1'], L['tab2'], L['tab3']])

# ==========================================
# التبويب الأول: Walk-In Logger Pro
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
            st.caption("No traffic logged yet today." if st.session_state.lang == 'English' else "لم يتم تسجيل أي حركة دخول بعد.")

# ==========================================
# التبويب الثاني: Repair Bag Pro Edition
# ==========================================
with tab2:
    st.header(L['repair_title'])
    
    with st.expander(f"🎒 {L['add_job']}"):
        with st.form("repair_bag_form", clear_on_submit=True):
            item = st.text_input(L['item_name'])
            issue = st.text_area(L['issue'])
            cost = st.number_input(L['cost'], min_value=0.0, step=5.0)
            status = st.selectbox(L['status'], ["Pending", "In Progress", "Completed"] if st.session_state.lang == 'English' else ["معلق", "قيد العمل", "تم التسليم"])
            
            submitted = st.form_submit_button(L['save_job'])
            if submitted and item:
                new_id = 501 + len(st.session_state.repair_bags)
                st.session_state.repair_bags.append({
                    "Ticket ID": new_id, "Item": item, "Service Required": issue, "Charge": cost, "Status": status
                })
                st.success("Ticket added to Repair Bag Pro!" if st.session_state.lang == 'English' else "تمت إضافة التذكرة بنجاح لـ Repair Bag Pro!")
                st.rerun()

    st.subheader(L['current_jobs'])
    if st.session_state.repair_bags:
        df_bags = pd.DataFrame(st.session_state.repair_bags)
        st.dataframe(df_bags, use_container_width=True, hide_index=True)
    else:
        st.caption("No active tickets found.")

# ==========================================
# التبويب الثالث: Sovereign Gold Calculator
# ==========================================
with tab3:
    st.header(L['calc_title'])
    
    col_g1, col_g2 = st.columns(2)
    with col_g1:
        weight = st.number_input(L['gold_weight'], min_value=0.0, step=0.1, format="%.2f")
        karat = st.selectbox(L['gold_karat'], ["24K", "22K", "21K", "18K"])
        base_price = st.number_input(L['gold_price_gram'], min_value=0.0, step=1.0)
        craft = st.number_input(L['craftmanship'], min_value=0.0, step=0.5)
        
        # معادلة حساب قيمة الذهب بناءً على العيار والمصنعية
        if st.button(L['calc_btn'], type="primary", use_container_width=True):
            # معاملات تحويل العيار بالنسبة لعيار 24
            karat_factors = {"24K": 1.0, "22K": 22/24, "21K": 21/24, "18K": 18/24}
            factor = karat_factors[karat]
            
            # الحسبة الملكية لجرام الذهب بالمصنعية
            total_valuation = weight * ((base_price * factor) + craft)
            st.session_state.gold_result = total_valuation

    with col_g2:
        if 'gold_result' in st.session_state:
            st.toast("Gold Valuation Updated!")
            st.metric(label=L['total_value'], value=f"${st.session_state.gold_result:,.2f}")
            
            # تفاصيل الحسبة الصغيرة
            st.caption(f"Calculation Basis: {weight}g of {karat} Gold with ${craft}/g craftsmanship.")

# تذييل الصفحة
st.markdown("---")
st.markdown(f"<p style='text-align: center; color: gray;'>{L['footer']}</p>", unsafe_allow_html=True)
