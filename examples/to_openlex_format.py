import shutil
import sys
import h5py
from dataclasses import dataclass
from pathlib import Path
import tyro
import open3d as o3d
import numpy as np

def h5_to_np(h5_path :Path, group_key: str):
    with h5py.File(h5_path, "r") as f:
        return f[group_key][:]

@dataclass
class ProgramArgs:
    cf_path : str = "saved-map"
    openlex_path : str = "openlex3d"

if __name__ == "__main__":

    args = tyro.cli(ProgramArgs)

    cf_path = Path(args.cf_path) / "pointclouds"
    openlex_path = Path(args.openlex_path)

    if not cf_path.exists():
        print(f"Path {cf_path} does not exist!")
        sys.exit(1)
    if openlex_path.exists():
        print(f"Path {openlex_path} already exists! Removing!")
        shutil.rmtree(openlex_path)
    openlex_path.mkdir(parents=True, exist_ok=False)
    

    # Read as numpy arrays
    point_path = cf_path / "pc_points.h5"
    color_path = cf_path / "pc_colors.h5"
    embedding_path = cf_path / "pc_embeddings.h5"

    points = h5_to_np(point_path, "pc_points")
    colors = h5_to_np(color_path, "pc_colors")
    embeddings = h5_to_np(embedding_path, "pc_embeddings")

    # Save point cloud as open3d point cloud
    pcd = o3d.geometry.PointCloud()
    pcd.points = o3d.utility.Vector3dVector(points)
    pcd.colors = o3d.utility.Vector3dVector(colors/255)
    o3d.io.write_point_cloud(openlex_path / "pointcloud.pcd", pcd)

    # Save embeddings as numpy array
    np.save(openlex_path / "embeddings.npy", embeddings)

    index = np.arange(len(embeddings))
    np.save(openlex_path / "index.npy", index)

    print(f"Saved point cloud and embeddings to {openlex_path}")
    


