# website-viewer-xblock

website-viewer-xblock to display https://www.proctortrack.com/ inside iframe.

Installation
------------

Install package
* Before installation activate your env then run below command:
```
  
  pip install git+https://github.com/shivom123/website-viewer-xblock.git
  
```
* restart your studio server then it will reflect there.

# Usage
* Add `xblock_website_viewer` to the list of advanced modules in the advanced settings of a course.
* Add a `WebViewer` component to your Unit. 
* If you want to alter iframe some fields value like iframe width, height display name and website url (which website you want to show under that iframe)
* Publish your content as usual and click on live preview.
* There, you will find ``` STAFF DEBUG INFO button ``` on right down click on that staff button you will find there location copy that location from.
# see below look like this location
```
location = block-v1:trimate+c01+2020+type@xblock_website_viewer+block@e495f38935294d8daafcf12c1400c37e

```
* 

# Open your lms url in browser with location take reference below
```
https://<lms-url>/xblock/copiedlocationhere

```
* You will find your iframe window there next step will be create a page
# Steps for create new content page:

* Click on content dropdown which is inside cms course, click pages for create a page.
* After created a page goto edit option and select their html option
pasted their lms full url which you do earlier access in above example.
* Second tab is settings click on that and set your tab name there.

# take reference below which url you have to pasted in content page html.
 complete url will be below it just an example
```
https://<lms-url>/xblock/block-v1:trimate+c01+2020+type@xblock_website_viewer+block@e495f38935294d8daafcf12c1400c37e

```

* Save and you will get a tab with instruter left side name which you set earlier using settings. 

-------


