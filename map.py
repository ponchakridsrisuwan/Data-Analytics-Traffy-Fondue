import streamlit as st
import pandas as pd
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go

district_dataset = {
    "พระนคร": ['ชนะสงคราม', 'ตลาดยอด', 'บวรนิเวศ', 'บางขุนพรหม', 'บ้านพานถม', 'พระบรมมหาราชวัง', 'วังบูรพาภิรมย์', 'วัดราชบพิธ', 'วัดสามพระยา', 'ศาลเจ้าพ่อเสือ', 'สำราญราษฎร์', 'เสาชิงช้า'],
    "ดุสิต": ['ดุสิต', 'ถนนนครไชยศรี', 'วชิรพยาบาล', 'สวนจิตรลดา', 'สี่แยกมหานาค'],
    "หนองจอก": ['หนองจอก', 'กระทุ่มราย', 'คลองสิบ', 'คลองสิบสอง', 'คู้ฝั่งเหนือ', 'โคกแฝด', 'ลำต้อยติ่ง', 'ลำผักชี'],
    "บางรัก": ['บางรัก', 'มหาพฤฒาราม', 'สี่พระยา', 'สีลม', 'สุริยวงศ์'],
    "บางเขน": ['ท่าแร้ง', 'อนุสาวรีย์'],
    "บางกะปิ": ['คลองจั่น', 'หัวหมาก'],
    "ปทุมวัน": ['ปทุมวัน', 'รองเมือง', 'ลุมพินี', 'วังใหม่'],
    "ป้อมปราบศัตรูพ่าย": ['คลองมหานาค', 'บ้านบาตร', 'ป้อมปราบ', 'วัดเทพศิรินทร์', 'วัดโสมนัส'],
    "พระโขนง": ['บางจาก'],
    "มีนบุรี": ['มีนบุรี', 'แสนแสบ'],
    "ลาดกระบัง": ['ลาดกระบัง', 'ขุมทอง', 'คลองสองต้นนุ่น', 'คลองสามประเวศ', 'ทับยาว', 'ลำปลาทิว'],
    "ยานนาวา": ['ช่องนนทรี', 'บางโพงพาง'],
    "สัมพันธวงศ์": ['สัมพันธวงศ์', 'จักรวรรดิ', 'ตลาดน้อย'],
    "พญาไท": ['สามเสนใน'],
    "ธนบุรี": ['ดาวคะนอง', 'ตลาดพลู', 'บางยี่เรือ', 'บุคคโล', 'วัดกัลยาณ์', 'สำเหร่', 'หิรัญรูจี'],
    "บางกอกใหญ่": ['วัดท่าพระ', 'วัดอรุณ'],
    "ห้วยขวาง": ['ห้วยขวาง', 'บางกะปิ', 'สามเสนนอก'],
    "คลองสาน": ['คลองสาน', 'คลองต้นไทร', 'บางลำภูล่าง', 'สมเด็จเจ้าพระยา'],
    "ตลิ่งชัน": ['ตลิ่งชัน', 'คลองชักพระ', 'ฉิมพลี', 'บางเชือกหนัง', 'บางพรม', 'บางระมาด'],
    "บางกอกน้อย": ['บางขุนนนท์', 'บางขุนศรี', 'บ้านช่างหล่อ', 'ศิริราช', 'อรุณอมรินทร์'],
    "บางขุนเทียน": ['ท่าข้าม', 'แสมดำ'],
    "ภาษีเจริญ": ['คลองขวาง', 'คูหาสวรรค์', 'บางจาก', 'บางด้วน', 'บางแวก', 'บางหว้า', 'ปากคลองภาษีเจริญ'],
    "หนองแขม": ['หนองแขม', 'หนองค้างพลู'],
    "ราษฎร์บูรณะ": ['ราษฎร์บูรณะ', 'บางปะกอก'],
    "บางพลัด": ['บางพลัด', 'บางบำหรุ', 'บางยี่ขัน', 'บางอ้อ'],
    "ดินแดง": ['ดินแดง'],
    "บึงกุ่ม": ['คลองกุ่ม'],
    "สาทร": ['ทุ่งมหาเมฆ', 'ทุ่งวัดดอน', 'ยานนาวา'],
    "บางซื่อ": ['บางซื่อ'],
    "จตุจักร": ['จตุจักร', 'จอมพล', 'จันทรเกษม', 'ลาดยาว', 'เสนานิคม'],
    "บางคอแหลม": ['บางโคล่', 'บางคอแหลม', 'วัดพระยาไกร'],
    "ประเวศ": ['ดอกไม้', 'ประเวศ', 'หนองบอน'],
    "คลองเตย": ['คลองเตย', 'คลองตัน', 'พระโขนง'],
    "สวนหลวง": ['สวนหลวง'],
    "จอมทอง": ['จอมทอง', 'บางขุนเทียน', 'บางค้อ', 'บางมด'],
    "ดอนเมือง": ['สีกัน'],
    "ราชเทวี": ['ถนนเพชรบุรี', 'ถนนพญาไท', 'ทุ่งพญาไท', 'มักกะสัน'],
    "ลาดพร้าว": ['ลาดพร้าว', 'จรเข้บัว'],
    "วัฒนา": ['คลองเตยเหนือ', 'คลองตันเหนือ', 'พระโขนงเหนือ'],
    "บางแค": ['บางแค', 'บางแคเหนือ', 'บางไผ่', 'หลักสอง'],
    "หลักสี่": ['ตลาดบางเขน', 'ทุ่งสองห้อง'],
    "สายไหม": ['สายไหม', 'คลองถนน', 'ออเงิน'],
    "คันนายาว": ['คันนายาว'],
    "สะพานสูง": ['สะพานสูง'],
    "วังทองหลาง": ['วังทองหลาง'],
    "คลองสามวา": ['ทรายกองดิน', 'ทรายกองดินใต้', 'บางชัน', 'สามวาตะวันตก', 'สามวาตะวันออก'],
    "บางนา": ['บางนา'],
    "ทวีวัฒนา": ['ทวีวัฒนา', 'ศาลาธรรมสพน์'],
    "ทุ่งครุ": ['ทุ่งครุ', 'บางมด'],
    "บางบอน": ['บางบอน']
}

