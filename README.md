# DifferNet for VisA Dataset

This project implements the "Same Same But DifferNet" model for semi-supervised defect detection using normalizing flows, applied to the VisA dataset. This work is based on the WACV 2021 paper "[Same Same But DifferNet: Semi-Supervised Defect Detection with Normalizing Flows](https://arxiv.org/abs/2008.12577)" by Marco Rudolph, Bastian Wandt and Bodo Rosenhahn.

## Project Overview

This project aims to detect anomalies in various object classes without having anomalous samples in the training set. We've adapted the original DifferNet implementation to work with the VisA dataset, which contains 12 different object classes.

## Dataset

The VisA dataset contains 12 subsets corresponding to different objects:
- 4 types of printed circuit boards (PCB)
- Multiple instance objects: Capsules, Candles, Macaroni1, and Macaroni2
- Roughly aligned objects: Cashew, Chewing gum, Fryum, and Pipe fryum

Total images: 10,821 (9,621 normal, 1,200 anomalous)

### Dataset Structure

```
Dataset Directory
├── class_1
│   ├── train
│   │   └── good
│   └── test
│       ├── good
│       └── anomaly
├── class_2
...
```

## Requirements

- Python 3.6
- Packages specified in `requirements.txt`

Install packages with:

```
$ pip install -r requirements.txt
```

## Configuration and Running

1. Modify `config.py` to set dataset paths and other parameters.
2. Run `main.py` to start the training process.

## Results

The model was trained on each class of the VisA dataset. Here's a summary of the results:

| Class Name  | AUROC (Max) | Epoch Max | Time Taken |
|-------------|-------------|-----------|------------|
| candle      | 0.8825      | 16        | 1:41:06    |
| capsules    | 0.7145      | 22        | 1:14:47    |
| cashew      | 0.9701      | 3         | 1:09:58    |
| chewinggum  | 0.9685      | 23        | 1:07:48    |
| fryum       | 0.9501      | 15        | 1:08:00    |
| pipe fryum  | 0.9637      | 23        | 1:05:15    |
| pcb1        | 0.9004      | 8         | 1:55:30    |
| pcb2        | 0.9825      | 23        | 1:46:44    |
| pcb3        | 0.8567      | 14        | 1:45:18    |
| pcb4        | 0.9897      | 20        | 1:45:57    |
| macaroni1   | 0.8205      | 1         | 1:39:47    |
| macaroni2   | 0.7748      | 21        | 1:46:24    |

## Conclusion

The model shows varying performance across different classes, with AUROC scores ranging from 0.7145 to 0.9897. PCB classes and some food items achieved high AUROC scores, while classes like capsules and macaroni showed lower performance.

## Future Work

- Improve model performance on lower-scoring classes
- Investigate factors contributing to varying detection accuracies across object types

## Citation

If you use this work, please cite the original paper:

```
@inproceedings{RudWan2021,
    author = {Marco Rudolph and Bastian Wandt and Bodo Rosenhahn},
    title = {Same Same But DifferNet: Semi-Supervised Defect Detection with Normalizing Flows},
    booktitle = {Winter Conference on Applications of Computer Vision (WACV)},
    year = {2021},
    month = jan
}
```

## License

This project is licensed under the MIT License.
