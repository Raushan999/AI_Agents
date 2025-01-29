## Agents
## 1.  Financial Analyst Agent
## 2.  Youtube Video Summarizer Agent
## problems faced in this project:-
1. Issue with importing `Identity` from `phi.utils`
    - Resolved by upgrading the `phidata` module to the latest version.
2. SSL certificate issue
    - Resolved by: Specified the groq model - `llama 3.3` in the final multi-agent,
    - By default it uses the `Openai` models

Also disabling the certificate verification resolved the issue of groq-api connection issue.
#### Disable SSL verification

```python
httpx_client = httpx.Client(verify=False)
model = Groq(id = "llama-3.3-70b-versatile",http_client=httpx_client)
```