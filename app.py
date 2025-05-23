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
        model="gpt-3.5-turbo",  # 使用する最新のモデルを指定
        messages=[
           {"role": "system", "content": f"""
あなたはプロのトラベルライターです。以下の宿泊施設に関する情報をもとに、魅力を紹介する文章を生成してください。

まずは出力の冒頭に、以下の情報を**タイトル付き（太字）で**明示してください。フォーマットは以下を参考にしてください：

**OTAキャッチコピー**  
{ota_copy}

**施設名**  
{facility_name}

**キャッチコピーキーワード1**  
{keyword1}

**キャッチコピーキーワード2**  
{keyword2}

**キャッチコピーキーワード3**  
{keyword3}

**館内での過ごし方1**  
{facility_activities1}

**館内での過ごし方2**  
{facility_activities2}

**館内での過ごし方3**  
（必要に応じて空白でも構いません）

**周辺エリアの見どころ1**  
{sightseeing1}

**周辺エリアの見どころ2**  
{sightseeing2}

**周辺エリアの見どころ3**  
（必要に応じて空白でも構いません）

**周辺の人気グルメ1**  
{restaurant1}

**周辺の人気グルメ2**  
{restaurant2}

**周辺の人気グルメ3**  
{restaurant3}

そのあとに、以下のフォーマットに従って魅力的な紹介文を生成してください。

1. 『{facility_name}へようこそ！』という文章で始めること（ここでは感嘆符使用OK）
2. OTAキャッチコピーを考慮しつつ、{keyword1}〜{keyword3}を元に、50文字以内の魅力的な1文キャッチコピーを作成
3. {keyword1}〜{keyword3}をもとに、それぞれの魅力を説明するセクション（タイトルは太字）
4. {facility_activities1}〜{facility_activities2} を元に館内の魅力セクション（タイトル太字、名称省略）
5. {sightseeing1}〜{sightseeing2} を使った周辺観光の紹介（タイトルに施設名使用）
6. {restaurant1}〜{restaurant3} を使ったグルメ紹介（タイトルに店名使用）

全体を通じて感嘆符の多用は避け、トーンは丁寧で、簡潔かつ魅力的にまとめてください。
"""}

    # 結果の生成
    generated_text = response['choices'][0]['message']['content'].strip()

    # 結果を表示
    st.text(generated_text)
