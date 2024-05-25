document.addEventListener('DOMContentLoaded', function () {
    fetch('songs.json')
        .then(response => response.json())
        .then(songs => {
            const songsContainer = document.getElementById('songs-container');
            songs.forEach(song => {
                const songElement = document.createElement('div');
                songElement.className = 'song';
                songElement.innerHTML = `<p><strong>${song.title}</strong> by ${song.artist}</p><a href="${song.url}" target="_blank">Listen on Spotify</a>`;
                songsContainer.appendChild(songElement);
            });
        })
        .catch(error => console.error('Error fetching songs:', error));
});