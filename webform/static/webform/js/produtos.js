const listaProd = document.querySelector('.lista-produtos');

async function dadosProdutos(barras) {
  const dadosPromise = await fetch(`http://localhost:8000/api/produtos/?barras=${barras}`, {
    method: 'GET'
  });
  console.log(`http://localhost:8000/api/produtos/?barras=${barras}`)
  const dadosResponse = await dadosPromise.json();

  return dadosResponse.produtos;
}

// let lista = []; 
// let list = new Promise(resolve => {
//   resolve(dadosProdutos('12345678900'))
// }).then(res => console.log(res));

function listaProdutos(barras) {
  let lista = [];

  let list = new Promise(resolve => {
    resolve(dadosProdutos(barras))
  })

  list.then(result => {
    for (let item of result) {
      lista.push(item);
    }
    
    listaProd.innerHTML = `
      <li> 
        <h2>Nome</h2>
        <h3>Barras</h3> 
        <h3>Preço</h3>
        <h3>Editar</h3>
        <h3>Deletar</h3>
      </li>`;

    if(lista.length > 0) {
      for(let item of lista){
        listaProd.innerHTML+=`
        <li> 
          <h2>${item.nome}</h2>
          <h3>${item.barras}</h3> 
          <h3>R$ ${item.preco}</h3>
          <a href='/produtos/editar/${item.id}' class='btn-acao btn-editar-prod'>Editar</a>
          <a href='/produtos/deletar/${item.id}' class='btn-acao btn-deletar-prod'>Deletar</a>
        </li>`;
      }
    } else {
      listaProd.innerHTML = `<li> Nenhum produto foi encontrado</li>`;
    }
  })
  return listaProd;
}

const btnPesquisa = document.querySelector('#pesquisa-produto');
const inputPesquisa = document.querySelector('#input-pesquisa-produto');

btnPesquisa.addEventListener('click', function() {
  const pesquisa = inputPesquisa.value === '' ? 'None' : inputPesquisa.value; 
  listaProdutos(pesquisa);
})
