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
* There, you will find ``` STAFF DEBUG INFO button ``` on right down click on that staff button copy that location from there.
# example below
```
location = block-v1:trimate+c01+2020+type@xblock_website_viewer+block@e495f38935294d8daafcf12c1400c37e

```
* open your lms url in browser

# example below
```
https://<lms-url>/xblock/copiedlocationhere

```
* You will find your iframe there next step will be create a page
* Click on content dropdown and click pages for create a page.
* after created a page goto edit option and select their html option
pasted their lmsfull url which present in above example.

#example
 complete url will be below it just an example
```
https://<lms-url>/xblock/block-v1:trimate+c01+2020+type@xblock_website_viewer+block@e495f38935294d8daafcf12c1400c37e

```


* https://<lms-ulr>/xblock/copiedlocation/
 *create a new page click on content drop down which is left on settings click on pages cr

Other easy to way to get a tab on course detail page for proctortrack.
-------

* click on content drop which left in settings click on pages create a new page and select html tag there add below code there:
```
<iframe src="https://www.proctortrack.com/">
  <p>Your browser does not support iframes.</p>
</iframe>

```
