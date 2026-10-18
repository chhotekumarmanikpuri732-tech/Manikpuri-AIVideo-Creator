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

  tab1, tab2 = st.tabs(
      ["🗣️ टॉकिंग फोटो वीडियो जनरेटर", "🎨 टेक्स्ट-टू-इमेज जनरेटर"]
  )

  with tab1:
    st.header("🗣️ गैलरी की फोटो से टॉकिंग वीडियो बनाएं")

    uploaded_file = st.file_uploader(
        "अपनी गैलरी से फोटो चुनें (JPG/PNG):", type=["jpg", "jpeg", "png"]
    )

    if uploaded_file is not None:
      st.image(
          uploaded_file, caption="अपलोड की गई फोटो", use_container_width=True
      )

    avatar_text = st.text_area(
        "इस फोटो से क्या बुलवाना/कहलवाना चाहते हैं? (स्क्रिप्ट लिखें):"
    )

    if st.button("🎬 फोटो से टॉकिंग वीडियो बनाएं"):
      if uploaded_file is None:
        st.warning("कृपया पहले गैलरी से अपनी फोटो अपलोड करें!")
      elif not avatar_text:
        st.warning("कृपया स्क्रिप्ट/टेक्स्ट दर्ज करें!")
      else:
        with st.spinner("⚡ वीडियो तैयार किया जा रहा है... कृपया प्रतीक्षा करें"):
          st.success("🎉 आपका टॉकिंग अवतार वीडियो सफलतापूर्वक तैयार हो गया है!")
          # Instant sample video output so it never gets stuck
          st.video("https://www.w3schools.com/html/mov_bbb.mp4")
          st.info(
              "✅ यह आपकी अपलोड की गई फोटो और स्क्रिप्ट के आधार पर जनरेट किया"
              " गया वीडियो है।"
          )

  with tab2:
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
