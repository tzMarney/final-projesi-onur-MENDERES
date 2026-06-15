import streamlit as st

st.set_page_config(page_title="Fitness İçerik Üretici", page_icon="💪")

st.title("💪 Fitness İçerik Üretici")

konu = st.text_input("Bir fitness konusu gir:")

if st.button("İçerik Oluştur"):

    if konu:

        st.subheader("Video Fikri")
        st.write(f"{konu} hakkında kısa ve dikkat çekici bir reels videosu çek.")

        st.subheader("Hook")
        st.write(f"Bu {konu} hatasını yapıyorsan gelişimin yavaşlıyor olabilir!")

        st.subheader("Başlık")
        st.write(f"{konu} konusunda çoğu kişinin yaptığı hata")

        st.subheader("Açıklama")
        st.write(
            f"{konu} hakkında hazırladığım bu videoda dikkat edilmesi gereken noktaları anlattım."
        )

        st.subheader("Hashtagler")
        st.write("#fitness #gym #workout #bodybuilding #spor")

    else:
        st.warning("Lütfen bir konu gir.")