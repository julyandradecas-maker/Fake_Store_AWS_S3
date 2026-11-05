const API = "http://127.0.0.1:8000";
const videoId = new URLSearchParams(location.search).get("id");

fetch(`${API}/videos/${videoId}`)
    .then(res => res.json())
    .then(video => {
        const player = document.createElement("video");
        player.src = video.source;
        player.autoplay = true;
        player.controls = true;

        const titulo = document.createElement("h1");
        titulo.textContent = video.titulo;

        document.querySelector("#reproductor").append(player, titulo);
    })

fetch(`${API}/videos/${videoId}/recomendados`)
    .then(res => res.json())
    .then(videos => {
        const aside = document.querySelector("#recomendados");

        videos.forEach(v => {
            const enlace = document.createElement("a");
            enlace.href = `video.html?id=${v.id}`;

            const mini = document.createElement("video");
            mini.src = v.source;
            mini.muted = true;
            mini.preload = "metadata";

            const t = document.createElement("h3");
            t.textContent = v.titulo;

            enlace.append(mini, t);
            aside.appendChild(enlace);
        });
    })

fetch(`${API}/videos/${videoId}/comentarios`)
    .then(res => res.json())
    .then(comentarios => {
        const lista = document.querySelector("#lista_comentarios");

        if (comentarios.length === 0) {
            const aviso = document.createElement("p");
            aviso.textContent = "Este video aún no tiene comentarios.";
            lista.appendChild(aviso);
            return;
        }

        comentarios.forEach(c => {
            const li = document.createElement("li");
            li.className = "comentario";

            const autor = document.createElement("strong");
            autor.textContent = c.autor;

            const texto = document.createElement("p");
            texto.textContent = c.texto;

            li.append(autor, texto);
            lista.appendChild(li);
        });
    })