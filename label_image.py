from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import tensorflow as tf

def load_image(filename):
    """Read in the image_data to be classified."""
    return tf.gfile.FastGFile(filename, 'rb').read()


def load_labels(filename):
    """Read in labels, one label per line."""
    return [line.rstrip() for line in tf.gfile.GFile(filename)]


def load_graph(filename):
    """Unpersists graph from file as default graph."""
    with tf.gfile.FastGFile(filename, 'rb') as f:
        graph_def = tf.GraphDef()
        graph_def.ParseFromString(f.read())
        tf.import_graph_def(graph_def, name='')


def run_graph(image_data, labels, input_layer_name, output_layer_name,
              num_top_predictions):
    with tf.Session() as sess:
        softmax_tensor = sess.graph.get_tensor_by_name(output_layer_name)
        predictions, = sess.run(softmax_tensor, {input_layer_name: image_data})

        top_k = predictions.argsort()[-num_top_predictions:][::-1]
        for node_id in top_k:
            human_string = labels[node_id]
            score = predictions[node_id]
            if score < 0.20:
                print('Undefined')
                return 'Undefined'
            else:
                print(human_string)
                return human_string


def main(image, label_loc, graph_loc):
    # load image
    image_data = load_image(image)

    # load labels
    labels = load_labels(label_loc)

    # load graph, which is stored in the default session
    load_graph(graph_loc)

    run_graph(image_data, labels, 'DecodeJpeg/contents:0', 'final_result:0', 1)
