""" A simple TensorFlow application """

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import tensorflow.compat.v1 as tf
tf.disable_v2_behavior()
# import tensorflow as tf

# msg = tf.string__join(['hello','Tensor'])
msg = tf.strings.join(['Hello ', 'TensorFlow'])

with tf.Session() as sess:
    print(sess.run(msg))
    print(sess.run(msg))

# with tf.compat.v1.Session() as sess:
#         print(sess.run(msg))

