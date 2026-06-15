import streamlit as st

st.set_page_config(page_title="Fitness İçerik Üretici", page_icon="💪")

st.title("💪 Fitness İçerik Üretici")

konu = st.text_input("Fitness konusu gir")

if st.button("İçerik Oluştur"):

    if konu:

        st.subheader("🎬 Video Fikri")
        st.write(f"{konu} konusunda insanların yaptığı en yaygın hataları anlatan kısa bir reels videosu.")

        st.subheader("🔥 Hook")
        st.write(f"{konu} yapıyorsan bu hatayı bırak!")

        st.subheader("📝 Başlık")
        st.write(f"{konu} konusunda çoğu kişinin bilmediği gerçek")

        st.subheader("📄 Açıklama")
        st.write(
            f"Bu videoda {konu} hakkında dikkat edilmesi gereken önemli noktaları anlattım. Daha fazla fitness içeriği için takip etmeyi unutma."
        )

        st.subheader("🏷️ Hashtagler")
        st.write("#fitness #gym #workout #bodybuilding #motivation")

        st.subheader("📹 Kısa Video Senaryosu")
        st.write(
            f"Videoya '{konu} yapıyorsan bunu bilmen gerekiyor' diyerek başla. Daha sonra yaygın hataları anlat ve sonunda doğru yöntemi göster."
        )

    else:
        st.warning("Lütfen bir konu gir.")