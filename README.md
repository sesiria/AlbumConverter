# AlbumConverter
Support music album info recognition and format convert

## Requirements list:  

https://docs.qq.com/sheet/DSWdLUVZNSW9UQnVM?tab=BB08J2

## Features has been done:

* Support Convert from wav to flac.  

  * Due to the limitation of the ffmpeg encoder which support max to 24bit-per-sample by default. 

  * Using libflac 1.4.0 will support 32bit-per-sample but some player can not support this format correctly.

* Support Convert from wav to alac. (Apple Lossless).  
  * ffmpeg only supports up-to 24bit.
  * Official afconvert doesn't support the Windows, only MacOSX/iOS is supported.

## Third Party Library: 

* https://ffmpeg.org/ 

* https://xiph.org/flac/index.html