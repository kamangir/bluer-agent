# rag: build: hnpagency

- uses [crawl/two/hnpagency](../../crawl/two/hnpagency.md)

🔥

```bash
@select crawl-hnpagency-2026-02-04-17-17-32-d24z45

@select corpus-hnpagency-$(@@timestamp)

@rag build_corpus upload .. .

@upload public,zip .
```



<details>
<summary>crawl metadata</summary>

```yaml
crawl:
  https://hnpagency.com/:
  - https://hnpagency.com
  - https://hnpagency.com/outdoormedia/
  - https://hnpagency.com/boards-category/%d8%a8%db%8c%d9%84%d8%a8%d9%88%d8%b1%d8%af/
  - https://hnpagency.com/boards-category/%d8%b9%d8%b1%d8%b4%d9%87-%d9%be%d9%84/
  - https://hnpagency.com/hnp-lightboard/
  - https://hnpagency.com/boards/lightboard-package-a-sadr-highway/
  - https://hnpagency.com/boards-category/%d9%84%d8%a7%db%8c%d8%aa-%d8%a8%d8%b1%d8%af/
  - https://hnpagency.com/boards/%d8%b9%d8%b1%d8%b4%d9%87-%d9%be%d9%84-bp34-%d9%85%d8%ad%d9%88%d8%b1-%d9%87%d9%85%d8%aa/
  - https://hnpagency.com/boards/%d8%b9%d8%b1%d8%b4%d9%87-%d9%be%d9%84-bp35-%d9%85%d8%ad%d9%88%d8%b1-%d9%87%d9%85%d8%aa/
  - https://hnpagency.com/boards/%d8%b9%d8%b1%d8%b4%d9%87-%d9%be%d9%84-ep17-%d9%85%d8%ad%d9%88%d8%b1-%da%86%d9%85%d8%b1%d8%a7%d9%86/
  - https://hnpagency.com/boards/%d8%a8%db%8c%d9%84%d8%a8%d9%88%d8%b1%d8%af-ep37-%d9%85%d8%ad%d9%88%d8%b1-%da%86%d9%85%d8%b1%d8%a7%d9%86/
  - https://hnpagency.com/boards/%d8%b9%d8%b1%d8%b4%d9%87-%d9%be%d9%84-dp1-%d9%85%d8%ad%d9%88%d8%b1-%d8%b5%d8%af%d8%b1/
  - https://hnpagency.com/boards/%d8%b9%d8%b1%d8%b4%d9%87-%d9%be%d9%84-kp10-%d9%85%d8%ad%d9%88%d8%b1-%d9%86%db%8c%d8%a7%db%8c%d8%b4/
  - https://hnpagency.com/boards/%d8%b9%d8%b1%d8%b4%d9%87-%d9%be%d9%84-kp11-%d9%85%d8%ad%d9%88%d8%b1-%d9%86%db%8c%d8%a7%db%8c%d8%b4/
  - https://hnpagency.com/boards-category/%d9%85%d9%88%d9%82%d8%b9%db%8c%d8%aa/
  - https://hnpagency.com/services/
  - https://hnpagency.com/about-us/
  - https://hnpagency.com/category/news/
  - https://hnpagency.com/category/the-best-of-month/
  - https://hnpagency.com/category/review/
  - https://hnpagency.com/contact-us/
  - https://hnpagency.com/hnp-academy/
  - https://hnpagency.com/outdoormedia/02188882525
  - https://hnpagency.com/boards/%d8%a8%db%8c%d9%84%d8%a8%d9%88%d8%b1%d8%af-n13-%d8%b3%d8%b9%d8%a7%d8%af%d8%aa-%d8%a2%d8%a8%d8%a7%d8%af/
  - https://hnpagency.com/boards/%d8%a8%db%8c%d9%84%d8%a8%d9%88%d8%b1%d8%af-n14-%d8%b3%d8%b9%d8%a7%d8%af%d8%aa-%d8%a2%d8%a8%d8%a7%d8%af/
  - https://hnpagency.com/boards/%d8%a8%db%8c%d9%84%d8%a8%d9%88%d8%b1%d8%af-c24-%d9%85%d8%ad%d9%88%d8%b1-%d8%a7%d9%85%d8%a7%d9%85-%d8%b9%d9%84%db%8c/
  - https://hnpagency.com/boards/%d8%a8%db%8c%d9%84%d8%a8%d9%88%d8%b1%d8%af-f44-%d9%85%d8%ad%d9%88%d8%b1-%d8%aa%d9%87%d8%b1%d8%a7%d9%86-%d9%82%d9%85/
  - https://hnpagency.com/boards/%d8%a8%db%8c%d9%84%d8%a8%d9%88%d8%b1%d8%af-f47-%d9%85%d8%ad%d9%88%d8%b1-%d9%82%d9%85-%d8%aa%d9%87%d8%b1%d8%a7%d9%86/
  - https://hnpagency.com/boards/%d8%a8%db%8c%d9%84%d8%a8%d9%88%d8%b1%d8%af-kt3-%d9%85%d8%ad%d9%88%d8%b1-%da%a9%d8%b1%d8%ac-%d8%aa%d9%87%d8%b1%d8%a7%d9%86/
  - https://hnpagency.com/boards/bridge-board-niayesh-kp26/
  - https://hnpagency.com/boards/bridge-board-niayesh-kp27/
  - https://hnpagency.com/boards/%d8%b9%d8%b1%d8%b4%d9%87-%d9%be%d9%84-bp14-%d9%85%d8%ad%d9%88%d8%b1-%d8%b4%db%8c%d8%ae-%d9%81%d8%b6%d9%84-%d8%a7%d9%84%d9%84%d9%87/
  - https://hnpagency.com/boards/%d8%b9%d8%b1%d8%b4%d9%87-%d9%be%d9%84-bp15-%d9%85%d8%ad%d9%88%d8%b1-%d8%b4%db%8c%d8%ae-%d9%81%d8%b6%d9%84-%d8%a7%d9%84%d9%84%d9%87/
  - https://hnpagency.com/boards/%d8%b9%d8%b1%d8%b4%d9%87-%d9%be%d9%84-p59-%d9%85%d8%ad%d9%88%d8%b1-%d8%b5%db%8c%d8%a7%d8%af-%d8%b4%db%8c%d8%b1%d8%a7%d8%b2%db%8c/
  - https://hnpagency.com/boards/%d8%b9%d8%b1%d8%b4%d9%87-%d9%be%d9%84-p57-%d9%85%d8%ad%d9%88%d8%b1-%d8%b3%d8%aa%d8%a7%d8%b1%db%8c-%d9%85%d8%ac%d8%aa%d9%85%d8%b9-%da%a9%d9%88%d8%b1%d9%88%d8%b4/
  - https://hnpagency.com/boards/%d8%b9%d8%b1%d8%b4%d9%87-%d9%be%d9%84-ep38-%d9%85%d8%ad%d9%88%d8%b1-%db%8c%d8%a7%d8%af%da%af%d8%a7%d8%b1-%d8%a7%d9%85%d8%a7%d9%85/
  - https://hnpagency.com/boards/%d8%b9%d8%b1%d8%b4%d9%87-%d9%be%d9%84-kp14-%d9%85%d8%ad%d9%88%d8%b1-%d9%85%db%8c%d8%b1%d8%af%d8%a7%d9%85%d8%a7%d8%af/
  - https://hnpagency.com/boards/%d8%b9%d8%b1%d8%b4%d9%87-%d9%be%d9%84-kp15-%d9%85%d8%ad%d9%88%d8%b1-%d9%85%db%8c%d8%b1%d8%af%d8%a7%d9%85%d8%a7%d8%af/
  - https://hnpagency.com/boards-category/%D8%B9%D8%B1%D8%B4%D9%87-%D9%BE%D9%84/page/2/
  - https://hnpagency.com/hnp-lightboard/02188882525
  - https://hnpagency.com/boards/lightboard-package-a-sadr-highway/02188882525
  - https://hnpagency.com/boards-category/%d9%86%d9%88%d8%b9-%d8%b1%d8%b3%d8%a7%d9%86%d9%87/
  - https://hnpagency.com/boards/%d8%b9%d8%b1%d8%b4%d9%87-%d9%be%d9%84-bp34-%d9%85%d8%ad%d9%88%d8%b1-%d9%87%d9%85%d8%aa/02188882525
  - https://hnpagency.com/boards/%d8%b9%d8%b1%d8%b4%d9%87-%d9%be%d9%84-bp35-%d9%85%d8%ad%d9%88%d8%b1-%d9%87%d9%85%d8%aa/02188882525
  - https://hnpagency.com/boards/%d8%b9%d8%b1%d8%b4%d9%87-%d9%be%d9%84-ep17-%d9%85%d8%ad%d9%88%d8%b1-%da%86%d9%85%d8%b1%d8%a7%d9%86/02188882525
  - https://hnpagency.com/boards/%d8%a8%db%8c%d9%84%d8%a8%d9%88%d8%b1%d8%af-ep37-%d9%85%d8%ad%d9%88%d8%b1-%da%86%d9%85%d8%b1%d8%a7%d9%86/02188882525
  - https://hnpagency.com/boards/%d8%b9%d8%b1%d8%b4%d9%87-%d9%be%d9%84-dp1-%d9%85%d8%ad%d9%88%d8%b1-%d8%b5%d8%af%d8%b1/02188882525
  - https://hnpagency.com/boards/%d8%b9%d8%b1%d8%b4%d9%87-%d9%be%d9%84-kp10-%d9%85%d8%ad%d9%88%d8%b1-%d9%86%db%8c%d8%a7%db%8c%d8%b4/02188882525
  - https://hnpagency.com/boards/%d8%b9%d8%b1%d8%b4%d9%87-%d9%be%d9%84-kp11-%d9%85%d8%ad%d9%88%d8%b1-%d9%86%db%8c%d8%a7%db%8c%d8%b4/02188882525
  - https://hnpagency.com/boards-category/%D9%85%D9%88%D9%82%D8%B9%DB%8C%D8%AA/page/2/
  - https://hnpagency.com/boards-category/%D9%85%D9%88%D9%82%D8%B9%DB%8C%D8%AA/page/3/
  - https://hnpagency.com/services/02188882525
  - https://hnpagency.com/about-us/02188882525
  - https://hnpagency.com/modern-h-n-p-lightboard/
  - https://hnpagency.com/contact-us/02188882525
  - https://hnpagency.com/contact-us/09129586040
  - https://hnpagency.com/hnp-academy/02188882525
  - https://hnpagency.com/boards/%d8%a8%db%8c%d9%84%d8%a8%d9%88%d8%b1%d8%af-n13-%d8%b3%d8%b9%d8%a7%d8%af%d8%aa-%d8%a2%d8%a8%d8%a7%d8%af/02188882525
  - https://hnpagency.com/boards/%d8%a8%db%8c%d9%84%d8%a8%d9%88%d8%b1%d8%af-n14-%d8%b3%d8%b9%d8%a7%d8%af%d8%aa-%d8%a2%d8%a8%d8%a7%d8%af/02188882525
  - https://hnpagency.com/boards/%d8%a8%db%8c%d9%84%d8%a8%d9%88%d8%b1%d8%af-c24-%d9%85%d8%ad%d9%88%d8%b1-%d8%a7%d9%85%d8%a7%d9%85-%d8%b9%d9%84%db%8c/02188882525
  - https://hnpagency.com/boards/%d8%a8%db%8c%d9%84%d8%a8%d9%88%d8%b1%d8%af-f44-%d9%85%d8%ad%d9%88%d8%b1-%d8%aa%d9%87%d8%b1%d8%a7%d9%86-%d9%82%d9%85/02188882525
  - https://hnpagency.com/boards/%d8%a8%db%8c%d9%84%d8%a8%d9%88%d8%b1%d8%af-f47-%d9%85%d8%ad%d9%88%d8%b1-%d9%82%d9%85-%d8%aa%d9%87%d8%b1%d8%a7%d9%86/02188882525
  - https://hnpagency.com/boards/%d8%a8%db%8c%d9%84%d8%a8%d9%88%d8%b1%d8%af-kt3-%d9%85%d8%ad%d9%88%d8%b1-%da%a9%d8%b1%d8%ac-%d8%aa%d9%87%d8%b1%d8%a7%d9%86/02188882525
  - https://hnpagency.com/boards/bridge-board-niayesh-kp26/02188882525
  - https://hnpagency.com/boards/bridge-board-niayesh-kp27/02188882525
  - https://hnpagency.com/boards/%d8%b9%d8%b1%d8%b4%d9%87-%d9%be%d9%84-bp14-%d9%85%d8%ad%d9%88%d8%b1-%d8%b4%db%8c%d8%ae-%d9%81%d8%b6%d9%84-%d8%a7%d9%84%d9%84%d9%87/02188882525
  - https://hnpagency.com/boards/%d8%b9%d8%b1%d8%b4%d9%87-%d9%be%d9%84-bp15-%d9%85%d8%ad%d9%88%d8%b1-%d8%b4%db%8c%d8%ae-%d9%81%d8%b6%d9%84-%d8%a7%d9%84%d9%84%d9%87/02188882525
  - https://hnpagency.com/boards/%d8%b9%d8%b1%d8%b4%d9%87-%d9%be%d9%84-p59-%d9%85%d8%ad%d9%88%d8%b1-%d8%b5%db%8c%d8%a7%d8%af-%d8%b4%db%8c%d8%b1%d8%a7%d8%b2%db%8c/02188882525
  - https://hnpagency.com/boards/%d8%b9%d8%b1%d8%b4%d9%87-%d9%be%d9%84-p57-%d9%85%d8%ad%d9%88%d8%b1-%d8%b3%d8%aa%d8%a7%d8%b1%db%8c-%d9%85%d8%ac%d8%aa%d9%85%d8%b9-%da%a9%d9%88%d8%b1%d9%88%d8%b4/02188882525
  - https://hnpagency.com/boards/%d8%b9%d8%b1%d8%b4%d9%87-%d9%be%d9%84-ep38-%d9%85%d8%ad%d9%88%d8%b1-%db%8c%d8%a7%d8%af%da%af%d8%a7%d8%b1-%d8%a7%d9%85%d8%a7%d9%85/02188882525
  - https://hnpagency.com/boards/%d8%b9%d8%b1%d8%b4%d9%87-%d9%be%d9%84-kp14-%d9%85%d8%ad%d9%88%d8%b1-%d9%85%db%8c%d8%b1%d8%af%d8%a7%d9%85%d8%a7%d8%af/02188882525
  - https://hnpagency.com/boards/%d8%b9%d8%b1%d8%b4%d9%87-%d9%be%d9%84-kp15-%d9%85%d8%ad%d9%88%d8%b1-%d9%85%db%8c%d8%b1%d8%af%d8%a7%d9%85%d8%a7%d8%af/02188882525
  - https://hnpagency.com/boards/%d8%b9%d8%b1%d8%b4%d9%87-%d9%be%d9%84-p58-%d9%85%db%8c%d8%af%d8%a7%d9%86-%d8%a7%d9%85%d8%a7%d9%85-%d8%ad%d8%b3%db%8c%d9%86/
  - https://hnpagency.com/boards/%d8%b9%d8%b1%d8%b4%d9%87-%d9%be%d9%84-p10-%d9%85%d8%ad%d9%88%d8%b1-%d9%85%d8%b5%d8%b7%d9%81%db%8c-%d8%ae%d9%85%db%8c%d9%86%db%8c/
  - https://hnpagency.com/boards/%d8%b9%d8%b1%d8%b4%d9%87-%d9%be%d9%84-fp28-%d8%a2%d8%b2%d8%a7%d8%af%d8%b1%d8%a7%d9%87-%d8%aa%d9%87%d8%b1%d8%a7%d9%86-%d9%82%d9%85/
  - https://hnpagency.com/boards/%d8%b9%d8%b1%d8%b4%d9%87-%d9%be%d9%84-fp29-%d8%a2%d8%b2%d8%a7%d8%af%d8%b1%d8%a7%d9%87-%d9%82%d9%85-%d8%aa%d9%87%d8%b1%d8%a7%d9%86/
  - https://hnpagency.com/boards/%d8%a8%db%8c%d9%84%d8%a8%d9%88%d8%b1%d8%af-fp20-%d9%85%d8%ad%d9%88%d8%b1-%d8%aa%d9%87%d8%b1%d8%a7%d9%86-%da%a9%d8%b1%d8%ac/
  - https://hnpagency.com/boards/%d8%b9%d8%b1%d8%b4%d9%87-%d9%be%d9%84-tk1-%d8%a2%d8%b2%d8%a7%d8%af%d8%b1%d8%a7%d9%87-%d8%aa%d9%87%d8%b1%d8%a7%d9%86-%da%a9%d8%b1%d8%ac/
  - https://hnpagency.com/boards/%d8%b9%d8%b1%d8%b4%d9%87-%d9%be%d9%84-kt1-%d8%a2%d8%b2%d8%a7%d8%af%d8%b1%d8%a7%d9%87-%d8%aa%d9%87%d8%b1%d8%a7%d9%86-%da%a9%d8%b1%d8%ac/
  - https://hnpagency.com/boards/%d8%b9%d8%b1%d8%b4%d9%87-%d9%be%d9%84-tk2-%d9%85%d8%ad%d9%88%d8%b1-%d8%aa%d9%87%d8%b1%d8%a7%d9%86-%da%a9%d8%b1%d8%ac/
  - https://hnpagency.com/boards/%d8%b9%d8%b1%d8%b4%d9%87-%d9%be%d9%84-kt2-%d9%85%d8%ad%d9%88%d8%b1-%d8%aa%d9%87%d8%b1%d8%a7%d9%86-%da%a9%d8%b1%d8%ac/
  - https://hnpagency.com/boards/%d8%b9%d8%b1%d8%b4%d9%87-%d9%be%d9%84-l1-%d9%85%d8%ad%d9%88%d8%b1-%d9%84%d9%88%d8%a7%d8%b3%d8%a7%d9%86-%d9%81%d8%b4%d9%85/
  - https://hnpagency.com/boards/%d8%b9%d8%b1%d8%b4%d9%87-%d9%be%d9%84-l2-%d9%85%d8%ad%d9%88%d8%b1-%d9%81%d8%b4%d9%85-%d9%84%d9%88%d8%a7%d8%b3%d8%a7%d9%86/
  - https://hnpagency.com/boards-category/%D8%B9%D8%B1%D8%B4%D9%87-%D9%BE%D9%84/
  - https://hnpagency.com/boards-category/%D9%86%D9%88%D8%B9-%D8%B1%D8%B3%D8%A7%D9%86%D9%87/page/2/
  - https://hnpagency.com/boards-category/%D9%86%D9%88%D8%B9-%D8%B1%D8%B3%D8%A7%D9%86%D9%87/page/3/
  - https://hnpagency.com/boards-category/%D9%85%D9%88%D9%82%D8%B9%DB%8C%D8%AA/
  - https://hnpagency.com/modern-h-n-p-lightboard/02188882525
  - https://hnpagency.com/tag/%d8%aa%d8%a8%d9%84%db%8c%d8%ba%d8%a7%d8%aa/
  - https://hnpagency.com/tag/%d8%b1%d8%b3%d8%a7%d9%86%d9%87/
  - https://hnpagency.com/tag/%d8%b1%d8%b3%d8%a7%d9%86%d9%87-%d9%85%d8%ad%db%8c%d8%b7%db%8c/
  - https://hnpagency.com/tag/%d9%85%d8%af%d8%b1%d8%b3/
  - https://hnpagency.com/tag/%d9%85%d8%af%d8%b1%d9%86/
  - https://hnpagency.com/boards/%d8%b9%d8%b1%d8%b4%d9%87-%d9%be%d9%84-p58-%d9%85%db%8c%d8%af%d8%a7%d9%86-%d8%a7%d9%85%d8%a7%d9%85-%d8%ad%d8%b3%db%8c%d9%86/02188882525
  - https://hnpagency.com/boards/%d8%b9%d8%b1%d8%b4%d9%87-%d9%be%d9%84-p10-%d9%85%d8%ad%d9%88%d8%b1-%d9%85%d8%b5%d8%b7%d9%81%db%8c-%d8%ae%d9%85%db%8c%d9%86%db%8c/02188882525
  - https://hnpagency.com/boards/%d8%b9%d8%b1%d8%b4%d9%87-%d9%be%d9%84-fp28-%d8%a2%d8%b2%d8%a7%d8%af%d8%b1%d8%a7%d9%87-%d8%aa%d9%87%d8%b1%d8%a7%d9%86-%d9%82%d9%85/02188882525
  - https://hnpagency.com/boards/%d8%b9%d8%b1%d8%b4%d9%87-%d9%be%d9%84-fp29-%d8%a2%d8%b2%d8%a7%d8%af%d8%b1%d8%a7%d9%87-%d9%82%d9%85-%d8%aa%d9%87%d8%b1%d8%a7%d9%86/02188882525
  - https://hnpagency.com/boards/%d8%a8%db%8c%d9%84%d8%a8%d9%88%d8%b1%d8%af-fp20-%d9%85%d8%ad%d9%88%d8%b1-%d8%aa%d9%87%d8%b1%d8%a7%d9%86-%da%a9%d8%b1%d8%ac/02188882525
  - https://hnpagency.com/boards/%d8%b9%d8%b1%d8%b4%d9%87-%d9%be%d9%84-tk1-%d8%a2%d8%b2%d8%a7%d8%af%d8%b1%d8%a7%d9%87-%d8%aa%d9%87%d8%b1%d8%a7%d9%86-%da%a9%d8%b1%d8%ac/02188882525
  - https://hnpagency.com/boards/%d8%b9%d8%b1%d8%b4%d9%87-%d9%be%d9%84-kt1-%d8%a2%d8%b2%d8%a7%d8%af%d8%b1%d8%a7%d9%87-%d8%aa%d9%87%d8%b1%d8%a7%d9%86-%da%a9%d8%b1%d8%ac/02188882525

```

</details>


```yaml
crawl:
  source: crawl-hnpagency-2026-02-04-17-17-32-d24z45

```

[corpus-hnpagency-2026-02-04-63hokm.tar.gz](https://kamangir-public.s3.ir-thr-at1.arvanstorage.ir/corpus-hnpagency-2026-02-04-63hokm.tar.gz)
