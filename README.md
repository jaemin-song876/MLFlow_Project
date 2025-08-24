
  <h1>MLflow_Project</h1>
  <p><strong>This project follows the tutorial:</strong><br>
    <a href="https://pub.towardsai.net/a-great-overview-of-machine-learning-operations-and-how-the-mlflow-project-made-it-easy-step-by-a49585a4863c" target="_blank" rel="noopener">
      A Great Overview of MLOps and How the MLflow Project Made It Easy
    </a>
  </p>
  <h2>What is MLOps?</h2>
  <p>
    <strong>MLOps</strong> is the operational discipline of taking machine-learning models to
    <em>production</em>, retraining them as data changes, and tracking experiments and artifacts
    so results are reproducible and auditable.
  </p>

  <figure>
    <!-- Replace the src below with your diagram path -->
    <img width="720" height="1018" alt="image" src="https://github.com/user-attachments/assets/f85ecdfe-52ac-485e-bbf3-30790c1b9dfe" />
  </figure>

  <h3>ETL pipeline (two components)</h3>
  <ul>
    <li><code>download data</code></li>
    <li><code>preprocessing</code></li>
  </ul>

  <p>When the ETL pipeline runs, the pipeline passes a URL to the
    <em>download-data</em> component. That component produces an artifact named
    <code>raw_data</code> and stores it in Weights &amp; Biases (W&amp;B).</p>

  <p>Next, the <em>preprocessing</em> component pulls that <code>raw_data</code> artifact from W&amp;B,
    transforms/cleans it, writes a new file <code>clean_data.csv</code>, and uploads it back to W&amp;B
    as another artifact. This is how files and directories are shared between steps via W&amp;B.</p>

  <hr>

  <h2>What this repo does (our hands-on)</h2>
  <ul>
    <li>Implements a <strong>data preprocessing component</strong> as an <strong>MLflow Project</strong> (<code>MLproject</code> → <code>run.py</code>).</li>
    <li>Generates a cleaned dataset artifact: <code>outputs/clean_data.csv</code>.</li>
    <li>Logs the CSV to <strong>MLflow Tracking</strong> so it appears in the MLflow web UI under <em>Artifacts</em>.</li>
    <li>Tracks execution parameters (<code>artifact_name</code>, <code>artifact_type</code>, <code>artifact_description</code>).</li>
  </ul>

  <h3>Run (Windows / PowerShell)</h3>
  <p><em>Optional (disable W&amp;B prompts for this demo):</em></p>
  <pre><code class="language-powershell">setx WANDB_DISABLED true
$env:WANDB_DISABLED="true"</code></pre>

  <p><em>Run the project (uses current Python environment):</em></p>
  <pre><code class="language-powershell">python -m mlflow run . --env-manager=local `
  -P artifact_name=clean_data.csv `
  -P artifact_type=clean_data `
  -P artifact_description=Clean_and_preprocessed_data</code></pre>

  <h3>Open the MLflow web UI</h3>
  <p>On Windows, a single worker and a non-default port are the most reliable:</p>
  <pre><code class="language-powershell">python -m mlflow ui --host 127.0.0.1 --port 5001 --workers 1
# then open http://127.0.0.1:5001 in your browser</code></pre>

  <h3>Where to find the artifact</h3>
  <ul>
    <li>Local file: <code>./outputs/clean_data.csv</code></li>
    <li>MLflow artifact on disk: <code>./mlruns/&lt;experiment_id&gt;/&lt;run_id&gt;/artifacts/artifacts/clean_data.csv</code></li>
  </ul>


</body>
</html>
