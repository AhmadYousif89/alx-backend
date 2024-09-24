import { expect, use, request } from 'chai';
import chaiHttp from 'chai-http';
import app from './9-stock';

use(chaiHttp);

describe('Stock API', () => {
  describe('GET /list_products', () => {
    it('should return all products', (done) => {
      request(app)
        .get('/list_products')
        .end((err, res) => {
          expect(res).to.have.status(200);
          expect(res.body).to.be.an('array');
          expect(res.body).to.have.lengthOf(4);
          done();
        });
    });
  });

  describe('GET /list_products/:itemId', () => {
    it('should return a specific product', (done) => {
      request(app)
        .get('/list_products/1')
        .end((err, res) => {
          expect(res).to.have.status(200);
          expect(res.body).to.be.an('object');
          expect(res.body).to.have.property('id', 1);
          expect(res.body).to.have.property('currentQuantity');
          done();
        });
    });

    it('should return 404 for non-existent product', (done) => {
      request(app)
        .get('/list_products/999')
        .end((err, res) => {
          expect(res).to.have.status(404);
          expect(res.body).to.have.property('status', 'Product not found');
          done();
        });
    });
  });

  describe('GET /reserve_product/:itemId', () => {
    it('should reserve a product', (done) => {
      request(app)
        .get('/reserve_product/2')
        .end((err, res) => {
          expect(res).to.have.status(200);
          expect(res.body).to.have.property('status', 'Reservation confirmed');
          expect(res.body).to.have.property('itemId', 2);
          done();
        });
    });

    it('should return 403 when stock is not available', (done) => {
      // Assuming item 3 has only 2 in stock, we'll reserve it twice
      request(app)
        .get('/reserve_product/3')
        .end(() => {
          request(app)
            .get('/reserve_product/3')
            .end(() => {
              request(app)
                .get('/reserve_product/3')
                .end((err, res) => {
                  expect(res).to.have.status(403);
                  expect(res.body).to.have.property(
                    'status',
                    'Not enough stock available',
                  );
                  expect(res.body).to.have.property('itemId', 3);
                  done();
                });
            });
        });
    });

    it('should return 404 for non-existent product', (done) => {
      request(app)
        .get('/reserve_product/999')
        .end((err, res) => {
          expect(res).to.have.status(404);
          expect(res.body).to.have.property('status', 'Product not found');
          done();
        });
    });
  });
});
