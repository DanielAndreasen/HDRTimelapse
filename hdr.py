#!/usr/bin/env python
# -*- coding: utf8 -*-

from __future__ import division
import os
import argparse


def chunks(l, n):
    """return a chunk of a list"""
    for i in xrange(0, len(l), n):
        yield l[i:i+n]


def _create_hdr(img_per_hdr, images, output='HDR1'):
    cmd = lambda i, files: "luminance-hdr-cli -o %s/HDR%s.jpg %s" % (output, i+1, files)
    for i, chunk in enumerate(chunks(images, img_per_hdr)):
        # os.system(cmd(i, ' '.join(chunk))
        print cmd(i, ' '.join(chunk))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Make timelapse of HDR pics')
    parser.add_argument('images', help='List of all the images, *.jpg e.g.',
                        nargs='+')
    parser.add_argument('number', help='Number of pics per HDR', type=int)
    args = parser.parse_args()

    images = args.images
    number = args.number

    if len(images) % number != 0:
        raise ValueError('The number of files (%s) is not a divisor of the number per HDR (%s)' % (len(images), number))

    hdr_dir = lambda i: os.path.dirname(os.path.realpath(images[0])) + '/HDR%s' % i
    i = 1
    while os.path.isdir(hdr_dir(i)):
        i += 1
    print 'Making new directory for HDRs at "%s"' % hdr_dir(i)
    # os.mkdir(hdr_dir(i))
    print 'Creating HDRs. This make take a while.'
    print 'Please wait...'
    _create_hdr(img_per_hdr=number, images=images, output=hdr_dir(i))
