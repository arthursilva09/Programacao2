const listaProd = document.querySelector('.lista-vendas');
const quantidadeProd = document.querySelector('#input-quantidade-produto');
const totalVenda = document.querySelector('#total-venda');

async function dadosVendas() {
  const dadosPromise = await fetch(`http://localhost:8000/api/vendas/`, {
    method: 'GET'
  });
  const dadosResponse = await dadosPromise.json();

  return dadosResponse.vendas;
}

function listaVendas() {
  let lista = [];

  let list = new Promise(resolve => {
    resolve(dadosVendas())
  })

  list.then(result => {
    console.log(result)
    for (let item of result) {
      lista.push(item);
    }
  
    if(lista.length > 0) {
      for(let item of lista){
        listaProd.innerHTML+=`
        <li> 
          <h3>${item.data_venda}</h3>
          <h2>${item.cliente}</h2>
          <h3>${item.valor_total}</h3> 
          <h3>R$ ${item.preco}</h3>
        </li>`;
      }
    } else {
      listaProd.innerHTML = `<li> Nenhuma venda foi encontrado</li>`;
    }
  })
  return listaProd;
}



const btnPesquisa = document.querySelector('#pesquisa-produto');
const inputPesquisa = document.querySelector('#input-pesquisa-produto');

document.addEventListener('DOMContentLoaded', function() { 
  listaVendas();
})

const btnFinalizarVenda = document.querySelector('.finalizar-venda');
btnFinalizarVenda.addEventListener('click', function() {
  window.location = `/vendas/forma_pagamento/${totalVenda.innerText}`;
})


