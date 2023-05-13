describe('Cenário de teste: Testar funcionalidade do botao de inicio', () => {
  it('Caso de teste: Ir para a etapa seguinte (filtro de indicação).', () => {
      cy.visit('http://localhost:8080/');
      cy.get('button').click();
      //expect(arguments).to.be.arguments;
      //expect(URL).to.be.equal('localhost:8080/Vamos-la');
  })
})