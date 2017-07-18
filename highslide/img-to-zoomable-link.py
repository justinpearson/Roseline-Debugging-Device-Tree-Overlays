#!/usr/bin/env python

'''
A Pandoc filter to replace images with thumbnails that zoom in when you click.

/Users/justin/Dropbox/Diablo2/

Note: also need highslide/highslide.js in order for zooming to work,
and put this example following YAML at the top of your md file in order for 
pandoc to put the <script> tag in the html's header.
---
title: My awesome page
header-includes:
    <meta name="keywords" content="things,cats,lulz" />
    <meta name="description" content="Just some wild stuff dawg!" />
    <script type="text/javascript" src="highslide/highslide.js" ></script>
---

'''

# from inspect import cleandoc as strip_universal_leading_whitespace # from http://stackoverflow.com/a/34579466
from pandocfilters import toJSONFilter, Image, Link, Str, Para, Code
import sys

def img_to_zoomable_link(key, value, format, meta):
  # I'm not really sure what 'format' and 'meta' are.
  # 'key' is a string telling you what kind of element you're processing, and
  # 'value' is some JSON list/object/something, depending on what 'key' is.

  # print("Hello world from pandoc filter!") # NO: stdout kills pandoc, since it's stream-based. Use stderr instead.

  # sys.stderr.write("key: {}\n".format(key))
  # sys.stderr.write("value: {}\n".format(value))


  if key != 'Image':
    return None # no processing required

  sys.stderr.write("Running img-to-zoomable-link.py\n")

  # sys.stderr.write("key: {}\n".format(key))
  # sys.stderr.write("value: {}\n".format(value))


  (identifier, classes, img_attributes), alt_text_shit, (img_path, img_caption) = value

  # sys.stderr.write("identifier: {}\n".format(identifier))
  # sys.stderr.write("alt_text_shit: {}\n".format(alt_text_shit))  
  # sys.stderr.write("img_path: {}\n".format(img_path))
  # sys.stderr.write("img_caption: {}\n".format(img_caption))

    

  # replacement = Code(['', [], []], 'ls -l') # works
  # replacement = Image( ("",[],[("width","200px")]), [],[img_path,"fig:blah"] ) # works
  # replacement = Link(  ("",[],[]), ["click","here!"], ["http://google.com",""] ) # no
  # replacement = Link(  ["",[],[]], ["click","here!"], ["http://google.com",""] ) # no
  # replacement = Link(  ["",[],[]], [Str('Click here!')], ["http://google.com",""] )  # yes 
  # replacement = Link(  ["",[],[]], [Image( ("",[],[("width","200px")]), [],[img_path,"fig:blah"] )], [img_path,""] )  # yes 
  # replacement = Para([Code(['', [], []], 'ls -lt')]) # no
  # replacement = Code(['', [], []], 'ls -lt') # yes
  # replacement = Para([Str('wtf!!')]) # no
  # replacement = Para([Image(['', [], []], [], [img_path, ""])]) # no: can't wrap an img in a para, recursion error.

  replacement = Link(
                    ["",[],[("onclick","return hs.expand(this)")]], 
                    [Image( 
                      ("",[],[("width","400px")]), 
                      [],
                      [img_path,"fig:blah"] 
                      )
                    ], 
                    [img_path,""] 
                  )
               


  


  # sys.stderr.write("replacement: {}\n".format(replacement))




  # target = strip_universal_leading_whitespace(target)

  # Create the Pandoc block element that will replace the code block.
  # (Note: Pandoc distinguishes between "inline" elements and "block" elements, 
  # and gives some sort of "no such element" error if you return an inline when it expects a block.)

  # I'm going to make a bulleted list. (Each bullet is itself a list of Pandoc block elements.)

  # bullet_points = [
  #   [Para([Code(['', [], []], 'ls -l')]),
  #    CodeBlock(['', [], []], '...\noutput\n...')],
  #   [Para([Code(['', [], []], 'ls -lt')]),
  #    CodeBlock(['', [], []], '...\nmore output\n...')]]

  # replacement = BulletList(bullet_points)

  return replacement

if __name__ == "__main__":

  # print("Hi from main of img_....py")
  toJSONFilter(img_to_zoomable_link)
