import streamlit as st

st.set_page_config(
    page_title="Fitness İçerik Üretici",
    page_icon="💪",
    layout="centered"
)

icerikler = {
    "göğüs antrenmanı": {
        "fikir": "Göğüs antrenmanında sık yapılan 3 hatayı gösteren kısa bir reels videosu.",
        "hook": "Göğsün gelişmiyorsa sebebi antrenman tekniğin olabilir.",
        "baslik": "Göğüs Antrenmanında Sık Yapılan Hatalar",
        "aciklama": "Göğüs çalışırken yapılan küçük hatalar gelişimi etkileyebilir. Bu içerikte dikkat edilmesi gereken noktalara değinilmiştir.",
        "hashtag": "#chestworkout #fitness #gym #workout #bodybuilding",
        "senaryo": "1. Göğüs hareketi görüntüsü\n2. Yapılan hatayı gösterme\n3. Doğru uygulamayı anlatma\n4. Kısa öneri ile bitirme"
    },
    "deadlift": {
        "fikir": "Deadlift yaparken dikkat edilmesi gereken form kurallarını anlatan kısa video.",
        "hook": "Deadlift yaparken belini korumak için forma dikkat etmelisin.",
        "baslik": "Deadlift Yaparken Dikkat Edilmesi Gerekenler",
        "aciklama": "Deadlift etkili bir egzersizdir ancak yanlış form sakatlık riskini artırabilir. Bu içerikte temel noktalara yer verilmiştir.",
        "hashtag": "#deadlift #fitness #gym #strength #workout",
        "senaryo": "1. Deadlift başlangıç pozisyonu\n2. Sırt pozisyonunu gösterme\n3. Bar yolunu anlatma\n4. Güvenli tekrar örneği gösterme"
    },
    "protein tozu": {
        "fikir": "Protein tozu hakkında en çok merak edilen soruları açıklayan bilgilendirici video.",
        "hook": "Protein tozu kullanmadan önce ne işe yaradığını bilmek gerekir.",
        "baslik": "Protein Tozu Hakkında Temel Bilgiler",
        "aciklama": "Protein tozu, günlük protein ihtiyacını tamamlamak için kullanılan bir takviyedir. Bu içerikte kullanım amacı basit şekilde anlatılmıştır.",
        "hashtag": "#protein #fitness #gym #supplement #workout",
        "senaryo": "1. Protein tozunu gösterme\n2. Ne işe yaradığını açıklama\n3. Ne zaman kullanılabileceğini söyleme\n4. Dengeli beslenme vurgusu yapma"
    },
    "yağ yakımı": {
        "fikir": "Yağ yakımı sürecinde beslenme ve antrenmanın önemini anlatan kısa video.",
        "hook": "Yağ yakmak sadece daha fazla terlemek değildir.",
        "baslik": "Yağ Yakımı İçin Temel Noktalar",
        "aciklama": "Yağ yakımı için kalori dengesi, düzenli antrenman ve sürdürülebilir beslenme önemlidir. Bu içerikte temel bilgiler verilmiştir.",
        "hashtag": "#fatloss #fitness #gym #diet #workout",
        "senaryo": "1. Yağ yakımıyla ilgili yanlış düşünceyi söyleme\n2. Kalori dengesini açıklama\n3. Antrenman örneği verme\n4. Süreklilik vurgusu yapma"
    },
    "bulk dönemi": {
        "fikir": "Bulk döneminde kas kazanmak için dikkat edilmesi gerekenleri anlatan video.",
        "hook": "Bulk dönemi sadece çok yemek yemek değildir.",
        "baslik": "Bulk Döneminde Dikkat Edilmesi Gerekenler",
        "aciklama": "Bulk döneminde amaç kontrollü şekilde kilo alarak kas gelişimini desteklemektir. Bu süreçte antrenman ve beslenme birlikte ilerlemelidir.",
        "hashtag": "#bulk #fitness #gym #muscle #bodybuilding",
        "senaryo": "1. Bulk döneminin amacını açıklama\n2. Beslenme düzeninden bahsetme\n3. Antrenman takibini söyleme\n4. Kontrollü kilo alma önerisi verme"
    }
}

st.title("💪 Fitness İçerik Üretici")
st.write("Fitness içerikleri için basit içerik fikri oluşturma aracı")

konu = st.text_input("Fitness konusu gir").strip().lower()

if st.button("İçerik Oluştur"):
    if konu:
        veri = icerikler.get(konu)

        if veri is None:
            veri = {
                "fikir": f"{konu.title()} konusu hakkında bilgilendirici kısa bir sosyal medya videosu.",
                "hook": f"{konu.title()} hakkında bilinmesi gereken temel noktalar.",
                "baslik": f"{konu.title()} İçin İçerik Önerisi",
                "aciklama": f"Bu içerikte {konu} hakkında temel bilgiler ve dikkat edilmesi gereken noktalar anlatılabilir.",
                "hashtag": "#fitness #gym #workout #spor #motivation",
                "senaryo": "1. Konuyu kısaca tanıtma\n2. Temel bilgileri anlatma\n3. Örnek verme\n4. Kısa öneri ile bitirme"
            }

        st.success("İçerik oluşturuldu!")

        st.subheader("🎬 Video Fikri")
        st.info(veri["fikir"])

        st.subheader("🔥 Hook")
        st.warning(veri["hook"])

        st.subheader("📝 Başlık")
        st.write(veri["baslik"])

        st.subheader("📄 Açıklama")
        st.write(veri["aciklama"])

        st.subheader("🏷️ Hashtagler")
        st.code(veri["hashtag"])

        st.subheader("📹 Kısa Video Senaryosu")
        st.write(veri["senaryo"])

    else:
        st.error("Lütfen bir konu gir.")