st.title("Data Analytics")
st.markdown(
    """
    สมาชิก
    - 63114540197 นายวรพล สุนทร 
    - 63114540210 นายวันเจริญ อุปมัย
    - 63114540424 นายพลชกฤษณ์ ศรีสุวรรณ์
    - 63114540554 นายฉัตรชัย แก้วฉุย
    """
)
st.markdown(
    """
    ข้อมูลจาก : https://www.traffy.in.th/?page_id=27351 
    - ระหว่าง : 1 กันยายน - 31 ตุลาคม 2565 
    - จำนวนข้อมูล : 30,000 แถว 20 คอลัมน์
    - Data Cleansing เหลือข้อมูล : 18,539 แถว 9 คอลัมน์ 
    - เทคนิคที่ใช้ในการ Data Cleansing : ลบค่า Missing value, ตัดคำ หรือ Tokenize, ลบ Emoji, ลบ Demoji ฯลฯ
    """)
st.markdown(
    """
    เป้าหมาย : 
    - หาประเภทการร้องเรียน จากประโยคที่ผู้ใช้กรอกเข้ามา เนื่องจากบางคนระบุประเภทและประโยคที่กรอกเข้ามาไม่ตรงกัน
    - Time Series Forecasting เพื่อหาและทำนายประเภทที่ผู้ใช้ร้องเรียนในแต่ละช่วงเวลา
    """)
st.markdown(
    """
    ประโยชน์ : 
    - ผู้บริหารหรือผู้ที่เกี่ยวข้อง สามารถดูได้ว่ามีคนร้องเรียนเรื่องใดในแต่ละช่วงเวลาใดบ้าง ช่วยให้สามารถวางแผนป้องกันและรับมือกับปัญหาได้ทันท่วงที
    """)


# load data
data = pd.read_csv("./dataset.csv")

st.markdown("### ข้อมูลการร้องเรียนในระบบ Traffy Fondue Data Table")
st.write(data)


st.markdown("### ประเภทการร้องเรียนในระบบ Traffy Fondue Map")
option = st.selectbox(
    'เลือกตัวเลือกการแสดง ?',
    ('word_df','district', 'subdistrict', 'status'))
st.write('คุณเลือก :', option)

fig = px.scatter_mapbox(
                        lon=data['longitude'],
                        lat=data['latitude'],
                        zoom=9,
                        color=data[option],
                        )
fig.update_layout(mapbox_style="open-street-map")
fig.update_layout(margin={"r": 0, "t": 50, "l": 0, "b": 10})
st.plotly_chart(fig, use_container_width=True)
         

