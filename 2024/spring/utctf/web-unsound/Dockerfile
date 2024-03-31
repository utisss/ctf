FROM ghcr.io/puppeteer/puppeteer:22.3.0

EXPOSE 9000

WORKDIR /var/www
COPY server/ /var/www
COPY wasm/pkg /var/www/pkg

USER root
RUN chown -R pptruser:pptruser /var/www

USER pptruser
RUN npm install
CMD /bin/bash -c "cd /var/www && node serve.js"
