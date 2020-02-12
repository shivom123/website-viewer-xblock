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
* If you want to alter some fields value like iframe width, height, display name apart from this you can change url as well if you want to display other web site in that iframe you can edit.
* Publish your content as usual.

Other easy to way to get a tab on course detail page for proctortrack.
-------

* click on content drop which left in settings click on pages create a new page and select html tag there add below code there:
```
<iframe src="https://www.proctortrack.com/">
  <p>Your browser does not support iframes.</p>
</iframe>

```
