import streamlit as st
import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

st.title("🧠 AI営業アシスタント")
st.write("商談履歴を入力すると、次のアクションを提案します。")

client = st.text_input("顧客名")
summary = st.text_area("商談の要点")
date = st.date_input("商談日付")

if st.button("提案を生成"):
    if not all([client, summary, date]):
        st.warning("すべての項目を入力してください。")
    else:
        with st.spinner("AIが分析中..."):
            prompt = f"""
あなたはB2B営業アシスタントです。
以下は、商談の要約と日付、および顧客名です。
これをもとに、営業担当者に対して次のアクションを3つの観点から提案してください：
1. 次に何をすべきか（Next Action）
2. その理由（Reason）
3. 関係強化のヒント（Relationship Tips）

顧客名: {client}
商談日: {date}
商談要約: {summary}

フォーマット:
- Next Action:
- Reason:
- Relationship Tips:
"""

            response = openai.ChatCompletion.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": "あなたは有能なB2B営業アシスタントです。"},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.5,
                max_tokens=500
            )
            result = response["choices"][0]["message"]["content"]
            st.success("提案が生成されました！")
            st.markdown(result)
