from fastapi import FastAPI
import googleapiclient.discovery

app = FastAPI()

API_KEY = "のりこし君のYoutubuAPIのキー"

service = googleapiclient.discovery.build("youtube", "v3", developerKey=API_KEY)

video_id = "kbWGclLiWhQ"

@app.get("/fetch_youtube_ladder_views")
async def fetch_youtube_views():
    response = service.videos().list(
    part="statistics",  # 動画の統計情報を取得
    id=video_id  # 動画のIDを指定
    ).execute()

    view_count = response["items"][0]["statistics"]["viewCount"]

    return {"view_count": view_count}
