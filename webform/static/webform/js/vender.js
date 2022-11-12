const listaProd = document.querySelector('.lista-vendas');
const quantidadeProd = document.querySelector('#input-quantidade-produto');
const totalVenda = document.querySelector('#total-venda');

async function dadosProdutos(barras) {
  const dadosPromise = await fetch(`http://localhost:8000/api/produtos/?barras=${barras}`, {
    method: 'GET'
  });
  console.log(`http://localhost:8000/api/produtos/?barras=${barras}`)
  const dadosResponse = await dadosPromise.json();

  return dadosResponse.produtos;
}

function listaProdutos(barras) {
  let lista = [];
  let somatorio = parseFloat(totalVenda.innerText);

  let list = new Promise(resolve => {
    resolve(dadosProdutos(barras))
  })

  list.then(result => {
    if(result.length>0) {
      for (let item of result) {
        lista.push(item);
      }
    
      if(lista.length > 0) {
        for(let item of lista){
          listaProd.innerHTML+=`
          <li> 
            <h2>${item.nome}</h2>
            <h3>${item.barras}</h3> 
            <h3>R$ ${item.preco}</h3>
          </li>`;
          somatorio= somatorio + (item.preco * parseInt(quantidadeProd.value));
          totalVenda.innerText = somatorio;
        }
      } else {
        listaProd.innerHTML = `<li> Nenhum produto foi encontrado</li>`;
      }
    } else {
      alert('Produto não encontrado');
    }
  })
  return listaProd;
}

const btnPesquisa = document.querySelector('#pesquisa-produto');
const inputPesquisa = document.querySelector('#input-pesquisa-produto');

btnPesquisa.addEventListener('click', function() {

  if(inputPesquisa.value === '') alert('Digite um código de barras.') 
  else listaProdutos(inputPesquisa.value);
})

const btnFinalizarVenda = document.querySelector('.finalizar-venda');
btnFinalizarVenda.addEventListener('click', function() {
  window.location = `/vendas/forma_pagamento/${totalVenda.innerText}`;
})


