# run.py
import argparse, os, pathlib, csv
# run.py 맨 위에 추가
import mlflow

# (선택) W&B로 아티팩트 올리기
use_wandb = True
try:
    import wandb
except Exception:
    use_wandb = False

def main():
    p = argparse.ArgumentParser(description="Create a demo artifact (CSV) and optionally log to W&B")
    p.add_argument("--artifact_name", type=str, required=True, help="Name for the output artifact")
    p.add_argument("--artifact_type", type=str, required=True, help="Artifact type")
    p.add_argument("--artifact_description", type=str, required=True, help="Artifact description")
    args = p.parse_args()

    out_dir = pathlib.Path("outputs"); out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / args.artifact_name
    # 데모용 CSV 생성
    with open(out_path, "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["feature1","feature2","label"])
        w.writerow([1.0, 2.0, 0])
        w.writerow([3.0, 4.0, 1])

    print(f"[OK] Created artifact file: {out_path.resolve()}")
    # CSV 저장 직후 아래 3줄 추가
    mlflow.log_param("artifact_name", args.artifact_name)
    mlflow.log_param("artifact_type", args.artifact_type)
    mlflow.log_artifact(str(out_path), artifact_path="artifacts")

    # 글처럼 '아티팩트'를 버전 관리하는 예시로 W&B 사용 (로그인 되어 있으면)
    if use_wandb:
        wandb.init(project="mlops-overview-demo", job_type="create_artifact")
        art = wandb.Artifact(
            name=args.artifact_name,
            type=args.artifact_type,
            description=args.artifact_description
        )
        art.add_file(str(out_path))
        wandb.log_artifact(art)
        wandb.finish()
        print("[OK] Logged artifact to Weights & Biases (wandb).")
    else:
        print("[INFO] wandb 미설치/미로그인. 로컬 파일만 생성했습니다.")

if __name__ == "__main__":
    main()
