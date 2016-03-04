# AppBegat
A Python GUI to setup a web project with your favorite cdn libraries in a snap.

App Begat is a Tkinter based Python program designed to configure a web project.  It will create a directory or directories based on the configuration and load the appropriate css, js, html and image files into the project directory.  External libraries like Dojo or jQuery can also be loaded as a CDN link in the index.html file.  All you have to do is check the boxes with the CDN links you want to add.  That easy!

If you have images, js files or css files you reuse often, copy them into the directories labeled, "myImages", "myCSS" and "myJS".  Whenever you check the option to copy any of them from the application's menu, App Begat will copy the files into new directories within your project AND load the links into the index.html file.

I packaged some of the libraries together--they're all under the JavaScript/Css section.  For example, checking the Dojo box will load both the dojo and dijit libraries hosted by google.  You may not want both, but deleting the stylesheet link is easier than finding it each time.

Also there are some CSS options like the CSS Reset by Eric Meyer.  Just check the box and your "style.css" file will have those elements updated.  Likewise with the palettes.

If you want to use the google maps API, you can add your key to the variable near the top of the launch.pyw script, and it will automatically populate in the index.html file.

