# rag: build: badkoobeh

- uses [crawl/two/badkoobeh](../../crawl/two/badkoobeh.md)

🔥

```bash
@select $BLUER_AGENT_CRAWL_SINGLE_ROOT_TEST_OBJECT

@select corpus-badkoobeh-$(@@timestamp)

@rag build_corpus upload .. .

@upload public,zip .
```


```yaml
crawl:
  https://badkoobeh.com/:
  - https://badkoobeh.com
  - https://badkoobeh.com/projects/
  - https://badkoobeh.com/services/
  - https://badkoobeh.com/about-us/
  - https://badkoobeh.com/clients/
  - https://badkoobeh.com/careers/
  - https://badkoobeh.com/contact/
  - https://badkoobeh.com/blog/
  - https://badkoobeh.com/casestudy/
  - https://badkoobeh.com/works/%da%a9%d8%a7%d8%b1-%d8%ad%d8%b1%d9%81%d9%87-%d8%a7%db%8c%d8%8c-%d8%a7%d8%a8%d8%b2%d8%a7%d8%b1-%d8%ad%d8%b1%d9%81%d9%87-%d8%a7%db%8c-%d9%85%db%8c-%d8%ae%d9%88%d8%a7%d9%87%d8%af/
  - https://badkoobeh.com/case/%d9%be%d8%b1%d9%88%d9%85%da%a9%d8%b3/
  - https://badkoobeh.com/case/%da%a9%d8%a7%d9%81%d9%87-%d8%a8%d8%a7%d8%b2%d8%a7%d8%b1/
  - https://badkoobeh.com/case/%da%a9%d8%b4%da%a9%d8%a7%d9%85/
  - https://badkoobeh.com/projectcat/%d8%aa%d9%84%d9%88%db%8c%d8%b2%db%8c%d9%88%d9%86-%d8%b1%d8%a7%d8%af%db%8c%d9%88/
  - https://badkoobeh.com/projectcat/%da%86%d8%a7%d9%be/
  - https://badkoobeh.com/projectcat/%d8%af%db%8c%d8%ac%db%8c%d8%aa%d8%a7%d9%84/
  - https://badkoobeh.com/projectcat/%d8%b1%d9%88%d8%b2%d9%86%d8%a7%d9%85%d9%87-%d9%88-%d9%85%d8%ac%d9%84%d9%87/
  - https://badkoobeh.com/projectcat/%d8%b1%d9%88%db%8c%d8%af%d8%a7%d8%af/
  - https://badkoobeh.com/projectcat/%d8%b3%d8%a7%db%8c%d8%b1/
  - https://badkoobeh.com/projectcat/%d9%85%d8%ad%db%8c%d8%b7%db%8c/
  - https://badkoobeh.com/works/%d8%a2%d8%b1%db%8c%d9%86-%d9%85%d9%88%d8%aa%d9%88%d8%b1/
  - https://badkoobeh.com/works/%d8%a8%d8%b1%d9%86%d8%af-%d8%a7%da%a9%d8%aa%db%8c%d9%88%db%8c%d8%b4%d9%86-%d9%85%da%a9%d8%b1%d8%b1/
  - https://badkoobeh.com/works/%d8%a8%d8%a7-%da%af%d8%a7%d8%b2-%d8%af%d8%a7%d8%aa%db%8c%d8%b3-%d8%a8%d8%ac%d9%88%d8%b4%db%8c%d8%af/
  - https://badkoobeh.com/works/%d8%a7%d9%85%d8%aa%d8%ad%d8%a7%d9%86%d8%b4-%d8%b1%d9%88-%d9%be%d8%b3-%d8%af%d8%a7%d8%af%d9%87/
  - https://badkoobeh.com/works/%d8%b1%d9%88%d8%ba%d9%86-%d9%85%d9%88%d8%aa%d9%88%d8%b1-%d8%a8%d8%b1%d8%a7%db%8c-%d9%86%d8%b3%d9%84-%d8%ac%d8%af%db%8c%d8%af-%d8%ae%d9%88%d8%af%d8%b1%d9%88/
  - https://badkoobeh.com/works/%da%af%d8%b1%d8%af%d9%87%d9%85%d8%a7%db%8c%db%8c-%d9%87%d9%85%d8%b1%d8%a7%d9%87%d8%a7%d9%86-%d8%b4%d9%88%d8%af%d8%b1/
  - https://badkoobeh.com/works/%d8%a8%d9%87-%d8%ae%d9%88%d8%af%d8%aa-%d9%86%d9%87-%d9%86%da%af%d9%88/
  - https://badkoobeh.com/works/%d9%81%d8%b1%d8%b5%d8%aa-%d9%87%d8%a7%db%8c-%d8%a8%d8%b1-%d8%a2%d8%a8-%d8%b1%d9%81%d8%aa%d9%87/
  - https://badkoobeh.com/works/%d9%81%d8%b1%d8%b5%d8%aa-%d9%87%d8%a7%db%8c-%d8%a8%d8%b1-%d8%a2%d8%a8-%d8%b1%d9%81%d8%aa%d9%87-2/
  - https://badkoobeh.com/works/3-%d9%81%d8%b1%d8%b5%d8%aa-%d9%87%d8%a7%db%8c-%d8%a8%d8%b1-%d8%a2%d8%a8-%d8%b1%d9%81%d8%aa%d9%87/
  - https://badkoobeh.com/works/4-%d9%81%d8%b1%d8%b5%d8%aa-%d9%87%d8%a7%db%8c-%d8%a8%d8%b1-%d8%a2%d8%a8-%d8%b1%d9%81%d8%aa%d9%87/
  - https://badkoobeh.com/%d9%85%d8%b7%d8%a7%d9%84%d8%b9%d8%a7%d8%aa-%d9%85%d9%88%d8%b1%d8%af%db%8c/
  - https://badkoobeh.com/case/%d9%81%d9%88%d9%84-%d8%aa%d8%a7%db%8c%d9%85/
  - https://badkoobeh.com/Capabilities/%d9%be%db%8c%d8%b4%d8%b1%d8%a7%d9%86-%d9%81%d8%b1%d9%88%d8%b4-%d9%88-%d8%aa%d8%b1%d9%88%db%8c%d8%ac-%d8%a8%d8%b1%d9%86%d8%af/
  - https://badkoobeh.com/Capabilities/%d8%a8%d8%a7%d8%b2%d8%a7%d8%b1%db%8c%d8%a7%d8%a8%db%8c-%d9%88-%d8%a8%d8%b1%d9%86%d8%af%d8%b3%d8%a7%d8%b2%db%8c/
  - https://badkoobeh.com/Capabilities/%d9%85%d8%b4%d8%a7%d9%88%d8%b1%d9%87-%d8%aa%d8%a8%d9%84%db%8c%d8%ba%d8%a7%d8%aa/
  - https://badkoobeh.com/Capabilities/%d8%b1%d9%88%d8%a7%d8%a8%d8%b7-%d8%b9%d9%85%d9%88%d9%85%db%8c/
  - https://badkoobeh.com/Capabilities/%d8%aa%d9%88%d8%a7%d9%86%d9%85%d9%86%d8%af-%d8%b3%d8%a7%d8%b2%db%8c-%d9%be%d8%b1%d8%b3%d9%86%d9%84-%d8%a8%d8%b1%d9%86%d8%af%d9%87%d8%a7-%d8%a7%d8%b2-%d8%b7%d8%b1%db%8c%d9%82-%d8%a8%d8%b1%da%af/
  - https://badkoobeh.com/Capabilities/%d8%b1%d8%a7%d9%87%da%a9%d8%a7%d8%b1%d9%87%d8%a7%db%8c-%d8%a7%d8%b3%d8%aa%d8%b1%d8%a7%d8%aa%da%98%db%8c%d8%8c-%d8%a8%d8%a7%d8%b2%d8%a7%d8%b1%db%8c%d8%a7%d8%a8%db%8c-%d9%88-%d9%81%d8%b1%d9%88%d8%b4/
  - https://badkoobeh.com/Capabilities/%d8%ae%d8%af%d9%85%d8%a7%d8%aa-%d8%aa%d8%a8%d9%84%db%8c%d8%ba%d8%a7%d8%aa%db%8c-btl/
  - https://badkoobeh.com/Capabilities/%d8%a7%db%8c%d8%af%d9%87%d9%be%d8%b1%d8%af%d8%a7%d8%b2%db%8c-%d8%aa%d8%a8%d9%84%db%8c%d8%ba%d8%a7%d8%aa%db%8c/
  - https://badkoobeh.com/Capabilities/%d8%b1%d8%a7%d9%87%da%a9%d8%a7%d8%b1%d9%87%d8%a7%db%8c-%d8%a8%d8%a7%d8%b2%d8%a7%d8%b1%db%8c%d8%a7%d8%a8%db%8c-%d8%af%db%8c%d8%ac%db%8c%d8%aa%d8%a7%d9%84/
  - https://badkoobeh.com/Capabilities/%d8%a8%d8%b1%d9%86%d8%a7%d9%85%d9%87-%d8%b1%db%8c%d8%b2%db%8c-%d8%b1%d8%b3%d8%a7%d9%86%d9%87/
  - https://badkoobeh.com/Capabilities/%d8%b1%d8%b3%d8%a7%d9%86%d9%87%d9%87%d8%a7%db%8c-%d9%86%d9%88%db%8c%d9%86-2/
  - https://badkoobeh.com/Capabilities/%d8%a2%da%af%d9%87%db%8c%d9%87%d8%a7%db%8c-%d8%aa%d9%84%d9%88%db%8c%d8%b2%db%8c%d9%88%d9%86%db%8c/
  - https://badkoobeh.com/Capabilities/%d8%aa%d9%88%d9%84%db%8c%d8%af-%d9%85%d8%ad%d8%aa%d9%88%d8%a7%db%8c-%d8%ae%d9%84%d8%a7%d9%82/
  - https://badkoobeh.com/Capabilities/%d8%aa%d8%ad%d9%82%db%8c%d9%82%d8%a7%d8%aa-%d8%a8%d8%a7%d8%b2%d8%a7%d8%b1/
  - https://badkoobeh.com/360-ad-campaign-guide/
  - https://badkoobeh.com/visual-brand-identity/
  - https://badkoobeh.com/common-marketing-mistakes/
  - https://badkoobeh.com/how-to-be-visible-online-with-low-budget/
  - https://badkoobeh.com/brand-building-guide/
  - https://badkoobeh.com/clients/%d8%b4%db%8c%d8%b1%d8%a2%d9%84%d8%a7%d8%aa-%d8%b3%d8%a7%d8%ae%d8%aa%d9%85%d8%a7%d9%86%db%8c-%d8%b4%d9%88%d8%af%d8%b1/
  - https://badkoobeh.com/clients/%d8%aa%d9%88%d8%b3%d9%86/
  - https://badkoobeh.com/clients/%d8%a7%d9%84-%d8%ac%db%8c-lg/
  - https://badkoobeh.com/clients/%d8%a8%db%8c%d9%85%d9%87-%d8%af%db%8c/
  - https://badkoobeh.com/clients/%d9%87%d9%85%d8%b1%d8%a7%d9%87-%d8%a7%d9%88%d9%84/
  - https://badkoobeh.com/clients/%d9%87%d9%81-%d9%87%d8%b4%d8%aa%d8%a7%d8%af/
  - https://badkoobeh.com/clients/%d8%b4%d8%a7%d9%88%d9%85%d8%a7/
  - https://badkoobeh.com/clients/%d9%85%d8%a7%db%8c-%d9%84%db%8c%d8%af%db%8c/
  - https://badkoobeh.com/clients/%db%8c%d9%88%d9%86%db%8c%d9%84%db%8c%d9%88%d8%b1/
  - https://badkoobeh.com/clients/%d9%86%d8%b3%d8%aa%d9%84%d9%87-%d9%be%db%8c%d9%88%d8%b1%d9%84%d8%a7%db%8c%d9%81/
  - https://badkoobeh.com/clients/%d9%81%d8%a7%d9%85%db%8c%d9%84%d8%a7/
  - https://badkoobeh.com/clients/%d8%a2%d8%b1%db%8c%d9%86-%d9%85%d9%88%d8%aa%d9%88%d8%b1/
  - https://badkoobeh.com/clients/%d9%87%d9%81%d8%aa-%d9%88-%d8%b3%db%8c/
  - https://badkoobeh.com/clients/%d9%85%d8%a8%db%8c%d9%86-%d9%86%d8%aa/
  - https://badkoobeh.com/clients/%da%af%d8%b1%d9%88%d9%87-%d8%aa%d8%b9%d8%a7%d9%88%d9%86%db%8c-%d9%be%db%8c%d8%b4%da%af%d8%a7%d9%85%d8%a7%d9%86/
  - https://badkoobeh.com/clients/%d8%b4%d8%a7%d8%aa%d9%84/
  - https://badkoobeh.com/clients/%d9%85%d8%a7%db%8c%da%a9%d8%aa/
  - https://badkoobeh.com/clients/%d8%a7%db%8c%d8%b1%d8%a7%d9%86%d8%b3%d9%84/
  - https://badkoobeh.com/clients/%d8%a2%db%8c-%d8%af%db%8c-%d9%be%db%8c/
  - https://badkoobeh.com/clients/%d8%af%db%8c%d9%88%d8%a7%d8%b1/
  - https://badkoobeh.com/clients/%d8%a2%d8%b3%d8%a7%d9%86-%d9%be%d8%b1%d8%af%d8%a7%d8%ae%d8%aa/
  - https://badkoobeh.com/clients/%d8%aa%d8%ac%d9%87%db%8c%d8%b2%d8%a7%d8%aa-%d8%af%d8%a7%d9%86%d8%a7/
  - https://badkoobeh.com/clients/%d8%aa%d8%b6%d9%85%db%8c%d9%86-%da%86%db%8c/
  - https://badkoobeh.com/clients/%d9%85%d9%88%d8%b3%d8%b3%d9%87-%d8%ae%db%8c%d8%b1%db%8c%d9%87-%d8%a8%d9%87%d9%86%d8%a7%d9%85-%d8%af%d9%87%d8%b4-%d9%be%d9%88%d8%b1/
  - https://badkoobeh.com/clients/%d9%85%d9%87%d8%b1-%d9%85%d8%a7%d9%86%d8%af%da%af%d8%a7%d8%b1/
  - https://badkoobeh.com/clients/%d8%b4%d8%b1%da%a9%d8%aa-%d8%aa%d9%88%d8%b2%db%8c%d8%b9-%d9%86%db%8c%d8%b1%d9%88%db%8c-%d8%a8%d8%b1%d9%82-%d8%aa%d9%87%d8%b1%d8%a7%d9%86-%d8%a8%d8%b2%d8%b1%da%af/
  - https://badkoobeh.com/clients/%d8%b4%d9%87%d8%b1%d8%af%d8%a7%d8%b1%db%8c-%d8%aa%d9%87%d8%b1%d8%a7%d9%86/
  - https://badkoobeh.com/clients/%d8%a2%d8%a8-%d9%86%db%8c%d8%b1%d9%88/
  - https://badkoobeh.com/clients/%d9%85%d8%a4%d8%b3%d8%b3%d9%87-%d8%ae%db%8c%d8%b1%db%8c%d9%87-%da%a9%d9%87%d8%b1%db%8c%d8%b2%da%a9/
  - https://badkoobeh.com/clients/%d8%af%d8%a7%d9%86%d8%b4%da%af%d8%a7%d9%87-%d8%a2%d8%b2%d8%a7%d8%af/
  - https://badkoobeh.com/clients/%d8%a7%d9%86%d8%ac%d9%85%d9%86-%d9%82%d9%82%d9%86%d9%88%d8%b3/
  - https://badkoobeh.com/clients/%da%a9%d9%85%db%8c%d8%aa%d9%87-%d8%a7%d9%85%d8%af%d8%a7%d8%af-%d8%a7%d9%85%d8%a7%d9%85-%d8%ae%d9%85%db%8c%d9%86%db%8c-%d8%b1%d9%87/
  - https://badkoobeh.com/clients/%d9%85%d8%ad%da%a9/
  - https://badkoobeh.com/clients/%d8%a7%d9%86%d8%ac%d9%85%d9%86-%d8%ae%db%8c%d8%b1%db%8c%d9%87-%d8%a7%d8%aa%db%8c%d8%b3%d9%85-%d8%a7%db%8c%d8%b1%d8%a7%d9%86/
  - https://badkoobeh.com/clients/%d8%a8%d8%ae%d8%b4%d8%b4/
  - https://badkoobeh.com/clients/%d8%a7%d8%b1%d9%81%da%a9/
  - https://badkoobeh.com/clients/%d8%ac%d9%85%d8%b9%db%8c%d8%aa-%d8%b7%d9%84%d9%88%d8%b9-%d8%a8%db%8c-%d9%86%d8%b4%d8%a7%d9%86-%d9%87%d8%a7/
  - https://badkoobeh.com/clients/%d8%a7%d9%86%d8%ac%d9%85%d9%86-%d8%a7%d9%87%d8%af%d8%a7%db%8c-%d8%b9%d8%b6%d9%88-%d8%a7%db%8c%d8%b1%d8%a7%d9%86%db%8c%d8%a7%d9%86/
  - https://badkoobeh.com/clients/%d9%88%d8%b2%d8%a7%d8%b1%d8%aa-%d9%88%d8%b1%d8%b2%d8%b4-%d9%88-%d8%ac%d9%88%d8%a7%d9%86%d8%a7%d9%86/
  - https://badkoobeh.com/clients/%d8%b4%d8%a8%da%a9%d9%87-%d8%a2%d9%85%d9%88%d8%b2%d8%b4-%d8%b3%db%8c%d9%85%d8%a7/
  - https://badkoobeh.com/clients/%d9%85%d8%b1%da%a9%d8%b2-%d8%aa%d9%88%d8%b3%d8%b9%d9%87-%d9%81%d9%86%d8%a7%d9%88%d8%b1%db%8c-%d8%a7%d8%b7%d9%84%d8%a7%d8%b9%d8%a7%d8%aa-%d9%88-%d8%b1%d8%b3%d8%a7%d9%86%d9%87-%d9%87%d8%a7%db%8c/
  - https://badkoobeh.com/clients/%d8%b5%d8%af%d8%a7-%d9%88-%d8%b3%db%8c%d9%85%d8%a7/
  - https://badkoobeh.com/clients/%d9%85%d9%88%d8%b3%d8%b3%d9%87-%d9%81%d8%b1%d9%87%d9%86%da%af%db%8c-%d9%87%d9%86%d8%b1%db%8c-%d8%b1%d9%88%d8%b2%da%af%d8%a7%d8%b1-%d8%b7%d8%b1%d9%81%d9%87/
  - https://badkoobeh.com/clients/%d8%b4%d8%b1%da%a9%d8%aa-%d9%85%d8%ae%d8%a7%d8%a8%d8%b1%d8%a7%d8%aa-%d8%a7%db%8c%d8%b1%d8%a7%d9%86/
  - https://badkoobeh.com/clients/%db%8c%d9%88%d9%86%db%8c%d8%b3%d9%81-unicef/
  - https://badkoobeh.com/clients/%d9%85%d9%88%d8%b3%d8%b3%d9%87-%d8%ae%db%8c%d8%b1%db%8c%d9%87-%d8%b2%d9%86%d8%ac%db%8c%d8%b1%d9%87-%d8%a7%d9%85%db%8c%d8%af/
  - https://badkoobeh.com/clients/%d8%a7%d9%86%d8%aa%d8%b4%d8%a7%d8%b1%d8%a7%d8%aa-%d8%a8%db%8c%d9%86-%d8%a7%d9%84%d9%85%d9%84%d9%84%db%8c-%da%af%d8%a7%d8%ac/
  - https://badkoobeh.com/clients/%d9%85%d8%af%d8%b1%d8%b3%d8%a7%d9%86-%d8%b4%d8%b1%db%8c%d9%81/

```

```yaml
crawl:
  source: crawl-badkoobeh-2026-02-04-17-17-42-by7jdk

```

[corpus-badkoobeh-2026-02-04-3attre.tar.gz](https://kamangir-public.s3.ir-thr-at1.arvanstorage.ir/corpus-badkoobeh-2026-02-04-3attre.tar.gz)
