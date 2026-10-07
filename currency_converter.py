
import streamlit as st
import requests
from datetime import datetime

# =========================================================
# PAGE CONFIGURATION
# =========================================================
st.set_page_config(
    page_title="Keerthi's Currency Converter",
    page_icon="💱",
    layout="centered"
)

# =========================================================
# CUSTOM CSS
# =========================================================
st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700;800&display=swap');

html, body, [class*="css"] {
    font-family: 'Poppins', sans-serif;
}

.stApp {
    background:
        radial-gradient(circle at 10% 10%, #35106b 0%, transparent 30%),
        radial-gradient(circle at 90% 10%, #064e78 0%, transparent 30%),
        linear-gradient(135deg, #080b18, #11162b, #080b16);
}

.block-container {
    max-width: 850px;
    padding-top: 35px;
    padding-bottom: 40px;
}

.main-title {
    text-align: center;
    font-size: 40px;
    font-weight: 800;
    background: linear-gradient(
        90deg,
        #ff4ecd,
        #a855f7,
        #38bdf8
    );
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.subtitle {
    text-align: center;
    color: #b8bfd9;
    font-size: 15px;
    margin-bottom: 30px;
}

.card {
    background: rgba(255,255,255,0.055);
    border: 1px solid rgba(255,255,255,0.12);
    border-radius: 25px;
    padding: 30px;
    box-shadow: 0 15px 45px rgba(0,0,0,0.35);
}

.section-title {
    text-align: center;
    color: white;
    font-size: 22px;
    font-weight: 700;
    margin-bottom: 20px;
}

.stNumberInput label,
.stSelectbox label {
    color: #d8def2 !important;
    font-weight: 600 !important;
}

.stNumberInput input {
    background: rgba(255,255,255,0.07) !important;
    color: white !important;
}

.stSelectbox div[data-baseweb="select"] > div {
    background: rgba(255,255,255,0.07);
    color: white;
}

.stButton > button {
    width: 100%;
    border-radius: 15px;
    border: none;
    background: linear-gradient(
        90deg,
        #7c3aed,
        #ec4899
    );
    color: white;
    font-size: 16px;
    font-weight: 700;
    padding: 13px;
    transition: 0.25s;
}

.stButton > button:hover {
    transform: translateY(-2px);
    box-shadow: 0 10px 28px rgba(236,72,153,0.4);
}

.result-card {
    background: linear-gradient(
        135deg,
        rgba(124,58,237,0.20),
        rgba(236,72,153,0.13)
    );
    border: 1px solid rgba(255,255,255,0.14);
    border-radius: 22px;
    padding: 28px;
    margin-top: 25px;
    text-align: center;
}

.result-label {
    color: #aeb7d4;
    font-size: 14px;
    font-weight: 600;
}

.result-amount {
    color: white;
    font-size: 38px;
    font-weight: 800;
    margin: 10px 0;
}

.rate-box {
    background: rgba(255,255,255,0.07);
    border-radius: 15px;
    padding: 15px;
    margin-top: 15px;
    color: #d8def2;
}

.info-card {
    background: rgba(255,255,255,0.06);
    border: 1px solid rgba(255,255,255,0.10);
    border-radius: 18px;
    padding: 18px;
    text-align: center;
}

.info-title {
    color: #9fa8c4;
    font-size: 13px;
    font-weight: 600;
}

.info-value {
    color: white;
    font-size: 20px;
    font-weight: 700;
    margin-top: 5px;
}

.history-card {
    background: rgba(255,255,255,0.05);
    border-radius: 18px;
    padding: 20px;
    margin-top: 20px;
}

.history-title {
    color: white;
    font-size: 18px;
    font-weight: 700;
    margin-bottom: 10px;
}

.history-item {
    color: #cbd5e1;
    padding: 8px 0;
    border-bottom: 1px solid rgba(255,255,255,0.08);
}

.footer {
    text-align: center;
    color: #737c9c;
    font-size: 13px;
    margin-top: 25px;
}

</style>
""", unsafe_allow_html=True)


# =========================================================
# CURRENCY DATA
# =========================================================
currencies = {
    "🇮🇳 INR - Indian Rupee": "INR",
    "🇺🇸 USD - US Dollar": "USD",
    "🇪🇺 EUR - Euro": "EUR",
    "🇬🇧 GBP - British Pound": "GBP",
    "🇯🇵 JPY - Japanese Yen": "JPY",
    "🇦🇺 AUD - Australian Dollar": "AUD",
    "🇨🇦 CAD - Canadian Dollar": "CAD",
    "🇨🇭 CHF - Swiss Franc": "CHF",
    "🇸🇬 SGD - Singapore Dollar": "SGD",
    "🇦🇪 AED - UAE Dirham": "AED",
    "🇸🇦 SAR - Saudi Riyal": "SAR",
    "🇰🇷 KRW - South Korean Won": "KRW"
}


# =========================================================
# SESSION STATE
# =========================================================
if "history" not in st.session_state:
    st.session_state.history = []


# =========================================================
# HEADER
# =========================================================
st.markdown(
    '<div class="main-title">💱 KEERTHI\'S CURRENCY CONVERTER</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    '🌎 Convert currencies using current exchange rates'
    '</div>',
    unsafe_allow_html=True
)


# =========================================================
# MAIN CARD
# =========================================================
st.markdown(
    '<div class="card">',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="section-title">💰 CONVERT YOUR MONEY</div>',
    unsafe_allow_html=True
)


# =========================================================
# AMOUNT
# =========================================================
amount = st.number_input(
    "💵 Enter Amount",
    min_value=0.01,
    value=100.0,
    step=1.0
)

st.write("")


# =========================================================
# CURRENCY SELECTION
# =========================================================
col1, col2 = st.columns(2)

with col1:
    from_currency_name = st.selectbox(
        "🌐 From Currency",
        list(currencies.keys()),
        index=0
    )

with col2:
    to_currency_name = st.selectbox(
        "🎯 To Currency",
        list(currencies.keys()),
        index=1
    )

st.write("")


# =========================================================
# CONVERT BUTTON
# =========================================================
convert = st.button(
    "⚡ CONVERT NOW",
    use_container_width=True
)

st.markdown(
    "</div>",
    unsafe_allow_html=True
)


# =========================================================
# CONVERSION
# =========================================================
if convert:

    from_currency = currencies[from_currency_name]
    to_currency = currencies[to_currency_name]

    # Same currency
    if from_currency == to_currency:

        converted_amount = amount
        rate = 1.0
        rate_date = "Same currency"

    else:

        try:

            # Public Frankfurter API
            url = (
                "https://api.frankfurter.dev/v2/rate/"
                + from_currency.lower()
                + "/"
                + to_currency.lower()
            )

            response = requests.get(
                url,
                timeout=15
            )

            if response.status_code != 200:

                st.error(
                    "❌ Exchange rate is currently unavailable. "
                    "Please try again."
                )

                st.stop()

            data = response.json()

            rate = float(data["rate"])

            rate_date = data.get(
                "date",
                "Latest available"
            )

            converted_amount = amount * rate

        except requests.exceptions.Timeout:

            st.error(
                "⏱️ The server took too long to respond. "
                "Please try again."
            )

            st.stop()

        except requests.exceptions.ConnectionError:

            st.error(
                "🌐 Internet connection problem. "
                "Please check your internet connection."
            )

            st.stop()

        except requests.exceptions.RequestException:

            st.error(
                "🌐 Could not connect to the exchange-rate service."
            )

            st.stop()

        except (KeyError, ValueError):

            st.error(
                "⚠️ Invalid exchange-rate information received."
            )

            st.stop()

        except Exception:

            st.error(
                "⚠️ Something went wrong. Please try again."
            )

            st.stop()


    # =====================================================
    # RESULT CARD
    # =====================================================
    st.markdown(
        '<div class="result-card">',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="result-label">CONVERSION RESULT</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        f'<div class="result-amount">'
        f'{converted_amount:,.2f} {to_currency}'
        f'</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        f'<div class="rate-box">'
        f'💱 1 {from_currency} = '
        f'<strong>{rate:,.6f} {to_currency}</strong>'
        f'<br><br>'
        f'📅 Rate date: {rate_date}'
        f'</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '</div>',
        unsafe_allow_html=True
    )


    # =====================================================
    # INFORMATION CARDS
    # =====================================================
    st.write("")

    info1, info2 = st.columns(2)

    with info1:

        st.markdown(
            f"""
            <div class="info-card">
                <div class="info-title">
                    💵 YOU ENTERED
                </div>
                <div class="info-value">
                    {amount:,.2f} {from_currency}
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    with info2:

        st.markdown(
            f"""
            <div class="info-card">
                <div class="info-title">
                    💰 YOU RECEIVE
                </div>
                <div class="info-value">
                    {converted_amount:,.2f} {to_currency}
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )


    # =====================================================
    # SAVE HISTORY
    # =====================================================
    current_time = datetime.now().strftime("%H:%M:%S")

    history_text = (
        f"{current_time} — "
        f"{amount:,.2f} {from_currency} → "
        f"{converted_amount:,.2f} {to_currency}"
    )

    st.session_state.history.insert(
        0,
        history_text
    )

    st.session_state.history = (
        st.session_state.history[:5]
    )


# =========================================================
# CONVERSION HISTORY
# =========================================================
if st.session_state.history:

    st.markdown(
        '<div class="history-card">',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="history-title">'
        '🕘 RECENT CONVERSIONS'
        '</div>',
        unsafe_allow_html=True
    )

    for item in st.session_state.history:

        st.markdown(
            f'<div class="history-item">{item}</div>',
            unsafe_allow_html=True
        )

    st.markdown(
        '</div>',
        unsafe_allow_html=True
    )


# =========================================================
# FOOTER
# =========================================================
st.markdown(
    """
    <div class="footer">
        💱 Keerthi's Currency Converter
        <br>
        Built with Python + Streamlit
        <br>
        Live exchange rates • No API key required
    </div>
    """,
    unsafe_allow_html=True
)
