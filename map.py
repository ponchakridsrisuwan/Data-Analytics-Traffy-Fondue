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

# load data
data = pd.read_csv("./file.csv")

st.markdown("### ข้อมูลการร้องเรียนในระบบ Traffy Fondue Data Table")
st.write(data)


st.markdown("### ประเภทการร้องเรียนในระบบ Traffy Fondue Map")
option = st.selectbox(
    'เลือกตัวเลือกการแสดง ?',
    ('district', 'subdistrict', 'status'))
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
                     {'title': f'date per {option} for {date}'}]
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
                         {'title': f'district per {option} for {district}'}]
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
                         {'title': f'subdistrict per {option} for {subdistrict}'}]
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
                         {'title': f'status per {option} for {status}'}]
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

st.markdown("### ประเภทการร้องเรียนในระบบ Traffy Fondue")
fig = go.Figure()
fig.add_trace(go.Histogram(x=data['word_df'], name='word_df'))
fig.add_trace(go.Histogram(x=data['word_token'], name='word_token'))
fig.add_trace(go.Histogram(x=data['word_emo'], name='word_emo'))
st.plotly_chart(fig, use_container_width=True)

st.markdown("### ประเภทการร้องเรียนในระบบ Traffy Fondue Line Chart")
fig = go.Figure()
fig.add_trace(go.Scatter(x=data['date'], y=data['word_df'], name='word_df'))
st.plotly_chart(fig, use_container_width=True)

st.markdown("### ประเภทการร้องเรียนในระบบ Traffy Fondue Scatter Chart")
fig = px.scatter(data, y=data['word_df'], x=data['date'], color="word_df", symbol="status")
fig.update_traces(marker_size=10)
st.plotly_chart(fig, use_container_width=True)
        
to_series =  data['word_df'].squeeze()

data_count = data['word_df'].str.count(to_series)

fig = px.scatter(data, x=data['word_df'], y=data_count,
	         size=data_count, color="color_word_df", size_max=60, hover_name="word_df")
st.plotly_chart(fig, use_container_width=True)