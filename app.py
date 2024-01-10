import matplotlib.pyplot as plt
import streamlit as st
import preprocessor,helper


st.set_page_config(layout='wide',page_title='Whatsapp chat analyzer',initial_sidebar_state="auto")


st.sidebar.title("Whats App Chat Analyzer")


uploaded_file = st.sidebar.file_uploader("Choose a file")
if uploaded_file is not None:
    # To read file as bytes:
    bytes_data = uploaded_file.getvalue()
    data = bytes_data.decode('utf-8')
    df = preprocessor.preprocess(data)

    st.dataframe(df)

    user_list =  df["sender"].unique().tolist()
    user_list.sort()
    user_list.insert(0 ,"Overall")

    selected_user = st.sidebar.selectbox("Show Analysis wrt",user_list)

    if st.sidebar.button("Show Analysis"):

        num_messages,words,num_media_messages,nums_links = helper.fecth_stats(selected_user,df)

        col1, col2 ,col3 ,col4 =st.columns(4)

        #Number of messsages
        with col1:
            st.header("Total messages")
            st.title(num_messages)

        # Total number of words sended by user
        with col2:
            st.header("Total words")
            st.title(words)

        # Number of media sended by user like photos and videos etc.
        with col3:
            st.header("Total Media")
            st.title(num_media_messages)

        # number of links and ulrs
        with col4:
            st.header("Number of Links")
            st.title(nums_links)

        if selected_user == "Overall":
            st.title("Most Busiest User")

            x , new_df = helper.most_busy_user(df)
            fig, ax = plt.subplots()

            col1, col2 = st.columns(2)
            with col1:
                ax.bar(x.index,x.values)
                st.pyplot(fig)

            with col2:
                st.dataframe(new_df)

        st.title("Word Cloud")
        df_wc = helper.create_word_cloud(selected_user,df)
        fig , ax = plt.subplots()
        ax.imshow(df_wc)
        st.pyplot(fig)





