# Helper function to get an RGBDDataset from the rgbd_dataset repo using CF arguments

from rgbd_dataset.rgbd_dataset.datasets.Replica import Replica
from rgbd_dataset.rgbd_dataset.datasets.HM3D import HM3D
from rgbd_dataset.rgbd_dataset.datasets.Scannetpp import ScannetppCOLMAP

def get_rgbd_dataset(dataset_name: str, basedir: str, sequence: str, start: int, end: int, stride: int, desired_height: int, desired_width: int):
    # Stride arg is ignored
    dataset_name = dataset_name.lower()
    if dataset_name == "replica":
        dataset = Replica(
            dataset_name= "replica",
            base_path= basedir,
            scene= sequence,
            width= 1200,
            height= 680,
            fx= 600.0,
            fy= 600.0,
            cx= 599.5,
            cy= 339.5,
            resized_width= desired_width,
            resized_height= desired_height,
            sequence_start= start,
            sequence_end= end,
            sequence_stride= 20,
            relative_pose= False,
            depth_scale= 6553.5,
            point_cloud= False,
            depth_trunc= 8.0,
        )
    elif dataset_name == "hm3d":
        dataset = HM3D(
            dataset_name= "hm3d",
            base_path= basedir,
            scene= sequence,
            width= 1080,
            height= 720,
            fx= 540.0,
            fy= 540.0,
            cx= 540.0,
            cy= 360.0,
            resized_width= desired_width,
            resized_height= desired_height,
            sequence_start= start,
            sequence_end= end,
            sequence_stride= 10,
            relative_pose= False,
            depth_scale= 1000.0,
            point_cloud= False,
            depth_trunc= 8.0,
        )
    elif dataset_name == "scannetpp":
        dataset = ScannetppCOLMAP(
            dataset_name= "scannetpp",
            base_path= basedir,
            scene= sequence,
            width= 1920,
            height= 1440,
            fx= 1437.56,
            fy= 1437.54,
            cx= 956.874,
            cy= 723.627,
            resized_width= desired_width,
            resized_height= desired_height,
            sequence_start= start,
            sequence_end= end,
            sequence_stride= 2,
            relative_pose= False,
            depth_scale= 1000.0,
            point_cloud= False,
            depth_trunc= 8.0,
        )
    else:
        raise ValueError(f"Unknown dataset name {dataset_name}")

    dataset.color_paths = dataset.rgb_paths

    return dataset