import 'dart:io';
import 'dart:ui' as ui;
import 'package:flutter/material.dart';
import 'package:image/image.dart' as img;

Future<img.Image> loadImage(String path) async {
    File file = File(path);
    List<int> fileBytes = await file.readAsBytes();
    img.Image image = img.decodeImage(fileBytes);
    return image;
}

img.Image resizeImage(img.Image image, int width, int height) {
    return img.copyResize(image, width: width, height: height);
}

void saveImage(img.Image image, String path) {
    File(path)..writeAsBytesSync(img.encodePng(image));
}

List<double> scaleBoundingBox(List<double> box, double widthRatio, double heightRatio) {
    return [
        (box[0] * widthRatio).roundToDouble(),
        (box[1] * heightRatio).roundToDouble(),
        (box[2] * widthRatio).roundToDouble(),
        (box[3] * heightRatio).roundToDouble(),
    ];
}

void createDirectories(String pathImages, String pathAnnotations, int width, int height) {
    Directory('$pathImages/${height}x$width').createSync(recursive: true);
    Directory('$pathAnnotations/${height}x$width').createSync(recursive: true);
}