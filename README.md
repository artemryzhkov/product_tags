## Description 

```text
The service allows you to highlight tags among a variety of product names. This can be useful for selecting filters or for categorizing a list of products.
```

## Start:

```bash
docker build -t product-tags .
docker run -d --restart unless-stopped \
           -p 4444:4444 \
           --name product-tags product-tags
```

## Example

To work correctly, JSON must contain all available products.
```bash
curl -i -H "Content-Type: application/json" -X POST -d '{"items": [{"id_product":432,"name_product":"Bio Zitronen 500g Netz (Italien)"}, {"id_product":243, "name_product":"Bio Zitronen 1 Stk. (grünlich, Chile)"}, {"id_product":123, "name_product":"Bio Zitronen 500g Netz (Spanien)"}, {"id_product":123, "name_product":"Frische Laktosefreie Milch"}, {"id_product":123, "name_product":"Arla Frische Laktosefreie Milch"}, {"id_product":123, "name_product":"Eipro Bio Eier"}, {"id_product":123, "name_product":"Eier Bruderhahn"}, {"id_product":123, "name_product":"Rewe Eier"}]}' http://localhost:4444/tags
```