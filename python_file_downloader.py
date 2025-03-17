import yt_dlp

def download_video(url, destination_folder="C:/Downloads"):
    try:
        # Definirea unui user-agent personalizat
        ydl_opts = {
            'outtmpl': f'{destination_folder}/%(title)s.%(ext)s',  # Șablon de salvare fișier
            'headers': {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
            },
        }

        # Descărcarea videoclipului
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])

        print("Descărcare finalizată!")

    except Exception as e:
        print(f"A apărut o eroare: {str(e)}")

# Solicită link-ul video-ului de la utilizator
url = input("Introduceti URL-ul videoclipului YouTube: ")
download_video(url)
