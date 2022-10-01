#include <math.h>
#include <stdio.h>
double obter_coeficiente(char frase[30]) {
  double aux;
  printf("%s", frase);
  scanf("%lf", &aux);
  return aux;
};
double calcular_delta(double coef_a, double coef_b, double coef_c) {
  double delta = pow(coef_b, 2) - (4 * coef_a * coef_c);
  return delta;
};
int responder_sem_raiz() {
  puts("A equação não possui raízes reais");
  return 0;
}
int responder_uma_raiz(double coef_a, double coef_b) {
  double raiz = -coef_b / (2 * coef_a);
  printf("A equação possui apenas uma raiz: %.6f.", raiz);
  return 0;
}
int responder_duas_raizes(double coef_a, double coef_b, double delta) {
  double raiz1 = (-coef_b + sqrt(delta)) / (2 * coef_a);
  double raiz2 = (-coef_b - sqrt(delta)) / (2 * coef_a);
  printf("A equação possui duas raízes %.6f e %.6f", raiz1, raiz2);
  return 0;
}
int main() {
  printf("Forma geral da equação do segundo grau: a x**2 + b x + c = 0\n");
  double coef_a = obter_coeficiente("Digite o coeficiente a: ");
  if (coef_a == 0) {
    printf("O coeficiente a não pode ser zero!\n");
    return 0;
  }
  double coef_b = obter_coeficiente("Digite o coeficiente b: ");
  double coef_c = obter_coeficiente("Digite o coeficiente c: ");
  double delta = calcular_delta(coef_a, coef_b, coef_c);
  if (delta < 0)
    responder_sem_raiz();
  else if (delta == 0)
    responder_uma_raiz(coef_a, coef_b);
  else
    responder_duas_raizes(coef_a, coef_b, delta);
  return 0;
}
