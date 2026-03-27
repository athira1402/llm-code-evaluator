import subprocess
import tempfile

def run_code(code, input_data):
    with tempfile.NamedTemporaryFile(delete=False, suffix=".py") as f:
        f.write(code.encode())
        file_name = f.name

    try:
        result = subprocess.run(
            ["python", file_name],
            input=input_data,
            text=True,
            capture_output=True,
            timeout=2
        )

        return {
            "output": result.stdout.strip(),
            "error": result.stderr.strip()
        }

    except Exception as e:
        return {"error": str(e)}
