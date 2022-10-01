#include <stdio.h>
#include <string.h>
#include <stdlib.h>

typedef enum { ELETRODOMESTICO, FERRAMENTA, VESTUARIO } cat;
char cat_str[3][20] = {"Eletrodomestico", "Ferramenta", "Vestuario"};

typedef enum { False, True } bool;

struct catalogo {
  int codigo;
  cat categoria;
  int estoque;
  char descricao[50];
  bool active;
} catalogo[20];


int produto_index = 0;

void novo_produto() {
  char desc[50];
  int cat;
  printf("\n\nDigite a descrição: ");
  scanf("\n%[^\n]", desc);
  printf("Categorias: \n");
  printf("(1) ELETRODOMESTICO\n");
  printf("(2) FERRAMENTA\n");
  printf("(3) VESTUARIO\n");
  printf("ESCOLHA: ");
  scanf("%d", &cat);

  catalogo[produto_index].codigo = produto_index + 1;
  catalogo[produto_index].estoque = 0;
  catalogo[produto_index].categoria = cat - 1;
  catalogo[produto_index].active = True;
  strcpy(catalogo[produto_index].descricao, desc);
  produto_index++;
}


void listar_catalogo() {
  for (int i = 0; i < produto_index; i++) {
    if (catalogo[i].active) {
      printf("\nProduto de codigo: %d\n", catalogo[i].codigo);
      printf("Produto de categoria: %s\n", cat_str[catalogo[i].categoria]);
      printf("Estoque: %d\n", catalogo[i].estoque);
      printf("Descricao: %s\n\n", catalogo[i].descricao);
    }
  }
}


void atualizar_estoque() {
  int id, quant;
  printf("\nDigite o codigo do produto: ");
  scanf("%d", &id);
  printf("Digite o novo estoque: ");
  scanf("%d", &quant);
  catalogo[id - 1].estoque = quant;
}


void aumentar_estoque() {
  int id, quant;
  printf("\nDigite o codigo do produto: ");
  scanf("%d", &id);
  printf("Digite o quanto quer adicionar: ");
  scanf("%d", &quant);
  catalogo[id - 1].estoque += quant;
}


void dimuir_estoque() {
  int id, quant;
  printf("\nDigite o codigo do produto: ");
  scanf("%d", &id);
  printf("Digite o quanto quer retirar: ");
  scanf("%d", &quant);
  catalogo[id - 1].estoque -= quant;
}


void remover_produto() {
  int id;
  printf("\nDigite o codigo do produto que voce quer remover: ");
  scanf("%d", &id);
  catalogo[id - 1].active = False;
}


int registro_opcao = 0;

void opcoes_disponiveis() {
  printf("\n\nAs opcoes sao:\n\n");
  printf("1: LISTAR CATALOGO\n");
  printf("2: IHC_inserir_produto\n");
  printf("3: IHC_remover_produto\n");
  printf("4: IHC_atualizar_estoque\n");
  printf("5: IHC_aumentar_estoque\n");
  printf("6: IHC_diminuir_estoque\n");
  printf("7: SAIR DO PROGRAMA\n\n");

  printf("ESCOLHA: ");
  scanf("%d", &registro_opcao);

  switch (registro_opcao) {
  case 0:
    printf("\nErro");
    exit(0);

  case 1:
    listar_catalogo();
    break;

  case 2:
    novo_produto();
    break;
    
  case 3:
    remover_produto();
    break;
    
  case 4:
    atualizar_estoque();
    break;

  case 5:
    aumentar_estoque();
    break;

  case 6:
    dimuir_estoque();
    break;

  case 7:
    exit(0);

  default:
    break;
  }
}

int main() {
  while (1)
    opcoes_disponiveis();
  return 0;
}
