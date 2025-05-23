import streamlit as st
import openai

# OpenAI APIキーの設定（Secretsから読み取る）
openai_api_key = st.secrets["OPENAI_API_KEY"]["openai_api_key"]
openai.api_key = openai_api_key

# 施設情報の入力フォーム
st.title("施設情報フォーム｜ミニサイト用")

# OTAキャッチコピー
ota_copy = st.text_input("OTAキャッチコピー", "ex.みんなで過ごすから、たのしい。ペット・家族の温泉旅行 応援宿。")

# 施設名
facility_name = st.text_input("施設名", "ex.筑後川温泉 ふくせんか")

# キャッチコピーキーワード
keyword1 = st.text_area("キャッチコピーキーワード1", "ex.貸切風呂の魅力。ふくせんかでは、4つの貸切風呂を完備しており、源泉かけ流しの温泉をプライベートに楽しむことができます。")
keyword2 = st.text_area("キャッチコピーキーワード2", "ex.地産地消の料理。地産地消の野菜や果物、新鮮な魚やお肉を使った会席料理。")
keyword3 = st.text_area("キャッチコピーキーワード3", "ex.特別室で贅沢な時間。ご家族連れに是非おすすめしたいのが完成したばかりの特別室への宿泊。")

# 館内での過ごし方
facility_activities1 = st.text_area("館内での過ごし方1", "ex.赤ちゃん連れでも安心。赤ちゃんとの旅行を手軽に楽しめるようパパ・ママにうれしいサービスや日用品を無料で提供")
facility_activities2 = st.text_area("館内での過ごし方2", "ex.ラウンジでくつろぎのひととき。ラウンジ前にはビールサーバー、ジュース、アイスクリームを無料で提供")

# 周辺エリアの見どころ
sightseeing1 = st.text_area("周辺エリアの見どころ1", "ex.つづら棚田。美しく積まれた石垣が印象的な棚田です。")
sightseeing2 = st.text_area("周辺エリアの見どころ2", "ex.やまんどんの果物農園。7種のいちごや、赤・白・黒系のぶどう、食感の違いを楽しめる梨など果物の品種が豊富な農園です。")

# 周辺の人気グルメ
restaurant1 = st.text_area("周辺の人気グルメ1", "ex.cafe たねの隣り。地元の旬の野菜を使ったランチや薬膳カレー、和洋の自家製デザート")
restaurant2 = st.text_area("周辺の人気グルメ2", "ex.うなぎ料理 和食処 松月(しょうげつ)。鰻の焼き加減は皮はパリッと身はフワフワと絶妙な焼き加減")
restaurant3 = st.text_area("周辺の人気グルメ3", "ex.馬庵このみ 吉井本店。馬肉は、自家牧場にておよそ2年の年月をかけて飼育されたもの")

# 結果の出力
if st.button("生成する"):
    # OpenAI APIにリクエストを送信して紹介文を生成
response = openai.ChatCompletion.create(
    model="gpt-4o",  # より高性能なGPT-4oモデルに変更
        messages=[
            {"role": "system", "content": "あなたはプロのトラベルライターです。施設の魅力あふれる紹介文を作成してください。目的はオンライントラベルエージェントに掲載する文章で宿泊施設の魅力が伝わり予約に結びつくことです。以下のフォーマットに従って、各セクションを分けて出力してください。『{facility_name}へようこそ！』という文章から始めてください。OTAキャッチコピー{ota_copy}を考慮に入れて、更に魅力的なキャッチコピーを{keyword1}、{keyword2}、{keyword3}を基に50文字以内の文章に仕上げてください。この宿の魅力をキーワード{keyword1}、{keyword2}、{keyword3}を基に、それぞれの特徴を詳しく説明するタイトルと文章を3つ作成してください。文章には名称を含めず、タイトルは太字に。館内での過ごし方のキーワード {facility_activities1} 、{facility_activities2}を基に、それぞれの設備やサービスを詳しく説明するタイトルと文章を3つ作成してください。補足情報がある場合は、それを考慮に入れてください。文章には名称を含めず、タイトルは太字に。周辺エリアの見どころは各見どころの名称をそのままタイトルとして使用し、{sightseeing1}{sightseeing2}を基にそれぞれの魅力を詳しく説明する文章を作成してください。文章には名称を含めず、タイトルは太字に。周辺の人気グルメ。各グルメの名称をそのままタイトルとして使用し、{restaurant1}{restaurant2}{restaurant3}を基にそれぞれの料理や雰囲気を詳しく説明する文章を作成してください。文章には名称を含めず、タイトルは太字に。感嘆符は使用せず、トーンとマナーを統一し、簡潔でわかりやすく、かつ読み応えのある内容にしてください。ただし、ウェルカムメッセージには感嘆符を使用します。"},
            {"role": "user", "content": f"""
            施設名: {facility_name}
            キャッチコピー: {ota_copy}
            : {keyword1}
            : {keyword2}
            : {keyword3}
            館内での過ごし方:
            - : {facility_activities1}
            - : {facility_activities2}
            周辺エリアの見どころ:
            - : {sightseeing1}
            - : {sightseeing2}
            周辺の人気グルメ:
            - : {restaurant1}
            - : {restaurant2}
            - : {restaurant3}
            """}
        ]
    )

    # 結果の生成
    generated_text = response['choices'][0]['message']['content'].strip()

    # 結果を表示
    st.text(generated_text)
