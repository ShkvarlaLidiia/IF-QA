describe('Log in', () => {
    it('Sign in', () => {
        try {
            cy.visit('https://unsplash.com/');
            cy.contains('Log in').click();
            cy.get('input[type="email"]').type('stf125@gmail.com');
            cy.get('input[type="password"]').type('111');
            cy.get('input[type="submit"]').click();

        } catch (e) {
            console.log(e.message);
        }
    });
});
