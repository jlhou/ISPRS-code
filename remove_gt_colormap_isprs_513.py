# Copyright 2018 The TensorFlow Authors All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================

"""Removes the color map from segmentation annotations.

Removes the color map from the ground truth segmentation annotations and save
the results to output_dir.
"""
import glob
import os.path
import numpy as np

from PIL import Image
import scipy.misc as misc
import tensorflow as tf

FLAGS = tf.app.flags.FLAGS

tf.app.flags.DEFINE_string('original_gt_folder',
                           'E:\\bishe\SAR\predict_005',
                           'Original ground truth annotations.')

tf.app.flags.DEFINE_string('segmentation_format', 'png', 'Segmentation format.')

tf.app.flags.DEFINE_string('output_dir',
                           'E:\\bishe\\accuracy\Xception_no_aspp_output_8\predict_labels_raw',
                           'folder to save modified ground truth annotations.')


def _remove_colormap(filename):
  """Removes the color map from the annotation.

  Args:
    filename: Ground truth annotation filename.

  Returns:
    Annotation without color map.
  """
  return np.array(Image.open(filename)).astype(dtype=np.uint8)

def trans_late(raw_annotation, score_map):
  annotation = np.zeros_like(raw_annotation[:, :, 0])
  tmp = np.zeros_like(raw_annotation)
  for cls_idx, cls in enumerate(score_map):
    tmp = raw_annotation.copy()
    tmp = np.sum(np.abs(tmp - cls), axis = 2)
    annotation[tmp == 0] = cls_idx
  # for i in range(raw_annotation.shape[0]):
  #   for j in range(raw_annotation.shape[1]):
  #     tmp = raw_annotation[i, j]
  #     for cls_idx, cls in enumerate(score_map):
  #       if np.sum(tmp - cls) == 0.0:
  #         annotation[i, j] = cls_idx
  print (np.max(annotation), np.min(annotation))
  return annotation

def _save_annotation(annotation, filename):
  """Saves the annotation as png file.

  Args:
    annotation: Segmentation annotation.
    filename: Output filename.
  """
  pil_image = Image.fromarray(annotation.astype(dtype=np.uint8))
  with tf.gfile.Open(filename, mode='w') as f:
    pil_image.save(f, 'PNG')


def main(unused_argv):
  # Create the output directory if not exists.
  score_map = [
    np.array([255, 255, 255]),
    np.array([0, 0, 255]),
    np.array([0, 255, 255]),
    np.array([0, 255, 0]),
    np.array([255, 255, 0]),
    np.array([255, 0, 0]),
  ]
  if not tf.gfile.IsDirectory(FLAGS.output_dir):
    tf.gfile.MakeDirs(FLAGS.output_dir)

  annotations = glob.glob(os.path.join(FLAGS.original_gt_folder,
                                       '*.' + FLAGS.segmentation_format))
  for annotation in annotations:
    print (annotation)
    raw_annotation = _remove_colormap(annotation)
    filename = os.path.basename(annotation)[:-4]

    bit8_annotation = trans_late(raw_annotation, score_map)
    # misc.imsave('E:\\bishe\SAR\ISPRS_semantic_labeling_Vaihingen\div_labels_vis/' + filename + '.jpg', bit8_annotation * 50)
    _save_annotation(bit8_annotation,
                     os.path.join(
                         FLAGS.output_dir,
                         filename + '.' + FLAGS.segmentation_format))
    # _save_annotation(bit8_annotation,
    #                  os.path.join(
    #                      FLAGS.output_dir,
    #                      filename + '.' + png))


if __name__ == '__main__':
  tf.app.run()