st.markdown("### ประเภทการร้องเรียนในระบบ Traffy Fondue Bar Chart")
options = ['word_df']
fig = make_subplots(rows=1, cols=1)
for option in options:
    if option == 'word_df':
        for word_df in data['word_df'].unique():
            fig.add_trace(go.Histogram(x=data[data['word_df'] == word_df]['word_df'],
                                       y=data[data['word_df'] ==
                                              word_df]['word_df'],
                                       name=str(word_df)))
updatemenus = [{
    'buttons': [
        {
            'label': str(option),
            'method': 'update',
            'args': [{'visible': [option == opt for opt in options]},
                     {'title': option}]
        } for option in options
    ],
    'direction': 'down',
    'showactive': True,
    'x': 0.0,
    'xanchor': 'left',
    'y': 1.1,
    'yanchor': 'top'
},
    {
    'buttons': [
        {
            'label': str(date),
            'method': 'update',
            'args': [{'x': [data[(data[option] == selected_date) & (data['date'] == date)]
                                ['date'] for selected_date in data[option].unique()]},
                     {'title': f'ข้อมูล {option} จากวันที่ {date}'}]
        } for date in data['date'].unique()
    ],
    'direction': 'down',
        'showactive': True,
        'x': 0.2,
        'xanchor': 'left',
        'y': 1.1,
        'yanchor': 'top'
},

    {
        'buttons': [
            {
                'label': district,
                'method': 'update',
                'args': [{'x': [data[(data[option] == selected_district) & (data['district'] == district)]
                                ['district'] for selected_district in data[option].unique()]},
                         {'title': f'ข้อมูล {option} จากเขต {district}'}]
            } for district in data['district'].unique()
        ],
        'direction': 'down',
        'showactive': True,
        'x': 0.4,
        'xanchor': 'left',
        'y': 1.1,
        'yanchor': 'top'
},
    {
        'buttons': [
            {
                'label': subdistrict,
                'method': 'update',
                'args': [{'x': [data[(data[option] == selected_subdistrict) & (data['subdistrict'] == subdistrict)]
                                ['subdistrict'] for selected_subdistrict in data[option].unique()]},
                         {'title': f'ข้อมูล {option} จากแขวง {subdistrict}'}]
            } for subdistrict in data['subdistrict'].unique()
        ],
        'direction': 'down',
        'showactive': True,
        'x': 0.6,
        'xanchor': 'left',
        'y': 1.1,
        'yanchor': 'top'
},
    {
        'buttons': [
            {
                'label': status,
                'method': 'update',
                'args': [{'x': [data[(data[option] == selected_status) & (data['status'] == status)]
                                ['status'] for selected_status in data[option].unique()]},
                         {'title': f'ข้อมูล {option} สถานะ {status}'}]
            } for status in data['status'].unique()
        ],
        'direction': 'down',
        'showactive': True,
        'x': 0.8,
        'xanchor': 'left',
        'y': 1.1,
        'yanchor': 'top'
}
]

fig.update_layout(
    updatemenus=updatemenus,
    xaxis=dict(title='ข้อมูลจาก word_df'),
    yaxis=dict(title='จำนวน'),
)
st.plotly_chart(fig, use_container_width=True)


st.markdown("### Traffy Fondue Line Chart by word_df")
word_counts = data['word_df'].value_counts()
fig = go.Figure()
fig = px.line(word_counts.reset_index(), x='index', y='word_df')
st.plotly_chart(fig, use_container_width=True)

st.markdown("### Traffy Fondue Line Chart by District")
word_counts = data['district'].value_counts()
fig = go.Figure()
fig = px.line(word_counts.reset_index(), x='index', y='district')
st.plotly_chart(fig, use_container_width=True)

st.markdown("### Traffy Fondue Line Chart by Subdistrict")
word_counts = data['subdistrict'].value_counts()
fig = go.Figure()
fig = px.line(word_counts.reset_index(), x='index', y='subdistrict')
st.plotly_chart(fig, use_container_width=True)


#st.markdown("### Time series of Traffy Fondue")
#data['date'] = pd.to_datetime(data['date'])
#df_word = data.set_index('date')
#fig = px.line(df_word, x=df_word.index, y='word_df')
#start_date = st.sidebar.date_input("Start date", min_value=df_word.index.min(), max_value=df_word.index.max(), value=df_word.index.min())
#end_date = st.sidebar.date_input("End date", min_value=df_word.index.min(), max_value=df_word.index.max(), value=df_word.index.max())
#filtered_df = df_word[(df_word.index >= start_date) & (df_word.index <= end_date)]
#fig = px.line(filtered_df, x=filtered_df.index, y='word_df')

#st.plotly_chart(fig, use_container_width=True)
