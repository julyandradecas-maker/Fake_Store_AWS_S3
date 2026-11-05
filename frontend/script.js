fetch("http://127.0.0.1:8000/videos")
            .then(res => res.json())
            .then(videos => {
                const divContainer = document.querySelector(".container");

                videos.forEach(video => {
                    const enlace = document.createElement("a");
                    enlace.href = `video.html?id=${video.id}`;
                    enlace.className = "card_link";

                    const contenedor = document.createElement("article");
                    contenedor.className = "container_item"; 

                    const videoContainer = document.createElement("video");
                    const videoTitulo = document.createElement("h3");

                    videoTitulo.textContent = video.titulo;
                    videoContainer.src = video.source;

                    contenedor.appendChild(videoContainer);
                    contenedor.appendChild(videoTitulo);
                    enlace.appendChild(contenedor);
                    divContainer.appendChild(enlace);
                });
            }) 
        
