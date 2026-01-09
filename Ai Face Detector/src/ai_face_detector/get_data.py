import kagglehub
import os

def import_data(out_path: str) -> None:
    os.environ["KAGGLEHUB_CACHE"] = f"{out_path}"
    
    path = kagglehub.dataset_download("hassnainzaidi/human-faces-data-set")
    print("Path to dataset files:", path)


if __name__ == "__main__":
    print("Fetching data...")
    import_data("Ai Face Detector")
    print("Data succesfully fetched.")