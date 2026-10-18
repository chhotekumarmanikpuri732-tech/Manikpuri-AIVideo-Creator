import streamlit as st

# पेज की सेटिंग्स
st.set_page_config(
    page_title="Manikpuri AI Video Creator", page_icon="✨", layout="centered"
)

# ऐप का शीर्षक
st.title("✨ Manikpuri AI Video Creator")
st.subheader("आपका अपना पर्सनल AI स्टूडियो (फ्री वर्शन)")

# साइडबार - लॉगिन / OTP सेक्शन
st.sidebar.header("🔐 यूज़र लॉगिन / साइन-अप")
user_phone = st.sidebar.text_input("अपना मोबाइल नंबर दर्ज करें:")

if st.sidebar.button("OTP भेजें"):
  if user_phone:
    st.sidebar.success(
      f"✅ OTP आपके नंबर {user_phone} पर भेज दिया गया है! (डेमो OTP: 1234)"
    )
  else:
    st.sidebar.warning("कृपया पहले अपना मोबाइल नंबर लिखें।")

entered_otp = st.sidebar.text_input("OTP दर्ज करें:", type="password")

if st.sidebar.button("लॉगिन करें"):
  if entered_otp == "1234":
    st.sidebar.success("🎉 लॉगिन सफल हुआ! अब आप AI फीचर्स का उपयोग कर सकते हैं।")
    st.session_state["logged_in"] = True
  else:
    st.sidebar.error("❌ गलत OTP, कृपया दोबारा प्रयास करें।")

# मुख्य स्क्रीन के फीचर्स (लॉगिन की स्थिति के आधार पर)
if st.session_state.get("logged_in", False):
  st.success(
    "👋 स्वागत है दादा! आपका अकाउंट सक्रिय है। नीचे दिए गए टूल्स का आनंद लें:"
  )

  tab1, tab2 = st.tabs(["🎨 टेक्स्ट-टू-इमेज जनरेटर", "🗣️ टॉकिंग अवतार वीडियो"])

  with tab1:
    st.header("🎨 AI इमेज जनरेटर")
    prompt_text = st.text_input(
      "आप किस तरह की तस्वीर बनाना चाहते हैं?",
      placeholder="जैसे: A futuristic city at sunset",
    )
    if st.button("तस्वीर बनाएं"):
      if prompt_text:
        st.info("🔄 आपकी तस्वीर जनरेट की जा रही है...")
        # यहाँ डमी इमेज दिखाई जाएगी
        st.image(
            "https://picsum.photos/600/400",
            caption=f"AI जनरेटेड इमेज: {prompt_text}",
        )
      else:
        st.warning("कृपया इमेज का विवरण दर्ज करें।")

  with tab2:
    st.header("🗣️ टॉकिंग अवतार वीडियो जनरेटर")
    avatar_text = st.text_area(
      "अवतार से क्या कहलवाना चाहते हैं? (टेक्स्ट लिखें):"
    )
    if st.button("वीडियो बनाएं"):
      if avatar_text:
        st.success(
            "🎬 आपका टॉकिंग अवतार वीडियो तैयार हो रहा है! (यह डेमो वर्शन"
            " है)"
        )
        st.info(
            "🔊 'नमस्ते! मानिकपुरी एआई क्रिएटर में आपका स्वागत है।' (ऑडियो"
            " जनरेटेड)"
        )
      else:
        st.warning("कृपया कुछ टेक्स्ट लिखें।")

else:
  st.info(
      "👉 वेबसाइट के सभी AI फीचर्स (इमेज और वीडियो मेकर) इस्तेमाल करने के लिए"
      " कृपया बाएं साइडबार से **मोबाइल नंबर डालकर लॉगिन** करें।"
  )
