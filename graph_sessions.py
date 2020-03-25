""" A simple TensorFlow application """

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import tensorflow.compat.v1 as tf
tf.disable_v2_behavior()

# Create two tensors and an addition operation
t1 = tf.constant([1.2, 2.3, 3.4, 4.5])
t2 = tf.random_normal([4])
t3 = t1 + t2
graph1 = tf.get_default_graph()

# Create a second graph and make it the default graph
graph2 = tf.Graph()
with graph2.as_default():

# Create two tensors in the second graph and a subtraction operation
    t4 = tf.constant([5.6, 6.7, 7.8, 8.9])
    t5 = tf.random_normal([4])
    t6 = t4 - t5

# Create a session and execute the addition operation from the first graph
with tf.Session(graph=graph1) as sess:
    print('Addition ', sess.run(t3))

# Create a second session and execute the subtraction operation from the second graph
with tf.Session(graph=graph2) as sess:
    print('Subtraction ', sess.run(t6))
