import yt_dlp
import os

def baixar_video(link, somente_audio = False):
    pasta_videos = os.path.expanduser("~/Videos")
    output_path = os.path.join(pasta_videos, '%(title)s.%(ext)s')

    opcoes = {
        'outtmpl': output_path,
    }

    if somente_audio:
        opcoes.update({
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
        })
    else:
        opcoes.update({'format': 'best'})

    with yt_dlp.YoutubeDL(opcoes) as ydl:
        ydl.download([link])

def main():
    url = input("\nCole o link do vídeo: ")
    escolha = input("Deseja baixar somente o áudio? (s/n): ").strip().lower()
    somente_audio = escolha == 's'
    baixar_video(url, somente_audio)
    print("\nDonload concluído. Você pode acessá-lo no diretório 'Vídeos'")

if __name__ == "__main__":
    main()