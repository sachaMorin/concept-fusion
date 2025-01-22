# Helper function to get an RGBDDataset from the rgbd_dataset repo using CF arguments

from rgbd_dataset.rgbd_dataset.datasets.Replica import Replica

def get_rgbd_dataset(dataset_name: str, basedir: str, sequence: str, start: int, end: int, stride: int, desired_height: int, desired_width: int):
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
            sequence_stride= stride,
            relative_pose= False,
            depth_scale= 6553.5,
            point_cloud= False,
            depth_trunc= 8.0,
        )
    else:
        raise ValueError(f"Unknown dataset name {dataset_name}")

    dataset.color_paths = dataset.rgb_paths

    return dataset