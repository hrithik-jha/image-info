import streamlit as st 
import pandas as pd
import random
from PIL import Image
def main():
    st.title('Image Processing Project')

    menu=['Thumbnail Customization','Details']
    item=st.sidebar.selectbox('',menu)
    st.sidebar.info('Made by Abhay R Patel and Hrithik Jha')
    github='''[ Fork/Star on Github](https://github.com/)'''
    st.sidebar.info(github)

    if(item=='Thumbnail Customization'):
        labels=['Action','Adventure','Animation','Biography','Comedy','Crime','Documentary','Drama','Family','Fantasy','History','Horror','Music','Musical','Mystery','N/A','News','Reality-TV','Romance','Sci-Fi','Short','Sport','Thriller','War','Western']
        selected_labels=st.multiselect('Choose Genres',labels)
        df1=pd.read_csv('MI3.csv')
        df2=pd.read_csv('MI4.csv')
        df3=pd.read_csv('MI5.csv')
        df4=pd.read_csv('MI6.csv')

        l1=selected_labels[0]
        

        r1=df1.loc[df1['Genre']==l1]
        st.write(type(r1))
        r1=r1['path'].tolist()
        r2=df2.loc[df2['Genre']==l1]
        r2=r2['path'].tolist()
        r3=df3.loc[df3['Genre']==l1]
        r3=r3['path'].tolist()
        r4=df4.loc[df4['Genre']==l1]
        r4=r4['path'].tolist()

        

        img1=r1[random.randint(0,len(r1)-1)]
        img2=r2[random.randint(0,len(r2)-1)]
        img3=r3[random.randint(0,len(r3)-1)]
        img4=r4[random.randint(0,len(r4)-1)]



        image1=Image.open(img1)
        st.write('MI3')
        st.image(image1)


        image1=Image.open(img2)
        st.write('MI4')
        st.image(image1)

        image1=Image.open(img3)
        st.write('MI5')
        st.image(image1)

        image1=Image.open(img4)
        st.write('MI6')
        st.image(image1)
        




if __name__ == "__main__":
    main()