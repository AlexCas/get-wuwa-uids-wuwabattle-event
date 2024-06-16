from TikTokApi import TikTokApi
import asyncio
import re

async def get_hashtag_videos():
    videos = list()
    async with TikTokApi() as api:        
        await api.create_sessions(num_sessions=1, headless=False)
        for _ in range(2):
            async for video in api.hashtag(name='wuwabattle').videos():
                videos.append(video)  
                desc = video.as_dict['desc']
                for match in re.finditer(r"(?:uid|uuid)\s*:\s*(\d{9})", desc, re.IGNORECASE):                    
                    print(match.group(1))


if __name__ == "__main__":
    asyncio.run(get_hashtag_videos())