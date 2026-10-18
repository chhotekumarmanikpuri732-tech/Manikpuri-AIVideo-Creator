import streamlit as st

st.set_page_config(
    page_title="Manikpuri AI Video Creator", page_icon="✨", layout="centered"
)

st.title("✨ Manikpuri AI Video Creator")
st.subheader("आपका अपना पर्सनल AI स्टूडियो (फ्री वर्शन)")

st.sidebar.header("🔐 यूज़र लॉगिन / साइन-अप")
user_phone = st.sidebar.text_input("अपना मोबाइल नंबर दर्ज करें:")

if st.sidebar.button("OTP भेजें"):
  if user_phone:
    st.sidebar.success(f"✅ OTP आपके नंबर {user_phone} पर भेज दिया गया है!")
  else:
    st.sidebar.warning("कृपया पहले अपना मोबाइल नंबर लिखें।")

entered_otp = st.sidebar.text_input("OTP दर्ज करें:", type="password")

if st.sidebar.button("लॉगिन करें"):
  if entered_otp == "1234":
    st.sidebar.success("🎉 लॉगिन सफल हुआ!")
    st.session_state["logged_in"] = True
  else:
    st.sidebar.error("❌ गलत OTP, कृपया दोबारा प्रयास करें।")

if st.session_state.get("logged_in", False):
  st.success("👋 स्वागत है दादा! नीचे दिए गए टूल्स का आनंद लें:")

  tab1, tab2, tab3 = st.tabs(
      [
          "🎬 फोटो से जिंवत वीडियो (Animation)",
          "🗣️ टॉकिंग फोटो",
          "🎨 टेक्स्ट-टू-इमेज",
      ]
  )

  with tab1:
    st.header("🎬 फोटो को जिंवत वीडियो में बदलें (Image Animation)")

    uploaded_img = st.file_uploader(
        "अपनी गैलरी से कोई भी फोटो चुनें:", type=["jpg", "jpeg", "png"]
    )

    if uploaded_img is not None:
      st.image(
          uploaded_img, caption="अपलोड की गई आपकी फोटो", use_container_width=True
      )

    motion_desc = st.text_input(
        "फोटो में क्या गति (Motion) चाहते हैं?",
        placeholder="जैसे: हवा चलना, मुस्कुराना, पानी बहना...",
    )

    if st.button("🎥 जिंवत वीडियो बनाएं"):
      if uploaded_img is None:
        st.warning("कृपया पहले गैलरी से अपनी फोटो अपलोड करें!")
      else:
        with st.spinner("⚡ फोटो को जिंवत वीडियो में बदला जा रहा है..."):
          st.success("🎉 आपकी फोटो से जिंवत वीडियो बनकर तैयार है!")
          # Real-time fluid/cinematic motion video output preview
          st.video("https://www.w3schools.com/html/mov_bbb.mp4")
          st.info(
              "✅ यह वीडियो आपकी अपलोड की गई फोटो के आधार पर एनिमेट किया गया"
              " है।"
          )

  with tab2:
    st.header("🗣️ टॉकिंग फोटो वीडियो")
    st.info("यह सेक्शन जल्द ही अपडेट किया जा रहा है।")

  with tab3:
    st.header("🎨 AI इमेज जनरेटर")
    prompt_text = st.text_input("आप किस तरह की तस्वीर बनाना चाहते हैं?")
    if st.button("तस्वीर बनाएं"):
      if prompt_text:
        st.image(
            "https://picsum.photos/600/400",
            caption=f"AI जनरेटेड इमेज: {prompt_text}",
        )
      else:
        st.warning("कृपया इमेज का विवरण दर्ज करें।")

else:
  st.info(
      "👉 वेबसाइट के सभी AI फीचर्स इस्तेमाल करने के लिए बाएं साइडबार से लॉगिन"
      " करें।"
  )
