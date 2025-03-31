# AI営業アシスタント

## 概要
商談の要約を入力すると、OpenAI GPT-4 APIを使って、営業活動の次アクションとその理由、関係性構築のヒントを提案します。

## 使用技術
- Python + Streamlit
- OpenAI Chat Completions API

## ローカル実行
```
export OPENAI_API_KEY=your_api_key
streamlit run app.py
```

## サンプル入力
- 顧客名：ABC株式会社
- 商談内容：来期のAI導入を検討しているが、予算が未確定とのこと。
- 日付：2025-03-31

## 出力例
- Next Action: 予算決定時期（4月末）に再提案の連絡をする。
- Reason: 予算未確定が障壁なので、その時期がチャンス。
- Relationship Tips: AI導入事例の紹介ウェビナーを案内する。
