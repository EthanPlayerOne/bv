var request = require('request');

request('https://market.yandex.ru/catalog--portativnaia-akustika/26992430/list?clid=703&text=*JBL%20Charge%205&hid=2724669&rs=eJwzamIOYDzKyHBA0BZEPgSRCclgtrgdiBTYCyQbhEAiD67bAEmFT3tAIjNB4govQeIKJiARBneQyINvIHJBI0hkwSUQ22EeWO-O3SDTHMDqW8FmFoLZq8Cy6WAbN4F0JbCDTTgIUr_AGCx7D2zOXZDtDWdA7ISY_SByF1j8MUjNAg2w7QpgM5NswS4Ek1PBbl4KNqcCbEs7yBYFJ7A57CDZhIfWIJGbIDaDHljXdZCaB8fApj0Am8AAJiXBfv8JJk-CZBmEQOIHIP79BXahHdh3TPtA4j_APgoGu-0H2LRpYJN5wS4Hu2dBpy0A-xKQcw%2C%2C&local-offers-first=0', function (error, response, body) {
  if (!error && response.statusCode == 200) {
    console.log(body);
  }
});
