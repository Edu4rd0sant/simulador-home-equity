# 🏦 Simulador de Home Equity (Lead Gen)

> Interface de captura de leads otimizada para campanhas de Crédito com Garantia de Imóvel (CGI/Home Equity). Focada em UX bancário e validação de regras de negócio no frontend.

## 🎯 Objetivo do Projeto
Este projeto visa resolver um problema comum em campanhas de tráfego para crédito: a geração de leads desqualificados. O simulador atua como um filtro ativo, educando o usuário sobre o limite de crédito (LTV) antes mesmo do lead ser enviado.

## ✨ Funcionalidades Principais

* **Regra de Negócio (LTV) em Tempo Real:** Implementação de lógica JS que limita o crédito solicitado a 60% do valor do imóvel (regra de mercado para Home Equity).
* **Formulário Condicional:** Campos de "Saldo Devedor" e "Banco Financiador" aparecem apenas se o usuário indicar que o imóvel não está quitado.
* **Integração Híbrida:**
    * **Frontend:** Disparo de eventos para Meta Ads (`fbq track Lead`).
    * **Backend:** Envio de dados para API proprietária (PHP/SQL) e redirecionamento para WhatsApp Business.
* **UX/UI Responsiva:** Barra de progresso visual e máscaras de input (R$ e Telefone) para facilitar a digitação mobile.

## 🛠️ Tecnologias Utilizadas
* HTML5 & CSS3
* JavaScript (Vanilla)
* Integração Meta Pixel (Events Manager)

## 🚀 Como usar
1.  Clone o repositório.
2.  Abra o arquivo `index.html` no navegador.
3.  **Nota:** Para funcionar a integração de API, é necessário configurar um endpoint backend ou alterar a URL no script para um serviço de testes (ex: Webhook.site).

## ⚠️ Disclaimer e Segurança
Este é um projeto de portfólio.
* **Dados Sensíveis:** Todas as credenciais reais (Pixel ID, Tokens de API, Telefones Corporativos) foram removidas ou substituídas por dados genéricos (`SEU_PIXEL_ID`, etc.) para segurança da informação.
* **Propriedade:** A lógica apresentada aqui é de autoria própria, focada na estrutura de captação, sem expor regras de crédito confidenciais da instituição financeira.

---
Desenvolvido por Eduardo Santos- Gestor de Tráfego & Desenvolvedor