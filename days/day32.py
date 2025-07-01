from youtube_transcript_api import YouTubeTranscriptApi
from dotenv import load_dotenv
import os
import openai

openai.api_key = ""

def get_video_id(url):
    if "v=" in url:
        return url.split("v=")[1].split("&")[0]
    elif "youtu.be/" in url:
        return url.split("youtu.be/")[1]
    return None

def get_transcription(video_url):
    video_id = get_video_id(video_url)
    transcript = YouTubeTranscriptApi.get_transcript(video_id, languages = ['pt', 'pt-BR', 'en'])
    full_text = " ".join([t["text"] for t in transcript])
    return full_text

def summarize_text(text):
    response = openai.ChatCompletion.create(
        model = "gpt-4o",
        messages=[
            {"role": "system", "content": "Você é um assistente que resume vídeos"},
            {"role": "user", "content": f"Resuma este vídeo em tópicos e de maneira clara: {text}"},
        ],
        temperature = 0.5,
        max_tokens = 700
    )
    return response['choices'][0]['message']['content']

def main():
    video_link = input("Cole o link do vídeo: ")
    texto = get_transcription(video_link)
    resumo = summarize_text(texto)

    print("\nResumo:")
    print(resumo)

if __name__ == "__main__":
    main()