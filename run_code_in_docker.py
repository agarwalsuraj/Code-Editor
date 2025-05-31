import tempfile
import subprocess
import uuid
import os

DOCKER_IMAGES = {
    'python': 'code_executor_python',
    #'javascript': 'code_executor_js',
    #'c': 'code_executor_c',
    #'cpp': 'code_executor_cpp',
    #'java': 'code_executor_java'
}

def run_code(code, language):
    if language not in DOCKER_IMAGES:
        raise ValueError(f"Unsupported language: {language}")

    image = DOCKER_IMAGES[language]
    ext = {
        'python': '.py',
        #'javascript': '.js',
        #'c': '.c',
        #'cpp': '.cpp',
        #'java': '.java'
    }[language]

    filename = f'code{ext}'
    temp_dir = tempfile.mkdtemp()
    file_path = os.path.join(temp_dir, filename)

    with open(file_path, 'w') as f:
        f.write(code)

    container_name = f"code-runner-{uuid.uuid4().hex[:8]}"

    try:
        result = subprocess.run([
            'docker', 'run', '--rm',
            '-v', f'{temp_dir}:/code',
            image
        ], stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=10, text=True)

        return result.stdout, result.stderr
    finally:
        os.remove(file_path)
        os.rmdir(temp_dir)
