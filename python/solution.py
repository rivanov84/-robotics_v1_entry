#!/usr/bin/env python3

from typing import (
    List,
    Tuple,
    Union
)

from utils.image import (
    ImageType,
    PackedImage,
    StrideImage,
)

from utils.function_tracer import FunctionTracer

def compute_solution(images: List[Union[PackedImage, StrideImage]]):
    ft = FunctionTracer("compute_solution", "seconds")
    for image in images:
       image.pixels_red = [x - 150 if x>=200 else x for x in image.pixels_red]
    del ft
