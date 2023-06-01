import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time


#Now
st.title('Ryomaの遊び場')

'Start!'

latest_iteration = st.empty()
bar = st.progress(0)
for i in range(100):
    latest_iteration.text(f'Ryoma のやる気{i+1}')
    bar.progress(i+1)
    time.sleep(0.01)
    



left_column, right_column = st.columns(2)
button = left_column.button('Ryomaの今の気持ちを表示')
if button:
    right_column.write('早く退勤してえ')


text = st.text_input('あなたが好きなことは？')  

condition = st.slider('あなたの今の調子は？' ,0, 100, 50)

'あなたの好きなことは', text, 'です'
'あなたの調子は', condition, 'です'



#Comment

#option = st.selectbox('あなたが好きな数字は？', list(range(1, 11)))  
#'あなたの好きな数字は', option, 'です'



#expander = st.expander('問い合わせ')
#expander.write('問い合わせ内容を書く')




# """

# # 章
# ## 節
# ### 項

# ```python
# ```

# """


# df = pd.DataFrame({
    # '1列目': [1, 2, 3, 4],
    # '2列目': [10, 20, 30, 40]
# }) 

# if st.checkbox('Ryomaに会いたいですか？'):
#     img = Image.open('IMG_2135.JPG')
#     st.image(img, caption='Ryoma', use_column_width=True)
#     """
#     # 'やあ、元気かい？'
#     """


# st.table(df.style.highlight_max(axis=0))

# st.line_chart(df)
# st.area_chart(df)
# st.bar_chart(df)


#df = pd.DataFrame(
    #np.random.rand(100, 2)/[50, 50] + [35.69, 139.70],
    #columns=['lat', 'lon']
#)

#st.map(df)

#text = st.sidebar.text_input('あなたが好きなことは？')  

#condition = st.sidebar.slider('あなたの今の調子は？' ,0, 100, 50)

