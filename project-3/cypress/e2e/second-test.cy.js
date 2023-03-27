describe ('flymark', () => {
    it('passes', () => {
        try {
            cy.visit('https://flymark.com.ua/');
            cy.get('.b-usermenu-list-item__link').eq(3).click();
            cy.get('#mat-input-0').type('Шкварла{enter}');
        } catch (e) {
            console.log(e.message);
        }
    })
});

