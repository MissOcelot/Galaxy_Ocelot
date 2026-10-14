// thumbnail function
// >> & "C:\Users\ocelo\AppData\Local\Microsoft\WinGet\Packages\Gyan.FFmpeg_Microsoft.Winget.Source_8wekyb3d8bbwe\ffmpeg-9.0.2-full_build\bin\ffmpeg.exe" -ss 00:00:02 -i "Maxmeetsjax.mp4" -frames:v 1 -vf "scale=640:360:force_original_aspect_ratio=increase,crop=640:360" -update 1 "../thumbnails/maxjax1.jpg"         

const videos = [
    {
        title: "Hi Maybell!",
        src: "videos/Himaybell.mp4",
        thumbnail: "thumbnails/may1.jpg"
    },
    {
        title: "Max meets Jax",
        src: "videos/Maxmeetsjax.mp4",
        thumbnail: "thumbnails/maxjax1.jpg"
    }
];