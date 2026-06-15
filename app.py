import streamlit as st

st.set_page_config(
    page_title="Fitness İçerik Üretici",
    page_icon="💪",
    layout="centered"
)

st.title("💪 Fitness İçerik Üretici")
st.write("Fitness içerikleri için hızlı fikir oluşturma aracı")

konu = st.text_input("Fitness konusu gir")

if st.button("İçerik Oluştur"):

    if konu:

        st.success("İçerik oluşturuldu!")

        with st.container():
            st.subheader("🎬 Video Fikri")
            st.info(
                f"{konu} konusunda insanların yaptığı yaygın hataları anlatan kısa bir reels videosu."
            )

        with st.container():
            st.subheader("🔥 Hook")
            st.warning(
                f"{konu} yapıyorsan bu hatayı bırak!"
            )

        with st.container():
            st.subheader("📝 Başlık")
            st.write(
                f"{konu} konusunda çoğu kişinin bilmediği gerçek"
            )

        with st.container():
            st.subheader("📄 Açıklama")
            st.write(
                f"Bu videoda {konu} hakkında dikkat edilmesi gereken noktaları anlattım. Daha fazla fitness içeriği için takip etmeyi unutma."
            )

        with st.container():
            st.subheader("🏷️ Hashtagler")
            st.code(
                "#fitness #gym #workout #bodybuilding #motivation"
            )

        with st.container():
            st.subheader("📹 Kısa Video Senaryosu")
            st.write(
                f"Videoya '{konu} yapıyorsan bunu bilmen gerekiyor' diyerek başla. Daha sonra yaygın hataları anlat ve sonunda doğru yöntemi göster."
            )

    else:
        st.error("Lütfen bir konu gir.")