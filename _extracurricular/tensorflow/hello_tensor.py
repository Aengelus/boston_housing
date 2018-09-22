# Just disables the warning "TensorFlow binary was not compiled to use: AVX2", doesn't enable AVX/FMA
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

import tensorflow as tf

# Create Tensorflow object called tensor
hello_constant = tf.constant('Hello World')

with tf.Session() as sess:
    # Run the tf.constant operation in the session
    output = sess.run(hello_constant)
    print(output)