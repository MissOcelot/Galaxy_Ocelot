// thumbnail function
// >> & "C:\Users\ocelo\AppData\Local\Microsoft\WinGet\Packages\Gyan.FFmpeg_Microsoft.Winget.Source_8wekyb3d8bbwe\ffmpeg-9.0.2-full_build\bin\ffmpeg.exe" -ss 00:00:02 -i "Maxmeetsjax.mp4" -frames:v 1 -vf "scale=640:360:force_original_aspect_ratio=increase,crop=640:360" -update 1 "../thumbnails/maxjax1.jpg"         

const videos = [
    {
        title: "Hi Maybell!",
        src: "videos/Himaybell.mp4",
        thumbnail: "Thumbnails/may1.jpg"
    },
    {
        title: "Max meets Jax",
        src: "videos/Maxmeetsjax.mp4",
        thumbnail: "Thumbnails/maxjax1.jpg"
    }
];

const videoGrid = document.getElementById("video-grid");
const mainVideo = document.getElementById("main-video");
const videoTitle = document.getElementById("video-title");

mainVideo.src = videos[0].src;
videoTitle.textContent = videos[0].title;

videos.forEach(function(video) {
    const button = document.createElement("button");
    button.className = "video-choice";
    button.type = "button";

    const image = document.createElement("img");
    image.src = video.thumbnail;
    image.alt = "";

    const label = document.createElement("span");
    label.textContent = video.title;

    button.appendChild(image);
    button.appendChild(label);

    button.addEventListener("click", function() {
        mainVideo.src = video.src;
        currentVideoIndex = videos.indexOf(video);
        mainVideo.load();
        mainVideo.play();

        videoTitle.textContent = video.title;
    });


    let currentVideoIndex = 0;

function playVideo(index) {
    // Wrap around if we go past either end
    currentVideoIndex = (index + videos.length) % videos.length;

    const video = videos[currentVideoIndex];

    mainVideo.src = video.src;
    mainVideo.load();
    videoTitle.textContent = video.title;
}

document.getElementById("prev-video").addEventListener("click", function() {
    playVideo(currentVideoIndex - 1);
});

document.getElementById("next-video").addEventListener("click", function() {
    playVideo(currentVideoIndex + 1);
});

    videoGrid.appendChild(button);
});