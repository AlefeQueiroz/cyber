// Função para preencher o campo de senha
function preencherSenha(senha) {
    document.getElementById('password').value = senha;
}

// Função para fazer a requisição AJAX e obter a senha gerada pelo servidor
function solicitarSenhaDoServidor() {
    var xhr = new XMLHttpRequest();
    xhr.onreadystatechange = function() {
        if (xhr.readyState === XMLHttpRequest.DONE) {
            if (xhr.status === 200) {
                var senhaGerada = xhr.responseText;
                preencherSenha(senhaGerada);
            } else {
                console.error('Erro ao solicitar senha ao servidor.');
            }
        }
    };
    xhr.open('GET', 'url_para_o_seu_endpoint_de_gerar_senha', true);
    xhr.send();
}

// Chamar a função para solicitar a senha ao servidor
solicitarSenhaDoServidor();
